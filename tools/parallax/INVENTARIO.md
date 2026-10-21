# Inventario contenuti prima / dopo il redesign PARALLAX

Confronto automatico (`tools/parallax/inventory.py`) tra il contenuto di `<main>` delle pagine al commit `fe39fa7` (prima del redesign) e le pagine ricostruite. Testi, testi alternativi, immagini, documenti, link esterni e ancore.

| Pagina (URL invariato) | Testi prima | Immagini | Documenti | Link esterni | Ancore | Testi dopo | Testi mancanti | Testi spostati su altra pagina | Asset/link mancanti | Ancore mancanti |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| index.html | 106 | 3 | 0 | 0 | 9 | 152 | 0 | 18 | 0 | 0 |
| progetti.html | 42 | 4 | 0 | 0 | 3 | 74 | 0 | 0 | 0 | 0 |
| progetto-farmacia-altesi.html | 210 | 0 | 0 | 4 | 17 | 258 | 0 | 0 | 0 | 0 |
| progetto-jojob.html | 158 | 5 | 7 | 2 | 11 | 198 | 0 | 0 | 0 | 0 |
| progetto-includo.html | 53 | 2 | 1 | 0 | 6 | 102 | 0 | 0 | 0 | 0 |
| progetto-linkedin-personal-branding.html | 78 | 4 | 1 | 1 | 7 | 128 | 0 | 0 | 0 | 0 |
| progetto-ai.html | 66 | 1 | 1 | 0 | 6 | 114 | 0 | 0 | 0 | 0 |
| esperienza-federlus.html | 93 | 0 | 0 | 0 | 11 | 151 | 0 | 0 | 0 | 0 |
| cv.html | 146 | 1 | 2 | 2 | 18 | 168 | 0 | 0 | 0 | 0 |
| contatti.html | 31 | 0 | 0 | 1 | 11 | 55 | 0 | 0 | 0 | 0 |

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

## Tagli e riscritture approvati dall’autrice (21 ottobre 2026)

Dopo la pubblicazione Benedetta ha chiesto di sostituire nel profilo gli ambiti generici con competenze UX/UI, tenere una sola frase d’apertura e accorciare i case study principali mantenendo le parti fondamentali.

- `index.html` · “Esperienze digitali chiare, progettate”: frase d'apertura doppia: resta il titolo “Dal design visivo alla progettazione di esperienze digitali.”
- `index.html` · “per le persone.”: seconda riga della stessa frase d'apertura
- `index.html` · “Experience Design”: profilo della home riscritto su richiesta dell'autrice: competenze UX/UI al posto degli ambiti generici
- `index.html` · “Creative Direction”: profilo della home riscritto su richiesta dell'autrice: competenze UX/UI al posto degli ambiti generici
- `index.html` · “Una cassetta degli attrezzi davvero trasversale.”: profilo della home riscritto su richiesta dell'autrice: competenze UX/UI al posto degli ambiti generici (titolo delle competenze)
- `index.html` · “Strategia, coordinamento e produzione: competenze diverse che lavorano insieme per portare ogni progetto dall’idea al risultato.”: profilo della home riscritto su richiesta dell'autrice: competenze UX/UI al posto degli ambiti generici (introduzione alle competenze)
- `index.html` · “Pianificazione e budget”: schede Project management ed Eventi unite in “Progetti ed eventi”
- `index.html` · “Monitoraggio e rendicontazione”: schede Project management ed Eventi unite in “Progetti ed eventi”
- `index.html` · “Coordinamento operativo”: schede Project management ed Eventi unite in “Progetti ed eventi”
- `index.html` · “Materiali e allestimenti”: schede Project management ed Eventi unite in “Progetti ed eventi”
- `index.html` · “Ricerca e architettura”: scheda UX/UI riscritta con competenze più precise
- `index.html` · “Wireframe e design system”: scheda UX/UI riscritta con competenze più precise
- `progetto-farmacia-altesi.html` · “Il piano è progettato per verificare comprensione, autonomia e fiducia su ricetta, servizi, shop, eventi e Altea. Non presento completion rate, tempi o punteggi come misurati: gli interventi mostrati derivano da progettazione e QA.”: accorciato: la seconda frase ripeteva la nota di trasparenza sul test ipotetico
- `progetto-jojob.html` · “Colore”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Palette primaria, neutri e colori semantici per feedback immediati.”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Tipografia”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Una gerarchia modulare per contenuti scansionabili su ogni device.”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Componenti”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Button, form, card e badge progettati con varianti e stati coerenti.”: schede Colore, Tipografia e Componenti rimosse: ripetevano il paragrafo sul design system
- `progetto-jojob.html` · “Responsive coerente”: case study accorciato: la scheda ripeteva l'introduzione della sezione
- `progetto-jojob.html` · “La struttura diventa verticale senza eliminare informazioni o funzionalità.”: case study accorciato: la scheda ripeteva l'introduzione della sezione
- `progetto-jojob.html` · “Flusso completo”: case study accorciato: la scheda ripeteva la didascalia dell'immagine
- `progetto-jojob.html` · “Home, ricerca, filtri, dettaglio, conferma, offerta del passaggio e dashboard.”: case study accorciato: la scheda ripeteva la didascalia dell'immagine
- `progetto-jojob.html` · “User Test 1 definisce il protocollo; User Test 2 documenta le sessioni e trasforma ciò che è emerso in ipotesi da verificare. Le due consegne diventano così un unico percorso, senza confondere obiettivi, risultati e decisioni progettuali.”: introduzione del test accorciata alla prima frase
- `progetto-jojob.html` · “scenari di test”: riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi
- `progetto-jojob.html` · “4/5”: riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi
- `progetto-jojob.html` · “smartphone come dispositivo abituale”: riquadro numerico rimosso: partecipanti, scenari e dispositivi sono già descritti nelle due fasi
- `progetto-jojob.html` · “Pianificazione → sessioni → evidenze → ipotesi di modifica → retest.”: citazione di processo rimossa (decorativa)
- `progetto-jojob.html` · “Percezione”: punto rimosso: ripeteva il paragrafo sulle evidenze (facilità e rapidità citate dai partecipanti)
- `progetto-jojob.html` · “I cinque contributi descrivono un’esperienza complessivamente positiva e un’interfaccia intuitiva.”: punto rimosso: ripeteva il paragrafo sulle evidenze (facilità e rapidità citate dai partecipanti)

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
- da `index.html`: Ideazione e organizzazione
