Title: Cypress + Mochawesome
Author: mkostyrko
Date: 2022-01-29 13:00
Updated:
Category: testing
Tags: cypress, mochawesome, reporting
Slug: mochawesome-cypress
related_posts:


        npx mochawesome-merge cypress/results/mochawesome/*.json > mochawesome.json && npx marge mochawesome.json


"scripts": {
     "mochawesome-merge": "npx mochawesome-merge cypress/results/mochawesome/*.json > mochawesome.json && npx marge mochawesome.json",
    "delete-mochawesome-report": "rm -rf mochawesome-report/* || true"
  },
  "devDependencies": {
    "mochawesome": "^6.1.1",
    "mochawesome-merge": "^4.1.0",
    "mochawesome-report-generator": "^5.1.0"
  }


https://docs.cypress.io/guides/tooling/reporters#Examples

npmjs.com/package/mochawesome-report-generator