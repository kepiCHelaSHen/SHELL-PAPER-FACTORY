#!/usr/bin/env python3
"""
epistemic_metrics.py — Measures reasoning quality across SHELL paper runs.

Read-only. Does not modify any files, prompts, or pipeline behavior.
Reads innovation logs, quality loop reports, regression fixtures, and papers
to compute quantitative epistemic metrics.

Usage:
    # Metrics for a single project
    python src/epistemic_metrics.py --project papers/CONSPIRACY_BAYES_2026-05-11_001

    # Compare metrics across multiple runs of the same paper
    python src/epistemic_metrics.py --compare papers/CONSPIRACY_BAYES_2026-05-11_001 papers/CONSPIRACY_BAYES_2026-05-11_002

    # Metrics from a quality loop report
    python src/epistemic_metrics.py --loop-report outputs/quality_loop_report.md
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

SHELL_ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(Path(__file__).parent))
from regression_tests import extract_fixtures


@dataclass
class ProjectMetrics:
    """Metrics for a single paper run."""
    project: str = ""
    paper_exists: bool = False
    paper_lines: int = 0
    halted: bool = False

    # Milestone metrics
    total_milestones: int = 4
    milestones_locked: int = 0
    total_submissions: int = 0
    total_rejections: int = 0
    first_try_accepts: int = 0
    rejection_rate: float = 0.0

    # Steelman metrics
    steelman_structural_flags: int = 0
    steelman_advisory_notes: int = 0
    steelman_novelty_kills: int = 0

    # Claim metrics (from paper.md)
    theorems: int = 0
    lemmas: int = 0
    propositions: int = 0
    corollaries: int = 0
    definitions: int = 0
    total_claims: int = 0

    # Citation metrics
    citations_total: int = 0
    citations_verified: int = 0
    citation_verification_rate: float = 0.0

    # Numerical results
    numerical_results: int = 0

    # Derived metrics
    theorem_density: float = 0.0  # claims per 100 lines
    rejection_convergence: list = field(default_factory=list)  # rejections per milestone


def extract_project_metrics(project_dir: Path) -> ProjectMetrics:
    """Extract all metrics from a completed paper project."""
    m = ProjectMetrics(project=project_dir.name)

    # Paper existence and size
    paper_path = project_dir / "paper.md"
    if paper_path.exists():
        m.paper_exists = True
        m.paper_lines = len(paper_path.read_text(encoding="utf-8").splitlines())

    # Halted?
    sv_path = project_dir / "state_vector.md"
    if sv_path.exists():
        sv = sv_path.read_text(encoding="utf-8")
        m.halted = "STATUS: HALTED" in sv
        # Count locked milestones
        m.milestones_locked = len(re.findall(r"M\d.*LOCKED", sv))

    # Innovation log parsing
    log_path = project_dir / "innovation_log.md"
    if log_path.exists():
        log_text = log_path.read_text(encoding="utf-8")

        # Count submissions and rejections
        submissions = re.findall(r"action:\s*SUBMIT", log_text)
        rejections = re.findall(r"action:\s*REJECT", log_text)
        accepts = re.findall(r"action:\s*ACCEPT", log_text)

        m.total_submissions = len(submissions)
        m.total_rejections = len(rejections)
        m.first_try_accepts = max(0, len(accepts) - len(rejections))

        if m.total_submissions > 0:
            m.rejection_rate = len(rejections) / m.total_submissions

        # Steelman metrics
        m.steelman_structural_flags = len(
            re.findall(r"action:\s*STRUCTURAL_FLAG", log_text)
        )
        m.steelman_advisory_notes = len(
            re.findall(r"action:\s*ADVISORY_ONLY", log_text)
        )
        m.steelman_novelty_kills = len(
            re.findall(r"NOVELTY_KILL", log_text)
        )

        # Per-milestone rejection counts
        for milestone in ["M1", "M2", "M3", "M4"]:
            # Find all entries for this milestone
            pattern = rf"milestone:\s*{milestone}.*?action:\s*REJECT"
            milestone_rejections = len(
                re.findall(pattern, log_text, re.DOTALL)
            )
            m.rejection_convergence.append(milestone_rejections)

    # Claim extraction from paper
    if paper_path.exists():
        fixtures = extract_fixtures(paper_path)
        claims = fixtures.get("claims", [])

        for claim in claims:
            kind = claim.get("kind", "").lower()
            if kind == "theorem":
                m.theorems += 1
            elif kind == "lemma":
                m.lemmas += 1
            elif kind == "proposition":
                m.propositions += 1
            elif kind == "corollary":
                m.corollaries += 1
            elif kind == "definition":
                m.definitions += 1

        m.total_claims = m.theorems + m.lemmas + m.propositions + m.corollaries + m.definitions
        m.numerical_results = len(fixtures.get("numerical_results", []))
        m.citations_total = len(fixtures.get("citations", []))

        if m.paper_lines > 0:
            m.theorem_density = (m.total_claims / m.paper_lines) * 100

    # Citation verification
    cite_path = project_dir / "outputs" / "citation_verification.md"
    if cite_path.exists():
        cite_text = cite_path.read_text(encoding="utf-8")
        verified = len(re.findall(r"VERIFIED", cite_text))
        unverified = len(re.findall(r"UNVERIFIED", cite_text))
        m.citations_verified = verified
        if m.citations_total == 0:
            m.citations_total = verified + unverified
        if m.citations_total > 0:
            m.citation_verification_rate = m.citations_verified / m.citations_total

    return m


def compute_cross_run_metrics(runs: list[ProjectMetrics]) -> dict:
    """Compute metrics that only make sense across multiple runs."""
    if len(runs) < 2:
        return {}

    cross = {
        "total_runs": len(runs),
        "completed_runs": sum(1 for r in runs if r.paper_exists and not r.halted),
        "halted_runs": sum(1 for r in runs if r.halted),
    }

    # Rejection convergence slope
    rejection_counts = [r.total_rejections for r in runs if r.paper_exists]
    if len(rejection_counts) >= 2:
        # Simple slope: (last - first) / (n - 1)
        slope = (rejection_counts[-1] - rejection_counts[0]) / (len(rejection_counts) - 1)
        cross["rejection_slope"] = round(slope, 2)
        cross["rejections_per_run"] = rejection_counts

    # Claim shrinkage rate
    claim_counts = [r.total_claims for r in runs if r.paper_exists]
    if len(claim_counts) >= 2:
        shrinkage = (claim_counts[0] - claim_counts[-1]) / claim_counts[0] if claim_counts[0] > 0 else 0
        cross["claim_shrinkage_rate"] = round(shrinkage, 3)
        cross["claims_per_run"] = claim_counts

    # Paper length trend
    lengths = [r.paper_lines for r in runs if r.paper_exists]
    if len(lengths) >= 2:
        cross["length_trend"] = lengths
        cross["length_change"] = lengths[-1] - lengths[0]

    # Citation stability
    cite_counts = [r.citations_total for r in runs if r.paper_exists]
    if len(cite_counts) >= 2:
        cross["citations_per_run"] = cite_counts

    # Theorem survival (requires regression fixtures)
    # Check if regression fixtures exist for consecutive runs
    completed = [r for r in runs if r.paper_exists]
    if len(completed) >= 2:
        survived = 0
        total_prior = 0
        for i in range(1, len(completed)):
            prior_dir = SHELL_ROOT / "papers" / completed[i - 1].project
            current_dir = SHELL_ROOT / "papers" / completed[i].project
            fixture_path = prior_dir / "regression_fixtures.json"
            current_paper = current_dir / "paper.md"

            if fixture_path.exists() and current_paper.exists():
                try:
                    from regression_tests import check_regressions
                    report = check_regressions(current_paper, fixture_path)
                    prior_fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
                    prior_claims = len(prior_fixtures.get("claims", []))
                    total_prior += prior_claims
                    survived += prior_claims - len(report.missing_theorems) - len(report.changed_theorems)
                except Exception:
                    pass

        if total_prior > 0:
            cross["theorem_survival_rate"] = round(survived / total_prior, 3)

    return cross


def format_single_report(m: ProjectMetrics) -> str:
    """Format a single project's metrics as a readable report."""
    lines = [
        f"# Epistemic Metrics: {m.project}",
        "",
        "## Paper",
        f"- Lines: {m.paper_lines}",
        f"- Complete: {m.paper_exists}",
        f"- Halted: {m.halted}",
        "",
        "## Claims",
        f"- Theorems: {m.theorems}",
        f"- Lemmas: {m.lemmas}",
        f"- Propositions: {m.propositions}",
        f"- Corollaries: {m.corollaries}",
        f"- Definitions: {m.definitions}",
        f"- **Total claims: {m.total_claims}**",
        f"- Claim density: {m.theorem_density:.1f} per 100 lines",
        f"- Numerical results: {m.numerical_results}",
        "",
        "## Pipeline",
        f"- Milestones locked: {m.milestones_locked}/{m.total_milestones}",
        f"- Total submissions: {m.total_submissions}",
        f"- Total rejections: {m.total_rejections}",
        f"- First-try accepts: {m.first_try_accepts}",
        f"- Rejection rate: {m.rejection_rate:.1%}",
        f"- Rejections per milestone: {m.rejection_convergence}",
        "",
        "## Steelman",
        f"- Structural flags: {m.steelman_structural_flags}",
        f"- Advisory notes: {m.steelman_advisory_notes}",
        f"- Novelty kills: {m.steelman_novelty_kills}",
        "",
        "## Citations",
        f"- Total: {m.citations_total}",
        f"- Verified: {m.citations_verified}",
        f"- Verification rate: {m.citation_verification_rate:.0%}",
    ]
    return "\n".join(lines)


