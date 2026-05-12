#!/usr/bin/env python3
"""
quality_loop.py — Iterative paper quality optimizer for SHELL.

Runs a paper, then Steelmans the completed paper.md as a hostile external
referee. Feeds the referee critique back into the init file as concrete
revision instructions. Runs again. Repeats until the Steelman finds nothing
substantive or max_runs is reached.

Usage:
    python src/quality_loop.py --init papers/init_sunk_cost.md --max-runs 3

The key insight: per-milestone Steelman reviews fragments. The quality loop
Steelmans the FINISHED paper end-to-end, like a real journal reviewer would.
"""

import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

# Add src/ to path so we can import sibling modules
sys.path.insert(0, str(Path(__file__).parent))
from regression_tests import extract_fixtures, save_fixtures, check_regressions


SHELL_ROOT = Path(__file__).parent.parent
PAPERS_DIR = SHELL_ROOT / "papers"
LOGS_DIR = SHELL_ROOT / "logs"

# On Windows, npm-installed CLIs need the .cmd wrapper for subprocess
CLAUDE_CMD = "claude.cmd" if sys.platform == "win32" else "claude"


class TeeWriter:
    """Writes to both a file and the original stream (stdout/stderr)."""

    def __init__(self, log_file: Path, original_stream):
        self.log_file = open(log_file, "a", encoding="utf-8", errors="replace")
        self.original = original_stream

    def write(self, text):
        self.original.write(text)
        self.original.flush()
        self.log_file.write(text)
        self.log_file.flush()

    def flush(self):
        self.original.flush()
        self.log_file.flush()

    def close(self):
        self.log_file.close()


def log(msg: str, log_file: Path | None = None):
    """Print a message and optionally append it to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    if log_file:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

STEELMAN_PROMPT = """You are a senior associate editor who has reviewed 200+ papers.
You have just read a complete academic paper. Your job is to write a referee
report — the kind that would come back from a top journal.

Be specific. Do not say "the proof could be stronger." Say exactly which step
is weak, what's missing, and what would fix it.

Organize your critique into:

## STRUCTURAL ISSUES (would cause rejection)
Numbered list. Each item: what's wrong, where in the paper, and what a
revision must do to fix it. If none, write "None identified."

## FRAMING & POSITIONING ISSUES (would cause major revision)
Numbered list. Terminology inflation, overclaiming, literature
mischaracterization, scope disguise. If none, write "None identified."

## MINOR ISSUES (would appear in a revise-and-resubmit letter)
Numbered list. If none, write "None identified."

## VERDICT
One of:
- ACCEPT: No structural issues. Ready for publication.
- MAJOR_REVISION: Structural issues exist but are fixable.
- REJECT: Fundamental problems that require a new approach.

## REVISION INSTRUCTIONS
If not ACCEPT: Write a numbered list of specific, actionable instructions
that the Author must follow in the next draft. Each instruction should be
concrete enough that a different author could execute it without ambiguity.
If ACCEPT: Write "No revisions needed."

---

Here is the paper:

{paper_text}

---

Here is the frozen specification this paper was written against:

