Title: Cypress: cy.intercept() - przechwytywanie zapytań HTTP
Author: mkostyrko
Date: 2022-02-02 10:00
Updated:
Category: angular
Tags: unfinished, angular, cypress, testy
Slug: cypress-intercept
related_posts:


![cypress](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.somkiat.cc%2Fcypress-access-element%2F&psig=AOvVaw2bv1cAfoF7EKJUw4EaZZL3&ust=1643823831383000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNjKj5KH3_UCFQAAAAAdAAAAABAJ)

### cy.intercept()

**Stubbing** - podstawianie danych pod zapytania

`cy.request() `- pozwala na przechwycenie zapytania typu HTTP przez test cypressowy - taka komenda może przydać się w przypadku gdy 1) chcemy aby dane zapytanie doszło do skutku zanim zaczniemy wykonywać kolejną komendę lub 2) gdy zależy nam na przechwyceniu requestu HTTP i podstawienia danych do niego, w celu testowania zachowania się aplikacji front-endowej.


    beforeEach(() => {
        cy.viewport(viewport)
        cy.intercept('GET', '/xxx/xxx_data?page=1', { fixture: 'xxx/xxx_data.json' })
    })
        
 ### cy.intercept() + cy.wait()
 
Nasłuchiwanie zapytania typu GET na `*/comments/*`

    cy.intercept('GET', '**/comments/*').as('getComment')

Sprawdzanie statusu

    cy.wait('@getComment').its('response.statusCode').should('be.oneOf', [200, 304])
    
Logowanie obiektu (DTO) w konsoli 

    cy.get('@post').then(console.log)


### cy.intercept() + cy.wait() + cy.commnad()

    Cypress.Commands.add('waitForApp2Start', dto => {
      cy.intercept('GET', '/xyz', { fixture: 'xdata' }).as('xdata')
      cy.intercept('GET', '/search_data?*', { fixture: 'searchData' }).as('searchData')
    })


    cy.waitForApp2Start()
    cy.visit('').wait('@xdata').wait('@searchData')

### przechwytywanie wielu zapytań / stubbowanie wielu zapytań

`cy.clock() `- pozwala na "zamrożenie" zegara oraz wszystkich funkcji związanych z mierzeniem czasu jak setInterval czy setTimeout

`cy.tick()` - pozawala na manualne sterowanie czasem

    it('fetches from the server (spies)', () => {
      cy.clock()
      cy.intercept('GET', '/favorite-fruits').as('fruits')
      cy.visit('/fruits.html')
      // pierwsze zapytanie
      cy.wait('@fruits').its('response.statusCode').should('equal', 200)

      // po 30 sekundach pytanie jest ponawiane 
      cy.tick(30000)
      cy.wait('@fruits').its('response.statusCode').should('equal', 200)
      [...]


Stubbing zapytania HTTP

      it('returns different fruits every 30 seconds', () => {
        cy.clock()
        let k = 0

        // za każdym razem kiedy pojawia się zapytanie inna odpowiedź jest podstawiana
        cy.intercept('/favorite-fruits', (req) => {
          k += 1
          switch (k) {
            case 1:
              return req.reply(['apples 🍎'])
            case 2:
              return req.reply(['grapes 🍇'])
            default:
              return req.reply(['kiwi 🥝'])
          }
        })

        cy.visit('/fruits.html')
        cy.contains('apples 🍎')
        cy.tick(30000)
        cy.contains('grapes 🍇')
        cy.tick(30000)
         cy.contains('kiwi 🥝')
    })
 
Za każdym razem kiedy intercept jest wywoływany używa pierwszego elementu z tablicy odpowiedzi i usuwa go.
Po pierwszych dwóch razach, responses.shift() zawsze zwraca **undefined** i wtedy odpowiedź jest w postaci tablicy zawierającej kiwi.


    it('returns different fruits every 30 seconds (array shift)', () => {
      cy.clock()

      // return difference responses on each call
      const responses = [
        ['apples 🍎'], ['grapes 🍇'],
      ]

      cy.intercept('/favorite-fruits', (req) => {
        req.reply(responses.shift() || ['kiwi 🥝'])
      })

      cy.visit('/fruits.html')
      cy.contains('apples 🍎')
      cy.tick(30000)
      cy.contains('grapes 🍇')
      cy.tick(30000)
      cy.contains('kiwi 🥝')
    })
    
   


Źródło:

[intercept - cypress.io](https://docs.cypress.io/api/commands/intercept)

[example.cypress.io/commands/waiting](https://example.cypress.io/commands/waiting)

[Asserting Network Calls from Cypress Tests](https://www.cypress.io/blog/2019/12/23/asserting-network-calls-from-cypress-tests/)

[Testing periodic network requests with cy.intercept and cy.clock combination](https://www.cypress.io/blog/2021/02/23/cy-intercept-and-cy-clock/)

