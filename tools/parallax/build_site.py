#!/usr/bin/env python3
"""
Builds the PARALLAX version of every portfolio page.

Source of truth for the content: the pages as they were before the redesign, read from git
(commit ORIGIN). Each page keeps its URL, its <head> metadata and the whole content of <main>;
the script replaces the old chrome (header, footer, scripts, stylesheet) with the shared PARALLAX
one and adds the new navigation aids: breadcrumb, "In breve" summary, labelled index,
previous / all / next project links and full-resolution links on images.

Usage (from the repository root):  python3 tools/parallax/build_site.py
"""
import html
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ORIGIN = "fe39fa7"  # last commit of main before the redesign

LINKEDIN = "https://www.linkedin.com/in/benedetta-petrucci-5b333b328/"
EMAIL = "petruccibenedetta93@gmail.com"
CV_IT = "assets/pdf/Benedetta_Petrucci_CV_UX_UI_IT_2026.pdf"
CV_EN = "assets/pdf/Benedetta_Petrucci_CV_UX_UI_EN_2026.pdf"
SITE = "https://petruccibenedetta93-wq.github.io/portfolio/"
NEW_TAB = '<span class="sr-only"> (si apre in una nuova scheda)</span>'

RINGS = [line for line in (HERE / "rings.paths.txt").read_text().splitlines() if line]
assert len(RINGS) == 12

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;family=Roboto+Mono:wght@400;500&amp;display=swap">\n'
)

# Order used for previous / next links (same order as the Progetti page).
PROJECTS = [
    ("progetto-jojob.html", "JOJOB"),
    ("progetto-farmacia-altesi.html", "Farmacia Altesi + Altea"),
    ("progetto-linkedin-personal-branding.html", "LinkedIn Personal Branding"),
    ("progetto-includo.html", "INCLUDO"),
    ("progetto-ai.html", "AI Assistant"),
]

NAV = [
    ("progetti", "progetti.html", "Progetti"),
    ("esperienza", "esperienza-federlus.html", "Esperienza"),
    ("cv", "cv.html", "CV"),
    ("contatti", "contatti.html", "Contatti"),
]


def original(name):
    return subprocess.run(["git", "show", f"{ORIGIN}:{name}"], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def rings_svg(css_class, indent="    "):
    paths = "\n".join(f'{indent}  <path d="{d}"/>' for d in RINGS)
    return (f'{indent}<svg class="{css_class}" viewBox="0 0 1280 800" preserveAspectRatio="xMidYMid meet" '
            f'aria-hidden="true" focusable="false">\n{paths}\n{indent}</svg>')


def header(current, exact):
    """current: active section; exact: True when this page is the section page itself."""
    state = ' aria-current="page"' if exact else ' aria-current="true"'
    items = []
    panel = []
    for key, href, label in NAV:
        cur = state if key == current else ""
        full = "Esperienza FederLUS" if key == "esperienza" else label
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        panel.append(f'<li><a href="{href}"{cur}>{full} <span aria-hidden="true">→</span></a></li>')
    panel.append(f'<li><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span>{NEW_TAB}</a></li>')
    return f"""<a class="skip-link" href="#contenuto">Vai al contenuto principale</a>
  <header class="px-header">
    <div class="px-header__bar">
      <a class="px-brand" href="index.html" aria-label="Benedetta Petrucci, home del portfolio"><span class="px-brand__mark" aria-hidden="true">bp</span><span class="px-brand__name" aria-hidden="true">Benedetta Petrucci</span></a>
      <nav class="px-nav" aria-label="Navigazione principale"><ul>{''.join(items)}</ul></nav>
      <button class="px-menu-button" type="button" aria-label="Apri il menu" aria-expanded="false" aria-controls="site-menu"><i></i><i></i></button>
    </div>
    <nav class="px-panel" id="site-menu" aria-label="Menu" hidden><ul>{''.join(panel)}</ul></nav>
  </header>"""


def footer():
    return f"""<footer class="px-footer">
    <div class="container-site">
      <div class="px-footer__grid">
        <div>
          <a class="px-footer__brand" href="index.html" aria-label="Benedetta Petrucci, home del portfolio">bp</a>
          <p>Benedetta Petrucci · UX/UI e visual designer · Roma</p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <nav aria-label="Pagine del portfolio">
          <h2>Portfolio</h2>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="progetti.html">Progetti</a></li>
            <li><a href="esperienza-federlus.html">Esperienza FederLUS</a></li>
            <li><a href="cv.html">CV</a></li>
            <li><a href="contatti.html">Contatti</a></li>
          </ul>
        </nav>
        <div>
          <h2>CV e profili</h2>
          <ul>
            <li><a href="{CV_IT}" download>CV italiano (PDF) <span aria-hidden="true">↓</span></a></li>
            <li><a href="{CV_EN}" download lang="en">English CV (PDF) <span aria-hidden="true">↓</span></a></li>
            <li><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span>{NEW_TAB}</a></li>
          </ul>
        </div>
      </div>
      <div class="px-footer__base"><span>Benedetta Petrucci · Portfolio 2026</span><a href="#top">Torna su ↑</a></div>
    </div>
  </footer>"""


def breadcrumb(trail):
    parts = []
    for label, href in trail:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f'<li aria-current="page">{label}</li>')
    return f'<nav class="breadcrumb" aria-label="Percorso"><ol>{"".join(parts)}</ol></nav>'


