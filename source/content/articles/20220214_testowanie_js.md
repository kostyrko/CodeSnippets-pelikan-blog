Title: JS - biblioteki/narzędzi do testowania
Author: mkostyrko
Date: 2022-02-14 13:00
Updated:
Category: qa
Tags: cypress, jmeter, k6, backstopJS, pactum
Slug: automatyzacja-testow-js
related_posts:

![js-testing-frameworks](https://techaffinity.com/blog/wp-content/uploads/2019/11/JavaScript-Unit-Testing-TechAffinity.jpg)

## Wprowadzenie

Ten artykuł jest jedynie spisem bibliotek powstałych z myślą o testowaniu automatycznym wykorzystujących `JavaScript` + ich alternatyw (docelowo ten spis ma stać się punktem wyjścia do tworzenia dalszych artykułów na ich temat - tak jak to się stało np. w przypadku Cypressa).

### Integracja/e2e

[Playwright](https://playwright.dev/)

[Nightwatch](https://nightwatchjs.org/)

[Cypress](https://www.cypress.io/)

---
### Testy wydajnościowe (performance)

[K6](https://k6.io/docs/)


**Python**


[Locust](https://locust.io/)



**GUI**


[Jmeter](https://jmeter.apache.org/)


--
### API / BE testing


[Pactum](https://pactumjs.github.io/#/)



patrz: [Writing API tests in JavaScript with Pactum](https://www.ontestautomation.com/writing-api-tests-in-javascript-with-pactum/)



[SuperTest](https://github.com/visionmedia/supertest)



patrz: [Write your first API Test using JavaScript](https://morioh.com/p/a5d2a4a50278?f=5c21fb01c16e2556b555ab32)



`+` jak już wcześniej wspomniałem również Cypress może być wykorzystany do testowania API => patrz: [bahmutov/cy-api](https://github.com/bahmutov/cy-api)


**Python:**


[requests](https://docs.python-requests.org/en/latest/)


**GUI:**


[Postman](https://www.getpostman.com/)

---

### Mobilne

[Appium](https://appium.io/)


patrz: [Mobile Automation with Appium in JavaScript](https://testautomationu.applitools.com/appium-javascript-tutorial/chapter1.5.html)


[Detox](https://github.com/wix/Detox)


patrz: [Getting Started with Detox](https://wix.github.io/Detox/docs/introduction/getting-started)

----
### Regresja UI


[BackstopJS](https://github.com/garris/BackstopJS)

---


### Bibl JS przydatne w testowaniu

[FakerJS](https://github.com/faker-js/faker) - projekt po małych [zawirowaniach na przełomie 2021/2022](https://www.youtube.com/watch?v=R6S-b_k-ZKY&ab_channel=Fireship) zyskał [nowe życie](https://fakerjs.dev/update.html).


patrz: [fakerjs.dev](fakerjs.dev)


[minifaker](https://github.com/g45t345rt/minifaker)



[falso](https://github.com/ngneat/falso)


patrz: [Meet Falso: The Replacement for Faker.js](https://javascript.plainenglish.io/thank-you-faker-now-its-time-to-move-on-27253d3b0885)

---

**Źródła**

[Workshop: Testing RESTful APIs in Python with requests](https://github.com/basdijkstra/requests-workshop)

[API Integration Testing Made Easy](https://dev.to/asaianudeep/api-integration-testing-made-easy-1lcp)

[20 Resources for generating fake and mock data](https://dev.to/iainfreestone/20-resources-for-generating-fake-and-mock-data-55g1)

