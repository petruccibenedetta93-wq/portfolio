# Portfolio UX/UI — Benedetta Petrucci

Portfolio personale realizzato come progetto finale HTML e CSS del Master, ridisegnato nel 2026 con il sistema visivo **PARALLAX** (ramo di lavoro, in revisione prima della pubblicazione).

## Redesign PARALLAX

- Tutte le 10 pagine usano lo stesso sistema: `assets/css/parallax.css` (palette carbone dalla foto, pannelli neri, Inter e Roboto Mono da Google Fonts come ripiego dei caratteri PX del prompt MotionSites) e `assets/js/site.js` (menu con Escape e focus, indice dei case study con sezione corrente, comparsa discreta dei blocchi, disattivata con `prefers-reduced-motion`).
- La home conserva hero, anelli e animazioni PARALLAX (12 tracciati identici al prompt, verificati dallo script) con la foto `assets/images/benedetta-parallax-16x9.jpg`.
- Le schermate dei progetti mantengono i colori originali: gli elementi disegnati in CSS e la demo di Altea di Farmacia Altesi sono in `assets/css/altesi.css`.
- Ogni case study si apre con una sintesi (tipo di progetto, problema, utenti e obiettivo, ruolo e contributo, scelte, output, risultati documentati e limiti) e i materiali originali (Figma, PDF), poi l'indice e gli approfondimenti; in fondo progetto precedente, tutti i progetti e progetto successivo.
- URL e ancore restano invariati. Il modulo di contatto continua a inviare tramite Formspree.
- Le pagine sono generate da `tools/parallax/build_site.py` a partire dal contenuto originale (commit `fe39fa7`); `tools/parallax/inventory.py` verifica che non manchi nessun testo, immagine, documento, link o ancora e scrive `tools/parallax/INVENTARIO.md`.
- `assets/css/main.css` e `assets/scss/` sono il foglio di stile precedente: restano nel repository ma non sono più collegati alle pagine.

## Contenuti

- Home (hero PARALLAX, progetti, profilo, esperienza FederLUS, contatti)
- Progetti
- Case study Farmacia Altesi + Altea, JOJOB, LinkedIn Personal Branding, INCLUDO, AI Assistant
- Esperienza professionale FederLUS
- Curriculum interamente in HTML, con PDF italiano e inglese
- Pagina Contatti con form (Formspree) e validazione nativa

## Tecnologie

- HTML5 semantico
- Sass / CSS3 con custom properties
- Utility CSS personalizzate
- CSS Grid e Flexbox
- GitHub Pages

Nella versione PARALLAX i caratteri arrivano da Google Fonts e un piccolo script gestisce menu, indice e animazioni; tutti i contenuti restano leggibili senza JavaScript.

## Avvio locale

Aprire `index.html` nel browser oppure avviare un server statico dalla cartella del progetto.

Per rigenerare le pagine PARALLAX e l'inventario dei contenuti:

```bash
python3 tools/parallax/build_site.py
python3 tools/parallax/inventory.py
```

## Pubblicazione su GitHub Pages

1. Creare un repository chiamato `portfolio`.
2. Caricare tutti i file mantenendo invariata la struttura delle cartelle.
3. Aprire `Settings > Pages`.
4. In `Build and deployment`, scegliere `Deploy from a branch`.
5. Selezionare il branch `main` e la cartella `/root`.
6. Salvare e attendere la pubblicazione.

Se il nome utente GitHub o il repository sono diversi, aggiornare i canonical URL, i tag Open Graph, `robots.txt` e `sitemap.xml` sostituendo `https://benedettapetrucci.github.io/portfolio/` con l’indirizzo definitivo.

## Form di contatto

Il form include label associate, campi obbligatori, tipi di input corretti, autocomplete e validazione HTML nativa. Prima della pubblicazione definitiva può essere collegato a EmailJS o a un servizio form compatibile con GitHub Pages.

## Accessibilità

- Link per saltare al contenuto principale
- Navigazione utilizzabile da tastiera
- Focus visibile
- Contrasto cromatico elevato
- Testi alternativi contestuali
- Gerarchia semantica dei titoli
- Supporto a `prefers-reduced-motion` e `prefers-contrast`
- Layout responsive da mobile a desktop
- Stili di stampa dedicati al CV
