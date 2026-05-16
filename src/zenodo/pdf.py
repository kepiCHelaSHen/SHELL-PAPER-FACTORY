"""Markdown to PDF conversion via pandoc."""

import subprocess
import shutil
import os
from pathlib import Path

# MiKTeX common install locations on Windows
_MIKTEX_PATHS = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/MiKTeX/miktex/bin/x64",
    Path("C:/Program Files/MiKTeX/miktex/bin/x64"),
    Path("C:/Users") / os.environ.get("USERNAME", "z") / "AppData/Local/Programs/MiKTeX/miktex/bin/x64",
]


def _extend_path():
    """Add MiKTeX to PATH if not already there."""
    for p in _MIKTEX_PATHS:
        if p.exists() and str(p) not in os.environ.get("PATH", ""):
            os.environ["PATH"] = str(p) + os.pathsep + os.environ.get("PATH", "")
            return


_PANDOC_PATHS = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "Pandoc",
    Path("C:/Program Files/Pandoc"),
    Path("C:/Users") / os.environ.get("USERNAME", "z") / "AppData/Local/Pandoc",
]


def pandoc_available() -> bool:
    """Check if pandoc is installed."""
    _extend_path()
    # Also add pandoc paths
    for p in _PANDOC_PATHS:
        if p.exists() and str(p) not in os.environ.get("PATH", ""):
            os.environ["PATH"] = str(p) + os.pathsep + os.environ.get("PATH", "")
    return shutil.which("pandoc") is not None


def detect_pdf_engine() -> str | None:
    """Detect the best available PDF engine."""
    _extend_path()
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
            cmd, capture_output=True, text=True, timeout=300
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
        print("  WARNING: pandoc timed out after 300s. Skipping PDF.")
        print("  (First run may be slow as MiKTeX downloads LaTeX packages.)")
        return False
    except FileNotFoundError:
        print("  WARNING: pandoc not found at runtime. Skipping PDF.")
        return False
