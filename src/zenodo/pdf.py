"""Markdown to PDF conversion via pandoc."""

import subprocess
import shutil
from pathlib import Path


def pandoc_available() -> bool:
    """Check if pandoc is installed."""
    return shutil.which("pandoc") is not None


def detect_pdf_engine() -> str | None:
    """Detect the best available PDF engine."""
    for engine in ("xelatex", "pdflatex", "wkhtmltopdf"):
        if shutil.which(engine):
            return engine
    return None


def render_pdf(paper_md: Path, output_pdf: Path, title: str, author: str) -> bool:
    """Convert markdown to PDF via pandoc.

    Returns True if PDF rendered successfully, False otherwise.
    Falls back through available PDF engines.
    """
    if not pandoc_available():
        print("  WARNING: pandoc not installed. Skipping PDF, uploading markdown only.")
        print("  Install: https://pandoc.org/installing.html")
        return False

    engine = detect_pdf_engine()
    if not engine:
        print("  WARNING: No PDF engine found (xelatex, pdflatex, wkhtmltopdf).")
        print("  Skipping PDF, uploading markdown only.")
        return False

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc", str(paper_md),
        "-o", str(output_pdf),
        f"--pdf-engine={engine}",
        f"--metadata=title:{title}",
        f"--metadata=author:{author}",
        "--variable=geometry:margin=1in",
        "--variable=fontsize:11pt",
    ]

    # xelatex/pdflatex support more options
    if engine in ("xelatex", "pdflatex"):
        cmd.extend([
            "--variable=linestretch:1.5",
            "--number-sections",
        ])

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0 and output_pdf.exists():
            print(f"  PDF rendered: {output_pdf.name} ({output_pdf.stat().st_size // 1024}KB)")
            return True
        else:
            print(f"  WARNING: pandoc failed (exit {result.returncode})")
            if result.stderr:
                # Print first 3 lines of error
                for line in result.stderr.splitlines()[:3]:
                    print(f"    {line}")
            return False
    except subprocess.TimeoutExpired:
        print("  WARNING: pandoc timed out after 120s. Skipping PDF.")
        return False
    except FileNotFoundError:
        print("  WARNING: pandoc not found at runtime. Skipping PDF.")
        return False