def summary(rows, materials=None, title="In breve"):
    items = []
    for label, value, *wide in rows:
        cls = ' class="is-wide"' if wide and wide[0] else ""
        items.append(f'<div{cls}><dt>{label}</dt><dd>{value}</dd></div>')
    mats = ""
    if materials:
        links = "".join(f"<li>{m}</li>" for m in materials)
        mats = f'<h3 class="kicker" style="margin-top:28px">Materiali originali</h3><ul class="materials">{links}</ul>'
    return f"""<section class="case-summary" id="in-breve" aria-labelledby="in-breve-title">
      <div class="container-site">
        <p class="eyebrow">Sintesi per chi seleziona</p>
        <h2 id="in-breve-title">{title}</h2>
        <dl>{''.join(items)}</dl>
        {mats}
      </div>
    </section>"""


def ext(href, label, primary=False):
    cls = "button" if primary else "button button--secondary"
    return f'<a class="{cls}" href="{href}" target="_blank" rel="noopener noreferrer">{label} <span aria-hidden="true">↗</span>{NEW_TAB}</a>'


def project_nav(name):
    names = [p[0] for p in PROJECTS]
    i = names.index(name)
    prev_href, prev_label = PROJECTS[i - 1]
    next_href, next_label = PROJECTS[(i + 1) % len(PROJECTS)]
    return (f'<nav class="project-navigation" aria-label="Navigazione tra i progetti">'
            f'<a href="{prev_href}"><span>← Progetto precedente</span><strong>{prev_label}</strong></a>'
            f'<a href="progetti.html"><span>Raccolta</span><strong>Tutti i progetti</strong></a>'
            f'<a href="{next_href}"><span>Progetto successivo →</span><strong>{next_label}</strong></a></nav>')


def zoom_images(main):
    """Wrap images of figures in a link to the full-size file and add a visible hint."""
    def wrap(match):
        fig_open, img, rest = match.group(1), match.group(2), match.group(3)
        src = re.search(r'src="([^"]+)"', img).group(1)
        link = (f'<a class="figure__zoom" href="{src}" target="_blank" rel="noopener noreferrer">{img}'
                f'<span class="sr-only"> (apri l’immagine a piena risoluzione in una nuova scheda)</span></a>')
        hint = '<span class="figure__hint" aria-hidden="true">Immagine a piena risoluzione ↗</span>'
        if "<figcaption>" in rest:
            rest = rest.replace("</figcaption>", f"{hint}</figcaption>", 1)
        else:
            rest = rest.replace("</figure>", f"<figcaption>{hint}</figcaption></figure>", 1)
        return fig_open + link + rest

    return re.sub(r'(<figure class="(?:figure|case-cover)[^"]*">)(<img [^>]+>)(.*?</figure>)', wrap, main, flags=re.S)


def fix_links(main):
    # Every link opening a new tab gets rel="noopener noreferrer".
    def rel(match):
        tag = match.group(0)
        if "rel=" in tag:
            return tag
        return tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    return re.sub(r'<a [^>]*target="_blank"[^>]*>', rel, main)


def hero_extras(main, trail):
    """Breadcrumb and rings inside the page hero."""
    def add(match):
        return f'{match.group(1)}\n{rings_svg("page-hero__rings", "      ")}\n      <div class="container-site">{breadcrumb(trail)}'
    return re.sub(r'(<header class="page-hero[^"]*">)\s*<div class="container-site">', add, main, count=1)


def label_index(main):
    if 'class="case-layout__label"' in main:
        return main.replace('<ul class="case-layout__index">', '<ul class="case-layout__index"><li><a href="#in-breve">In breve</a></li>', 1)
    return main.replace('<ul class="case-layout__index">',
                        '<p class="case-layout__label">Nel progetto</p><ul class="case-layout__index"><li><a href="#in-breve">In breve</a></li>', 1)


def head(orig, name, extra_css=()):
    h = orig[orig.index("<head>") + 6: orig.index("</head>")]
    h = re.sub(r'\s*<link rel="stylesheet" href="assets/css/main\.css[^"]*">', "", h)
    h = re.sub(r'<meta name="theme-color" content="[^"]*">', '<meta name="theme-color" content="#161a1f">', h)
    # Two pages carried canonical / og URLs of an older account: point them at the live address.
    h = h.replace("https://benedettapetrucci.github.io/portfolio/", SITE)
    css = "".join(f'  <link rel="stylesheet" href="assets/css/{c}">\n' for c in (*extra_css, "parallax.css"))
    return f"<head>{h.rstrip()}\n  {FONTS}{css}</head>"


def page(name, current, trail, transform, extra_css=(), scripts=("site.js",), exact=True):
    orig = original(name)
    main = re.search(r"<main.*?</main>", orig, re.S).group(0)
    main = hero_extras(main, trail)
    main = transform(main)
    main = zoom_images(main)
    main = fix_links(main)
    script_tags = "\n  ".join(f'<script src="assets/js/{s}" defer></script>' for s in scripts)
    out = (f'<!DOCTYPE html>\n<html lang="it">\n{head(orig, name, extra_css)}\n<body id="top">\n  {header(current, exact)}\n\n  '
           f'{main}\n\n  {footer()}\n  {script_tags}\n</body>\n</html>\n')
    (ROOT / name).write_text(out)
    return out


def insert_after_cover(main, block):
    """Summary first (right after the hero), then the cover image and the case-study body."""
    main = main.replace('<div class="container-site"><figure class="case-cover">', '<div class="container-site case-cover-wrap"><figure class="case-cover">', 1)
    main = re.sub(r'<div class="container-site">(\s*<div class="case-cover altesi-cover-experience")', r'<div class="container-site case-cover-wrap">\1', main, count=1)
    m = re.search(r"</header>", main)
    return main[: m.end()] + "\n    " + block + main[m.end():]


def replace_project_nav(main, name):
    return re.sub(r'<nav class="project-navigation".*?</nav>', project_nav(name), main, flags=re.S)


# ---------------------------------------------------------------- case studies