def format_comparison_report(runs: list[ProjectMetrics], cross: dict) -> str:
    """Format a comparison report across multiple runs."""
    lines = [
        "# Epistemic Metrics — Cross-Run Comparison",
        f"",
        f"**Runs:** {len(runs)}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    # Comparison table
    headers = ["Metric"] + [r.project for r in runs]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join("------" for _ in headers) + "|")

    rows = [
        ("Paper lines", [str(r.paper_lines) for r in runs]),
        ("Total claims", [str(r.total_claims) for r in runs]),
        ("Theorems", [str(r.theorems) for r in runs]),
        ("Definitions", [str(r.definitions) for r in runs]),
        ("Claim density", [f"{r.theorem_density:.1f}" for r in runs]),
        ("Rejections", [str(r.total_rejections) for r in runs]),
        ("Rejection rate", [f"{r.rejection_rate:.0%}" for r in runs]),
        ("Steelman flags", [str(r.steelman_structural_flags) for r in runs]),
        ("Citations", [str(r.citations_total) for r in runs]),
        ("Citation verify %", [f"{r.citation_verification_rate:.0%}" for r in runs]),
        ("Numerical results", [str(r.numerical_results) for r in runs]),
    ]

    for label, vals in rows:
        lines.append(f"| {label} | " + " | ".join(vals) + " |")

    # Cross-run metrics
    if cross:
        lines.append("")
        lines.append("## Cross-Run Metrics")
        lines.append("")

        if "rejection_slope" in cross:
            slope = cross["rejection_slope"]
            direction = "improving" if slope < 0 else "degrading" if slope > 0 else "stable"
            lines.append(f"- **Rejection convergence slope:** {slope} ({direction})")
            lines.append(f"  Rejections per run: {cross['rejections_per_run']}")

        if "claim_shrinkage_rate" in cross:
            rate = cross["claim_shrinkage_rate"]
            lines.append(f"- **Claim shrinkage rate:** {rate:.1%}")
            lines.append(f"  Claims per run: {cross['claims_per_run']}")

        if "theorem_survival_rate" in cross:
            lines.append(f"- **Theorem survival rate:** {cross['theorem_survival_rate']:.1%}")

        if "length_change" in cross:
            change = cross["length_change"]
            direction = "shorter" if change < 0 else "longer" if change > 0 else "same"
            lines.append(f"- **Length change:** {change:+d} lines ({direction})")
            lines.append(f"  Lengths per run: {cross['length_trend']}")

        if "citations_per_run" in cross:
            lines.append(f"- **Citations per run:** {cross['citations_per_run']}")

    # Assessment
    lines.append("")
    lines.append("## Assessment")
    lines.append("")

    completed = [r for r in runs if r.paper_exists and not r.halted]
    if not completed:
        lines.append("No completed runs to assess.")
    else:
        latest = completed[-1]
        first = completed[0]

        if latest.total_rejections < first.total_rejections:
            lines.append("Pipeline is converging: rejections decreased across runs.")
        elif latest.total_rejections > first.total_rejections:
            lines.append("WARNING: Rejections increased across runs. Revision briefs may be introducing new problems.")
        else:
            lines.append("Rejections stable across runs.")

        if cross.get("claim_shrinkage_rate", 0) > 0.3:
            lines.append("WARNING: Claim shrinkage >30%. Steelman may be overcorrecting — important results being dropped.")
        elif cross.get("claim_shrinkage_rate", 0) < -0.1:
            lines.append("Claims growing across runs — scope may be expanding rather than tightening.")

        if cross.get("theorem_survival_rate", 1.0) < 0.8:
            lines.append("WARNING: Theorem survival <80%. Significant regression between runs.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="SHELL epistemic metrics — measures reasoning quality (read-only)"
    )
    parser.add_argument(
        "--project", nargs="+",
        help="Path(s) to project directory(ies)"
    )
    parser.add_argument(
        "--compare", nargs="+",
        help="Compare metrics across multiple project directories"
    )
    parser.add_argument(
        "--output",
        help="Write report to file (default: print to stdout)"
    )
    args = parser.parse_args()

    projects = args.compare or args.project
    if not projects:
        parser.error("Provide --project or --compare with project directory path(s)")

    # Resolve paths
    dirs = []
    for p in projects:
        d = Path(p)
        if not d.is_absolute():
            d = SHELL_ROOT / d
        if not d.exists():
            print(f"WARNING: {d} does not exist, skipping", file=sys.stderr)
            continue
        dirs.append(d)

    if not dirs:
        sys.exit("ERROR: No valid project directories found")

    # Extract metrics
    all_metrics = [extract_project_metrics(d) for d in dirs]

    # Format report
    if len(all_metrics) == 1:
        report = format_single_report(all_metrics[0])
    else:
        cross = compute_cross_run_metrics(all_metrics)
        report = format_comparison_report(all_metrics, cross)

    # Output
    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = SHELL_ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"Report written to {out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
