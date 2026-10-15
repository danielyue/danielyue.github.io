# Worklog

## 2026-10-14 -- paper status labels after the PNAS R&R

- Open-models paper now "2nd Revise & Resubmit / PNAS"; I, Google now "2nd Revise & Resubmit / Management
  Science"; PyTorch paper now "Revise & Resubmit / Organization Science" (`data/papers.yml`).
- `index.html` rendering: a review status replaces the "Working Paper" label; the journal sits on its own darker
  line (`.review .journal`) and "&" stays with the next word, so nothing wraps alone in the narrow margin column.
  Published papers show only the venue badge (plain "Published" only when no venue is given).
- Checked in a local preview before each push; all three deploys succeeded.
- Commits: `743316b` (labels), `93bbaf3` (layout), `6f6ee7d` (Org Sci label).

## 2026-10-09 -- bio press sentence, trimmed press chips, News section

- Bio: press outlets moved out of the awards clause into their own unlinked
  sentence in the same paragraph (FT, NPR's Morning Edition, CNN, Fortune,
  SCMP).
- Press chips: CNN Business removed from the data-center paper (the piece was
  about AI and inflation, not the paper); NPR relabeled "NPR Morning Edition";
  MIT Sloan removed from the open-models paper.
- New News section at the bottom of the page, driven by `data/news.yml`
  (personal updates and coverage, newest first); `scripts/build.py` adds it to
  `content.json`. Previewed locally before pushing.

## 2026-10-09 -- data-center press: CNN Business, NPR, AJC

- Added CNN Business (9/28, quotes Daniel), NPR (9/22, quotes Daniel) and the
  AJC (7/13, Conversation reprint) to the data-center paper's `media:` list,
  at Daniel's request. Links checked (HTTP 200); build OK.
- Not added: FOX45 Baltimore (9/24), which credits Daniel with a line Yiyang
  said in the Sinclair taping.

## 2026-09-25 -- GoatCounter analytics access notes

- Analytics check only; no site changes. GoatCounter is live on the site
  (`data/site.yml` `analytics.goatcounter_code: "danielyue"`); the dashboard
  is <https://danielyue.goatcounter.com> and needs a login.
- Account login email is `daniel.yue@scheller.gatech.edu` (signed up
  2026-04-24; welcome email is in the GT Archive folder). The password is not
  in 1Password, and the public visitor-counter setting is off, so the counter
  JSON endpoints return 403.
- Next step: recover the password (Chrome saved passwords, or "Forgot
  password?"), save it to 1Password, and store a read-only API key in
  `Agent Vault` so agents can pull stats without a browser login.

## 2026-07-30 — KERA + New Lede coverage added to the data-center paper

- Data-center paper card (`data/papers.yml`): added **The New Lede** to
  `media:` —
  <https://www.thenewlede.org/2026/07/kansas-ai-data-center-opposition/>
  ("The Kansas community fighting data centers before they arrive", Jul 2026).
  Interview 7/15; the piece quotes Daniel twice and links the SSRN paper
  directly.
- Data-center paper card (`data/papers.yml`): added `KERA News (NPR)` to
  `media:` —
  <https://www.keranews.org/news/2026-07-27/do-data-centers-benefit-economy>
  ("Are data centers actually going to help the economy?", Miranda Suarez,
  KERA/NTX Now, published 2026-07-27). Prerecorded interview taped 7/23; the
  article is an edited Q&A with the audio segment embedded.
- Follows the recorded convention: lower-tier pickups and repeat outlets go on
  the paper card's `media:` list rather than the bio press sentence.
- Open question for a later pass: The Conversation piece sits under `links:`
  (correct — it is self-authored) so it does not render in the coverage row;
  consider cross-listing it under `media:` as well.
- Build verified locally (`uv run scripts/build.py`); coverage row now reads
  Fortune · Yahoo Finance · Futurism · KERA News (NPR).

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

Last updated: 2026-10-14