def pdf(href, label):
    return f'<a class="pill pill--dark" href="{href}" target="_blank" rel="noopener noreferrer">{label} (PDF) <span aria-hidden="true">↗</span>{NEW_TAB}</a>'


def fig(href, label):
    return f'<a class="pill pill--dark" href="{href}" target="_blank" rel="noopener noreferrer">{label} <span aria-hidden="true">↗</span>{NEW_TAB}</a>'


FIGMA_JOJOB = "https://www.figma.com/design/FuznxCcEmjamVz2U5KTjfD/Homepage-BlaBla-Car-di-Benedetta-Petrucci?node-id=1337-283&amp;t=hwzjuE8hg4MaOMQ6-1"
PROTO_JOJOB = "https://www.figma.com/proto/FuznxCcEmjamVz2U5KTjfD/Homepage-BlaBla-Car-di-Benedetta-Petrucci?node-id=1580-418&amp;starting-point-node-id=1580%3A418&amp;scaling=scale-down&amp;show-proto-sidebar=0&amp;hide-ui=1&amp;hotspot-hints=0"
FIGMA_ALTESI = "https://www.figma.com/design/Zacs8qK50wRRVo4hlJXGjB"
SURVEY_ALTESI = "https://www.figma.com/design/Zacs8qK50wRRVo4hlJXGjB?node-id=512-2"
PROTO_ALTESI_D = "https://www.figma.com/proto/Zacs8qK50wRRVo4hlJXGjB?node-id=136-2&amp;starting-point-node-id=136%3A2&amp;scaling=scale-down"
PROTO_ALTESI_M = "https://www.figma.com/proto/Zacs8qK50wRRVo4hlJXGjB?node-id=142-2&amp;starting-point-node-id=142%3A2&amp;scaling=scale-down"

