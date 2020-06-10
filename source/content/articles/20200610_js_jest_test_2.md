Title: JavaScript - kolejny test w JEST (TDD)
Author: mkostyrko
Date: 2020-06-10 12:00
Updated:
Category: javascript
Tags: test, jest, tdd, node, npm, babel, transpilacja, transpilator, babel.js, babeljs
Slug: js-jest-test-2
related_posts:

![jest](https://tamalweb.com/wp-content/uploads/2019/07/jest_js-700x394.png)

Poniższy wpis powstał na podstawie tego [materiału](https://www.youtube.com/watch?v=gX440uva4NU), patrz również [tutaj](https://exercism.io/my/solutions/ca7b90c2164a49e5aed19f12518ac333) i jego założeniem jest próbą wprowadzenia do TDD (test driven development). W pierwszej kolejności znane są wytyczne/scenariusz funkcji następnie powstaje test a na jego podstawie funkcja

Zadanie stwórz funkcję spełniającą następujące warunki


    1. Bob answers 'Sure.' if you ask him a question.

    2. He answers 'Whoa, chill out!' if you yell at him.

    3. He retorts 'Calm down, I know what I'm doing!' if you yell a question at him.

    4. He says 'Fine. Be that way!' if you address him without actually saying anything.
    
    5. He answers 'Whatever.' to anything else.


Test 1

`talkToBob.test.js`

    import talkToBob from './talkToBob'

    it("answers Sure, if ask him a question", () => {
      expect(talkToBob("How are You?").toBe('Sure.'))
    })

`talkToBob.js`

    const talkToBob = (msg = "") => {
      if(msg.endsWidth("?")) return "Sure"
    };

    export default talkToBob

----

Test 2...

![TBC](https://steveworkingthroughtheword.files.wordpress.com/2016/03/tobecontinued.jpg)



---

Źródła:

https://jestjs.io/


https://www.youtube.com/watch?v=gX440uva4NU

https://medium.com/javascript-scene/tdd-changed-my-life-5af0ce099f80 --TDD
