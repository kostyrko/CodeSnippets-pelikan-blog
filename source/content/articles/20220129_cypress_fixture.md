Title: Cypress - Fixtures
Author: mkostyrko
Date: 2022-01-29 13:00
Updated:
Category: testing
Tags: cypress
Slug: cypress-fixtures
related_posts:

Plik znajduje się w folderze fixture (wpisanie jego nazwy) lub należy podać ścieżkę do pliku.

### 1. sposób odwołani się do fixture - korzystając z this

/// <reference types="cypress" />

describe("Test Contact Us form", () => {
    before(function() {
        cy.fixture('example').then(function(data) {
            //this.data = data;
            // albo
            globalThis.data = data;
        })
    })
    it("Should be able to submit a form", () => { 
        cy.get('[name="first_name"]').type(data.first_name);
        cy.get('[name="last_name"]').type(data.last_name);
        cy.get('[name="email"]').type(data.email)
        cy.get("button[title='Submit']").click();
    });
})


### 2. sposób odwołania się do fixture - używając aliasu


describe("Test Contact Us form", () => {
    before(function() {
        cy.fixture("userDetails").as("user")
    })
    it("Should be able to submit a form", () => {
        cy.get("@user").then((user) => {
            cy.get('#ContactUsFrm_first_name').type(user.first_name);
            cy.get('#ContactUsFrm_email').type(user.email);
        })
        cy.get("button[title='Submit']").click();
    });
})