SUMMARIES = {
    "progetto-jojob.html": summary([
        ("Tipo di progetto", "Project work formativo di UX/UI design (2026); la parte di UI mobile è stata valutata con il massimo risultato nel modulo User Interface 2."),
        ("Problema", "JOJOB facilita la condivisione dei tragitti casa-lavoro, ma percorsi poco chiari, processi percepiti come lunghi e pochi segnali di sicurezza frenano l’adozione."),
        ("Utenti e obiettivo", "Pendolari casa-lavoro, sintetizzati in tre personas. Obiettivo: rendere la mobilità condivisa semplice da capire e abbastanza affidabile da provare."),
        ("Il mio ruolo e contributo", "UX/UI Designer: Discovery (5 micro-interviste, questionario con 40 risposte, empathy map, personas), architettura informativa, wireframe desktop e mobile, UI e design system, UI mobile, piano e sessioni di user testing."),
        ("Scelte progettuali e motivazioni", "Architettura costruita intorno ai due task principali (cercare e offrire un passaggio); sicurezza, community e vantaggi resi visibili prima; prenotazione in cinque passaggi con feedback; target touch di 44 px e componenti riutilizzabili."),
        ("Output", "Wireframe desktop e mobile, UI ad alta fedeltà desktop e mobile, prototipo Figma, documentazione di User Test 1 (protocollo) e User Test 2 (sessioni e analisi)."),
        ("Risultati documentati e limiti", "Test moderato con 5 partecipanti: 3 citano facilità o intuitività, 2 la rapidità; emergono 2 punti da approfondire (ritorno dalla dashboard alla Home, visibilità della conferma). Le modifiche proposte sono ipotesi da verificare in un retest; la copertura dei task non è uniforme, quindi non è calcolato un tasso di successo complessivo.", True),
    ], [fig(FIGMA_JOJOB, "File Figma"), fig(PROTO_JOJOB, "Prototipo mobile"), pdf("assets/docs/jojob-discovery.pdf", "Discovery"),
        pdf("assets/docs/jojob-wireframing-desktop.pdf", "Wireframe desktop"), pdf("assets/docs/jojob-wireframing-mobile.pdf", "Wireframe mobile"),
        pdf("assets/docs/jojob-ui.pdf", "UI desktop"), pdf("assets/docs/jojob-user-interface-mobile.pdf", "UI mobile"),
        pdf("assets/docs/jojob-user-test-1.pdf", "User Test 1"), pdf("assets/docs/jojob-user-test-2.pdf", "User Test 2")]),
    "progetto-farmacia-altesi.html": summary([
        ("Tipo di progetto", "Progetto finale del Master UX/UI Design di start2impact (formativo), 2026."),
        ("Problema", "Il sito di partenza distribuiva prenotazioni, contatti e richieste su canali distinti: mancava continuità tra ciò che una persona inizia online e ciò che deve verificare il farmacista."),
        ("Utenti e obiettivo", "Clienti abituali e occasionali di una farmacia di prossimità. Obiettivo: rendere semplice un’azione pratica online mantenendo chiari responsabilità, limiti e intervento professionale."),
        ("Il mio ruolo e contributo", "UX/UI &amp; Visual Designer, dalla ricerca ai prototipi: logo e identità, audit, benchmark, survey, journey, architettura, wireframe responsive, UI, prototipi, conversational UX di Altea e piano di test."),
        ("Scelte progettuali e motivazioni", "Stati espliciti (ricevuta, in verifica, confermata) per non confondere una richiesta con una conferma; ricetta in tre passaggi con verifica del farmacista; Altea facoltativa e con passaggio evidente a una persona, perché 11 persone su 13 vogliono il farmacista per domande personali sui farmaci; target di 44–48 px e contrasti verificati in fase di design."),
        ("Output", "10 schermate (5 desktop e 5 mobile), 2 prototipi Figma collegati, file Figma con componenti, demo interattiva rule-based di Altea in questa pagina."),
        ("Risultati documentati e limiti", "Survey esplorativa reale con 13 risposte (campione piccolo e non rappresentativo). Il test di usabilità descritto è ipotetico e non è stato svolto: i relativi risultati sono simulati. Non sono presentate metriche di efficacia; Altea è un concept, non un agente clinico validato.", True),
    ], [fig(FIGMA_ALTESI, "File Figma"), fig(PROTO_ALTESI_D, "Prototipo desktop"), fig(PROTO_ALTESI_M, "Prototipo mobile"),
        fig(SURVEY_ALTESI, "Risultati della survey in Figma"),
        '<a class="pill pill--dark" href="#altea">Demo di Altea in questa pagina <span aria-hidden="true">↓</span></a>']),
    "progetto-linkedin-personal-branding.html": summary([
        ("Tipo di progetto", "Progetto formativo di personal branding (2026), valutato con il massimo risultato."),
        ("Problema", "Riposizionare il profilo LinkedIn verso UX/UI Design senza cancellare il valore di oltre sei anni nella comunicazione."),
        ("Utenti e obiettivo", "Recruiter, Talent Acquisition, UX/UI Lead, Product Designer e hiring manager. Obiettivo: aumentare visibilità e credibilità attraverso progetti, metodo e risultati verificabili."),
        ("Il mio ruolo e contributo", "UX/UI Designer · Content Strategist: posizionamento, ottimizzazione di ogni sezione del profilo, piano editoriale, protocollo di networking e misurazione."),
        ("Scelte progettuali e motivazioni", "Progetti in primo piano prima dei certificati, come prova del lavoro; headline con ruolo target e competenze ricercabili; sei contenuti su tre pillar, ognuno con formato, CTA e KPI."),
        ("Output", "Profilo riposizionato, sei contenuti strategici, piano KPI e di networking, documento completo del progetto."),
        ("Risultati documentati e limiti", "Metriche iniziali osservate: 36 visualizzazioni del profilo, 749 impression del post, 15 apparizioni nelle ricerche. Il Social Selling Index non era accessibile alla rilevazione: non è riportato alcun valore stimato.", True),
    ], [pdf("assets/docs/progetto-linkedin-personal-branding-benedetta-petrucci.pdf", "Progetto completo"),
        fig(LINKEDIN, "Profilo LinkedIn")]),
    "progetto-includo.html": summary([
        ("Tipo di progetto", "Project work di brand identity (2026)."),
        ("Problema", "Serviva un marchio contemporaneo, affidabile e applicabile su supporti digitali diversi, che non si limitasse a dichiarare l’inclusione."),
        ("Utenti e obiettivo", "Obiettivo: tradurre inclusione, dignità del lavoro, trasmissione del sapere e comunità in un’identità riconoscibile. Il progetto non documenta un pubblico specifico né ricerca con utenti."),
        ("Il mio ruolo e contributo", "Visual Designer: concept, progettazione del marchio, costruzione geometrica, palette, tipografia, linee guida e applicazioni per web e social media."),
        ("Scelte progettuali e motivazioni", "Pittogramma dalla stretta di mano geometrizzata, gesto di accordo e fiducia; “DO” evidenziato come invito all’azione condivisa; verde per crescita e inclusione, blu per fiducia e stabilità; versioni e regole d’uso per la riconoscibilità in ogni contesto."),
        ("Output", "Marchio nelle versioni orizzontale, verticale e pittogramma; Brand Guidelines; applicazioni per Facebook, Instagram, YouTube, sito web e set di icone."),
        ("Risultati documentati e limiti", "Non sono documentati test con utenti o metriche. Prossimo passo indicato: validare il sistema su touchpoint fisici e definire tono di voce, motion e accessibilità dei contenuti.", True),
    ], [pdf("assets/docs/includo-brand-guidelines.pdf", "Brand Guidelines")]),
    "progetto-ai.html": summary([
        ("Tipo di progetto", "Project work sperimentale di AI e automazione (2026): un prototipo funzionante, non un prodotto in uso."),
        ("Problema", "Ridurre il lavoro operativo trasformando richieste espresse normalmente — “scrivi a…”, “fissa un appuntamento…” — in operazioni complete, senza esporre la complessità tecnica."),
        ("Utenti e obiettivo", "Obiettivo: un’unica conversazione, più strumenti coordinati, meno passaggi manuali. Il progetto non documenta un gruppo di utenti specifico."),
        ("Il mio ruolo e contributo", "AI Workflow Designer: configurazione dell’agente in n8n con Telegram, OpenAI, Airtable, Gmail e Google Calendar; System Message, credenziali e parametri dinamici; test end-to-end."),
        ("Scelte progettuali e motivazioni", "L’agente sceglie lo strumento in base alla richiesta; conferme in italiano, concise e senza dettagli tecnici superflui; memoria del contesto durante la conversazione."),
        ("Output", "Workflow n8n come prototipo funzionante e documento completo del progetto."),
        ("Risultati documentati e limiti", "I test end-to-end hanno verificato l’invio effettivo delle email e la corretta creazione degli eventi. Non ci sono metriche d’uso; mancano ancora conferme prima delle azioni sensibili, gestione degli errori, log e permessi granulari.", True),
    ], [pdf("assets/docs/agente-ai.pdf", "Progetto completo")]),
}


def case_study(name, title_crumb, extra_css=(), scripts=("site.js",), extra=None):
    def transform(main):
        main = insert_after_cover(main, SUMMARIES[name])
        main = label_index(main)
        main = replace_project_nav(main, name)
        if extra:
            main = extra(main)
        return main
    page(name, "progetti", [("Home", "index.html"), ("Progetti", "progetti.html"), (title_crumb, None)], transform, extra_css, scripts, exact=False)


