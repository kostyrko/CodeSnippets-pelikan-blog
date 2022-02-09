Title: Cypress - Page Objects
Author: mkostyrko
Date: 2022-02-09 13:00
Updated:
Category: qa
Tags: cypress, page object model, page object
Slug: cypress-page-objects
related_posts: testing-good-practices

### Page objects

**Page object pattern** - główne założenia: wprowadzenie modułowości w testach -> skupienie logiki testu w jednym miejscu a w innym stworzenie samego testu.
👉 pozwala na ograniczenie używania selektorów w testach (✌️ pozytywnie wpływa na czytelność kodu) 
🤌 niewielkie zmiany dokonane w testowanej aplikacji powinny mieć wpływ na zmianę Page Objectu, unikając zmian w kodzie testu (🤜 testy prostsze w utrzymaniu).

Podsumowując

- wprowadza dodatkową abstrakcję dla interakcji z UI

- zawiera szczegóły struktury UI strony oraz (części) jej funkcjonalności w jednej klasie/obiekcie


Page objecty przechowujemy w dedykowanym folderze (np. pageObjects) znajdującym się po za folderem 'integrations' jak reszta plików z kodem testowym.

#### 1. Page object oparty na klasie


        export class CreditsPgObj {
            getCreditsCheckbox() {
                cy.get('[data-cy="creditBox"]')
            }

            static getCreditsInfo() {
                cy.get('[data-cy="creditsInfo"]')
            }

            [...]
        }

        export class ThanksCreditsPg {
            getProviderName() {
                return cy.get('[data-cy="providerName"]')
            }

            static getTransactionId() {
                return cy.get('[data-cy="transactionId"]')
            }
        }


Wykorzystanie

        /// <reference types="cypress" />
        import { viewports } from '../../support/main'
        import { CreditsPage } from '../../support/credits'

        viewports.forEach(viewport => {
        describe(`Bonus credits management - (${viewport})`, () => {
            const creditsPage = new CreditsPgObj()
            beforeEach(() => {
                cy.viewport(viewport)
                cy.visit('').wait('@xyz').wait('@yz').wait('@zx')
            })

            it('Bonus credits offer should be displayed')
            () => {
                CreditsPage.getLimitedTimeOffer().should('be.visible')
                CreditsPage.getCreditsProductBonus().should('be.visible')
                CreditsPage.getCreditsProductBonus().first().should('include.text', '100 Credits')
            },
            )
        })
        })


#### 2. Page object oparty na obiekcie

        export const menuPage = {
        menuOpen: () => {
            cy.get(menuSelectors.openMenuBtn).click();
        },
        menuClose: () => {
            cy.get(menuSelectors.closMenuBtn).click().should('not.be.visible');
        },
        logOut: () => {
            cy.get(menuSelectors.menuItems.logout).click();
            cy.url().should('include', '/login');
        },
        };

#### 3. Sposób na podział logiki w Page Objecty Model (POM)

 Swego czasu tutaj: [Dobre zasady testowania](https://kostyrko.github.io/zfrontu/testing-good-practices.html) pisałem, że dobry układ testu tj 3xA (Arrange/aranżacja, Act/działanie, Assert/sprawdzanie) - jak to się odnosi do tzw POM? Ja to rozumiem w sposób następujący - PageObject jest odpowiedzialny za interakcję ze stroną (przechowuje akcje, które są powtarzane w tekście) - jednak sama asercja (sprawdzenie poprawności wykonania się akcji) powinna znajdować się wewnątrz testu. Przygotowanie testu odbywać się może w różnych miejscach i na różne sposoby (pomijając przygotowanie środowiska-> cy.visit/cy.intercept czy localStorage, które mogą się znaleźć np. w beforeEach) ale skupiać w sobie będzie zebranie selektorów (w osobnej klasie bądź obiekcie), które następnie będą wykorzystane zarówno w ramach testu jak i w Page Object.

Scenariusz testowy w kontekście testowania aplikacji blogowej może przedstawiać się w sposób następujący: logujemy się, przechodzimy do sekcji z nowymi artykułami, tworzymy treść nowego artykuły, postujemy go - a następnie sprawdzamy czy artykuł został dodany/opublikowany.

**Często spotykane podejście (podejście liniowe)** => 1. Zebranie selektorów w obiekcie (w którym przechowywany jest PageObject), 2. wykorzystanie PageObjectu min. do cy.get() + funkcjonalność 3. wykorzystanie w tekście getterów z PageObjectu do tworzenia asercji.

const SELECTORS = {
    ACCEPT_BUTTON: "#accept-cookies",
    REJECT_BUTTON: "#reject-cookies",
    LOCALSTORAGE_DISABLED_WARNING: "#localstorage-disabled-warning",
  };

**Alternatywne podejście: rozbicie logiki na 3 klasy/obiekty/części (podejście funkcjonalne)** => 1. przechowuje gettery = cy.get() + selektory 2. akcje/funkcjonalność (wykorzystuje logikę 1.) 3. test (tu wykorzystywana jest logika z 1. 2.)

        const getSubmitSearchButton = () => cy.get('[cypress-id]=submit-search');

wykorzystując [cypress-selectors](https://anton-kravchenko.github.io/cypress-selectors/) zapis może wyglądać następująco:

        @ByType('input') static searchInput: Selector;

----

Źródła:

[Using PageObject pattern with Cypress](https://medium.com/geekculture/using-pageobject-pattern-with-cypress-6d9907850522) => [anton-kravchenko/cypress-page-object-example](https://github.com/anton-kravchenko/cypress-page-object-example) => [cypress-selectors](https://anton-kravchenko.github.io/cypress-selectors/)

[CYPRESS Page Object Model EXAMPLE | POM in CYPRESS](https://www.youtube.com/watch?v=bC9bGHDgpQk&list=PLYDwWPRvXB8-8LG2hZv25HO6C3w_vezZb&index=15)


[Stop using Page Objects and Start using App Actions](https://www.cypress.io/blog/2019/01/03/stop-using-page-objects-and-start-using-app-actions/)



