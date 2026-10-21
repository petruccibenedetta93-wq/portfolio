#!/usr/bin/env python3
"""
Content inventory before / after the PARALLAX redesign.

For every page it compares the original <main> (commit ORIGIN) with the rebuilt page:
text segments, image sources and alt texts, documents, external links and anchor ids.
A text segment counts as preserved when it appears in the same page; if it only appears
on another page it is reported as moved. Writes tools/parallax/INVENTARIO.md.
"""
import html
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORIGIN = "fe39fa7"
PAGES = ["index.html", "progetti.html", "progetto-farmacia-altesi.html", "progetto-jojob.html", "progetto-includo.html",
         "progetto-linkedin-personal-branding.html", "progetto-ai.html", "esperienza-federlus.html", "cv.html", "contatti.html"]
DECORATIVE = {"→", "↗", "↓", "←", "–", "✓", "●", "*", "A", "·"}

# Old navigation labels and decorative chrome replaced by an equivalent, documented here.
INTENTIONAL = {
    ("index.html", "Scopri i progetti"): "pulsante dell'hero, ora “Progetti ↓” (stessa destinazione: i progetti) e menu “Progetti”",
    ("index.html", "Consulta il CV"): "pulsante dell'hero, ora “CV (PDF)” nell'hero e “CV” nel menu e nel piè di pagina",
    ("index.html", "Roma · Italia"): "firma decorativa; la città compare come “Roma, Italia” nell'hero e nei contatti",
    ("index.html", "Scroll to explore"): "invito decorativo allo scorrimento, sostituito dal pulsante “Progetti ↓”",
    ("index.html", "Selected work"): "etichetta della sezione progetti, ora “Progetti in evidenza”",
    ("index.html", "Ritratto professionale di Benedetta Petrucci, UX/UI Designer e Digital Product Designer"): "testo alternativo del vecchio ritratto: la hero usa il fotogramma 16:9 della stessa foto, con un testo alternativo descrittivo",
    ("index.html", "assets/images/benedetta-cutout-hq.png"): "il ritaglio resta nel repository; la hero usa assets/images/benedetta-parallax-16x9.jpg, la stessa foto su fondo carbone",
}
NAV_LABEL = re.compile(r"^(← )?(Precedente|Prossimo|Tutti i progetti)")

# Cuts and rewrites Benedetta asked for after the redesign (21 Oct 2026): (page, text prefix) -> what replaced it.
PROFILE = "profilo della home riscritto su richiesta dell'autrice: competenze UX/UI al posto degli ambiti generici"
EDITED = {
    ("index.html", "Esperienze digitali chiare, progettate"): "frase d'apertura doppia: resta il titolo “Dal design visivo alla progettazione di esperienze digitali.”",
    ("index.html", "per le persone."): "seconda riga della stessa frase d'apertura",
    ("index.html", "Experience Design"): PROFILE,
    ("index.html", "Creative Direction"): PROFILE,
    ("index.html", "Una cassetta degli attrezzi davvero trasversale."): PROFILE + " (titolo delle competenze)",
    ("index.html", "Strategia, coordinamento e produzione"): PROFILE + " (introduzione alle competenze)",
    ("index.html", "Pianificazione e budget"): "schede Project management ed Eventi unite in “Progetti ed eventi”",
    ("index.html", "Monitoraggio e rendicontazione"): "schede Project management ed Eventi unite in “Progetti ed eventi”",
    ("index.html", "Coordinamento operativo"): "schede Project management ed Eventi unite in “Progetti ed eventi”",
    ("index.html", "Materiali e allestimenti"): "schede Project management ed Eventi unite in “Progetti ed eventi”",
    ("index.html", "Ricerca e architettura"): "scheda UX/UI riscritta con competenze più precise",
    ("index.html", "Wireframe e design system"): "scheda UX/UI riscritta con competenze più precise",
    ("progetto-farmacia-altesi.html", "Il piano è progettato per verificare"): "accorciato: la seconda frase ripeteva la nota di trasparenza sul test ipotetico",
    ("progetto-jojob.html", "Responsive coerente"): "case study accorciato: la scheda ripeteva l'introduzione della sezione",
    ("progetto-jojob.html", "La struttura diventa verticale"): "case study accorciato: la scheda ripeteva l'introduzione della sezione",
    ("progetto-jojob.html", "Flusso completo"): "case study accorciato: la scheda ripeteva la didascalia dell'immagine",
    ("progetto-jojob.html", "Home, ricerca, filtri, dettaglio"): "case study accorciato: la scheda ripeteva la didascalia dell'immagine",
    ("progetto-jojob.html", "User Test 1 definisce il protocollo"): "introduzione del test accorciata alla prima frase",
    ("progetto-jojob.html", "scenari di test"): "riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi",
    ("progetto-jojob.html", "4/5"): "riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi",
    ("progetto-jojob.html", "smartphone come dispositivo abituale"): "riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi",
    ("progetto-jojob.html", "Pianificazione → sessioni"): "citazione di processo rimossa (decorativa)",
    ("progetto-jojob.html", "Percezione"): "punto rimosso: ripeteva il paragrafo sulle evidenze (facilità e rapidità citate dai partecipanti)",
    ("progetto-jojob.html", "I cinque contributi descrivono"): "punto rimosso: ripeteva il paragrafo sulle evidenze (facilità e rapidità citate dai partecipanti)",
    **{("progetto-jojob.html", t): "schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system"
       for t in ("Colore", "Palette primaria", "Tipografia", "Una gerarchia modulare", "Componenti", "Button, form, card e badge")},
}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.texts, self.alts, self.srcs, self.hrefs, self.ids = [], [], [], [], []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "img":
            self.srcs.append(a.get("src", ""))
            if a.get("alt"):
                self.alts.append(norm(a["alt"]))
        if tag == "a" and a.get("href"):
            self.hrefs.append(html.unescape(a["href"]))
        if a.get("aria-label") and tag not in ("a", "button", "nav", "ul", "div", "section", "aside"):
            self.texts.append(norm(a["aria-label"]))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if self.skip:
            return
        t = norm(data)
        if t and t not in DECORATIVE and len(t) > 1:
            self.texts.append(t)


