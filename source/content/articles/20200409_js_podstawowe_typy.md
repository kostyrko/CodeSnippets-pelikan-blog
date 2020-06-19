Title: JavaScript - składnia, deklaracje i podstawowe typy danych oraz ich operatory
Author: mkostyrko
Date: 2020-04-09 10:00
Updated:
Category: javascript
Tags: javascript, js, typy, dane, data types, operatory
Slug: js-podstawowe-typy
related_posts: js-obiekty, js-tablice


W JavaScript istnieją dwa typy danych - proste/prymitywne i referencyjne, poniżej zostaną przedstawione te pierwsze. Typy referencyjne przechowywane są w pamięci podręcznej a zmienna jest do nich referencją.

---
### Postawy i deklaracje

w JS instrukcje nazywane są wyrażeniami i rozdzielone są średnikiem `;`

składnia komentarza

    // jednoliniowy

    */ wielo - 
      liniowy
    */
    
Istnieją trzy typy deklaracji zmiennych

![starWars_zmienne](https://miro.medium.com/max/640/0*2Iz9vcaOtPNivfen.png)

  * `const` - podstawowa deklaracja, nie ulega zmianie, tylko do odczytu
  * `let` - deklaracja stosowana w przypadku gdy zmienna będzie musiała ulec zmianie, jest lokalna i ograniczona do bloku, w którym jest zawarta
  * `var` - wcześniej podstawowa zmienna (przed ES6), obecnie rzadziej stosowana (po wprowadzeniu const i let) więcej na ten temat [tutaj](https://medium.com/@larry.sassainsworth/let-vs-var-vs-const-in-javascript-8b898f868394) lub poniżej.


---
`var` vs `let` -> 4 istotne różnice w:
1) **zakresie** (scope) 
2) **podnoszeniu** (hoisting) 
3) **ponownej deklaracji** (redeclaration) 
4) **tworzeniu globalnego obiektu** (global object property)

`let` w odróżnieniu od `var` nie jest globalnie dostępny a przypisany do najbliższych funkcji etc. jest dostępny w sposób skryptowy (linia po linii, podobnie jak w pythonie), wartość mu przypisana może być zmieniona ale nie może zostać ponownie zadeklarowany, nie tworzy globalnie dostępnego obiektu.


| słowo kluczowe | Zakres | Windowanie | Czy może być jej ponownie przypisana wartość | Czy może być ponownie zadeklarowana?
|---|---|---|---|---| 
| `var` | Zakres funkcji | Tak | Tak | Tak |
| `let` | Zakres bloku | nie | Tak | nie |
| `var` | Zakres bloku| nie | nie | nie |

