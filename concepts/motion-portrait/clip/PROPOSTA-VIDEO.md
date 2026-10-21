# Proposta video da progettare (non avviata)

Stato: **solo proposta**. Nessuna generazione avviata, nessun costo autorizzato. Non sostituisce la bozza PARALLAX, che resta la direzione corrente con la foto statica.

## Riferimento inviato da Benedetta

`https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260618_174853_aac61aa2-0f3f-4cf1-bc78-7f657dd11164.mp4`

Ritratto cinematografico su fondo azzurro/grigio, cuffie luminose e giacca futuristica trasparente. È il video del template, non un'immagine di Benedetta: resta solo riferimento di atmosfera.

Benedetta chiede una scena simile con il suo volto, realistica e non troppo artificiale.

## Materiale sorgente fornito da Benedetta (21 ottobre 2026)

| Voce | Valore |
| --- | --- |
| File | `WhatsApp Video 2026-10-21 at 12.32.28.mp4` |
| Dove si trova | conservato da Benedetta; i riferimenti di accesso sono in una nota privata fuori dal repository |
| Dati tecnici (verificati con ffprobe) | 10,67 s, 30 fps, 320 fotogrammi, H.264 1024×576 con rotazione di 90°: in visione corretta è verticale 576×1024; audio AAC stereo quasi muto (media −55,5 dB, picco −38,7 dB), da rimuovere comunque |
| Contenuto | selfie a braccio teso in un ufficio: Benedetta con capelli lunghi mossi e riga centrale, maglione blu scuro; pareti chiare, una giacca verde appesa sullo sfondo, luce interna dall'alto |
| Stato | **ricevuto il 21 ottobre come allegato alla sessione** e conservato in una cartella privata fuori dal repository; analizzato in locale (metadati e fotogrammi), senza caricarlo su servizi esterni |

Regole: è materiale personale, non va pubblicato né messo nel repository del sito (che è pubblico); l'audio va rimosso in ogni derivato; nessun link di condivisione del video va inserito nelle pagine o nel repository. Non sostituisce la foto dell'hero PARALLAX.

## Analisi del girato (fotogrammi a 1,5 al secondo)

- **0–4,5 s**: mezzo busto quasi frontale, piccole rotazioni della testa verso destra e sinistra e sguardi di tre quarti. È il tratto più adatto alla clip: movimento naturale e contenuto.
- **4,5–6 s**: la camera si avvicina; inquadratura più stretta sul viso.
- **6–9,5 s**: primo piano frontale, sguardo in camera, testa quasi ferma; buono per un fotogramma finale o un poster alternativo.
- **ultimo secondo circa**: la camera si abbassa, immagine mossa e soffitto in vista; da scartare.
- Camera a mano (selfie): leggero tremolio e variazioni di distanza; servono stabilizzazione e un ritaglio un po' più stretto.
- Il braccio che regge il telefono entra a tratti nel bordo sinistro; lo sfondo (pareti, giacca appesa) va sostituito con lo scontorno.
- Capelli mossi e voluminosi: è la parte più difficile da scontornare in modo pulito.
- Abbigliamento diverso dalla foto della hero (maglione blu invece di dolcevita e blazer neri): la clip non va affiancata alla foto come se fossero lo stesso momento.

## Trattamento proposto a partire dal video reale

Obiettivo: l'atmosfera del riferimento (luce fredda, cuffie luminose, giacca futuristica trasparente) mantenendo il più possibile il volto vero.

Due strade, in ordine di fedeltà al volto:

1. **Compositing e color grading sul girato reale** (consigliata). Il volto resta quello ripreso: si stabilizza e si ritaglia il video in verticale o a mezzo busto, si scontorna Benedetta, si sostituisce lo sfondo con il fondo azzurro-grigio, si applica una correzione colore fredda e si aggiungono cuffie luminose e giacca come elementi grafici tracciati sul movimento (After Effects o simili). Richiede lavoro di editing manuale; il risultato dipende dalla qualità del tracciamento, soprattutto su capelli mossi e mani.
2. **Modello video "video-to-video"** con il girato come guida. Più veloce, ma il modello ridisegna il volto: lineamenti e proporzioni possono cambiare. Va controllato fotogramma per fotogramma e scartato se la somiglianza non regge.

