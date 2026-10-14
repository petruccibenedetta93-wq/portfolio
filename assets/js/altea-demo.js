(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('[data-showcase-tabs]').forEach((showcase) => {
    const tabs = [...showcase.querySelectorAll('[role="tab"]')];
    const panels = [...showcase.querySelectorAll('[role="tabpanel"]')];

    const activateTab = (tab, moveFocus = false) => {
      tabs.forEach((item) => {
        const selected = item === tab;
        item.setAttribute('aria-selected', String(selected));
        item.tabIndex = selected ? 0 : -1;
      });

      panels.forEach((panel) => {
        panel.hidden = panel.id !== tab.getAttribute('aria-controls');
      });

      if (moveFocus) tab.focus();
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activateTab(tab));
      tab.addEventListener('keydown', (event) => {
        let nextIndex = null;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') nextIndex = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') nextIndex = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') nextIndex = 0;
        if (event.key === 'End') nextIndex = tabs.length - 1;
        if (nextIndex === null) return;
        event.preventDefault();
        activateTab(tabs[nextIndex], true);
      });
    });

    if (tabs[0]) {
      showcase.classList.add('is-enhanced');
      activateTab(tabs[0]);
    }
  });

  const demo = document.querySelector('[data-altea-demo]');
  if (!demo) return;

  const messages = demo.querySelector('[data-altea-messages]');
  const choices = demo.querySelector('[data-altea-choices]');
  const reset = demo.querySelector('[data-altea-reset]');
  const initialMessages = messages.innerHTML;
  const initialChoices = choices.innerHTML;
  let responseTimer = null;
  demo.classList.add('is-enhanced');

  const paths = {
    prescription: {
      user: 'Come funziona l’invio di una ricetta?',
      bot: 'Nel concept il percorso ha tre momenti: invio dei dati, verifica del farmacista e conferma. La richiesta non equivale a un acquisto e la disponibilità resta da verificare.',
      choices: [
        ['prescription-data', 'Quali dati servono?'],
        ['prescription-modes', 'Ritiro o consegna?'],
        ['pharmacist', 'Quando interviene il farmacista?']
      ]
    },
    'prescription-data': {
      user: 'Quali dati servono?',
      bot: 'Nel prototipo vengono richiesti NRE, codice fiscale dell’intestatario e un recapito. Qui non inserire dati reali: questa è soltanto una demo del comportamento progettato.',
      choices: [
        ['prescription-modes', 'Come funziona dopo l’invio?'],
        ['pharmacist', 'Quando chiedere aiuto a una persona?']
      ]
    },
    'prescription-modes': {
      user: 'Cosa succede dopo l’invio?',
      bot: 'Il farmacista controlla la richiesta. Solo dopo la verifica la farmacia comunica disponibilità e modalità possibili di ritiro o consegna.',
      choices: [
        ['availability', 'Come viene verificata la disponibilità?'],
        ['pharmacist', 'Quando interviene il farmacista?']
      ]
    },
    availability: {
      user: 'Come viene verificata la disponibilità?',
      bot: 'Nel flusso previsto Altea può preparare una richiesta, ma non promettere una scorta. La disponibilità viene confermata dalla farmacia; se manca un’informazione, interviene il farmacista.',
      choices: [
        ['prescription', 'Come funziona il flusso ricetta?'],
        ['pharmacist', 'Quando avviene il passaggio umano?']
      ]
    },
    services: {
      user: 'Come trovo servizi e orari?',
      bot: 'Nel concept Altea orienta tra servizi, eventi, orari e contatti. Per una prenotazione mostra lo stato della richiesta e il prossimo passo, senza promettere una conferma automatica.',
      choices: [
        ['availability', 'Come chiedere una disponibilità?'],
        ['pharmacist', 'Quando interviene il farmacista?']
      ]
    },
    pharmacist: {
      user: 'Quando interviene il farmacista?',
      bot: 'Per domande personali o cliniche il concept prevede un passaggio sempre visibile, con riepilogo e conferma esplicita prima di condividere il contesto autorizzato. Questa demo non apre contatti e non condivide dati.',
      choices: [
        ['prescription', 'Come funziona il flusso ricetta?'],
        ['services', 'Come si trovano servizi e orari?']
      ]
    }
  };

  const appendMessage = (text, type) => {
    const message = document.createElement('p');
    message.className = `altea-message altea-message--${type}`;
    const speaker = document.createElement('span');
    speaker.className = 'sr-only';
    speaker.textContent = type === 'bot' ? 'Altea: ' : 'Tu: ';
    message.append(speaker, text);
    messages.append(message);
    messages.scrollTo({ top: messages.scrollHeight, behavior: reduceMotion ? 'auto' : 'smooth' });
    return message;
  };

  const renderChoices = (items) => {
    choices.replaceChildren();
    items.forEach(([intent, label]) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.alteaIntent = intent;
      button.textContent = label;
      choices.append(button);
    });
  };

  choices.addEventListener('click', (event) => {
    const button = event.target.closest('[data-altea-intent]');
    if (!button || !choices.contains(button)) return;

    const path = paths[button.dataset.alteaIntent];
    if (!path) return;

    appendMessage(path.user, 'user');
    [...choices.querySelectorAll('button')].forEach((item) => { item.disabled = true; });
    demo.setAttribute('aria-busy', 'true');

    responseTimer = window.setTimeout(() => {
      const response = appendMessage(path.bot, 'bot');
      response.tabIndex = -1;
      renderChoices(path.choices);
      demo.removeAttribute('aria-busy');
      responseTimer = null;
      response.focus({ preventScroll: true });
    }, reduceMotion ? 0 : 320);
  });

  reset.addEventListener('click', () => {
    if (responseTimer !== null) {
      window.clearTimeout(responseTimer);
      responseTimer = null;
    }
    messages.innerHTML = initialMessages;
    choices.innerHTML = initialChoices;
    demo.removeAttribute('aria-busy');
    messages.querySelector('.altea-message')?.focus({ preventScroll: true });
  });
})();
