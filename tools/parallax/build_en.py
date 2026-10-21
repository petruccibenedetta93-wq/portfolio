#!/usr/bin/env python3
"""
Builds the English version of the portfolio under en/.

Source: the Italian pages written by build_site.py. Every piece of visible text, the alt,
aria-label, title and placeholder attributes, the meta descriptions and the JSON-LD texts are
looked up in i18n/en.json, keyed by the Italian text. The English pages keep the same structure,
ids, images and documents; internal links point to the English pages and the IT/EN switch to the
Italian twin. The drawn Farmacia Altesi screens stay in Italian (the product was designed for an
Italian pharmacy) and are marked lang="it".

Usage (from the repository root):
  python3 tools/parallax/build_en.py --extract         add new Italian strings to i18n/en.json
  python3 tools/parallax/build_en.py --merge FILE.json  copy {id: English} translations into en.json
  python3 tools/parallax/build_en.py                   build en/*.html (fails on any missing string)
"""
import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_site as site  # noqa: E402

ROOT = site.ROOT
DICT = HERE / "i18n" / "en.json"
OUT = ROOT / "en"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
INLINE = {"a", "abbr", "b", "br", "code", "em", "i", "img", "mark", "q", "s", "small", "span", "strong", "sub", "sup", "time", "u", "wbr"}
SKIP_TAGS = {"script", "style", "svg"}
# Drawn screens of the Farmacia Altesi product: part of the design, kept in Italian.
KEEP_ITALIAN = re.compile(r"(^|\s)(prototype-canvas|mobile-prototypes|altea-flow-preview|altesi-cover-experience__visuals|wireframe-board__screens|identity-board__mark|project-card__media--altesi)(\s|$)")
ATTRS = ("alt", "aria-label", "title", "placeholder")
META = ("description", "og:title", "og:description", "og:image:alt", "twitter:title", "twitter:description")
LETTER = re.compile(r"[A-Za-zÀ-ÿ]")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def key_id(it):
    return hashlib.sha1(it.encode()).hexdigest()[:8]


def needs_translation(fragment):
    text = html.unescape(re.sub(r"<[^>]+>", "", fragment))
    return len(LETTER.findall(text)) > 1


class Node:
    def __init__(self, tag, attrs, start, inner_start, parent):
        self.tag, self.attrs, self.start, self.inner_start, self.parent = tag, dict(attrs), start, inner_start, parent
        self.inner_end = self.end = None
        self.children, self.runs = [], []


