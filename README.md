# danielyue.github.io

Personal academic website for Daniel Yue. Live at <https://danielyue.github.io/>.

Content-driven static site. Source of truth is YAML under `data/`; a Python
build step compiles that into `content.json` and assembles a self-contained
`_site/` directory that the single-file front-end (`index.html`) fetches at
load time.

## Layout

```
.
├── data/                    Source of truth — edit these
│   ├── site.yml             Bio, affiliation, contact, hero lines
│   ├── papers.yml           Papers (working + published)
│   └── courses.yml          Courses taught
├── scripts/
│   └── build.py             YAML + static assets → _site/
├── index.html               Front-end (layout, styles, JS)
├── portrait.png             Sidebar portrait
├── uploads/                 Other static images
├── _site/                   Build output (gitignored)
└── .github/workflows/
    └── deploy.yml           GitHub Actions → Pages
```

## Update workflow

1. Edit the relevant YAML under `data/`
2. Commit and push to `main`
3. GitHub Actions builds and deploys to Pages (~1 min)

## Local preview

```bash
uv run scripts/build.py                           # builds _site/
python3 -m http.server --directory _site 8000
# open http://localhost:8000
```

## Schemas

Inline comments at the top of each YAML file document field shapes. See also
`index.html`'s own `HOW TO UPDATE THIS SITE` block for the full contract
between the front-end and `content.json`.

## Deployment

- **Hosting:** GitHub Pages (public repo, free tier)
- **URL:** `https://danielyue.github.io/` (personal Pages convention — repo
  name matches username)
- **Build:** Python via `uv` in `.github/workflows/deploy.yml`, then
  `actions/deploy-pages@v4` uploads `_site/`

## Credits

Front-end design: content-driven, no framework, no trackers. Typography:
Newsreader + JetBrains Mono via Google Fonts.
