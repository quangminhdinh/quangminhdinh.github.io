#!/usr/bin/env python3
"""
sync_garden.py — translate published Obsidian vault notes into Hugo garden posts.

Opt-in by design: only notes with `publish: true` in their frontmatter are
copied across. Generated notes carry `source: obsidian` so hand-written garden
notes (no marker) are never touched or removed.

Run:
    python scripts/sync_garden.py           # sync
    python scripts/sync_garden.py --dry-run # show what would happen
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("This script needs PyYAML:  pip install pyyaml\n")
    sys.exit(1)

# ---- config ---------------------------------------------------------------

VAULT = Path(r"C:\Users\minh1\Documents\Research Projects\Experiment\Experiment")
OUTPUT = Path(__file__).resolve().parent.parent / "content" / "garden"
MARKER = "obsidian"
EXCLUDE_DIRS = {".obsidian", ".trash", "Templates", "Media", "_About me"}

# ---- regex ----------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.DOTALL)
WIKILINK_RE    = re.compile(r"(!?)\[\[([^\[\]]+?)\]\]")
TAG_LINE_RE    = re.compile(r"^_\*\*Tags:\*\*_\s*(.+)$", re.MULTILINE)
HASHTAG_RE     = re.compile(r"#([A-Za-z][A-Za-z0-9_\-]*)")

# ---- small helpers --------------------------------------------------------

def truthy(v):
    if isinstance(v, bool): return v
    if isinstance(v, str):  return v.strip().lower() in ("true", "yes", "1")
    return bool(v)

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    s = re.sub(r"-+", "-", s)
    return s

def as_iso(v, fallback: str) -> str:
    if v is None or v == "":
        return fallback
    if hasattr(v, "isoformat"):
        return v.isoformat()[:10] if hasattr(v, "year") else str(v)
    return str(v)[:10] if len(str(v)) >= 10 else str(v)

def parse_frontmatter(raw: str):
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return {}, raw
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, m.group(2)

def load_note(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    return parse_frontmatter(raw)

def iter_vault_notes(vault: Path):
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for f in files:
            if f.lower().endswith(".md"):
                yield Path(root) / f

def first_sentence(body: str, limit: int = 180) -> str:
    for block in re.split(r"\n\s*\n", body.strip()):
        block = block.strip()
        if not block or block.startswith("#") or block.startswith("$$"):
            continue
        text = WIKILINK_RE.sub(lambda m: m.group(2).split("|")[-1], block)
        text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
        text = re.sub(r"\$[^$]+\$", "", text)
        text = re.sub(r"[*_`]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if len(text) > limit:
            text = text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
        return text
    return ""

# ---- main -----------------------------------------------------------------

def main(dry_run: bool) -> int:
    if not VAULT.exists():
        sys.stderr.write(f"Vault not found: {VAULT}\n")
        return 1
    OUTPUT.mkdir(parents=True, exist_ok=True)

    # pass 1 — index every note in the vault
    index = {}      # lowercased-title-or-alias -> (slug, published)
    published = []  # [(path, fm, body, slug, title)]
    for path in iter_vault_notes(VAULT):
        fm, body = load_note(path)
        title = fm.get("title") or path.stem
        slug  = slugify(str(fm.get("slug") or title))
        pub   = truthy(fm.get("publish"))
        key   = str(title).lower()
        index[key] = (slug, pub)
        for alias in (fm.get("aliases") or []):
            index.setdefault(str(alias).lower(), (slug, pub))
        if pub:
            published.append((path, fm, body, slug, str(title)))

    if not published:
        print("No vault notes carry `publish: true` — nothing to sync.")
        return 0

    broken = []
    generated_slugs = set()
    wrote = skipped = 0

    for path, fm, body, slug, title in published:
        # 1 — pull tags from the Obsidian "_**Tags:**_" line and drop that line
        obsidian_tags: list[str] = []
        def collect(m):
            obsidian_tags.extend(HASHTAG_RE.findall(m.group(1)))
            return ""
        body_clean = TAG_LINE_RE.sub(collect, body)

        fm_tags = fm.get("tags") or []
        if isinstance(fm_tags, str):
            fm_tags = [fm_tags]
        raw_tags = list(fm_tags) + obsidian_tags
        seen = set()
        tags = []
        for t in raw_tags:
            s = slugify(str(t).replace("_", "-"))
            if s and s not in seen:
                seen.add(s); tags.append(s)

        # 2 — convert wikilinks
        links_out: list[str] = []
        def convert(m):
            embed_mark, inner = m.group(1), m.group(2).strip()
            if embed_mark == "!":          # ![[Image.png]] — leave the literal text
                return m.group(0)
            target = inner; label = None
            if "|" in target:
                target, label = target.split("|", 1)
            if "#" in target:
                target = target.split("#", 1)[0]
            target = target.strip()
            if label is not None:
                label = label.strip()

            entry = index.get(target.lower())
            if not entry:
                broken.append((title, target))
                return label or target
            tslug, pub = entry
            if not pub:
                return label or target
            if tslug != slug and tslug not in links_out:
                links_out.append(tslug)
            if label:
                esc = label.replace('"', '\\"')
                return '{{< wl "' + tslug + '" "' + esc + '" >}}'
            return '{{< wl "' + tslug + '" >}}'

        body_conv = WIKILINK_RE.sub(convert, body_clean)

        # 3 — frontmatter
        stat = path.stat()
        created  = datetime.fromtimestamp(stat.st_ctime, tz=timezone.utc).date().isoformat()
        modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).date().isoformat()

        description = fm.get("description") or first_sentence(body_conv)

        out_fm = {
            "title":       str(title),
            "date":        as_iso(fm.get("date"), created),
            "lastmod":     as_iso(fm.get("lastmod"), modified),
            "description": description,
            "status":      str(fm.get("status") or "seedling"),
            "tags":        tags,
            "links":       links_out,
            "source":      MARKER,
        }
        out_fm = {k: v for k, v in out_fm.items() if v not in (None, "", [], {})}

        # 4 — write (only touch files that don't exist or are marker-owned)
        generated_slugs.add(slug)
        out_path = OUTPUT / f"{slug}.md"
        if out_path.exists():
            e_fm, _ = load_note(out_path)
            if e_fm.get("source") != MARKER:
                print(f"  skip (hand-written): {out_path.name}")
                skipped += 1
                continue

        body_final = re.sub(r"\n{3,}", "\n\n", body_conv.strip()) + "\n"
        fm_yaml = yaml.safe_dump(
            out_fm, sort_keys=False, allow_unicode=True,
            default_flow_style=False, width=120,
        ).strip()
        full = f"---\n{fm_yaml}\n---\n\n{body_final}"

        if dry_run:
            print(f"  [dry-run] write {out_path.name}  ({len(body_final)} chars)")
        else:
            out_path.write_text(full, encoding="utf-8", newline="\n")
            print(f"  wrote {out_path.name}")
        wrote += 1

    # 5 — remove orphans we previously generated
    removed = 0
    for f in OUTPUT.glob("*.md"):
        if f.stem == "_index" or f.stem in generated_slugs:
            continue
        e_fm, _ = load_note(f)
        if e_fm.get("source") != MARKER:
            continue
        if dry_run:
            print(f"  [dry-run] remove orphan {f.name}")
        else:
            f.unlink()
            print(f"  removed orphan {f.name}")
        removed += 1

    # 6 — report
    print()
    print(f"summary: {wrote} written · {skipped} skipped · {removed} removed")
    if broken:
        print(f"{len(broken)} broken wikilinks (target not found in vault):")
        for src, tgt in broken:
            print(f"  [{src}] → {tgt}")
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    sys.exit(main(args.dry_run))
