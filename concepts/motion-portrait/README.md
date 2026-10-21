# Bozza: hero con ritratto (varianti A e B)

Proposta visiva **isolata e non pubblicata** per la home del portfolio. Non sostituisce `index.html` e non modifica il resto del sito: tutto vive in questa cartella.

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
- **B**: su desktop il ritratto è spostato a destra (64%) invece che al centro, perché centrato il titolo cadeva sulla bocca. Titolo ridotto a "Idee che prendono forma." per stare in due righe; il ruolo UX/UI è nel sottotitolo e nella prima pillola. Il form email del template è sostituito da due azioni reali (progetti, CV). Il menu è utilizzabile a ogni larghezza: link in linea da 768 px, hamburger sotto.
- Sfumature funzionali (alone dietro il ritratto, scurimento in basso) per separare la giacca nera dal fondo e tenere leggibili titolo e pulsanti.
- La skill Taste vieta glass, pillole ed etichette maiuscole spaziate: qui prevale la specifica dei template richiesta dall'autrice.

## Verifiche svolte

Build e TypeScript senza errori. Playwright (Chromium) a 1383×695, 1440×900, 768×1024, 390×844, 320×568 e 844×390: nessuno scorrimento orizzontale, nessun testo o CTA tagliato, tutti i link interni rispondono 200, nessun `href="#"`. Menu: `aria-expanded`/`aria-controls`, focus spostato nel menu, Tab e Shift+Tab confinati, Escape chiude, focus restituito al pulsante, contenuto dietro `inert`, i link chiudono il menu; con reduced-motion transizioni del menu e deriva del ritratto disattivate.