def altesi_extra(main):
    old = "<p>Il piano è progettato per verificare comprensione, autonomia e fiducia su ricetta, servizi, shop, eventi e Altea. Non presento completion rate, tempi o punteggi come misurati: gli interventi mostrati derivano da progettazione e QA.</p>"
    assert old in main
    note = ('<p class="note"><strong>Trasparenza:</strong> il test di usabilità descritto è ipotetico e non è stato svolto; '
            'i relativi risultati sono simulati e non vanno letti come evidenze. L’unica ricerca svolta con persone reali è la survey con 13 risposte.</p>')
    return main.replace(old, old + "\n            " + note, 1)


# ---------------------------------------------------------------- other pages

def progetti_transform(main):
    types = {
        "progetto-jojob.html": "Project work formativo",
        "progetto-farmacia-altesi.html": "Progetto finale del Master",
        "progetto-linkedin-personal-branding.html": "Progetto formativo",
        "progetto-includo.html": "Project work",
        "progetto-ai.html": "Project work sperimentale",
    }
    for href, label in types.items():
        main = re.sub(
            rf'(<a class="project-card__media[^"]*" href="{re.escape(href)}"[^>]*>.*?</a><div class="project-card__body">)',
            rf'\1<p class="eyebrow">{label}</p>', main, count=1, flags=re.S)
    # Cards are announced by their title link: the decorative image links stay out of the tab order.
    main = main.replace('<h2 class="sr-only" id="all-projects">Tutti i progetti</h2>',
                        '<h2 class="sr-only" id="all-projects">Tutti i progetti</h2>'
                        '<p class="lead" style="margin-bottom:32px">Cinque progetti in ordine di presentazione. Ogni scheda apre direttamente il case study, con sintesi iniziale, materiali originali e collegamenti al progetto precedente e successivo.</p>')
    federlus = f"""<section class="section" aria-labelledby="professional-work">
      <div class="container-site section-heading">
        <div><p class="eyebrow">Lavoro professionale</p><h2 id="professional-work">Progetti e comunicazione per FederLUS, dal 2020.</h2></div>
        <div><p class="lead">Le esperienze sopra sono project work e progetti formativi. Il lavoro professionale in FederLUS — progetti, eventi, comunicazione e visual design — è raccontato nella sua pagina.</p><div class="button-row"><a class="button" href="esperienza-federlus.html">Esperienza FederLUS <span aria-hidden="true">→</span></a><a class="button button--secondary" href="cv.html">CV completo <span aria-hidden="true">→</span></a></div></div>
      </div>
    </section>"""
    return main.replace("</main>", f"  {federlus}\n  </main>")


def federlus_transform(main):
    block = summary([
        ("Tipo di esperienza", "Lavoro professionale, da gennaio 2020 a oggi."),
        ("Organizzazione e contesto", "Federazione BCC Lazio, Umbria e Sardegna, Area Progetti e Comunicazione, Roma."),
        ("Ruolo", "Communication, Design &amp; Project Management Specialist.", True),
        ("Responsabilità documentate", "<ul><li>Gestione di progetti per la Federazione e le BCC associate: raccolta dei bisogni, obiettivi, pianificazione, budget, scadenze, monitoraggio e rendicontazione.</li><li>Coordinamento di direzione, banche, partner, docenti, relatori e fornitori: briefing, flussi operativi, feedback e consegne.</li><li>Organizzazione di eventi istituzionali e territoriali, programmi di educazione finanziaria, iniziative per giovani soci, sostenibilità e mutualità.</li><li>Ideazione di campagne e identità visive; produzione di articoli, pagine web, contenuti social, presentazioni, video e kit grafici coordinati.</li><li>Gestione di WordPress e touchpoint digitali; contributo alla chiarezza, all’accessibilità e alla UX/UI di strumenti interni.</li></ul>", True),
        ("Output tipici", "Campagne e identità visive, materiali coordinati per eventi (locandine, programmi, roll-up, badge, slide), articoli, newsletter, contenuti web e social, foto e video, report e rendicontazioni delle attività, verbali e testi istituzionali."),
        ("Competenze trasferibili alla UX/UI", "Ascolto di bisogni e stakeholder, definizione di obiettivi e priorità, scrittura chiara, sistemi visivi coerenti, coordinamento con team e fornitori, gestione di contenuti WordPress e attenzione all’accessibilità."),
        ("Cosa non è pubblicato", "Rendicontazioni economiche, verbali e documenti interni restano riservati: i progetti sono descritti senza materiali o dati interni.", True),
    ], None)
    m = re.search(r"</header>", main)
    main = main[: m.end()] + "\n    " + block + main[m.end():]
    outputs = """<section class="section" aria-labelledby="outputs-title">
      <div class="container-site">
        <div class="section-heading">
          <div><p class="eyebrow">Output e materiali</p><h2 id="outputs-title">Cosa produco, dal brief alla consegna.</h2></div>
          <p class="lead">Materiali coordinati e documenti che accompagnano progetti ed eventi, tenendo insieme comunicazione, progettazione grafica e gestione operativa.</p>
        </div>
        <ul class="output-list">
          <li><strong>Comunicazione istituzionale</strong>Articoli, newsletter, pagine web su WordPress, contenuti social e presentazioni.</li>
          <li><strong>Progettazione grafica</strong>Identità visive e campagne; locandine, programmi, roll-up, badge e slide coordinati per gli eventi.</li>
          <li><strong>Foto e video</strong>Contenuti foto e video istituzionali, storytelling territoriale e social content.</li>
          <li><strong>Eventi</strong>Programmi, sopralluoghi, allestimenti, rapporti con relatori, location e service, gestione operativa degli appuntamenti.</li>
          <li><strong>Pianificazione e rendicontazione</strong>Cronoprogrammi, budget, monitoraggio, reporting e rendicontazione delle attività.</li>
          <li><strong>Lavoro editoriale istituzionale</strong>Redazione di testi istituzionali e verbali, con cura della chiarezza e della precisione.</li>
        </ul>
        <p class="note">I materiali citati non sono pubblicati in questo portfolio: molti sono documenti interni o di proprietà della Federazione.</p>
      </div>
    </section>"""
    anchor = '<section class="section section--white" aria-labelledby="projects-title">'
    assert anchor in main
    return main.replace(anchor, outputs + "\n\n    " + anchor, 1)


