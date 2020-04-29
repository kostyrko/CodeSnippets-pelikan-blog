Title: JavaScript - właściwości i metody łańcucha znaków
Author: mkostyrko
Date: 2020-04-10 10:00
Updated:
Category: javascript
Tags: javascript, js, string, łańcuch znaków, metody
Slug: js-metody-lancucha-znakow
related_posts: 

Jedną z podstawowych i często stosowanych właściwości stringów jest **`length`** który zwraca długość łańcucha znaków

    const fu = "bar"
    console.log(fu.length)
    >> 3

Metod, które można zastosować wobec stringów jest o wiele więcej - poniżej przedstawię tylko część z nich.
Wszystkie metody łańcucha zwracają nową wartość nie zmieniając oryginalnej

`charAt()` - zwraca znak znajdujący się na wskazanym indeksie

    let droid = 'r2d2'
    droid.charAt(2) // d

`concat()` - łączy ze sobą ciągi znaków, pozwala na wprowadzenie więcej niż jednego argumentu

    let droid = 'r2d2'
    droid = droid.concat('&', 'c3po')
    droid // r2d2&c3po

`endsWith()` - sprawdza czy ciąg znaków kończy się wskazanym znakiem

`includes()` - sprawdza czy ciąg znaków zawiera wskazany znak // zwraca true albo flase

`indexOf()` - zwraca pozycję indeksową (pierwszego) wskazanego znaku

    let droid = 'r2d2'
    droid[2] // d

    droid.indexOf('r') // 0

`lastIndexOf()` - zwraca pozycję indeksową (ostatniego) wskazanego znaku

    droid.lastIndexOf('2') // 3

`match()` - sprawdza ciąg znaków w poszukiwaniu wskazanego wyrażenia

`repeat()` - zwraca ciąg znaków który jest wielokrotnym powtórzeniem danego ciągu

`replace()`  - przeszukuje ciąg znaków w poszukiwaniu znaku lub wyrażenia i zwraca nowy string gdzie wskazany wcześniej ciąg lub znak jest zmieniony

    let str = "Visit Microsoft!";
    res = str.replace("Microsoft", "W3Schools");
    >> str = "Visit W3Schools!";

`search()` - przeszukuje ciąg znaków w poszukiwaniu znaku lub wyrażenia i zwraca ich indeks

`split()` - tnie łańcuch znaków i tworzy z niego tablicę (jako argument przyjmuje separator)

    let droid = 'r2d2, c3po'
    console.log(droid.split(",")) // [ "r2d2"," c3po"]

`slice()` - wyciąga część łańcucha znaków i zwraca nowy na tej podstawie / przyjmuje również liczbę ujemną (zaczyna od końca)

    let droid = 'r2d2'
    console.log(droid.substring(-3,3)) // 2d

`substring() ` - przyjmuje dwa argumenty (indeks - 1. łącznie, 2. wyłącznie) i zwraca części łańcucha zawarte pomiędzy nimi 

    let droid = 'r2d2'
    console.log(droid.substring(1,3)) // 2d

`toLowerCase()`/`toUpperCase()` - zwraca łańcuch zmieniając wszystkie litery na małe/duże

`trim()` - pozbywa się spacji z końca i początku łańcucha znaków


Źródła:

https://www.w3schools.com/jsref/jsref_obj_string.asp