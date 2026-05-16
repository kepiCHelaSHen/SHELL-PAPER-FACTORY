"""Configuration loader for Zenodo publishing."""

import os
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

BASE = Path("C:/PROJECTS/SHELL")
DEFAULT_CONFIG = BASE / "publish_config.yaml"
ENV_FILE = BASE / "api.env"


def load_config(config_path: Path = None) -> dict:
    """Load publish_config.yaml."""
    if yaml is None:
        raise RuntimeError("pyyaml required: pip install pyyaml")
    path = config_path or DEFAULT_CONFIG
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_tokens() -> dict:
    """Load Zenodo tokens from environment or api.env.

    Returns dict with 'sandbox' and 'production' keys.
    Raises RuntimeError if tokens are empty.
    """
    tokens = {
        "sandbox": os.environ.get("ZENODO_SANDBOX_TOKEN", ""),
        "production": os.environ.get("ZENODO_TOKEN", ""),
    }

    # Fall back to api.env file
    if not tokens["sandbox"] or not tokens["production"]:
        if ENV_FILE.exists():
            for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("ZENODO_SANDBOX_TOKEN="):
                    tokens["sandbox"] = line.split("=", 1)[1].strip().strip('"')
                elif line.startswith("ZENODO_TOKEN="):
                    tokens["production"] = line.split("=", 1)[1].strip().strip('"')

    # Validate
    if not tokens["sandbox"]:
        raise RuntimeError(
            "ZENODO_SANDBOX_TOKEN is empty. Set it in api.env or environment.\n"
            "Get one at: https://sandbox.zenodo.org/account/settings/applications/"
        )
    if not tokens["production"]:
        raise RuntimeError(
            "ZENODO_TOKEN is empty. Set it in api.env or environment.\n"
            "Get one at: https://zenodo.org/account/settings/applications/"
        )

    return tokens


def get_base_url(sandbox: bool) -> str:
    """Return the appropriate Zenodo API base URL."""
    if sandbox:
        return "https://sandbox.zenodo.org/api"
    return "https://zenodo.org/api"
