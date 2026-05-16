"""SHELL Zenodo Publishing Pipeline.

Usage:
    python -m src.zenodo                              # Default config
    python -m src.zenodo --config path/to/config.yaml # Custom config
    python -m src.zenodo --sandbox-only               # Skip production
    python -m src.zenodo --papers SLUG1 SLUG2         # Subset
    python -m src.zenodo --skip-pdf                   # No PDF rendering
"""
