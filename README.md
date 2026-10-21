# Portfolio UX/UI — Benedetta Petrucci

Portfolio personale realizzato come progetto finale HTML e CSS del Master, ridisegnato nel 2026 con il sistema visivo **PARALLAX**.

Sito pubblicato: https://petruccibenedetta93-wq.github.io/portfolio/ (versione inglese: https://petruccibenedetta93-wq.github.io/portfolio/en/)

## Redesign PARALLAX

- Tutte le 10 pagine usano lo stesso sistema: `assets/css/parallax.css` (palette carbone dalla foto, pannelli neri, Inter e Roboto Mono da Google Fonts come ripiego dei caratteri PX del prompt MotionSites) e `assets/js/site.js` (menu con Escape e focus, indice dei case study con sezione corrente, comparsa discreta dei blocchi, disattivata con `prefers-reduced-motion`).
- La home conserva hero, anelli e animazioni PARALLAX (12 tracciati identici al prompt, verificati dallo script) con la foto `assets/images/benedetta-parallax-16x9.jpg`.
- Le schermate dei progetti mantengono i colori originali: gli elementi disegnati in CSS e la demo di Altea di Farmacia Altesi sono in `assets/css/altesi.css`.
- Ogni case study si apre con una sintesi (tipo di progetto, problema, utenti e obiettivo, ruolo e contributo, scelte, output, risultati documentati e limiti) e i materiali originali (Figma, PDF), poi l'indice e gli approfondimenti; in fondo progetto precedente, tutti i progetti e progetto successivo.
- URL e ancore restano invariati. Il modulo di contatto continua a inviare tramite Formspree.
- Le pagine sono generate da `tools/parallax/build_site.py` a partire dal contenuto originale (commit `fe39fa7`); `tools/parallax/inventory.py` verifica che non manchi nessun testo, immagine, documento, link o ancora e scrive `tools/parallax/INVENTARIO.md`.

## Versione inglese

- Il sito italiano resta quello principale. La cartella `en/` contiene le stesse 10 pagine in inglese, con nomi di file inglesi (`projects.html`, `project-jojob.html`, `contact.html`…), gli stessi id e gli stessi file in `assets/`.
- Ogni pagina ha il tasto **EN / IT** nell'header e il link “English version” / “Versione italiana” nel piè di pagina; il tasto porta alla pagina equivalente nell'altra lingua e mantiene la sezione aperta. I tag `hreflang` e `sitemap.xml` collegano le due versioni.
- Le pagine inglesi sono generate da `tools/parallax/build_en.py` a partire dalle pagine italiane: ogni testo, testo alternativo, etichetta e meta descrizione è tradotto in `tools/parallax/i18n/en.json` (italiano e inglese affiancati). La generazione si ferma se un testo italiano non ha la traduzione.
- Restano in italiano, e sono marcate `lang="it"`, le schermate disegnate di Farmacia Altesi (sono il prodotto progettato per una farmacia italiana). I PDF e i file Figma dei progetti sono in italiano; il CV ha anche la versione inglese, proposta per prima nelle pagine inglesi. La demo di Altea e i testi dei menu sono bilingui (`assets/js/altea-demo.js`, `assets/js/site.js`).
- Il modulo di contatto inglese usa lo stesso indirizzo Formspree e segnala l'origine “Pagina Contatti (versione inglese)”.

## Contenuti

- Home (hero PARALLAX, progetti, profilo, esperienza FederLUS, contatti)
- Progetti
- Case study Farmacia Altesi + Altea, JOJOB, LinkedIn Personal Branding, INCLUDO, AI Assistant
- Esperienza professionale FederLUS
- Curriculum interamente in HTML, con PDF italiano e inglese
- Pagina Contatti con form (Formspree) e validazione nativa

## Tecnologie

- HTML5 semantico
- CSS3 con custom properties
- CSS Grid e Flexbox
- GitHub Pages

Nella versione PARALLAX i caratteri arrivano da Google Fonts e un piccolo script gestisce menu, indice e animazioni; tutti i contenuti restano leggibili senza JavaScript.

## Avvio locale

Aprire `index.html` nel browser oppure avviare un server statico dalla cartella del progetto.

Per rigenerare le pagine PARALLAX e l'inventario dei contenuti:

```bash
python3 tools/parallax/build_site.py
python3 tools/parallax/inventory.py
python3 tools/parallax/build_en.py --extract   # dopo una modifica ai testi italiani: elenca i testi nuovi da tradurre in i18n/en.json
python3 tools/parallax/build_en.py             # rigenera en/ (si ferma se manca una traduzione)
```

## Pubblicazione su GitHub Pages

1. Creare un repository chiamato `portfolio`.
2. Caricare tutti i file mantenendo invariata la struttura delle cartelle.
3. Aprire `Settings > Pages`.
4. In `Build and deployment`, scegliere `Deploy from a branch`.
5. Selezionare il branch `main` e la cartella `/root`.
6. Salvare e attendere la pubblicazione.

Se l'indirizzo del sito cambia, aggiornare `SITE` in `tools/parallax/build_site.py`, rigenerare le pagine (canonical URL e tag Open Graph) e aggiornare `robots.txt` e `sitemap.xml`.

## Form di contatto

Il form include label associate, campi obbligatori, tipi di input corretti, autocomplete e validazione HTML nativa. I messaggi sono inviati tramite Formspree; la pagina lo dichiara e indica anche l'email diretta.

## Accessibilità

- Link per saltare al contenuto principale
- Navigazione utilizzabile da tastiera
- Focus visibile
- Contrasto cromatico elevato
- Testi alternativi contestuali
- Gerarchia semantica dei titoli
- Supporto a `prefers-reduced-motion`
- Layout responsive da mobile a desktop
- Stili di stampa essenziali (senza menu, piè di pagina e decorazioni)
