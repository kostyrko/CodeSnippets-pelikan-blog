Title: JavaScript - obiekt Math
Author: mkostyrko
Date: 2020-04-13 09:00
Updated:
Category: javascript
Tags: javascript, js, math, obiekt math, object
Slug: js-math
related_posts: js-obiekty-wbudowane

Math jest wbudowanym obiektem (najwyższego poziomu), który posiada właściwości i metody związane z metodami stałymi i matematycznymi.

`Math.Pi` - właściwość (jedna z wielu) - pozwala odwołać się do wartości Pi (ok. 3.14159)


### Metody (wybrane):

`Math.random()` - zwraca liczbę pseudolosową z przedziału [0,1)


`Math.ceil()` - zwraca najmniejszą liczbę całkowitą większą do lub równą danej

      Math.ceil(.95);   // 1
      Math.ceil(4);     // 4
      Math.ceil(7.004); // 8

`Math.abs()` - zwraca wartość bezwzględną danej liczby

      Math.abs('-1'); // 1 
      Math.abs(-2); // 2 
      Math.abs(null); // 0 
      Math.abs('string'); // NaN 

`Math.floor()` - zwraca największą liczbę całkowitą mniejszą od lub równą danej

      Math.floor( 45.95); //  45
      Math.floor(-45.95); // -46

`Math.round()` - zwraca liczbę zaokrągloną do najbliższej liczby całkowitej

      x = Math.round(20.5)
      //zwraca 21

`Math.sign()` - zwraca znak liczby  w postaci wynikowej `1, -1, 0, -0, NaN`

      Math.sign(3)     //  1
      Math.sign(-3)    // -1
      Math.sign("-3")  // -1
      Math.sign(0)     //  0
      Math.sign(-0)    // -0
      Math.sign(NaN)   // NaN
      Math.sign("foo") // NaN

`Math.trunc()` - z floata robi integer poprzez usunięcie wartości po kropce

      Math.trunc(13.37) // = 13
      Math.trunc(-0.123) // = 0

`Math.min()/max()` - zwraca mniejszą/większą z dwóch liczb lub większej ilości liczb, argumentem może być również tablica

      console.log(Math.max(-1, -3, -2));
      // oczekiwany rezultat: -1

      const array1 = [1, 3, 2];
      console.log(Math.max(...array1));
      // oczekiwany rezultat: 3

::: wykorzystanie Array.reduce() do znalezienia największego elementu w tablicy zawierającej liczby - tworzy pary i porównuje je liczby ze sobą :::

      const arr = [1,2,3];
      const max = arr.reduce(function (a,b){
            return Math.max(a,b);
      });

`Math.pow()` - dana liczba podniesiona do potęgi

      Math.pow(7, 2); // 49

`Math.sqrt()` - zwraca pierwiastek kwadratowy danej liczby

      Math.sqrt(9); // 3
      Math.sqrt(2); // 1.414213562373095
      Math.sqrt(1);  // 1



Źródła:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

h