def form_note(main, form_title_id):
    note = (f'<p class="form-note">Il modulo invia il messaggio tramite Formspree, un servizio esterno. '
            f'In alternativa scrivi direttamente a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>')
    pattern = rf'(<h2 id="{form_title_id}" class="form-card__title">.*?</h2>)'
    return re.sub(pattern, r"\1" + note.replace("\\", "\\\\"), main, count=1, flags=re.S)


def contatti_transform(main):
    main = main.replace("<section class=\"section\"><div class=\"container-site contact-grid\">",
                        "<section class=\"section\"><div class=\"container-site\">" + breadcrumb([("Home", "index.html"), ("Contatti", None)]) + "</div><div class=\"container-site contact-grid\">", 1)
    direct = (f'<div class="contact-direct"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>'
              f'<div class="button-row" style="margin-top:8px"><a class="button" href="{CV_IT}" download>CV italiano (PDF) <span aria-hidden="true">↓</span></a>'
              f'<a class="button button--secondary" href="{CV_EN}" download lang="en">English CV (PDF) <span aria-hidden="true">↓</span></a>'
              f'<a class="button button--secondary" href="cv.html">CV online <span aria-hidden="true">→</span></a></div></div>')
    marker = '<div class="button-row"><a class="button button--secondary" href="https://www.linkedin.com/in/benedetta-petrucci-5b333b328/"'
    assert marker in main
    main = main.replace(marker, direct + marker, 1)
    return form_note(main, "form-title")


def cv_transform(main):
    return form_note(main, "cv-form-title")


def federlus_page_transform(main):
    return form_note(federlus_transform(main), "federlus-form-title")


# ---------------------------------------------------------------- home

