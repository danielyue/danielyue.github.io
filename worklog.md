# Worklog

## 2026-07-16 — AIEI fellowship + data-center press coverage

- Bio (`data/site.yml`): new paragraph "I am also a Senior Fellow of the
  Microsoft AI Economy Institute…" (links to Microsoft's Cohort-3 announcement)
  + the J-PAL Science for Progress affiliation; Fortune added to the
  FT/SCMP press list; all `<strong>` emphasis removed from the bio per Daniel.
- Data-center paper card (`data/papers.yml`): The Conversation article added
  to `links`; new `media:` list with Fortune, Yahoo Finance, Futurism.
- Conventions (recorded in the `/personal-profiles` skill): bio press sentence
  names outlets only (one link per outlet, FT-tier names); lower-tier pickups
  and repeat outlets go on paper cards' `media:` lists.
- Commits: `fa9c76b`, `a955b6b`, `9819933`, `875992f`. CV updated in parallel
  (Overleaf + Drive `DNY_CV`) with the same content.

## 2026-04-22 — Initial setup

- Created repo at `~/Code/danielyue.github.io/` for the personal academic site
  (successor to the Google Sites page).
- Front-end (single-file `index.html` with inline fallback `DATA`, loads
  `content.json` at runtime) provided as a zip. Design by Daniel; content
  migrated from the prior Google Sites page.
- Initially scaffolded as a Quarto project, then pivoted: since the front-end
  does all rendering client-side and there are no `.qmd` files, Quarto was
  pure overhead. Simplified to a plain Python build.
- Build pipeline:
  - `data/site.yml`, `data/papers.yml`, `data/courses.yml` — source of truth
  - `scripts/build.py` — compiles YAML into `_site/content.json` and copies
    `index.html`, `portrait.png`, `uploads/` into `_site/`
- GitHub Actions workflow (`.github/workflows/deploy.yml`) runs the build and
  deploys `_site/` to GitHub Pages via `actions/deploy-pages@v4`.
- Published at <https://danielyue.github.io/> via the personal Pages convention
  (repo name matches username → served from the Actions artifact).

Last updated: 2026-07-16
