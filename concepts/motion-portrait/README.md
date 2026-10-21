# Bozza: hero con ritratto (PARALLAX corrente, B e A di confronto)

Proposta visiva **isolata e non pubblicata** per la home del portfolio. Non sostituisce `index.html` e non modifica il resto del sito: tutto vive in questa cartella.

## Direzione corrente: PARALLAX (21 ottobre 2026)

Benedetta ha scelto di lavorare sul prompt MotionSites "Parallax" (`https://motionsites.ai/?prompt=parallex`) per il portfolio, con la sua foto e i colori carbone già usati. **B · Editorial portrait resta come backup e confronto**; A resta solo alternativa.

- **Dove**: `parallax/src/` (template, `rings.paths.txt` con i 12 tracciati), `parallax/index.html` (build per il repository), `standalone/benedetta-parallax.html` (file unico con la foto incorporata, si apre con doppio clic). Build: `node scripts/build-parallax.mjs` (repository), `... standalone`, `... artifact <cartella>`. Lo script verifica che i 12 `d` siano identici a `rings.paths.txt` e che non ci siano `href="#"`.
- **Foto**: `parallax/assets/benedetta-16x9.jpg`, conversione JPEG di `clip/start-frame-16x9.png` (1920×1080, la foto originale su fondo carbone). Non è stata generata né ritoccata; nel layout è solo scalata e spostata (880 unità di scena) per portare il volto dentro gli archi di destra. Sugli schermi verticali la scena si sposta per tenere il volto al centro.
- **Cosa resta del prompt**: 12 path esatti nell'ordine dato, disegno degli anelli dal centro, comparsa coordinata di lettere, testi, barra, logo, menu e pulsanti con gli stessi tempi e curve, doppia scala `--sc`/`--u`, regole mobile, focus, `prefers-reduced-motion` senza ingresso.
- **Adattamenti voluti da Benedetta**: identità e testi suoi (nessun "PX", nessuna campagna o premio), sfondo carbone `#161a1f` invece di `#3a5462`, nome su due righe con il ruolo sotto, menu funzionante (Escape, clic fuori, link, Tab confinato, area di tocco 44 px), testo dell'interfaccia mai sotto i 13 px, hero a tutto schermo seguito da sezioni scorrevoli (case study, FederLUS, contatti) invece di una pagina bloccata; sui telefoni piccoli l'hero ha un'altezza minima di 660 px e si scorre un poco invece di rimpicciolire testi e pulsanti.
- **Percorsi**: un clic dalla home a Farmacia Altesi + Altea, JOJOB e INCLUDO; "Tutti i progetti" secondario; CV in PDF (italiano e inglese), email, LinkedIn e modulo di contatto reali; esperienza FederLUS con contesto, ruolo, contributo e progetti rappresentativi, più il link alla pagina esistente.
- **Caratteri**: i file PX Mono / PX Sans del template non sono disponibili; si usano gli stack di ripiego previsti dal prompt, Inter e Roboto Mono da Google Fonts.
- **Verifiche svolte** (tecniche, non test con utenti): Playwright a 1920×1080, 1440×900, 1383×695, 1062×590, 768×1024, 390×844, 320×568, 844×390; nessuno scorrimento orizzontale, nessun testo sul volto o sovrapposto ad altri testi, menu da tastiera e con clic, reduced-motion, link interni e PDF che rispondono 200.
- **Avviso del controllo di design "flat type hierarchy"** su `parallax/src/template.html`: falso positivo. Le dimensioni sono scritte con `clamp()`/`calc()` in unità di scena e lo strumento non le risolve; nelle schermate i titoli di sezione misurano 34–60 px contro 17 px del testo e il nome nell'hero è nettamente più grande. Nessuna soppressione automatica è conservata nel repository.
- **Proposta video** separata e non avviata: `clip/PROPOSTA-VIDEO.md`. Il 21 ottobre Benedetta ha fornito un breve video reale (nel suo spazio Adobe, non scaricabile da questo ambiente): è registrato lì con trattamento, storyboard e limiti. Non va pubblicato né usato nell'hero.

## Decisione di direzione (21 ottobre 2026)

Benedetta ha scelto la **variante B · Editorial portrait** (adattamento del template Aurai) come base del portfolio: il suo ritratto reale, serif leggera, superfici glass, azioni verso Progetti, CV e Contatti.

