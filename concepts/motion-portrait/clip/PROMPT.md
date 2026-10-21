# Clip image-to-video per la variante B: preventivo e prompt

Stato: **non generata, bloccata dal piano**. Benedetta ha approvato una prova Kling 3.0 pro, 5 s, entro 8,75 crediti.

## Tentativo del 21 ottobre 2026: rifiutato dal piano

- Stima immediatamente prima dell'invio (foto originale come start ed end, prompt per la foto originale, 5 s, pro, 16:9, audio spento, 1 clip): **8,75 crediti**. Higgsfield aveva suggerito il preset "IN THE DARK"; è stato rifiutato per restare sul modello approvato.
- Invio con `use_unlim: false`: risposta esatta di Higgsfield **"Error starting generation: Requires plus plan or higher."**
- Nessun job creato, quindi **nessun job id**. Saldo dopo il tentativo: **10 crediti, piano free** (nessun credito speso).
- Non è stato cambiato modello, non è stato fatto alcun acquisto o upgrade, non ci sono stati altri tentativi.
- Il preventivo restituito da `get_cost` non segnala il requisito del piano: va tenuto presente per gli altri modelli in tabella, il cui accesso con piano free non è verificato.
- Per procedere serve una decisione di Benedetta: passare a un piano Plus o superiore, oppure approvare un altro modello (da verificare prima che sia accessibile con il piano free).

## Piano eseguibile scelto (21 ottobre 2026)

Si usa la **foto originale già importata in Higgsfield** come immagine iniziale e finale. Il fotogramma 16:9 (`start-frame-16x9.png`) resta solo un riferimento estetico: non serve caricarlo e non va cambiata nessuna impostazione di rete o di permessi.

| Voce | Valore |
| --- | --- |
| Immagine (start e end) | `benedetta-cutout-hq.png`, importata da `https://petruccibenedetta93-wq.github.io/portfolio/assets/images/benedetta-cutout-hq.png` |
| Media id Higgsfield | `cdb42b7f-ca66-4403-869d-d9de673f77a0` (ruoli `start_image` e `end_image`) |
| Modello | `kling3_0`, `mode: pro` |
| Durata / formato / audio | 5 s, `aspect_ratio: 16:9`, `sound: off`, `count: 1` |
| Costo verificato con questa immagine | **8,75 crediti** (saldo 10) |
| Limite da far approvare a Benedetta | **1 clip, massimo 8,75 crediti**. Nessun avvio prima dell'approvazione, nessun acquisto se il costo cambia o il saldo non basta |
| Prompt | la versione "per la foto originale" più sotto |

La foto è un ritaglio con sfondo trasparente in formato 3:4: in 16:9 il modello completerà lo sfondo e probabilmente terrà il soggetto al centro. Per questo la posizione a destra non si chiede alla clip ma si ottiene nel sito (vedi "Integrazione").

### Prompt per la foto originale

```
Static portrait of the same woman from the start image, keeping her exact face, features, hairstyle, black turtleneck and black blazer unchanged. Plain dark grey-blue studio backdrop, softly lit behind her, no objects. Minimal, natural motion only: a slow, subtle shift of gaze, a very slight head movement of a few degrees, one natural blink, a faint movement in the ends of her hair as if from soft air. Calm, neutral expression, mouth closed. Locked-off camera, no zoom, no pan, no camera shake. Even studio light that does not change. Head-and-torso framing stays the same for the whole clip. The clip ends in the same pose as it starts, for a seamless loop.
```

Da evitare: lo stesso elenco della sezione "Prompt" qui sotto.

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

**Ricontrollo con immagine allegata (21 ottobre 2026)**: Kling 3.0 pro, 5 s, 16:9, audio spento, stessa immagine come `start_image` e `end_image`, 1 clip → **8,75 crediti**, invariato. Saldo dopo il controllo: 10 crediti (nessun job avviato, nessun credito speso).

- Immagine usata per il ricontrollo: la foto originale `benedetta-cutout-hq.png`, importata in Higgsfield dal sito pubblico del portfolio (media id `cdb42b7f-ca66-4403-869d-d9de673f77a0`). Il fotogramma `start-frame-16x9.png` **non è stato caricato**: la rete di questo ambiente rifiuta la connessione verso `upload.higgsfield.ai`. Va caricato da un ambiente con accesso a quel dominio (o dal sito Higgsfield) prima della generazione, e il costo va riconfermato con quell'immagine.
- Risoluzione: il catalogo Higgsfield non espone la risoluzione in pixel delle modalità std e pro di Kling 3.0 (solo la modalità `4k` la dichiara nel nome). Dato non verificato.

**Limite proposto per l'approvazione: 1 clip, massimo 8,75 crediti.** Nessun avvio prima dell'approvazione; se il costo confermato supera il limite o il saldo, nessun acquisto: ci si ferma e si riporta il nuovo valore.
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

- Da 1024 px in su la clip va **solo nel riquadro ritratto della colonna destra** (lo stesso contenitore che oggi ospita la foto), mai a tutta pagina: il contenitore resta separato dalla colonna dei testi, con ritaglio (`overflow: hidden` e la stessa maschera sfumata in basso) e `object-fit` / `object-position` decisi dopo aver visto la clip, in modo che volto e capelli non coprano mai titolo, descrizione e pulsanti.
- La foto originale resta `poster` durante il caricamento e immagine di ripiego.
- Sotto i 1024 px e con `prefers-reduced-motion: reduce` resta la foto statica (già gestito da `src/shared/PortraitMedia.tsx`).
- Dopo l'inserimento: ricontrollare a 1440×900, 1383×695, 1062×590 e 1024×768 che non ci siano sovrapposizioni.
