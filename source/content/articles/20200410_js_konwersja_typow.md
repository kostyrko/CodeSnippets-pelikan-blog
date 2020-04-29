Title: JavaScript - konwersja/translacja pomiędzy numbers i string
Author: mkostyrko
Date: 2020-04-10 09:00
Updated:
Category: javascript
Tags: javascript, js, string, łańcuch znaków, metody
Slug: js-konwersja-typow
related_posts: js-podstawowe-typy


W przy pomocy metod istnieje możliwość wymuszenia konwersji różnego typu danych (boolean, string, numbers)

W ten sposób można przekształcić **boolean lub number w string**

** Konwersja na string** `String()`, `x.toString()`

    String(123)        // '123'
    String(-12.3)      // '-12.3'
    String(null)       // 'null'
    String(undefined)  // 'undefined'
    String(true)       // 'true'
    String(false)      // 'false'

    x = 50
    x.toString() // '50'
    (123).toString()
    null.toString() // Cannot read property 'toString' of null

    false.toString() // 'false'
    String(true) // 'true'

    String(Date()) // "Wed Apr 29 2020 11:49:20 GMT+0200 (Central European Summer Time)"
    Date().toString() // "Wed Apr 29 2020 11:49:20 GMT+0200 (Central European Summer Time)"

W ten sposób można przekształcić **boolean lub string w number** -> `Number(), parseInt(), parseFloat()`

    Number(null)                   // 0
    Number(undefined)              // NaN
    Number(true)                   // 1
    Number(false)                  // 0
    Number(" 12 ")                 // 12
    Number("-12.34")               // -12.34
    Number("\n")                   // 0
    Number(" 12s ")                // NaN
    Number(123)                    // 123
    Number("")                     // 0
    Number("99 88")                // NaN

Zmienia string w integer

    parseInt('123.32') // 123

Zmienia string w float 

    parseFloat('123.32') // 123.32

Pozwala na łączenie z metodami liczb

    Number('154.223').toPrecision(4) // 154.2

W ten sposób można przekształcić **boolean do stringu w number** `Boolean()`

    Boolean('')           // false
    Boolean(0)            // false     
    Boolean(-0)           // false
    Boolean(NaN)          // false
    Boolean(null)         // false
    Boolean(undefined)    // false
    Boolean(false)        // false


**Domniemane (automatyczne) wymuszanie typów**

Tak zwane *domniemane wymuszenie typów* (type coersion) jest procesem konwersji danych z jednego typu na inny bezpośrednio przez JS - to może dokonać się zarówno na typach prymitywnych jak i obiektach. 

Do takiego wymuszenia zachodzi wówczas gdy dokonujemy **porównania** danych bez sprawdzenia ich typu
zatem zastosowanie `==` zamiast `===`

    'true' == true // true
    true' === true // false

    12 / "6" // 2

    12 > "6" // true

    12 < "6" // false

Do `wymuszenia` może dojść również w trakcie podjęcia próby **sumowania** różnego typu danych

    x = 5

    x + 5 // 10

    '5' + 5 // 10

    'five' + 5 // five5

    true + 5 // 6 (ponieważ => true = 1)

    false + 5 // 5 (ponieważ => false = 0)

    true + true // 2

W przypadku obiektów

    [1,2,3] == [1,2,3]       // false (zmiana nie jest wymuszana, ale sprawdzana jest instancja a nie zawartość)
    ['x'] == 'x'             // true 


Źródła:

https://www.w3schools.com/js/js_type_conversion.asp
https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/