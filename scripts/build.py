#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
# ]
# ///
"""Build the static site into _site/.

Reads source YAML from data/, compiles it into content.json, and copies the
front-end assets (index.html, portrait.png, uploads/) into _site/. The
resulting _site/ is a self-contained directory that can be served locally
with `python3 -m http.server --directory _site 8000` or uploaded to GitHub
Pages by the deploy workflow.

Run directly:

    uv run scripts/build.py
"""

from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SITE_DIR = REPO_ROOT / "_site"

# Static files + directories copied verbatim into _site/.
STATIC_ASSETS = [
    "index.html",
    "portrait.png",
    "favicon.svg",
    "uploads",
]


def load_yaml(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_content() -> dict:
    site = load_yaml(DATA_DIR / "site.yml") or {}
    papers = load_yaml(DATA_DIR / "papers.yml") or []
    courses = load_yaml(DATA_DIR / "courses.yml") or []

    return {
        "_comment": (
            "GENERATED FILE — do not edit. Source of truth lives in data/*.yml. "
            "Regenerate via `uv run scripts/build.py`."
        ),
        "affiliation": site["affiliation"],
        "cv": site["cv"],
        "contact": site["contact"],
        "heroLines": site["heroLines"],
        "bio": site["bio"],
        "papers": papers,
        "courses": courses,
        "updated": site.get("updated") or dt.date.today().strftime("%B %Y"),
    }


def copy_static(src: Path, dst: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)


def main() -> int:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    content = build_content()
    (SITE_DIR / "content.json").write_text(
        json.dumps(content, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    for name in STATIC_ASSETS:
        src = REPO_ROOT / name
        if not src.exists():
            print(f"warning: static asset missing — {name}", file=sys.stderr)
            continue
        copy_static(src, SITE_DIR / name)

    n_papers = len(content["papers"])
    n_courses = len(content["courses"])
    print(f"built _site/ — {n_papers} papers, {n_courses} courses")
    return 0


if __name__ == "__main__":
    sys.exit(main())