class Tree(HTMLParser):
    """Element tree with source offsets, so text can be replaced in place."""

    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.src = source
        self.lines = [0]
        for m in re.finditer("\n", source):
            self.lines.append(m.end())
        self.root = Node("#root", [], 0, 0, None)
        self.stack = [self.root]
        self.feed(source)
        self.close()
        assert len(self.stack) == 1, [n.tag for n in self.stack]

    def pos(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.pos()
        node = Node(tag, attrs, start, start + len(self.get_starttag_text()), self.stack[-1])
        self.stack[-1].children.append(node)
        if tag in VOID:
            node.inner_end = node.end = node.inner_start
        else:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        start = self.pos()
        node = Node(tag, attrs, start, start + len(self.get_starttag_text()), self.stack[-1])
        node.inner_end = node.end = node.inner_start
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        start = self.pos()
        assert self.stack[-1].tag == tag, (tag, self.stack[-1].tag, self.src[start - 80:start + 20])
        node = self.stack.pop()
        node.inner_end = start
        node.end = self.src.index(">", start) + 1

    def _text(self, length):
        start = self.pos()
        runs = self.stack[-1].runs
        if runs and runs[-1][1] == start:
            runs[-1][1] = start + length
        else:
            runs.append([start, start + length])

    def handle_data(self, data):
        self._text(len(data))

    def handle_entityref(self, name):
        self._text(len(name) + 2)

    def handle_charref(self, name):
        self._text(len(name) + 3)


def has_text(node, src):
    return any(src[a:b].strip() for a, b in node.runs)


def has_block(node):
    return any(c.tag not in INLINE or has_block(c) for c in node.children)


def segments(node, src, out):
    """(start, end) ranges of translatable text: whole inner HTML of text blocks, or single text runs."""
    if node.tag in SKIP_TAGS or "data-lang-switch" in node.attrs or KEEP_ITALIAN.search(node.attrs.get("class") or ""):
        return
    if node.tag != "#root" and has_text(node, src) and not has_block(node):
        out.append((node.inner_start, node.inner_end))
        return
    for a, b in node.runs:
        if src[a:b].strip():
            out.append((a, b))
    for child in node.children:
        segments(child, src, out)


def keep_italian_nodes(node, out):
    if KEEP_ITALIAN.search(node.attrs.get("class") or ""):
        out.append(node)
        return
    for child in node.children:
        keep_italian_nodes(child, out)


def strings_of(src):
    """Every Italian string of a page that needs an English counterpart."""
    tree = Tree(src)
    found = []
    ranges = []
    segments(tree.root, src, ranges)
    for a, b in ranges:
        if needs_translation(src[a:b]):
            found.append(norm(src[a:b]))
    skipped = []
    keep_italian_nodes(tree.root, skipped)
    hidden = [(n.start, n.end) for n in skipped]
    for m in re.finditer(r'\s(?:%s)="([^"]*)"' % "|".join(ATTRS), src):
        if any(a <= m.start() < b for a, b in hidden) or re.search(r'data-lang-switch', src[src.rfind("<", 0, m.start()):m.start()]):
            continue
        if needs_translation(m.group(1)):
            found.append(norm(m.group(1)))
    for m in re.finditer(r'<meta (?:name|property)="(%s)" content="([^"]*)">' % "|".join(META), src):
        found.append(norm(m.group(2)))
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        data = json.loads(block)
        found += [norm(html.escape(data[k], quote=False)) for k in ("name", "description") if isinstance(data.get(k), str)]
    return found, ranges, hidden


def load():
    return json.loads(DICT.read_text()) if DICT.exists() else {}


def save(entries):
    DICT.parent.mkdir(exist_ok=True)
    DICT.write_text(json.dumps(entries, ensure_ascii=False, indent=1) + "\n")


def extract():
    entries = load()
    seen = set()
    order = {}
    for name in site.EN_SLUG:
        found, _, _ = strings_of((ROOT / name).read_text())
        for it in found:
            k = key_id(it)
            seen.add(k)
            order.setdefault(k, (name, it))
    new = {k: v for k, v in order.items() if k not in entries}
    for k, (name, it) in order.items():
        entries.setdefault(k, {"page": name, "it": it, "en": ""})
    unused = sorted(set(entries) - seen)
    save({k: entries[k] for k in order})  # strings no longer on any page are dropped
    missing = sum(1 for k in order if not entries[k]["en"])
    print(f"{len(order)} strings, {len(new)} new, {missing} without English, {len(unused)} no longer used: {unused}")


def merge(path):
    entries = load()
    text = Path(path).read_text()
    if path.endswith(".txt"):  # one "id | English" per line
        updates = dict(line.split(" | ", 1) for line in text.splitlines() if line.strip())
    else:
        updates = json.loads(text)
    for k, en in updates.items():
        assert k in entries, f"unknown id {k}"
        entries[k]["en"] = en
    save(entries)
    print(f"merged {len(updates)} translations")


def en_href(value, name):
    if value.startswith("assets/"):
        return "../" + value
    m = re.fullmatch(r"([a-z0-9-]+\.html)(#.*)?", value)
    if m and m.group(1) in site.EN_SLUG:
        return site.EN_SLUG[m.group(1)] + (m.group(2) or "")
    return value


def build_page(name, table):
    src = (ROOT / name).read_text()
    slug = site.EN_SLUG[name]
    it_href = "../" + ("index.html" if name == "index.html" else name)
    # IT/EN switch: on the English page it leads back to the Italian twin.
    src = re.sub(r'<a class="([\w-]+)" href="en/[^"]*" hreflang="en" lang="en" data-lang-switch>EN<span class="([\w-]+)">, English version</span></a>',
                 rf'<a class="\1" href="{it_href}" hreflang="it" lang="it" data-lang-switch>IT<span class="\2">, versione italiana</span></a>', src)
    src = re.sub(r'<a href="en/[^"]*" hreflang="en" lang="en" data-lang-switch>English version</a>',
                 f'<a href="{it_href}" hreflang="it" lang="it" data-lang-switch>Versione italiana</a>', src)
    missing = []

    def tr(it):
        en = table.get(norm(it))
        if not en:
            missing.append(norm(it))
            return it
        return en

    _, ranges, hidden = strings_of(src)
    for a, b in sorted(ranges, reverse=True):
        raw = src[a:b]
        if not needs_translation(raw):
            continue
        lead, trail = raw[: len(raw) - len(raw.lstrip())], raw[len(raw.rstrip()):]
        src = src[:a] + lead + tr(raw) + trail + src[b:]
    english = set(table.values())

    def attr(m):
        value = m.group(2)
        if not needs_translation(value) or norm(value) in english:
            return m.group(0)
        return f' {m.group(1)}="{tr(value)}"'
    # Attributes inside the kept Italian screens stay as they are: they are only aria-hidden decorations.
    kept = Tree(src)
    keep = []
    keep_italian_nodes(kept.root, keep)
    parts, last = [], 0
    for node in sorted(keep, key=lambda n: n.start):
        parts.append(re.sub(r'\s(%s)="([^"]*)"' % "|".join(ATTRS), attr, src[last:node.start]))
        parts.append(src[node.start:node.end].replace(">", ' lang="it">', 1))
        last = node.end
    parts.append(re.sub(r'\s(%s)="([^"]*)"' % "|".join(ATTRS), attr, src[last:]))
    src = "".join(parts)
    src = re.sub(r'(<meta (?:name|property)="(?:%s)" content=")([^"]*)(">)' % "|".join(META),
                 lambda m: m.group(1) + tr(m.group(2)) + m.group(3), src)

    def ld(m):
        data = json.loads(m.group(1))
        for k in ("name", "description"):
            if isinstance(data.get(k), str):
                data[k] = html.unescape(tr(html.escape(data[k], quote=False)))
        data["inLanguage"] = "en"
        data["url"] = site.SITE + "en/" + slug
        return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>"
    src = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, src, flags=re.S)

    # Language, canonical address, links and assets.
    page_url = site.SITE + ("" if name == "index.html" else name)
    en_url = site.SITE + "en/" + ("" if name == "index.html" else slug)
    src = src.replace('<html lang="it">', '<html lang="en">', 1).replace('content="it_IT"', 'content="en_GB"')
    src = src.replace(f'<link rel="canonical" href="{page_url}">', f'<link rel="canonical" href="{en_url}">')
    src = src.replace(f'<meta property="og:url" content="{page_url}">', f'<meta property="og:url" content="{en_url}">')
    src = re.sub(r'(\s(?:href|src|action)=")([^"]*)(")', lambda m: m.group(1) + en_href(m.group(2), name) + m.group(3), src)
    # The English pages offer the English CV first: CV links that do not name the Italian version use it.
    src = re.sub(r'(<a [^>]*href=")\.\./assets/pdf/Benedetta_Petrucci_CV_UX_UI_IT_2026\.pdf("[^>]*>)(.*?)(</a>)',
                 lambda m: m.group(0) if "Italian" in m.group(3) else m.group(1) + "../" + site.CV_EN + m.group(2) + m.group(3) + m.group(4),
                 src, flags=re.S)
    src = src.replace('name="origine" value="Pagina Contatti"', 'name="origine" value="Pagina Contatti (versione inglese)"')
    return src, missing


def build():
    entries = load()
    table = {}
    for e in entries.values():
        if e["en"]:
            table[e["it"]] = e["en"]
    OUT.mkdir(exist_ok=True)
    problems = {}
    for name, slug in site.EN_SLUG.items():
        out, missing = build_page(name, table)
        if missing:
            problems[name] = sorted(set(missing))
        assert 'href="#"' not in out
        (OUT / slug).write_text(out)
    if problems:
        for name, items in problems.items():
            print(f"{name}: {len(items)} strings without English")
            for it in items[:8]:
                print("   ", it[:110])
        sys.exit(1)
    print(f"built {len(site.EN_SLUG)} English pages in en/")


if __name__ == "__main__":
    if "--extract" in sys.argv:
        extract()
    elif "--merge" in sys.argv:
        merge(sys.argv[sys.argv.index("--merge") + 1])
    else:
        build()