def home():
    tpl = (HERE / "home.template.html").read_text()
    word = lambda w: '<span class="word">' + "".join(f'<span aria-hidden="true">{c}</span>' for c in w) + "</span>"
    headmeta = """<meta name="description" content="Portfolio di Benedetta Petrucci, UX/UI e visual designer a Roma: case study Farmacia Altesi + Altea, JOJOB, INCLUDO, LinkedIn Personal Branding e AI Assistant, esperienza professionale in FederLUS, CV e contatti.">
<meta name="author" content="Benedetta Petrucci">
<meta name="theme-color" content="#161a1f">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="Benedetta Petrucci — UX/UI Designer | Visual &amp; Digital Design">
<meta property="og:description" content="UX/UI e visual design per rendere servizi digitali più chiari, con progetti documentati dalla ricerca al prototipo.">
<meta property="og:url" content="https://petruccibenedetta93-wq.github.io/portfolio/">
<meta property="og:image" content="https://petruccibenedetta93-wq.github.io/portfolio/assets/images/benedetta-parallax-16x9.jpg">
<meta property="og:image:alt" content="Ritratto di Benedetta Petrucci su fondo scuro">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://petruccibenedetta93-wq.github.io/portfolio/">
<link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">"""
    sections = f"""<main id="contenuto">
  <section class="home-section" id="progetti" aria-labelledby="projects-title">
    <div class="wrap">
      <p class="kicker">Progetti in evidenza</p>
      <h2 id="projects-title">Progetti, dalla ricerca all'interfaccia.</h2>
      <p class="lead">Ricerca e test sul carpooling, progettazione di un servizio sanitario e personal branding misurabile per il posizionamento UX/UI. Ogni scheda apre direttamente il case study.</p>
      <ul class="cases">
        <li><a class="case" href="progetto-farmacia-altesi.html">
          <span class="case__tags">Progetto finale del Master · UX/UI · Ricerca · Prototipi responsive</span>
          <span class="case__title">Farmacia Altesi + Altea</span>
          <span class="case__text">Da una survey con 13 risposte a dieci schermate responsive e un hub conversazionale con passaggio esplicito al farmacista. Il test di usabilità descritto è ipotetico e non è stato svolto.</span>
          <span class="case__cta">Apri il case study →</span>
        </a></li>
        <li><a class="case" href="progetto-jojob.html">
          <span class="case__tags">Project work · UX research · Redesign · User testing</span>
          <span class="case__title">JOJOB</span>
          <span class="case__text">Un percorso completo dalla ricerca all’interfaccia ad alta fedeltà, seguito da due fasi di user testing per trasformare le evidenze in ipotesi di miglioramento.</span>
          <span class="case__cta">Apri il case study →</span>
        </a></li>
        <li><a class="case" href="progetto-includo.html">
          <span class="case__tags">Project work · Brand identity · Visual design</span>
          <span class="case__title">INCLUDO</span>
          <span class="case__text">Un sistema visivo completo: concept, marchio, geometrie, palette, tipografia, regole d'uso e applicazioni digitali.</span>
          <span class="case__cta">Apri il case study →</span>
        </a></li>
      </ul>
      <ul class="cases cases--more">
        <li><a class="case" href="progetto-linkedin-personal-branding.html">
          <span class="case__tags">Progetto formativo · Personal branding · Content strategy · Analytics</span>
          <span class="case__title">LinkedIn Personal Branding</span>
          <span class="case__text">Dal riposizionamento del profilo a sei contenuti misurabili: un progetto valutato con il massimo risultato.</span>
          <span class="case__cta">Apri il case study →</span>
        </a></li>
        <li><a class="case" href="progetto-ai.html">
          <span class="case__tags">Project work sperimentale · AI agents · Automation</span>
          <span class="case__title">AI Assistant</span>
          <span class="case__text">Un agente conversazionale che orchestra Airtable, Gmail e Google Calendar tramite n8n e OpenAI.</span>
          <span class="case__cta">Apri il case study →</span>
        </a></li>
      </ul>
      <a class="more" href="progetti.html">Tutti i progetti <span aria-hidden="true">→</span></a>
    </div>
  </section>

  <section class="home-section home-section--alt" id="profilo" aria-labelledby="about-title">
    <div class="wrap">
      <p class="kicker">Profilo · UX/UI Design · Visual Design · Ricerca utenti</p>
      <h2 id="about-title">Dal design visivo alla progettazione di esperienze digitali.</h2>
      <p class="lead">Esperienze digitali chiare, progettate per le persone. Ciao, sono Benedetta. Progetto interfacce e sistemi visivi partendo da bisogni, evidenze e test. Dal 2020 lavoro nella comunicazione digitale e nel coordinamento di progetti per FederLUS; oggi applico questo bagaglio ai progetti UX/UI.</p>
      <p class="lead">In FederLUS progetto contenuti e identità digitali, dialogo con stakeholder e accompagno il lavoro fino alla consegna. Ho concluso il percorso del Master UX/UI Design di start2impact, approfondendo ricerca, architettura, prototipazione e verifica con utenti: JOJOB, Farmacia Altesi e il progetto LinkedIn Personal Branding mostrano come collego metodo, interfacce e comunicazione.</p>
      <dl class="facts">
        <div class="fact"><dt>Ruolo che cerco</dt><dd>Ruoli UX/UI, UI e visual design: da remoto in Italia o ibridi a Roma.</dd></div>
        <div class="fact"><dt>Esperienza</dt><dd>Dal 2020 progetti, comunicazione ed eventi in FederLUS.</dd></div>
        <div class="fact"><dt>Formazione UX/UI</dt><dd>Master UX/UI Design di start2impact, concluso (2025–2026).</dd></div>
      </dl>
      <div class="stats">
        <div class="stats__item"><strong>6+</strong><span>anni di esperienza professionale</span></div>
        <div class="stats__item"><strong>30+</strong><span>progetti sviluppati</span></div>
        <div class="stats__item"><strong>13</strong><span>BCC supportate</span></div>
      </div>
      <ul class="keywords" aria-label="Ambiti"><li>Communication</li><li>Experience Design</li><li>Project Management</li><li>Creative Direction</li></ul>

      <h3 id="process-title" style="margin-top:72px">Dal bisogno alla soluzione.</h3>
      <p class="lead">Un processo iterativo che mantiene le persone al centro e rende ogni scelta progettuale motivata.</p>
      <div class="process-grid">
        <article class="process-card"><span class="process-card__number">01</span><h3>Comprendere</h3><p>Analizzo contesto, utenti, bisogni e criticità.</p></article>
        <article class="process-card"><span class="process-card__number">02</span><h3>Definire</h3><p>Traduco gli insight in priorità e obiettivi misurabili.</p></article>
        <article class="process-card"><span class="process-card__number">03</span><h3>Progettare</h3><p>Costruisco flussi, wireframe e sistemi visivi coerenti.</p></article>
        <article class="process-card"><span class="process-card__number">04</span><h3>Verificare</h3><p>Prototipo, testo e miglioro la soluzione nel tempo.</p></article>
      </div>

      <h3 id="skills-title" style="margin-top:72px">Una cassetta degli attrezzi davvero trasversale.</h3>
      <p class="lead">Strategia, coordinamento e produzione: competenze diverse che lavorano insieme per portare ogni progetto dall’idea al risultato.</p>
      <div class="skills-grid">
        <article class="skill-card"><h3>UX/UI</h3><ul><li>Ricerca e architettura</li><li>Wireframe e design system</li><li>Prototipi responsive</li></ul></article>
        <article class="skill-card"><h3>Visual &amp; digital</h3><ul><li>Brand e graphic design</li><li>WordPress, HTML e CSS</li><li>Video e contenuti multimediali</li></ul></article>
        <article class="skill-card"><h3>Comunicazione</h3><ul><li>Comunicazione istituzionale</li><li>Campagne e contenuti</li><li>Articoli, presentazioni e social</li></ul></article>
        <article class="skill-card"><h3>Project management</h3><ul><li>Pianificazione e budget</li><li>Stakeholder e fornitori</li><li>Monitoraggio e rendicontazione</li></ul></article>
        <article class="skill-card"><h3>Eventi</h3><ul><li>Ideazione e organizzazione</li><li>Coordinamento operativo</li><li>Materiali e allestimenti</li></ul></article>
        <article class="skill-card"><h3>AI &amp; automazione</h3><ul><li>Agenti AI con n8n</li><li>Prompt design</li><li>Workflow automation</li></ul></article>
      </div>
      <div class="links">
        <a class="pill" href="cv.html">CV completo <span aria-hidden="true">→</span></a>
        <a class="pill pill--dark" href="{CV_IT}" download>CV italiano (PDF) <span aria-hidden="true">↓</span></a>
      </div>
    </div>
  </section>

  <section class="home-section" id="federlus" aria-labelledby="experience-title">
    <div class="wrap">
      <p class="kicker">Esperienza professionale · 2020 — Oggi</p>
      <h2 id="experience-title">Progetti e comunicazione per FederLUS.</h2>
      <p class="lead">Strategia, coordinamento, contenuti, visual design ed eventi per la Federazione delle Banche di Credito Cooperativo del Lazio, Umbria e Sardegna. Seguo progetti dalla pianificazione alla rendicontazione, coordinando stakeholder, partner e fornitori e sviluppando campagne, eventi, contenuti e identità visive.</p>
      <dl class="facts">
        <div class="fact"><dt>Ruolo</dt><dd>Communication, Design &amp; Project Management Specialist</dd></div>
        <div class="fact"><dt>Contesto</dt><dd>Area Progetti e Comunicazione, Federazione BCC Lazio, Umbria e Sardegna</dd></div>
        <div class="fact"><dt>Sede</dt><dd>Roma, dal 2020 a oggi</dd></div>
      </dl>
      <ul class="keywords" aria-label="Aree professionali"><li>Comunicazione istituzionale</li><li>Project management</li><li>Eventi</li><li>Visual design</li><li>Digital</li></ul>
      <div class="duties">
        <div><h3>Progetti ed eventi</h3><p>Coordinamento di progetti ed eventi; rapporti con BCC, partner, fornitori e relatori; pianificazione, scadenze, reporting e rendicontazioni.</p></div>
        <div><h3>Comunicazione istituzionale</h3><p>Contenuti per il sito WordPress, newsletter, social e articoli; redazione di testi istituzionali e verbali.</p></div>
        <div><h3>Visual design e video</h3><p>Identità e materiali per gli eventi (locandine, programmi, roll-up, badge, slide) e contenuti foto e video.</p></div>
      </div>
      <div class="works">
        <h3>Progetti rappresentativi</h3>
        <ul>
          <li><strong>ABC Finanza</strong><span>Educazione finanziaria</span></li>
          <li><strong>Una Bella Educazione</strong><span>Educazione</span></li>
          <li><strong>ESG in Pillole</strong><span>Sostenibilità · video</span></li>
          <li><strong>BCC CAMP</strong><span>Giovani soci</span></li>
          <li><strong>Sviluppo Mutue BCC</strong><span>Mutualità</span></li>
          <li><strong>LEAF</strong><span>Formazione</span></li>
          <li><strong>Ricerca e Convegno</strong><span>Eventi istituzionali</span></li>
          <li><strong>Forum Giovani Soci</strong><span>Community · evento</span></li>
        </ul>
      </div>
      <div class="links">
        <a class="pill" href="esperienza-federlus.html">Esplora l’esperienza <span aria-hidden="true">→</span></a>
        <a class="pill pill--dark" href="cv.html">Vedi il CV <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </section>

  <section class="home-section home-section--alt" id="contatti" aria-labelledby="contact-title">
    <div class="wrap">
      <p class="kicker">Contatti</p>
      <h2 id="contact-title">Costruiamo qualcosa di chiaro, utile e capace di lasciare il segno.</h2>
      <p class="lead">Valuto ruoli UX/UI da remoto in Italia o ibridi a Roma. Se il mio percorso può essere utile al tuo team, scrivimi.</p>
      <div class="contact-grid" style="margin-top:32px;align-items:end">
        <div>
          <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
          <p class="text-muted-site" style="margin-top:10px">Roma, Italia</p>
        </div>
        <div class="links" style="margin-top:0">
          <a class="pill" href="contatti.html">Scrivimi <span aria-hidden="true">→</span></a>
          <a class="pill pill--dark" href="{CV_IT}" download>CV italiano (PDF) <span aria-hidden="true">↓</span></a>
          <a class="pill pill--dark" href="{CV_EN}" download lang="en">English CV (PDF) <span aria-hidden="true">↓</span></a>
          <a class="pill pill--dark" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span>{NEW_TAB}</a>
        </div>
      </div>
    </div>
  </section>
</main>"""
    out = (tpl.replace("__HEADMETA__", headmeta)
              .replace("__RINGS__", "\n".join(f'      <path d="{d}"/>' for d in RINGS))
              .replace("__TITLE__", word("BENEDETTA") + word("PETRUCCI"))
              .replace("__IMG__", "assets/images/benedetta-parallax-16x9.jpg")
              .replace("__SECTIONS__", sections)
              .replace("__FOOTER__", footer())
              .replace('<a class="skip" href="#progetti">Vai ai progetti</a>', '<a class="skip" href="#contenuto">Vai al contenuto principale</a>')
              .replace("<body>", '<body id="top">', 1)
              .replace("</body>", '<script src="assets/js/site.js" defer></script>\n</body>'))
    found = re.findall(r'<path d="([^"]*)"/>', out)
    assert found == RINGS, "home rings differ from rings.paths.txt"
    assert 'href="#"' not in out
    (ROOT / "index.html").write_text(out)


def main():
    home()
    page("progetti.html", "progetti", [("Home", "index.html"), ("Progetti", None)], progetti_transform, ("altesi.css",))
    case_study("progetto-jojob.html", "JOJOB")
    case_study("progetto-farmacia-altesi.html", "Farmacia Altesi + Altea", ("altesi.css",), ("site.js", "altea-demo.js"), altesi_extra)
    case_study("progetto-linkedin-personal-branding.html", "LinkedIn Personal Branding")
    case_study("progetto-includo.html", "INCLUDO")
    case_study("progetto-ai.html", "AI Assistant")
    page("esperienza-federlus.html", "esperienza", [("Home", "index.html"), ("Esperienza FederLUS", None)], federlus_page_transform)
    page("cv.html", "cv", [("Home", "index.html"), ("CV", None)], cv_transform)
    page("contatti.html", "contatti", [], contatti_transform)
    for name in ["index.html", "progetti.html", "esperienza-federlus.html", "cv.html", "contatti.html"] + [p[0] for p in PROJECTS]:
        text = (ROOT / name).read_text()
        assert "main.css" not in text and 'href="#"' not in text, name
    print("built 10 pages")


if __name__ == "__main__":
    main()
