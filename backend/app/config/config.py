"""Configuration module."""
from __future__ import annotations

from pathlib import Path

from dynaconf import Dynaconf

current_dir = Path(__file__).parent.absolute()

settings = Dynaconf(
    root_path=current_dir,
    settings_files=['settings.toml'],
    environment=True,
    default_env='default',
)
