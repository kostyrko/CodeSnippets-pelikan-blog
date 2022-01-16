Title: Cypress: ciągi oraz asynchroniczność
Author: mkostyrko
Date: 2022-01-16 12:00
Updated:
Category: testing
Tags: testing, cypress, wprowadzenie
Slug: cypress-chaining
related_posts:


## Cypress i tworzenie ciągów

Cypress oparty jest o tworzenie ciągów (łączeniu ze sobą funkcji w celu stworzenia testu). Cypress sam zajmuje się Promisami.

    cy.get('textarea.post-body')
        .type('{enter}')

    cy.get('textarea.post-body')
        .contains('xyz')
        .click()

    cy.get('textarea.post-body')
        .find('.productname')
        .eq(1)
        .click()

`cy.find()` - szuka dziecka w wybranego elementu na podstawie selektora


Przykładowe funkcje, które pozwalają na interakcję z testowaną stroną - 

`.blur() `- Blur na wcześniej sfokusowanym elemencie DOM.

`.focus()` - Focus na wybranych elemencie DOM.

`.clear()` -  Czyści input lub textarea.

`.check()` - Zaznacza checkbox(es) or radio(s).

`.uncheck()` - Odznacza checkbox(es).

`.select()` - Select an <option> within a <select>.

`.dblclick()` - podwójny-click na wybrany element DOM.

.`rightclick()` - prawy-klik na wybrany element DOM.


### Cypress i Asynchroniczność
