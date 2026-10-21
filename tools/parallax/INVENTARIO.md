# Inventario contenuti prima / dopo il redesign PARALLAX

Confronto automatico (`tools/parallax/inventory.py`) tra il contenuto di `<main>` delle pagine al commit `fe39fa7` (prima del redesign) e le pagine ricostruite. Testi, testi alternativi, immagini, documenti, link esterni e ancore.

| Pagina (URL invariato) | Testi prima | Immagini | Documenti | Link esterni | Ancore | Testi dopo | Testi mancanti | Testi spostati su altra pagina | Asset/link mancanti | Ancore mancanti |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| index.html | 106 | 3 | 0 | 0 | 9 | 151 | 0 | 18 | 0 | 0 |
| progetti.html | 42 | 4 | 0 | 0 | 3 | 71 | 0 | 0 | 0 | 0 |
| progetto-farmacia-altesi.html | 210 | 0 | 0 | 4 | 17 | 255 | 0 | 0 | 0 | 0 |
| progetto-jojob.html | 158 | 5 | 7 | 2 | 11 | 212 | 0 | 0 | 0 | 0 |
| progetto-includo.html | 53 | 2 | 1 | 0 | 6 | 99 | 0 | 0 | 0 | 0 |
| progetto-linkedin-personal-branding.html | 78 | 4 | 1 | 1 | 7 | 125 | 0 | 0 | 0 | 0 |
| progetto-ai.html | 66 | 1 | 1 | 0 | 6 | 111 | 0 | 0 | 0 | 0 |
| esperienza-federlus.html | 93 | 0 | 0 | 0 | 11 | 148 | 0 | 0 | 0 | 0 |
| cv.html | 146 | 1 | 2 | 2 | 18 | 165 | 0 | 0 | 0 | 0 |
| contatti.html | 31 | 0 | 0 | 1 | 11 | 52 | 0 | 0 | 0 | 0 |

## Elementi mancanti

Nessuno: ogni testo, immagine, documento, link esterno e ancora delle pagine originali è presente nel nuovo sito.

## Sostituzioni intenzionali (etichette di navigazione e decorazioni)

- `index.html` · “Scopri i progetti”: pulsante dell'hero, ora “Progetti ↓” (stessa destinazione: i progetti) e menu “Progetti”
- `index.html` · “Consulta il CV”: pulsante dell'hero, ora “CV (PDF)” nell'hero e “CV” nel menu e nel piè di pagina
- `index.html` · “Roma · Italia”: firma decorativa; la città compare come “Roma, Italia” nell'hero e nei contatti
- `index.html` · “Scroll to explore”: invito decorativo allo scorrimento, sostituito dal pulsante “Progetti ↓”
- `index.html` · “Selected work”: etichetta della sezione progetti, ora “Progetti in evidenza”
- `index.html` · “Ritratto professionale di Benedetta Petrucci, UX/UI Designer e Digital Product Designer”: testo alternativo del vecchio ritratto: la hero usa il fotogramma 16:9 della stessa foto, con un testo alternativo descrittivo
- `index.html` · “assets/images/benedetta-cutout-hq.png”: il ritaglio resta nel repository; la hero usa assets/images/benedetta-parallax-16x9.jpg, la stessa foto su fondo carbone
- `progetto-farmacia-altesi.html` · “← Precedente: JOJOB”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-farmacia-altesi.html` · “Prossimo: Personal Branding →”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-jojob.html` · “← Tutti i progetti”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-jojob.html` · “Prossimo: Farmacia Altesi →”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-includo.html` · “← Precedente: Personal Branding”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-includo.html` · “Prossimo: AI Assistant →”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-linkedin-personal-branding.html` · “← Precedente: Farmacia Altesi”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-linkedin-personal-branding.html` · “Prossimo: INCLUDO →”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-ai.html` · “← Precedente: INCLUDO”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”
- `progetto-ai.html` · “Tutti i progetti →”: vecchio link precedente/successivo: sostituito dalla navigazione “Progetto precedente · Tutti i progetti · Progetto successivo”

## Testi spostati su un’altra pagina

- da `index.html`: UX Research
- da `index.html`: Wireframing
- da `index.html`: User Testing
- da `index.html`: JOJOB — Redesign del carpooling
- da `index.html`: Esplora il case study →
- da `index.html`: ALTESI
- da `index.html`: farmacia
- da `index.html`: Una farmacia più vicina,
- da `index.html`: anche online.
- da `index.html`: Ricetta
- da `index.html`: Servizi
- da `index.html`: Responsive UI
- da `index.html`: Conversational UX
- da `index.html`: Farmacia Altesi + Altea — Progetto finale UX/UI
- da `index.html`: Content Strategy
- da `index.html`: LinkedIn Personal Branding — Strategia e KPI
- da `index.html`: Metodo
- da `index.html`: Competenze
