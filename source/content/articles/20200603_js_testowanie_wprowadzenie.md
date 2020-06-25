Title: JavaScript - krótkie wprowadzenie do testowania kodu
Author: mkostyrko
Date: 2020-06-03 10:00
Updated:
Category: javascript
Tags: 
Slug: js-testowanie-wprowadzenie
related_posts: 


![TDD](https://i.pinimg.com/originals/6a/74/6c/6a746c70228203d1cbd8835bf63840b1.jpg#center)

Dlaczego warto stosować testy/Do czego służą testy?

[..........]

TDD - test driven development - testowanie aplikacji na bieżąco, podczas realizacji kolejnych kroków, może to być związane z tworzeniem testu jeszcze przed napisaniem danego bloku kodu

Unit test - inaczej testowanie jednostkowe - polega na rozbiciu kodu na jak najmniejsze części i poddawanie ich testom (w JS jest to np. funkcja - którą należy odizolować od kodu od którego jest zależna - to można zrobić przy wykorzystaniu STUBów i markerów, które zastępują zewnętrzne zależności)

International - testowanie modułów, a nawet całych aplikacji oraz przepływu przez nie informacji, mogą korzystać z zewnętrznych zależności

Functional - testowanie całych aplikacji z wykorzystaniem przeglądarki

---

Istotne wyrażenia:


Dummy - obiekt zastępujący obiekt nad którym się pracuje

STUB - obiekt lub funkcja, której należy podać jaką ma przyjąć odpowiedź

SPY - zwraca jak obiekt jest używany

MOCK - imitacja obiektu, należy wskazać w jaki sposób jest użyty

FAKE - podobne do STUB ale może posiadać funkcjonalność

---

Wymagania: NODEJS, NPM

![nodejs&npm-logo](https://miro.medium.com/max/1400/1*hj-_anuWthYZs0x22hE9lA.png){width:"75px"}

---

### Frameworki: 

![mocha](https://camo.githubusercontent.com/af4bf83ab2ca125346740f9961345a24ec43b3a9/68747470733a2f2f636c6475702e636f6d2f78465646784f696f41552e737667)

MOCHA

https://github.com/mochajs/mocha

CHAI - assertion library

SINON - tworzy test doubles (MOCK,FAKE etc.)


Źródło-tutorial: https://github.com/flawgical/Mocha-Chai-TTD

http://jsdn.pl/nowoczesne-testowanie-kodu-w-javascript-czesc-pierwsza-setup/

http://jsdn.pl/testy-jednostkowe-javascript/

https://blog.piotrnalepa.pl/2016/01/10/js-testowanie-kodu-javascript-za-pomoca-gulp-js-karma-i-mocha-js/

https://www.youtube.com/watch?v=pnQVrUePcu8

https://www.youtube.com/watch?v=MLTRHc5dk6s

https://www.youtube.com/watch?v=MLTRHc5dk6s

- Behavior-driven development (BDD)

---

![Jasmine](https://www.nafrontendzie.pl/assets/images/jasmine_small.png)

Jasmine

Źródło-tutorial: https://www.nafrontendzie.pl/jasmine-podstawy-testowania

- nie jest uzależniony od elementów DOM 

- skupiony na testowaniu zachowania

---

![Jest](https://miro.medium.com/max/956/1*Ov3_LfV1tNqb0PMioxvpaw.png)

Jest

Źródło-tutorial: https://devenv.pl/testowanie-w-node-js-jest-alternatywa/

https://www.youtube.com/watch?v=gX440uva4NU - PL

https://www.youtube.com/watch?v=_zEX9sHzqS4 - PL

https://www.youtube.com/watch?v=FgnxcUQ5vho



---

QUnit

![QUnit](https://www.nafrontendzie.pl/assets/images/qunit.png)

Źródło-tutorial: ---


---

Zestawienie

![podsumowanie](https://3fxtqy18kygf3on3bu39kh93-wpengine.netdna-ssl.com/wp-content/uploads/2019/10/TOP-5-JS-700x1513.png)

#### Wtyczki

Wallaby.js - wtyczka do IDE stworzona do testowania JS - współpracuje z frameworkami wyżej wymienionymi

https://wallabyjs.com/

Źródło-tutorial: https://www.youtube.com/watch?v=P4UQ-jTTJJ4



---

Źródła:


https://jestjs.io/


https://jestjs.io/docs/en/mock-functions.html


