# Portfolio UX/UI — Benedetta Petrucci

Portfolio personale realizzato come progetto finale HTML e CSS del Master.

## Contenuti

- Home responsive
- Panoramica dei progetti
- Case study JOJOB
- Case study INCLUDO
- Case study AI Assistant
- Curriculum interamente in HTML
- Pagina Contattami con form e validazione nativa

## Tecnologie

- HTML5 semantico
- Sass / CSS3 con custom properties
- Utility CSS personalizzate
- CSS Grid e Flexbox
- GitHub Pages

Il progetto non utilizza JavaScript personalizzato né dipendenze CSS esterne. Palette, tipografia, bordi e ombre sono gestiti attraverso custom properties definite in `:root`. Anche il menu mobile è realizzato con elementi HTML nativi e CSS.

## Avvio locale

Aprire `index.html` nel browser oppure avviare un server statico dalla cartella del progetto.

Per ricompilare Sass:

```bash
npm install
npm run sass
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
