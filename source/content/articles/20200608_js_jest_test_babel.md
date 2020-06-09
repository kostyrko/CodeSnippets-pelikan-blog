Title: JavaScript - pierwszy test w JEST (+ Babel)
Author: mkostyrko
Date: 2020-06-08 10:00
Updated:
Category: javascript
Tags: test, jest, tdd, node, npm, babel, transpilacja, transpilator, babel.js, babeljs
Slug: js-jest-test-babel
related_posts: js-babel, js-jest-test-2

![Jest](https://miro.medium.com/max/956/1*Ov3_LfV1tNqb0PMioxvpaw.png)

Do stworzenia pierwszego testu posłużyłem się [dokumentacją JEST](https://jestjs.io/docs/en/getting-started#generate-a-basic-configuration-file) oraz [tym materiałem](https://www.youtube.com/watch?v=_zEX9sHzqS4) (autorstwa Kacpra Kozaka)

_Jest_ wyszuka pliku, w którego nazwie znajduje się słowo kluczowe `test` poprzedzone `kropką` o rozszerzeniu `js` którego pierwszy człon nazwy jest taki sam jak plik, w którym przechowywany jest kod do testowania. Przykładowo test dla `sum.js` znajdzie się w pliku `sum.test.js`

W pierwszej kolejności należy stworzyć plik `sum.js` w którym znajdzie się testowany kod, w którym należy wskazać moduł do eksportu (umożliwia wykorzystanie funkcji w innym pliki/tworzy moduł)

    function sum(a, b) {
      return a + b;
    }

    module.exports = sum;

W pliku `sum.test.js` należy zaimportować stworzony moduł oraz napisać dla niego test

    const sum = require('./sum');

    test('adds 1 + 2 to equal 3', () => { // funkcja testująca
      expect(sum(1, 2)).toBe(3); // oczekiwany wynik
    });

Następnie należy zainicjować projekt przy pomocy npm/node.js wpisując w terminal

    npm init -y

Oraz zainstalować framework *jest*

    npm install --save-dev jest

W pliku `package.json` należy wskazać *jest* jako framework testujący

    {
      "name": "2_Jest",
      "version": "1.0.0",
      "description": "",
      "main": "sum.js",
      "scripts": {
        "test": "jest" // w tym miejscu należy wpisać "jest"
      },
      "keywords": [],
      "author": "",
      "license": "ISC",
      "dependencies": {
        "jest": "^26.0.1"
      }
    }

Podstawowa konfiguracja jest już skończona, zatem wystarczy w terminalu (z pozycji folderu projektu) wpisać

    npm run test

---

#### Porządkowanie/blokowanie testów

Porządkowanie testów odbywa się poprzez ich blokowanie wykorzystując słowo kluczowe `describe` a następnie zamknięcie testów przypisanych do jednego modułu w anonimowej funkcji poprzedzonej krótkim opisem

    describe('Function - sum', () => { // grupowanie testów
      test('adds 1 + 2 to equal 3', () => {
        expect(sum(1, 2)).toBe(3);
      });

      test('add negative numbers', () => {
        expect(sum(-5, -10)).toBe(-15);
      });

      test('add Infinity', () => { // wartość brzegowa
        expect(sum(0, Infinity)).toBe(Infinity);
      });
    });

---

### Babel X 3

Jak widać w powyższym przykładzie zastosowano składnię ES6 oraz wcześniejszą. Ograniczeniem, które narzuca tego typu rozwiązanie jest node.js, stąd aby w pełni wykorzystać możliwości składni wprowadzonej przez ES6 należy skorzystać z `Babel.js` - jego konfiguracja może być wykonana na parę sposobów, poniżej wykorzystam tą przedstawioną w [dokumentacji JEST](https://jestjs.io/docs/en/getting-started#generate-a-basic-configuration-file)

Zawartość `sum.js` ulegnie zmianie i zostanie nieco skrócona

    export const add = (a,b) => {
      return a + b;
    };

Podobnie stanie się z `sum.test.js` gdzie sposób importowania modułu będzie inny

    import { add } from './add';

    test('add two numbers', () => {
      expect(add(1,2)).toBe(3);
    })

==================================

Wpisując jedną komendę w terminalu

    npm i babel-jest @babel/core @babel/preset-env


W ten sposób zostanie zainstalowany [Babel](https://pl.wikipedia.org/wiki/Babel_(transpilator)) (transpilator konwertujący ES6< na ES5) wraz z niezbędnymi dodatkami. Do projektu zostaną dodane następujące zależności/wtyczki

    "dependencies": {
      "@babel/core": "^7.10.2",
      "@babel/preset-env": "^7.10.2",
      "babel-jest": "^26.0.1",
      "jest": "^26.0.1"
    }

W następnym kroku należy stworzyć plik `babel.config.js` w którym należy skonfigurować narzędzie *Babel*

    module.exports = {
      presets: [
        [
          '@babel/preset-env',
          {
            targets: {
              node: 'current',
            },
          },
        ],
      ],
    };

==================================

Alternatywnie należy zainstalować `babel-cli` oraz również `@babel/preset-env` (patrz [tutaj](https://babeljs.io/setup#installation)) w ten sposób babel zainstaluje potrzebne mu wtyczki

    npm install --save-dev babel-cli

    npm install @babel/preset-env --save-dev

plik konfiguracyjny powinien nosić nazwę `.babelrc` i zawierać:

  {
    "presets": ["@babel/preset-env"]
  }

==================================

Jeśli korzystamy z VSC najprostszym rozwiązaniem może być jednak instalacja wtyczki `vscode-babel-repl`, która dokonuje transpilacji w locie i wykorzystanie kodu wynikowego -> `F1` -> `babel repl`

  [vscode-babel-repl](https://raw.githubusercontent.com/t-sauer/vscode-babel-repl/master/babel.gif)


---

Źródła:

https://jestjs.io/

https://www.youtube.com/watch?v=_zEX9sHzqS4

https://www.youtube.com/watch?v=gX440uva4NU