{frozen_spec}
"""


def extract_base_slug(init_file: Path) -> str:
    """Extract the SLUG from an init file."""
    text = init_file.read_text(encoding="utf-8")
    match = re.search(r"^SLUG:\s*(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip().upper()
    return init_file.stem.replace("init_", "").upper()


def find_latest_project(base_slug: str) -> Path | None:
    """Find the most recently created project directory for a given base slug."""
    matches = sorted(PAPERS_DIR.glob(f"{base_slug}[-_]*"), key=lambda p: p.name)
    return matches[-1] if matches else None


def run_paper(init_file: Path, run_num: int, meta_log: Path) -> Path | None:
    """Run a paper through the SHELL pipeline. Returns the project directory.
    Captures all Claude CLI output to a per-run log file."""
    base_slug = extract_base_slug(init_file)
    before = set(PAPERS_DIR.glob(f"{base_slug}[-_]*"))

    run_log = LOGS_DIR / f"{base_slug}_run{run_num}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    log(f"GENERATING PAPER: {init_file.name}", meta_log)
    log(f"Run log: {run_log}", meta_log)

    # Claude CLI uses an interactive terminal renderer that doesn't work
    # when stdout is piped or wrapped. Let it run natively on the terminal.
    # Claude's own output is captured in the project's innovation_log.md,
    # state_vector.md, and paper.md. The quality loop logs its own decisions
    # to the meta log.
    log(f"--- Claude CLI running (output appears below) ---", meta_log)

    # Run Claude in interactive mode via Popen. When the user presses Ctrl+C,
    # it kills Claude but Python survives because we use Popen + wait instead
    # of call (which propagates KeyboardInterrupt and kills Python too).
    log(f"Claude will run interactively. When COMPLETE, press Ctrl+C to continue.", meta_log)
    print(f"\n  >>> When Claude shows the completion summary and the prompt, press Ctrl+C <<<\n")

    import signal
    # Ignore SIGINT in the parent so Ctrl+C only kills the child (Claude)
    old_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)

    process = subprocess.Popen(
        [CLAUDE_CMD, "--dangerously-skip-permissions", str(init_file)],
        cwd=str(SHELL_ROOT),
    )
    process.wait()
    returncode = process.returncode

    # Restore original signal handler
    signal.signal(signal.SIGINT, old_handler)

    print(f"\n  >>> Claude exited — continuing quality loop <<<\n")
    log(f"--- Claude CLI finished (exit code {returncode}) ---", meta_log)

    # After Claude finishes, copy the project's innovation log to our run log
    # so we have a record of what happened
    with open(run_log, "w", encoding="utf-8") as lf:
        lf.write(f"# SHELL Pipeline Log — {init_file.name} — Run {run_num}\n")
        lf.write(f"# Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        lf.write(f"# Exit code: {returncode}\n")
        lf.write(f"{'='*80}\n\n")
        # Find the new project dir and copy its innovation log
        after_dirs = set(PAPERS_DIR.glob(f"{base_slug}[-_]*")) - before
        if after_dirs:
            new_dir = max(after_dirs, key=lambda p: p.name)
            for logfile in ["innovation_log.md", "state_vector.md"]:
                src = new_dir / logfile
                if src.exists():
                    lf.write(f"\n--- {logfile} ---\n")
                    lf.write(src.read_text(encoding="utf-8", errors="replace"))
                    lf.write("\n")

    log(f"Pipeline finished (exit code {returncode}). Log: {run_log.name}", meta_log)

    after = set(PAPERS_DIR.glob(f"{base_slug}[-_]*"))
    new_dirs = after - before
    if new_dirs:
        project_dir = max(new_dirs, key=lambda p: p.name)
        log(f"Created: {project_dir.name}", meta_log)
        # Copy the run log into the project directory too
        shutil.copy2(run_log, project_dir / "pipeline_log.txt")
        return project_dir

    latest = find_latest_project(base_slug)
    if latest and latest not in before:
        shutil.copy2(run_log, latest / "pipeline_log.txt")
        return latest

    log("WARNING: Could not identify new project directory", meta_log)
    return None


def steelman_paper(project_dir: Path, run_num: int, meta_log: Path) -> str:
    """Run a full-paper Steelman review via Claude CLI. Returns the critique."""
    paper_path = project_dir / "paper.md"
    spec_path = project_dir / "frozen_spec.md"

    if not paper_path.exists():
        return "ERROR: paper.md not found — pipeline may have halted."

    paper_text = paper_path.read_text(encoding="utf-8")
    frozen_spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else "(not found)"

    prompt = STEELMAN_PROMPT.format(paper_text=paper_text, frozen_spec=frozen_spec)

    log(f"STEELMAN REVIEW: {project_dir.name} ({len(paper_text):,} chars)", meta_log)
    print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write(prompt)
        tmp_path = f.name

    try:
        with open(tmp_path, "r", encoding="utf-8") as prompt_file:
            result = subprocess.run(
                [CLAUDE_CMD, "-p", "--output-format", "text"],
                stdin=prompt_file,
                capture_output=True,
                text=True,
                timeout=300,
                encoding="utf-8",
                errors="replace",
            )
        if result.returncode == 0 and result.stdout.strip():
            critique = result.stdout.strip()
        else:
            critique = f"ERROR: Claude CLI returned: {result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        critique = "ERROR: Steelman review timed out (300s)"
    except Exception as e:
        critique = f"ERROR: {e}"
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    # Save critique to project directory
    critique_path = project_dir / "steelman_full_paper_critique.md"
    critique_path.write_text(
        f"# Full-Paper Steelman Critique\n\n"
        f"**Project:** {project_dir.name}\n"
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        f"---\n\n{critique}",
        encoding="utf-8",
    )
    log(f"Saved: {critique_path.name}", meta_log)

    # Also log the critique to the meta log
    with open(meta_log, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"STEELMAN CRITIQUE — Run {run_num}\n")
        f.write(f"{'='*60}\n")
        f.write(critique)
        f.write(f"\n{'='*60}\n\n")

    return critique


def extract_verdict(critique: str) -> str:
    """Extract the verdict from a Steelman critique."""
    if "ACCEPT" in critique and "MAJOR_REVISION" not in critique and "REJECT" not in critique:
        # Check it's in the verdict section, not just mentioned
        verdict_match = re.search(
            r"##\s*VERDICT\s*\n+\s*[-*]?\s*(ACCEPT|MAJOR_REVISION|REJECT)",
            critique,
            re.IGNORECASE,
        )
        if verdict_match:
            return verdict_match.group(1).upper()
    for v in ["REJECT", "MAJOR_REVISION", "ACCEPT"]:
        if re.search(rf"##\s*VERDICT.*?{v}", critique, re.IGNORECASE | re.DOTALL):
            return v
    return "UNKNOWN"


def extract_revision_instructions(critique: str) -> str:
    """Extract the revision instructions section from a critique."""
    match = re.search(
        r"##\s*REVISION INSTRUCTIONS\s*\n(.*?)(?:\n##|\Z)",
        critique,
        re.DOTALL | re.IGNORECASE,
    )
    if match:
        instructions = match.group(1).strip()
        if "no revisions needed" in instructions.lower():
            return ""
        return instructions
    return ""


def extract_structural_issues(critique: str) -> str:
    """Extract structural issues section from a critique."""
    match = re.search(
        r"##\s*STRUCTURAL ISSUES.*?\n(.*?)(?:\n##|\Z)",
        critique,
        re.DOTALL | re.IGNORECASE,
    )
    if match:
        issues = match.group(1).strip()
        if "none identified" in issues.lower():
            return ""
        return issues
    return ""


def patch_init_file(init_file: Path, critique: str, run_number: int) -> None:
    """Inject Steelman revision instructions into the init file."""
    revision_instructions = extract_revision_instructions(critique)
    structural_issues = extract_structural_issues(critique)

    if not revision_instructions and not structural_issues:
        print("  No revision instructions to inject.")
        return

    text = init_file.read_text(encoding="utf-8")

    patch_lines = [
        "",
        f"# === STEELMAN REVISION BRIEF (from run {run_number}) ===",
        f"# The following issues were identified by a full-paper Steelman review.",
        f"# The next run MUST address every item. These are not suggestions.",
        "",
    ]

    if structural_issues:
        patch_lines.append("# STRUCTURAL ISSUES TO FIX:")
        patch_lines.append(structural_issues)
        patch_lines.append("")

    if revision_instructions:
        patch_lines.append("# REVISION INSTRUCTIONS:")
        patch_lines.append(revision_instructions)
        patch_lines.append("")

    patch = "\n".join(patch_lines)

    # Insert before KNOWN_DRIFT_RISKS or at end of INPUTS section
    marker = "KNOWN_DRIFT_RISKS:"
    if marker in text:
        text = text.replace(marker, patch + "\n" + marker)
    else:
        # Find end of inputs section (before --- separator or ## SETUP)
        setup_match = re.search(r"\n---\s*\n.*?## SETUP", text, re.DOTALL)
        if setup_match:
            text = text[:setup_match.start()] + patch + text[setup_match.start():]
        else:
            text += patch

    init_file.write_text(text, encoding="utf-8")
    issue_count = len(re.findall(r"^\d+\.", patch, re.MULTILINE))
    print(f"  Patched {init_file.name} with {issue_count} revision items")


def extract_metrics(project_dir: Path) -> dict:
    """Extract quality metrics from a completed paper run."""
    metrics = {
        "project": project_dir.name,
        "paper_exists": (project_dir / "paper.md").exists(),
        "total_rejections": 0,
        "steelman_structural_flags": 0,
        "steelman_verdict": "N/A",
        "citations_verified": 0,
        "citations_total": 0,
        "orchestrator_verdict": "UNKNOWN",
        "halted": False,
    }

    log_path = project_dir / "innovation_log.md"
    if log_path.exists():
        log_text = log_path.read_text(encoding="utf-8")
        metrics["total_rejections"] = len(re.findall(r"action:\s*REJECT", log_text))
        metrics["steelman_structural_flags"] = len(
            re.findall(r"action:\s*STRUCTURAL_FLAG", log_text)
        )

    cite_path = project_dir / "outputs" / "citation_verification.md"
    if cite_path.exists():
        cite_text = cite_path.read_text(encoding="utf-8")
        verified = len(re.findall(r"VERIFIED", cite_text))
        unverified = len(re.findall(r"UNVERIFIED", cite_text))
        metrics["citations_verified"] = verified
        metrics["citations_total"] = verified + unverified

    audit_path = project_dir / "outputs" / "orchestrator_audit.md"
    if audit_path.exists():
        audit_text = audit_path.read_text(encoding="utf-8")
        if "PROCESS_CLEAN" in audit_text:
            metrics["orchestrator_verdict"] = "PROCESS_CLEAN"
        elif "PROCESS_FLAG" in audit_text:
            metrics["orchestrator_verdict"] = "PROCESS_FLAG"

    sv_path = project_dir / "state_vector.md"
    if sv_path.exists():
        sv_text = sv_path.read_text(encoding="utf-8")
        metrics["halted"] = "STATUS: HALTED" in sv_text

    critique_path = project_dir / "steelman_full_paper_critique.md"
    if critique_path.exists():
        critique = critique_path.read_text(encoding="utf-8")
        metrics["steelman_verdict"] = extract_verdict(critique)

    return metrics


def format_metrics_table(all_metrics: list[dict]) -> str:
    """Format a comparison table of metrics across runs."""
    lines = []
    lines.append("| Metric | " + " | ".join(m["project"] for m in all_metrics) + " |")
    lines.append("|--------|" + "|".join("------" for _ in all_metrics) + "|")

    rows = [
        ("Paper complete", "paper_exists"),
        ("Halted", "halted"),
        ("Total rejections", "total_rejections"),
        ("In-pipeline Steelman flags", "steelman_structural_flags"),
        ("Full-paper Steelman verdict", "steelman_verdict"),
        ("Citations verified", "citations_verified"),
        ("Citations total", "citations_total"),
        ("Orchestrator verdict", "orchestrator_verdict"),
    ]

    for label, key in rows:
        vals = " | ".join(str(m.get(key, "—")) for m in all_metrics)
        lines.append(f"| {label} | {vals} |")

    return "\n".join(lines)


def write_report(all_metrics: list[dict], critiques: list[str], init_file: Path) -> Path:
    """Write the quality loop comparison report."""
    report_path = SHELL_ROOT / "outputs" / "quality_loop_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Quality Loop Report",
        "",
        f"**Init file:** {init_file.name}",
        f"**Runs:** {len(all_metrics)}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Comparison",
        "",
        format_metrics_table(all_metrics),
        "",
    ]

    # Convergence analysis
    verdicts = [m["steelman_verdict"] for m in all_metrics]
    lines.append("## Convergence")
    lines.append("")
    for i, v in enumerate(verdicts):
        lines.append(f"- Run {i+1}: **{v}**")
    lines.append("")

    if verdicts and verdicts[-1] == "ACCEPT":
        lines.append("Converged: Steelman accepted the final run.")
    elif len(verdicts) >= 2 and verdicts[-1] == "MAJOR_REVISION" and verdicts[0] == "REJECT":
        lines.append("Improving: moved from REJECT to MAJOR_REVISION.")
    lines.append("")

    # Recommend best run
    completed = [m for m in all_metrics if m["paper_exists"] and not m["halted"]]
    if completed:
        # Prefer ACCEPT verdict, then fewest rejections
        def score(m):
            v = {"ACCEPT": 0, "MAJOR_REVISION": 1, "REJECT": 2, "UNKNOWN": 3, "N/A": 3}
            return (v.get(m["steelman_verdict"], 3), m["total_rejections"])
        best = min(completed, key=score)
        lines.append("## Recommended Run")
        lines.append("")
        lines.append(f"**{best['project']}** — Steelman verdict: {best['steelman_verdict']}, "
                      f"rejections: {best['total_rejections']}.")

    # Include critique summaries
    lines.append("")
    lines.append("## Steelman Critiques")
    lines.append("")
    for i, critique in enumerate(critiques):
        verdict = extract_verdict(critique)
        lines.append(f"### Run {i+1} — {verdict}")
        lines.append("")
        # Include just the structural issues and verdict, not the full critique
        structural = extract_structural_issues(critique)
        if structural:
            lines.append("**Structural issues:**")
            lines.append(structural)
        else:
            lines.append("No structural issues identified.")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(
        description="SHELL quality loop — iterative paper optimizer via full-paper Steelman review"
    )
    parser.add_argument(
        "--init", required=True,
        help="Path to init file (e.g., papers/init_sunk_cost.md)"
    )
    parser.add_argument(
        "--max-runs", type=int, default=3,
        help="Maximum number of runs (default: 3)"
    )
    args = parser.parse_args()

    init_file = Path(args.init)
    if not init_file.is_absolute():
        init_file = SHELL_ROOT / init_file
    if not init_file.exists():
        sys.exit(f"ERROR: Init file not found: {init_file}")

    max_runs = args.max_runs
    base_slug = extract_base_slug(init_file)

    # Create logs directory
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    # Terminal transcript — captures everything Claude CLI renders to screen
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    transcript_path = LOGS_DIR / f"terminal_{base_slug}_{timestamp}.log"
    if sys.platform == "win32":
        subprocess.call(
            ["powershell.exe", "-NoProfile", "-Command",
             f"Start-Transcript -Path '{transcript_path}' -Append"],
            timeout=10,
        )

    # Meta log — the quality loop's own log (across all runs)
    meta_log = LOGS_DIR / f"quality_loop_{base_slug}_{timestamp}.log"

    # Backup init file before any modifications
    backup_path = init_file.with_suffix(".md.bak")
    if not backup_path.exists():
        shutil.copy2(init_file, backup_path)
        log(f"Backed up {init_file.name} -> {backup_path.name}", meta_log)

    all_metrics = []
    all_critiques = []
    prev_fixture_path = None

    log(f"{'#'*60}", meta_log)
    log(f"  SHELL QUALITY LOOP", meta_log)
    log(f"  Init: {init_file.name}", meta_log)
    log(f"  Base slug: {base_slug}", meta_log)
    log(f"  Max runs: {max_runs}", meta_log)
    log(f"  Meta log: {meta_log.name}", meta_log)
    log(f"  Strategy: Generate paper -> Full-paper Steelman -> Inject revision -> Regenerate", meta_log)
    log(f"{'#'*60}", meta_log)

    for run_num in range(1, max_runs + 1):
        log(f"", meta_log)
        log(f"{'*'*60}", meta_log)
        log(f"  RUN {run_num}/{max_runs}", meta_log)
        log(f"{'*'*60}", meta_log)

        # Step 1: Generate the paper
        project_dir = run_paper(init_file, run_num, meta_log)
        if project_dir is None:
            log(f"Run {run_num} failed to produce a project directory. Stopping.", meta_log)
            break

        # Step 2: Check if paper was produced
        if not (project_dir / "paper.md").exists():
            log(f"No paper.md produced (pipeline may have halted). Stopping.", meta_log)
            metrics = extract_metrics(project_dir)
            all_metrics.append(metrics)
            all_critiques.append("Pipeline halted — no paper to review.")
            break

        # Step 2b: Extract regression fixtures and check for regressions
        paper_path = project_dir / "paper.md"
        fixtures = extract_fixtures(paper_path)
        fixture_path = project_dir / "regression_fixtures.json"
        save_fixtures(fixtures, fixture_path)
        log(f"Extracted {len(fixtures.get('claims', []))} claims, "
            f"{len(fixtures.get('citations', []))} citations, "
            f"{len(fixtures.get('numerical_results', []))} numerical results", meta_log)

        if run_num > 1 and prev_fixture_path and prev_fixture_path.exists():
            regression_report = check_regressions(paper_path, prev_fixture_path)
            log(f"Regression check: {regression_report.verdict}", meta_log)
            if regression_report.verdict == "REGRESSION":
                log(f"  REGRESSIONS DETECTED:", meta_log)
                for t in regression_report.missing_theorems:
                    log(f"    MISSING: {t}", meta_log)
                for t in regression_report.changed_theorems:
                    log(f"    CHANGED: {t}", meta_log)
                for c in regression_report.missing_citations:
                    log(f"    CITATION DROPPED: {c}", meta_log)
                for n in regression_report.missing_numbers:
                    log(f"    NUMBER LOST: {n}", meta_log)
                # Append regression info to the critique context
                regression_note = f"\n\nREGRESSION WARNING: {regression_report.summary()}"
            else:
                regression_note = ""
                if regression_report.new_theorems:
                    log(f"  New claims added: {len(regression_report.new_theorems)}", meta_log)
        else:
            regression_note = ""

        prev_fixture_path = fixture_path

        # Step 3: Full-paper Steelman review
        critique = steelman_paper(project_dir, run_num, meta_log)
        if regression_note:
            critique += regression_note
        all_critiques.append(critique)

        verdict = extract_verdict(critique)
        log(f"Steelman verdict: {verdict}", meta_log)

        # Step 4: Extract metrics
        metrics = extract_metrics(project_dir)
        all_metrics.append(metrics)

        log(f"Rejections: {metrics['total_rejections']}", meta_log)
        log(f"Citations: {metrics['citations_verified']}/{metrics['citations_total']}", meta_log)

        # Step 5: Check if we're done
        if verdict == "ACCEPT":
            log(f"Steelman ACCEPTED the paper. Quality loop complete.", meta_log)
            break

        if critique.startswith("ERROR:"):
            log(f"Steelman review failed: {critique[:100]}", meta_log)
            break

        # Step 6: Patch init file with revision instructions for next run
        if run_num < max_runs:
            patch_init_file(init_file, critique, run_num)
            log(f"Waiting 10s before next run...", meta_log)
            time.sleep(10)
        else:
            log(f"Max runs ({max_runs}) reached.", meta_log)

    # Write comparison report
    if all_metrics:
        report_path = write_report(all_metrics, all_critiques, init_file)

        # Restore original init file
        if backup_path.exists():
            shutil.copy2(backup_path, init_file)

        verdicts = [extract_verdict(c) for c in all_critiques]

        log(f"", meta_log)
        log(f"{'#'*60}", meta_log)
        log(f"  QUALITY LOOP COMPLETE", meta_log)
        log(f"  Runs: {len(all_metrics)}", meta_log)
        log(f"  Verdicts: {' -> '.join(verdicts)}", meta_log)
        log(f"  Report: {report_path}", meta_log)
        log(f"  Meta log: {meta_log}", meta_log)
        log(f"  Per-run logs: {LOGS_DIR}", meta_log)
        log(f"  Terminal transcript: {transcript_path}", meta_log)
        log(f"  Restored original {init_file.name} from backup", meta_log)
        log(f"{'#'*60}", meta_log)

    # Stop terminal transcript
    if sys.platform == "win32":
        subprocess.call(
            ["powershell.exe", "-NoProfile", "-Command", "Stop-Transcript"],
            timeout=10,
        )


if __name__ == "__main__":
    main()
