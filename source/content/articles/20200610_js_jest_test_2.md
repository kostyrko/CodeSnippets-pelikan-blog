Title: JavaScript - kolejny test w JEST (TDD)
Author: mkostyrko
Date: 2020-06-10 12:00
Updated:
Category: javascript
Tags: test, jest, tdd, node, npm, babel, transpilacja, transpilator, babel.js, babeljs
Slug: js-jest-test-2
related_posts:

![jest](https://tamalweb.com/wp-content/uploads/2019/07/jest_js-700x394.png#center)

Poniższy wpis powstał na podstawie tego [materiału](https://www.youtube.com/watch?v=gX440uva4NU), patrz również [tutaj](https://exercism.io/my/solutions/ca7b90c2164a49e5aed19f12518ac333) i jego założeniem jest próbą wprowadzenia do TDD (test driven development). W pierwszej kolejności znane są wytyczne/scenariusz funkcji następnie powstaje test a na jego podstawie funkcja

Zadanie stwórz funkcję spełniającą następujące warunki


    1. Bob answers 'Sure.' if you ask him a question.

    2. He answers 'Whoa, chill out!' if you yell at him.

    3. He retorts 'Calm down, I know what I'm doing!' if you yell a question at him.

    4. He says 'Fine. Be that way!' if you address him without actually saying anything.
    
    5. He answers 'Whatever.' to anything else.


#### Test 1

`talkToBob.test.js`

    const talkToBob = require('./talkToBob');

    test("answers Sure, if ask him a question", () => {
      expect(talkToBob("How are You?")).toBe("Sure")
    });

`talkToBob.js`

    function talkToBob(info = "") {
      if(info.endsWith("?")) return "Sure";
    };

    module.exports = talkToBob;

#### Test 2

`talkToBob.test.js`

    const talkToBob = require('./talkToBob');

    describe('Function - talkToBob', () => {
      test("answers Sure, if ask him a question", () => {
        expect(talkToBob("How are You?")).toBe("Sure")
      });
      test("Answers 'Whoa, chill out!' if you yell at him", () => {
        expect(talkToBob("WHAT?")).toBe("Whoa, chill out!")
      });
    });

`talkToBob.js`

    function talkToBob(info = "") {
      if(info.endsWith("?") && info !== info.toUpperCase()) return "Sure";
      if(info === info.toUpperCase()) return "Whoa, chill out!";
    };

    module.exports = talkToBob;

#### Test 3

`talkToBob.test.js`

    const talkToBob = require('./talkToBob');

    describe('Function - talkToBob', () => {
      test("answers Sure, if ask him a question", () => {
        expect(talkToBob("How are You?")).toBe("Sure")
      });
      test("Answers 'Whoa, chill out!' if you yell at him", () => {
        expect(talkToBob("DON'T")).toBe("Whoa, chill out!")
      });
      test("He retorts 'Calm down, I know what I'm doing!' if you yell a question at him.", () => {
        expect(talkToBob("WHAT?")).toBe("Calm down, I know what I'm doing!")
      });
    });

`talkToBob.js`

    function talkToBob(info = "") {
      if(info.endsWith("?") && info !== info.toUpperCase()) return "Sure";
      if(info === info.toUpperCase() && !info.endsWith("?")) return "Whoa, chill out!";
      if(info.endsWith("?")) return "Calm down, I know what I'm doing!";
      if(info === "") return "Fine. Be that way!";
      else return 'Whatever.'
    };

    module.exports = talkToBob;

#### Test 4-5

`talkToBob.test.js`

    const talkToBob = require('./talkToBob');

    describe('Function - talkToBob', () => {
      test("answers Sure, if ask him a question", () => {
        expect(talkToBob("How are You?")).toBe("Sure")
      });
      test("Answers 'Whoa, chill out!' if you yell at him", () => {
        expect(talkToBob("DON'T")).toBe("Whoa, chill out!")
      });
      test("He retorts 'Calm down, I know what I'm doing!' if you yell a question at him.", () => {
        expect(talkToBob("WHAT?")).toBe("Calm down, I know what I'm doing!")
      });
      test("He says 'Fine. Be that way!' if you address him without actually saying anything.", () => {
        expect(talkToBob("")).toBe('Fine. Be that way!')
      });
      test("He answers 'Whatever.' to anything else.", () => {
        expect(talkToBob("whatever")).toBe('Whatever.')
      });
    });

`talkToBob.js`

    function talkToBob(info = "") {
      if(info.endsWith("?") && info !== info.toUpperCase()) return "Sure";
      if(info === info.toUpperCase() && !info.endsWith("?") && info.length !== 0 ) return "Whoa, chill out!";
      if(info.endsWith("?")) return "Calm down, I know what I'm doing!";
      if(info === "") return "Fine. Be that way!";
      else return 'Whatever.'
    };

    module.exports = talkToBob;

::: Niezastosowanie przy drugim warunku  `&& info.length !== 0` a wprowadzenie dowolnej wartości jako domyślnej wprowadzanego, który stanie się wywołaniem czwartego warunku nie spełni wymogu założonego przez piąty test:::

---

Źródła:

https://jestjs.io/


https://www.youtube.com/watch?v=gX440uva4NU

https://medium.com/javascript-scene/tdd-changed-my-life-5af0ce099f80 --TDD