więcej na ten temat [tutaj](https://www.taniarascia.com/es6-syntax-and-feature-overview/)


*Hoisting* - "przenoszenie" zmiennych na sam początek kodu, do globalnego zasięgu lub zasięgu funkcji ([więcej tutaj na ten temat](http://blog.pjuskiewicz.com/2017/11/11/hoisting-windowanie-javascript/))

---


deklaracji dokonujemy poprzez użycie słowa kluczowego (let, const) + identyfikator (nazwy zmiennej np. foo lub fu etc.), oraz poprzez opcjonalne przypisanie jej wartości (np. 'bar')

    let fu = "bar"

* zmienne nie mogą zaczynać się od cyfr
* wielkość liter na znaczenie `fu` to nie to samo co `Fu`
* nazwa zmiennej nie może zawierać spacji, myślników, kropek - stosowany natomiast jest podkreślnik np. _fu
* nazwa zmiennej nie może być [słowem kluczowym](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords)

----

### Podstawowe typy danych

Do podstawowych (tzw. prymitywnych) typów danych wykorzystywanych w JS zaliczyć można:

* **string** - ciągi znaków tzw łańcuchowy (np. "ab2c ala" - wymaga cudzysłowu lub apostrofu)
* **number** - typ liczbowy (np. 123 - brak cudzysłowu)
* **undefined** - typ specjalny, niezainicjowana zmienna/nieistniejąca właściwość obiektu
* **null** - type specjalny, określa pustą wartość (wykorzystywany przy obiektach)
* **boolean** - typ logiczny (Prawda/Fałsz - True/False)

____

### Typ łańcuchowy

Operator `+` pozwala na dodanie treści do zadeklarowanego wcześniej łańcucha znaków

    let droid = 'r2d2'
    droid += '&c3po'
    droid // r2d2&c3po

Można uzyskać wybrany znak z łańcuch po indeksie

    let droid = 'r2d2'
    droid[2] // d

    droid.indexOf('r') // 0

::: (Template literals) istnieje również możliwość włączania wartości zmiennej w ciąg łańcucha znaków poprzez zamknięcie treście w `` + zastosowaniu $ i nawiasów klamrowych - w ten sposób można wstawiać również równania( zwraca wynik), jak i funkcje etc. :::

    const droid = 'r2d2'

    console.log(`to nie jest %{droid}, którego szukamy`)
lub:

    console.log("to nie jest" + " " + droid + " którego szukamy")
wynik będzie ten sam:

    >> `to nie jest r2d2, którego szukamy`

Przydatne kolokacje znaków (tzw. escaping) wykorzystanych w typie łańcuchowym

`\n` - nowy wiersz

`\r `- reset pozycji kursora i powrót na nową linię

`\t` - tabulacja

`\` - lewy ukośnik jest również wymagany przed `\` , `"` lub **`** z racji tego, że są znakami specjalnymi dla JS -> np. 

    \"

* pozwala na łączenie ze sobą ciągów znaków przy pomocy operatora `+`

:::Napisy szablonowe - osadzenie do w ramach łańcucha zmiennej wymaga zastosowanie znaku dolara nawiasów klamrowych oraz tylniego apostrofu `String ${variable}` więcej na ten temat [tutaj](https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/template_strings):::

    const cat = "Deedee"
    console.log(`kot ${cat}`)
    > kot Deedee

::: metody łańcucha znaków String.formCharCode() - "Zwraca łańcuch znaków stworzony przez podaną sekwencję kodów Unicode.", String.fromCodePoint() - zwraca łańcuch stworzony na podstawie specyficznej sekwencji punktów kodu, String.raw() :::


---

### Typ liczbowy

* jeśli zaczyna się od zera tj traktowany jako wartość ósemkowa a od 0x jako szesnastkowa

* może być zapisywana wartość w notacji wykładniczej "X.YeZ, gdzie X to część całkowita, Y część dziesiętna, natomiast Z to wykładnik potęgi liczby 10. Zapis taki oznacza to samo, co X.Y * 10Z" ([źródło](http://webmaster.helion.pl/index.php/kjs-cechy-jezyka/kjs-typy-danych))

Przykładowe zastosowanie: 123, -123, 1.1, -1.1, 0.1E2, -0x0f

* pozwala na przeprowadzanie stosowanie operatorów arytmetycznych -> `* + - /`

* operator `%` modulo dzieli z resztą

* operator `--` oraz `++` dokonuje dekrementacji oraz inkrementacji/ zmniejszenia lub zwiększenia wartości o 1 (`x--` lub `--x` tj to samo co `x = x -1`)

* pozwala również na stosowanie *operatorów porównania (relacyjnych)* np `<= < > >= !== === !=` oraz *bitowych*

* `==` równy?

* `===` równy tego samego typu?

* `!==` nierówny?

---

### Typ logiczny

* pozwala na stosowanie operatorów logicznych `&&` - and/i, `||` - or/albo, `!` - not/nie

---

### typeof

w przypadku niepewności jakiego typ danych przechowuje dana zmienna istniej możliwość zastosowania operatora `typeof`, który zwraca łańcuch zwierający typ tzw. operandu (argument operatora)

    schemat: typeof operand
    
przykład1: 
    
    typeof 1
    >> 'number'

przykład2:

    const robot = 'r2d2'
    typeof robot
    >> 'string'

Zastosowanie z innymi typami danych:

    typeof [1,2,3,4]              // "object"
    typeof {name:'John', age:34}  // "object"
    typeof new Date()             // "object"
    typeof function () {}         // "function"
    typeof myCar                  // "undefined"

---

Źródła:

https://launchschool.com/books/javascript/read/basics#datatypes

https://developer.mozilla.org/pl/docs/Web/JavaScript/Guide/Sk%C5%82adnia_i_typy

http://webmaster.helion.pl/index.php/kjs-cechy-jezyka/kjs-typy-danych

http://webmaster.helion.pl/index.php/kjs-cechy-jezyka/kjs-operatory/kjs-operatory-arytmeyczne

http://webmaster.helion.pl/index.php/kjs-cechy-jezyka/kjs-operatory/kjs-operatory-logiczne

http://kursjs.pl/kurs/super-podstawy/zmienne.php

https://medium.com/@larry.sassainsworth/let-vs-var-vs-const-in-javascript-8b898f868394

https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var

https://www.youtube.com/watch?v=JFDScHg6Dws