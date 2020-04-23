Title: JavaScript - kontrola przepływu (if...else/switch/operator warunkowy)
Author: mkostyrko
Date: 2020-04-09 11:00
Updated:
Category: javascript
Tags: javascript, js, if...else, switch, else...if
Slug: js-kontorla-przeplywu
related_posts: 

Polecenie `if...else` pozwala na kontrolę przepływu kodu -> gdy pewien warunek jest spełniony (`if`) kod jest wykonywany a jeśli nie to może sprawdzić kolejny warunek (`else if`) lub wykonać określony kod (`else`)

      if (warunek) {
            kod do wywołania jeśli warunek spełniony
      } else if (inny warunek) {
            kod do wywołania jeśli warunek spełniony
      } else {
            kod do wywołania jeśli żaden z powyższych warunków nie jest spełniony
      }

      if (time < 10) {
      greeting = "Good morning";
      } else if (time < 20) {
      greeting = "Good day";
      } else {
      greeting = "Good evening";
      }

:::w JS - nie zawsze wymagane jest stosowanie polecania `else` i samo `if` jest czasem wystarczające np. jeśli sprawdzamy pewien warunek w pętli, wówczas w domyśle `continue` :::

      if (hour < 18) {
      greeting = "Good day";
      }

---

### Operator warunkowy

W przypadku prostej kontroli przepływu opierającej się na sprawdzaniu dwóch warunków można oprzeć się na operatorze warunkowym

Gdzie po spisaniu warunku stawia się znak zapytania a następnie rozdziela się wyrażenie1 od wyrażenie2 dwukropkiem

      warunek ? wyrażenie1 : wyrażenie2

      Przykład 1:

      let time = 11
      time < 10 ? greeting = "Good morning" : greeting = "Good day"
      console.log(greeting)
      >> Good day


      Przykład 2:
      
      // jeśli w tablicy nic nie ma zwróć null w przeciwnym wypadku wykonaj na tablicy metodę reduce...

      return newArr.length === 0
      ? null
      : newArr.reduce((acc, elem) => acc + elem, 0);

---
### Switch

Polecenie if jest używane wówczas gdy należy wywołać określony kod przy zaistnieniu odpowiednich warunków

      switch(wyrażenie_zwracające_warunek) {
            case warunek1:
                  kod1;
                  break;
            case warunek2:
                  kod2;
                  break;
            default:
                  jeśli powyższe nie są spełnione
      }

            switch (new Date().getDay()) {
            default:
                  text = "Looking forward to the Weekend";
                  break;
            case 6:
                  text = "Today is Saturday";
                  break;
            case 0:
                  text = "Today is Sunday";
            }

Źródła:

https://codeburst.io/javascript-the-conditional-ternary-operator-explained-cac7218beeff

https://www.w3schools.com/js/js_if_else.asp

https://pl.wikipedia.org/wiki/Operator_warunkowy

