# Quang Minh Dinh - personal website

Source for [quangminhdinh.github.io](https://quangminhdinh.github.io/), an academic
homepage with publications, projects, and a [digital garden](https://quangminhdinh.github.io/garden/)
of interlinked notes you can also explore as an interactive
[knowledge graph](https://quangminhdinh.github.io/reading/).

Built with [Hugo](https://gohugo.io/) and a vendored copy of the
[PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

## Quick start

You need **Hugo extended** (the build was made with `v0.160.1`):

```powershell
# Windows
winget install Hugo.Hugo.Extended
# macOS
brew install hugo
```

Then run the dev server from the project root:

```powershell
hugo server
```

Open <http://localhost:1313/>. The server live-reloads as you edit. Add `-D` to
preview draft posts:

```powershell
hugo server -D
```

To produce the static site for deployment (output lands in `public/`):

```powershell
hugo --minify
```

## Project layout

| Path | What's there |
| --- | --- |
| `hugo.toml` | Site config: menus, params, social links, the homepage intro |
| `content/` | All page content (Markdown) |
| `content/garden/` | Digital-garden notes (seedling → budding → evergreen) |
| `content/reading/` | The interactive note graph page |
| `content/publications/`, `content/projects/` | Section landing pages |
| `data/books.yaml` | Reading list data |
| `layouts/` | Custom templates that override the theme |
| `layouts/reading/list.html` | Builds the force-directed note graph from garden links |
| `layouts/shortcodes/` | `wl` (wikilink) and `project` shortcodes |
| `assets/css/extended/custom.css` | Site-specific styling on top of PaperMod |
| `themes/PaperMod/` | Vendored theme (no submodule, just clone and go) |
| `scripts/sync_garden.py` | Syncs published Obsidian notes into `content/garden/` |
| `static/` | Files served as-is (`cv.pdf`, `favicon.ico`, …) |

## The digital garden

Garden notes live in `content/garden/` as Markdown. Each carries a `status`
(`seedling`, `budding`, or `evergreen`) and a `links:` list of other note slugs;
those links are what the graph page renders as edges.

Many notes are authored in an Obsidian vault and pulled in with the sync script:

```powershell
python scripts/sync_garden.py --dry-run   # preview changes
python scripts/sync_garden.py             # write notes into content/garden/
```

It's opt-in: only vault notes with `publish: true` in their frontmatter are
copied, and generated files are tagged `source: obsidian` so hand-written garden
notes are never overwritten or removed. Requires `pip install pyyaml`. The vault
path is set at the top of the script.

## Deploying

`hugo --minify` writes the finished site to `public/`. Push that output (or the
source, via a GitHub Pages build) to publish to the `baseURL` set in `hugo.toml`.
