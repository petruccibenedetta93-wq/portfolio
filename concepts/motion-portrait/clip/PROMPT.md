# Clip image-to-video per la variante B: preventivo e prompt

Stato: **preparata, non generata**. L'idea della clip è approvata; l'importo in crediti va ancora approvato da Benedetta.

## Fotogramma di partenza

`start-frame-16x9.png` (1920×1080). È la foto originale `assets/images/benedetta-cutout-hq.png`, ridimensionata senza ritocchi e posata su un fondale da studio scuro con i colori della variante B. Il soggetto occupa l'80% dell'altezza, a destra; i capelli iniziano al 61% della larghezza, quindi il 60% sinistro resta libero per l'interfaccia. Nessuna parte del volto o del corpo è stata generata o modificata.

## Preventivo (verificato il 21 ottobre 2026, solo stima, nessun job avviato)

Saldo Higgsfield letto dall'account: **10 crediti**, piano free. Costi restituiti dalla stima ufficiale del tool (`get_cost`), per **1 clip**, audio spento:

| Modello | Impostazioni | Crediti |
| --- | --- | --- |
| **Kling 3.0, modalità pro** (consigliato) | 5 s, 16:9, start e end image = stesso fotogramma | **8,75** |
| Kling 3.0, modalità std | 5 s, 16:9 | 7,5 |
| Kling 3.0, modalità std | 6 s, 16:9 | 9 |
| Minimax Hailuo 2.3 | 6 s, 768p | 6 |
| Minimax Hailuo 2.3 | 6 s, 1080p | 10 |
| Seedance 2.5 | 5 s, 720p | 35 (oltre il saldo) |

Limiti di cosa è verificato:

- La stima è stata chiesta **senza caricare la foto** (caricare è già una scrittura sull'account). Il prezzo potrebbe variare con l'immagine allegata: va riconfermato con `get_cost` dopo il caricamento e prima della generazione.
- Il catalogo non dichiara la risoluzione in pixel di Kling std/pro.
- Con 10 crediti c'è margine per **un solo tentativo**: se la clip non convince (somiglianza, raccordo), un secondo tentativo richiede altri crediti.

Raccomandazione: Kling 3.0 pro, 5 s, 16:9, audio spento, con lo stesso fotogramma come immagine iniziale e finale per favorire il loop. Alternativa economica: Minimax Hailuo 2.3, 6 s, 768p (6 crediti), meno nitida.

## Prompt (inglese, per il modello)

```
Static portrait shot of the same woman from the start image, keeping her exact face, features, hairstyle, outfit and framing unchanged. She stands still on the right side of the frame against a plain dark studio backdrop. Minimal, natural motion only: a slow, subtle shift of gaze, a very slight head movement of a few degrees, one natural blink, a faint movement in the ends of her hair as if from soft air. Calm, neutral expression throughout, mouth closed. Locked-off camera, no zoom, no pan, no camera shake. Soft, even studio light that does not change. The left half of the frame stays empty dark backdrop for the whole clip. The clip ends in the same pose as it starts, for a seamless loop.
```

Da evitare (se il modello accetta un negative prompt, altrimenti tenere il prompt sopra così com'è):

```
text, captions, logos, watermark, talking, lip movement, smiling, facial transformation, changing identity, face morphing, extra people, hands entering frame, camera movement, zoom, lighting change, background change, subject moving to the left half of the frame
```

## Controllo della clip prima di usarla

- Somiglianza: confrontare fotogramma per fotogramma con la foto originale. Se il volto cambia, la clip non si usa. Non è garantita un'identità perfetta.
- Raccordo del loop: il passaggio fine/inizio può avere un piccolo scatto; va guardato a velocità reale. Non è garantito un loop perfetto.
- Nessun elemento entra nella metà sinistra dell'inquadratura.
- Esportazione per il web: MP4 H.264 e WebM, 1280–1920 px di larghezza, sotto 2–3 MB, senza audio.

## Integrazione prevista nella variante B

- Da 1024 px in su la clip diventa il fondale dell'hero (`object-fit: cover`, ancorata a destra), con la foto come `poster` durante il caricamento.
- Sotto i 1024 px resta la foto statica nel blocco ritratto separato dai testi.
- Con `prefers-reduced-motion: reduce` resta la foto statica (già gestito da `src/shared/PortraitMedia.tsx`).
