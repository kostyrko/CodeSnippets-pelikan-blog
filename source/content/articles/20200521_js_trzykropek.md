Title: JavaScript i trzykropek (...)
Author: mkostyrko
Date: 2020-05-21 10:00
Updated:
Category: javascript
Tags: javascript, js, array, tablica, ES6, ES2015
Slug: js-trzykropek
related_posts: js-podstawowe-typy, js-tablice


Zastosowanie trzech kropek wprowadzonych w ES6 - pozwala na rozwinięcie wyrażenia iterowalnego (wielokorotnie powtarzalnego/przejściowego) jako `spread` operator lub parametr `rest`. 

Trzykropek można stosować w kontekście obiektów, tablic, stringów, zbiorów (setów) i map.


### Spread Operator

*Dzieli kolekcję tworząc tablicę*

Pozwala na rozciągnięcie (rozwinięcie) obiektu mogącego ulec iteracji wewnątrz odbiorcy (np. zamiast tworzenia zagnieżdżonej tablicy1 w tablicy2 - tablice2 przyjmuje właściwości tablicy1)

    const arr1 = ['r4', 'c3po']
    const arr2 = [arr1, 'r2dr']
    console.log(arr2) >> [['r4', 'c3po'], 'r2dr']
    vs
    const arr3 = [...arr1, 'r2d2']
    console.log(arr3) >> ['r4', 'c3po', 'r2dr']

Przykładowo pozwala na stworzenie tablicy z elementów zbliżonych (argument) do tablicy lub ze stringa [argument jak i odbiorca mogą być obiektem tablicą, łańcuchem znaków (stringiem), zbiorem lub map]

  let arr = [...HTML-collection]

Przykładowe zastosowanie

    function sum(...theArgs) {
        return theArgs.reduce((previous, current) => {
          return previous + current;
        });
      }

      console.log(sum(1, 2, 3));
      >> 6

Przy wywoływaniu funkcji i podawaniu jako argumentu tablicy pozwala na jej rozłożenie na pojedyncze argumenty (wyjmuje je z tablicy)

Przykładowe zastosowanie

    function sum(x, y, z) {
      return x + y + z;
    }

    const numbers = [1, 2, 3]; // tablica

    console.log(sum(...numbers)); // rozłożenie tablicy na pojedyncze argumentu
    >> 6

### Rest parameters

*Sumuje poszczególne parametry (w) tworząc tablicę*

Pozwala na wskazanie możliwości zastosowania nieokreślonej liczby argumentów, w funkcji, które zostaną zamienione w tablicę. Pozwala również na podanie poprzedzających parametrów nazwanych (te wówczas nie znają się w tablicy).



    function myFunc(a, b, ...args) {
    console.log(a); // 22
    console.log(b); // 98
    console.log(args); // [43, 3, 26]
    };
    myFunc(22, 98, 43, 3, 26);

    -------------------

    function myFunc(...args) {
    args.forEach( a => console.log(a))
    return args
    }

    console.log(myFunc(1, 2, 3)) 

    >> 1
    >>  2
    >>  3
    >>  [1,2,3]

    ----

    function myFunc(...[x, y, z]) {
        return x + y + z;
      }

      myFunc(1)          // NaN - brak agrumentów
      myFunc(1, 2, 3)    // 6
      myFunc(1, 2, 3, 4) // 6 - tylko pierwsze trzy są brane pod uwagę




Źródła:

https://dev.to/sagar/three-dots---in-javascript-26ci

https://dev.to/blacksonic/the-tale-of-three-dots-in-javascript-4287

https://stackoverflow.com/questions/42184674/what-is-the-meaning-of-args-three-dots-in-a-function-definition

https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Operatory/Sk%C5%82adnia_rozwini%C4%99cia