Title: Cypress: wprowadzenie cz. 2
Author: mkostyrko
Date: 2022-01-16 12:00
Updated:
Category: testing
Tags: testing, cypress, wprowadzenie, then, promise, chaining, variables, zmienne
Slug: cypress-intro-2
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


### Cypress i jego Asynchroniczność

Cypressowe komendy są asynchroniczne  (JS jest jednowątkowy, a Cypress jest na Node.js) - jakikolwiek krok jest możliwy do egzekucji to zostanie wykonany/ może wykonywać więcej niż jeden wątek na raz - cypressowe funkcje nie są wykonywane w trakcie wywołania a są kolejkowane w celu ich wykonania. Można mieć wpływ na kolejność wykonywania się testów poprzez użycie `then`.


### Cypress promise i then

Cypressowe komendy działają na zasadzie promisa/ są promisami.

then jest używany w przypadku pozytywnego wyniku promisa (resolve), catch w przypadku negatywnego (reject).


        let promise = new Promise((resolve, reject) => {
            let a = 1 + 1
            if(a == 2) {
                resolve('Promise Fulfilled')
            } else {
                reject('Promise not fulfilled')
            }
        })

        promise.then((message) => {
            console.log(message + ', promise has passed!')
        }).catch((message) => {
            console.log(message + ', promise has failed')
        })

Cy.then() - pozwala na pracę z obiektem dostarczonym poprzez poprzedzającą funkcję np. cy.get()

        cy.get('xyz').then(($xyz) => {}) // 1) dostarcza xyz 2) wykonuje na xyz funkcję


### Stosowanie zmiennych

W kontekście stosowania zmiennych należy mieć na uwadze asynchroniczność oraz promisy (dlatego aby wykorzystać obiekt, który cypress zwraca należy wykorzystać komendę then lub zasadę łańcuchowania/łączenia ciągów komend).

        //To podejście nie zadziała, ponieważ cy.get() zwraca Promise
        const header = cy.get("div .header");
        cy.log(header.text())

        //To podejście zadziała, ponieważ cy.get() jest odpowiednio obsłużony poprzez zastosowanie cy.then()
        cy.get("div .header")
            .then($header => {
                const headerText = $header.text()
                expect(headerText).to.equal("xyz")
            })

### Iteracje