# danielyue.github.io — Claude Context

Personal academic website for Daniel Yue. Live at <https://danielyue.github.io/>.

## What this repo is

A content-driven static site. The front-end (`index.html`) is a single
self-contained HTML file with inline CSS and JS. It fetches `content.json`
at load time to populate the page. YAML files under `data/` are the source
of truth; `scripts/build.py` compiles them into `_site/content.json` and
copies static assets into `_site/`.

No Quarto, no framework — just Python + HTML. If blog posts or other
`.qmd`-driven pages become useful later, adding Quarto on top is
straightforward (the current build script already isolates the content
pipeline).

## Update workflow

1. Edit YAML under `data/`
2. `git commit && git push` to main
3. GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys

## Local preview

```bash
uv run scripts/build.py
python3 -m http.server --directory _site 8000
# open http://localhost:8000
```

## Key files

| File | Purpose |
|------|---------|
| `data/site.yml` | Affiliation, bio, contact, hero lines, updated date |
| `data/papers.yml` | Papers (working + published), sorted newest-first |
| `data/courses.yml` | Courses taught |
| `scripts/build.py` | YAML + static → `_site/` |
| `index.html` | Front-end (edit rarely, for design changes only) |
| `.github/workflows/deploy.yml` | GitHub Actions pipeline |

## Conventions

- Paper authors: `"Daniel Yue"` is auto-highlighted; keep that exact spelling.
- Paper `status`: `"Working Paper"` or `"Published"`. A `review` field on
  working papers surfaces R&R / revision states.
- Link `label` should be the source name (`"SSRN"`, `"arXiv"`, `"ACM"`), not
  a generic word like `"PDF"` or `"Paper"`.
- `_site/` and `content.json` are gitignored — regenerated on every build.

## Python tooling

Uses `uv` per the user's global convention. `build.py` has a PEP 723 inline
script header so it runs via `uv run scripts/build.py` without a dedicated
venv.

## Worklog

See `worklog.md` — update after any substantive change.