- Lo sviluppo prosegue **solo su B** (`src/variant-b/`, `app/b/`).
- La **variante A** (Motion portrait / Pixel) resta nel repository solo come alternativa di confronto: non va più sviluppata né aggiornata.
- **Correzione del 21 ottobre**: in B il ritratto è più piccolo (al massimo il 78% dell'altezza della finestra) e sta in un riquadro a destra, separato dalla colonna dei testi; titolo, descrizione, CTA e pillole stanno tutti a sinistra. Sotto i 1024 px il ritratto è un blocco a sé tra navigazione e testi, senza sovrapposizioni.
- **Clip**: la clip image-to-video è approvata come idea; preventivo, prompt e fotogramma di partenza sono in `clip/`. Nessuna clip è stata generata.
- Restano valide le condizioni della bozza: nessuna pubblicazione o modifica della home senza un'indicazione esplicita, nessun video generato, caratteri provvisori da verificare (Newsreader al posto di Askan Light).

- **A · Motion portrait / Pixel**: nero, Inter + carattere pixel, ritratto protagonista a tutta pagina.
- **B · Editorial portrait**: serif leggero, superfici glass, fondale da studio.

Entrambe usano lo stesso ritratto reale (`assets/images/benedetta-cutout-hq.png`, riusato dal repository senza copiarlo), gli stessi contenuti professionali e solo link a pagine esistenti: `progetti.html`, `index.html#profilo`, `cv.html`, `contatti.html`, LinkedIn.

## Aprire la bozza senza terminale

Nella cartella `standalone/` ci sono due file HTML autonomi, uno per variante:

- `standalone/variante-a-motion-portrait.html`
- `standalone/variante-b-editorial-portrait.html`

Basta un doppio clic per aprirli nel browser: JavaScript, CSS e ritratto (il PNG originale, invariato) sono incorporati nel file. I caratteri arrivano da Google Fonts, quindi serve la connessione; offline compaiono i caratteri di sistema. I link della navigazione portano alle pagine reali del portfolio online. Per rigenerarli: `npm run build:standalone`.

## Aprire la bozza con un server locale

La cartella `preview/` contiene la build già pronta. Serve un server statico avviato dalla **radice del repository** (i moduli JavaScript non si aprono con `file://`):

```bash
# dalla radice del repository
python3 -m http.server 4173
# poi aprire http://localhost:4173/concepts/motion-portrait/preview/
```

Da lì si sceglie la variante A o B. Gli screenshot di riferimento sono in `screenshots/`.

## Sviluppo

```bash
cd concepts/motion-portrait
npm install
npm run dev        # anteprima con ritratto e link presi dal sito online
npm run typecheck
npm run build      # rigenera preview/ con percorsi relativi al repository
```

Stack: React, TypeScript, Tailwind CSS 3, Vite, lucide-react. Il resto del repository resta HTML/CSS statico.

## Caratteri

| Previsto dal template | Usato nella bozza | Motivo |
| --- | --- | --- |
| basis33 (pixel) | **VT323**, Google Fonts, SIL OFL | basis33 risulta distribuito con una licenza permissiva (Manchson, su base Proggy Clean), ma la fonte ufficiale con il `LICENSE.txt` non era raggiungibile da questo ambiente, e il link del template punta a un CDN di terze parti (onlinewebfonts) senza licenza verificabile. VT323 è più largo e più "terminale" di basis33. |
| Askan Light (serif) | **Newsreader 300**, Google Fonts, SIL OFL | Askan è un carattere commerciale di Hoftype (Dieter Hofrichter). Non va caricato dal CDN di terze parti del template. |
| Inter | Inter, Google Fonts | Come da template. |

Per passare a basis33: scaricare il pacchetto dalla fonte dell'autore, verificare il `LICENSE.txt`, ospitare il file in questa cartella con `@font-face` e cambiare `fontFamily.pixel` in `tailwind.config.ts`.

## Ritratto e video

In questa prima bozza il ritratto è **statico**. Il movimento è solo una leggera deriva del ritratto verso il puntatore (pochi pixel), attiva con mouse/trackpad e disattivata su touch e con `prefers-reduced-motion`. Nessun video è stato generato o presentato come tale.

I video dei template originali restano **solo riferimento** e non sono usati come asset né come volto:

- A (MotionSites, "Adam Roberts"): `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260725_114042_d2ed2a89-f2fa-449b-9609-da456344257b.mp4`
- B ("Aurai"): `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260618_174853_aac61aa2-0f3f-4cf1-bc78-7f657dd11164.mp4`

Per un futuro filmato personale, `src/shared/PortraitMedia.tsx` accetta già una prop `videoSrc`: con un file impostato mostra un video muto in loop con la foto come poster, e con reduced-motion torna alla foto. Prima servono: scelta della variante, decisione sui crediti Higgsfield, una clip breve (5–8 s, loop pulito, stessa inquadratura testa+torso, sfondo coerente con la variante), versioni compresse (MP4 H.264 + WebM, sotto 2–3 MB) e verifica del contrasto del testo sul fotogramma più chiaro.

## Scostamenti dal template, motivati

- Nessun riferimento ad Adam Roberts, Grilled Pixels, Aurai, premi o contatori; monogramma BP originale disegnato su griglia pixel.
- **A**: titolo "Do forma / alle idee, / progetto / esperienze" (righe 2 e 4 in pixel) al posto di "Do forma a nuove idee e creo esperienze", più naturale e con il verbo del mestiere. Interlinea 0,92 / 0,82 al posto di 0,72, che con VT323 sovrapponeva le righe. Su mobile e finestre basse il ritratto è nel flusso tra griglia e titolo, e la pagina scorre in verticale invece di tagliare il contenuto.
- **B**: (superato dalla correzione del 21 ottobre, vedi sopra) ritratto fuori centro perché centrato il titolo cadeva sulla bocca. Titolo ridotto a "Idee che prendono forma." per stare in due righe; il ruolo UX/UI è nel sottotitolo e nella prima pillola. Il form email del template è sostituito da due azioni reali (progetti, CV). Il menu è utilizzabile a ogni larghezza: link in linea da 768 px, hamburger sotto.
- Sfumature funzionali (alone dietro il ritratto, scurimento in basso) per separare la giacca nera dal fondo e tenere leggibili titolo e pulsanti.
- La skill Taste vieta glass, pillole ed etichette maiuscole spaziate: qui prevale la specifica dei template richiesta dall'autrice.

## Verifiche svolte

Build e TypeScript senza errori. Playwright (Chromium) a 1383×695, 1440×900, 768×1024, 390×844, 320×568 e 844×390: nessuno scorrimento orizzontale, nessun testo o CTA tagliato, tutti i link interni rispondono 200, nessun `href="#"`. Menu: `aria-expanded`/`aria-controls`, focus spostato nel menu, Tab e Shift+Tab confinati, Escape chiude, focus restituito al pulsante, contenuto dietro `inert`, i link chiudono il menu; con reduced-motion transizioni del menu e deriva del ritratto disattivate.