In entrambi i casi Claude può preparare direzione, riferimenti, prompt e storyboard, controllare i fotogrammi e integrare la clip nel sito; editing, compositing o generazione richiedono uno strumento esterno, e i costi vanno approvati a parte. **Nessuna identità perfetta è garantita** con la strada 2; nemmeno la strada 1 garantisce un risultato "come il riferimento", che è una scena interamente generata.

### Storyboard sul girato (basato sull'analisi dei fotogrammi)

1. 0–2 s: mezzo busto, Benedetta di tre quarti; fondo azzurro-grigio con vignettatura; cuffie con un bordo luminoso freddo.
2. 2–5 s: segue le piccole rotazioni reali della testa (tratto 0–4,5 s del girato, stabilizzato); riflessi freddi sul viso dalla fonte luminosa delle cuffie.
3. 5–7 s: sguardo in camera (tratto 6–9,5 s del girato, raccordato con una dissolvenza perché la camera nel frattempo si avvicina); la giacca trasparente riflette la luce.
4. Chiusura: dissolvenza o ritorno vicino alla posa iniziale per un loop accettabile (un loop perfetto da un girato reale non è garantito).

Formato di consegna per il sito: verticale 9:16 per mobile e una versione ritagliata per il riquadro destro su desktop; MP4 H.264 + WebM, senza audio, sotto 3 MB; foto come poster e ripiego; nessun elemento sopra testi e pulsanti.

## Chi fa cosa

- **Claude**: direzione visiva, prompt, storyboard, controllo dei fotogrammi e integrazione della clip nel sito (contenitore dedicato, foto come poster e ripiego, foto statica con `prefers-reduced-motion` e su mobile).
- **La clip** va realizzata da un modello video o da una piccola produzione. Claude non genera video da solo.

## Cosa serve per un risultato credibile

- **Materiale migliore**: un breve video autentico di Benedetta (fornito il 21 ottobre, vedi sopra). Partire dal girato reale preserva molto meglio il volto. Per una resa più pulita sarebbe utile anche una seconda ripresa con il telefono appoggiato (non a mano), fondo neutro e luce frontale morbida.
- **Con una sola foto**: si può tentare, ma l'identità non è garantita; lineamenti, proporzioni e capelli possono cambiare tra un fotogramma e l'altro.
- **Costi**: dipendono dal servizio e dal piano. Il tentativo con Higgsfield (Kling 3.0 pro) è stato rifiutato perché richiede un piano Plus o superiore; la clip Firefly generata in precedenza è stata scartata da Benedetta e non va usata. Nessun nuovo costo è autorizzato.
- Nessun risultato fotorealistico può essere promesso in anticipo, né un uso gratuito illimitato.

## Storyboard proposto (5–8 s, loop)

1. Inquadratura fissa a mezzo busto, soggetto a destra, fondo azzurro-grigio uniforme con leggera vignettatura; metà sinistra libera per i testi.
2. Benedetta guarda di tre quarti, poi porta lentamente lo sguardo verso la camera; un battito di ciglia.
3. Riflessi freddi e morbidi sul viso, come da una fonte luminosa fuori campo; capelli quasi fermi.
4. Ritorno alla posa iniziale per chiudere il loop.

Elementi del riferimento da valutare con Benedetta prima di qualsiasi prova: cuffie luminose e giacca trasparente sono costumi aggiunti dal modello; possono rendere la scena più artificiale e allontanarla dal suo abbigliamento reale (dolcevita e blazer neri).

## Prompt di partenza (inglese, da adattare al servizio scelto)

```
Cinematic medium close-up of the same woman from the reference, keeping her real face, features, long straight brown hair with a centre part, black turtleneck and black blazer. Plain blue-grey studio backdrop with a soft vignette, subject on the right third, left half empty. She slowly turns her gaze from three-quarter view to the camera and blinks once. Soft, cool reflected light on her face, subtle and realistic. Locked-off camera, no zoom. Natural skin texture, no beauty filter, no text, no talking. Ends in the starting pose for a seamless loop.
```

## Prima di usarla nel sito

- Somiglianza controllata fotogramma per fotogramma con le foto reali; se il volto cambia, la clip non si usa.
- Nessun elemento della clip sopra testi e pulsanti; contenitore riservato e ritaglio decisi dopo aver visto l'asset.
- MP4 H.264 + WebM, senza audio, sotto 3 MB; foto come poster e ripiego.