def norm(s):
    return re.sub(r"\s+", " ", s.replace(" ", " ")).strip()


def collect(markup):
    c = Collector()
    c.feed(markup)
    return c


def main_of(markup):
    m = re.search(r"<main.*?</main>", markup, re.S)
    return m.group(0) if m else markup


def flat_text(markup):
    c = collect(markup)
    return " ".join(c.texts + c.alts)


def original(name):
    return subprocess.run(["git", "show", f"{ORIGIN}:{name}"], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def main():
    new_pages = {p: (ROOT / p).read_text() for p in PAGES}
    new_flat = {p: flat_text(t) for p, t in new_pages.items()}
    all_flat = " ".join(new_flat.values())
    all_new = " ".join(new_pages.values())
    rows, problems, moved_all, intentional, edited = [], [], [], [], []
    for p in PAGES:
        before = collect(main_of(original(p)))
        after = collect(new_pages[p])
        missing, moved = [], []
        for t in dict.fromkeys(before.texts + before.alts):
            if t in new_flat[p]:
                continue
            if (p, t) in INTENTIONAL:
                intentional.append((p, t, INTENTIONAL[(p, t)]))
                continue
            if NAV_LABEL.match(t):
                intentional.append((p, t, "vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”"))
                continue
            reason = next((why for (page, prefix), why in EDITED.items() if page == p and t.startswith(prefix)), None)
            if reason:
                edited.append((p, t, reason))
                continue
            (moved if t in all_flat else missing).append(t)
        assets_b = {s.split("?")[0] for s in before.srcs if s}
        docs_b = {h for h in before.hrefs if h.startswith("assets/")}
        ext_b = {h for h in before.hrefs if h.startswith(("http", "mailto:"))}
        lost_assets = []
        for a in sorted(assets_b | docs_b):
            if a in all_new:
                continue
            if (p, a) in INTENTIONAL:
                intentional.append((p, a, INTENTIONAL[(p, a)]))
            else:
                lost_assets.append(a)
        lost_ext = sorted(h for h in ext_b if html.escape(h, quote=False) not in all_new and h not in all_new)
        lost_ids = sorted(i for i in before.ids if f'id="{i}"' not in new_pages[p])
        rows.append((p, len(set(before.texts + before.alts)), len(assets_b), len(docs_b), len(ext_b), len(before.ids),
                     len(set(after.texts + after.alts)), len(missing), len(moved), len(lost_assets) + len(lost_ext), len(lost_ids)))
        for kind, items in (("testo mancante", missing), ("asset mancante", lost_assets), ("link esterno mancante", lost_ext), ("ancora mancante", lost_ids)):
            for it in items:
                problems.append((p, kind, it))
        moved_all += [(p, t) for t in moved]

    out = ["# Inventario contenuti prima / dopo il redesign PARALLAX", "",
           f"Confronto automatico (`tools/parallax/inventory.py`) tra il contenuto di `<main>` delle pagine al commit `{ORIGIN}` "
           "(prima del redesign) e le pagine ricostruite. Testi, testi alternativi, immagini, documenti, link esterni e ancore.", "",
           "| Pagina (URL invariato) | Testi prima | Immagini | Documenti | Link esterni | Ancore | Testi dopo | Testi mancanti | Testi spostati su altra pagina | Asset/link mancanti | Ancore mancanti |",
           "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    out += ["", "## Elementi mancanti", ""]
    out += [f"- `{p}` · {k}: {t}" for p, k, t in problems] or ["Nessuno: ogni testo, immagine, documento, link esterno e ancora delle pagine originali è presente nel nuovo sito."]
    out += ["", "## Sostituzioni intenzionali (etichette di navigazione e decorazioni)", ""]
    out += [f"- `{p}` · “{t}”: {why}" for p, t, why in intentional] or ["Nessuna."]
    out += ["", "## Tagli e riscritture approvati dall’autrice (21 ottobre 2026)", "",
            "Dopo la pubblicazione Benedetta ha chiesto di sostituire nel profilo gli ambiti generici con competenze UX/UI, "
            "tenere una sola frase d’apertura e accorciare i case study principali mantenendo le parti fondamentali.", ""]
    out += [f"- `{p}` · “{t}”: {why}" for p, t, why in edited] or ["Nessuno."]
    out += ["", "## Testi spostati su un’altra pagina", ""]
    out += [f"- da `{p}`: {t}" for p, t in moved_all] or ["Nessuno."]
    (Path(__file__).parent / "INVENTARIO.md").write_text("\n".join(out) + "\n")
    print(f"pages {len(rows)}, problems {len(problems)}, moved {len(moved_all)}, intentional {len(intentional)}, edited {len(edited)}")
    for p, k, t in problems:
        print(f"  {p} | {k} | {t[:110]}")
    for p, t in moved_all:
        print(f"  MOVED {p} | {t[:110]}")


if __name__ == "__main__":
    main()
