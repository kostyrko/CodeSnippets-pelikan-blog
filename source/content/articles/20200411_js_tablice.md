Title: JavaScript - tablice (obiekt array)
Author: mkostyrko
Date: 2020-04-11 10:00
Updated:
Category: javascript
Tags: javascript, js, array, tablica
Slug: js-tablice
related_posts: js-obiekty, js-podstawowe-typy


Tablica (array) jest uporządkowaną listą zawierająca elementy, gdzie każdy z elementów ma dowolną wartość (są heterogeniczne). Tablica jest definiowana poprzez umieszczenie wartości pomiędzy kwadratowymi nawiasami (literałami tablicy), które nazywają się jej elementami.

    let Arr = []; // pusta tablica
    let arr = ["Mikolaj", 2020, "kwiecień", 17.04];

Zadeklarowanie tablicy słowem kluczowym **`const`** pozwala na modyfikację jej zawartości ale nie na zmianę miejsca, w którym jest ona przechowywana.

W przypadku użycia słowa kluczowego **`let`** istnieje możliwość nadpisania tablicy

Każdemu elementowi przyporządkowana jest liczba indeksowa, pozwalająca na odwołanie się do niego.
Tablica może zawierać również obiekty jak i tablice.

    arr[0]
    > Mikolaj

Właściwość `length` zwraca "długość" tablicy

    arr.length
    > 4

Aby odwołać się do ostatniego elementu należy zastosować `length - 1`

    arr[arr.length - 1]
    > 17.04

### Zmiana elementów

Przy wykorzystaniu operator składającego się z kwadratowych nawiasów `[]` oraz wpisanego w nie indeksu można zmieniać wybrany element tablicy

    arr[2] = "maj"
    ["Mikolaj", 2020, "maj", 17.04]

### "Długość" tablicy

Wykorzystując właściwość `length` można również dodać element do końca tablicy

    arr[arr.length]  = "ostatnia"
    > arr = ["Mikolaj", 2020, "kwiecień", 17.04. "ostatnia"]
    
### Undefined

Jeśli dana tablica nie zawiera elementu pod indeksem do którego się odwołujemy wówczas zwraca `undefined`

        let arr = ["Mikolaj", 2020, "kwiecień", 17.04];
        console.log(arr[4])
        > undefined



Źródła:

https://www.youtube.com/watch?v=8FmBEN0XZyI

http://kursjs.pl/kurs/super-podstawy/tablice.php

https://launchschool.com/books/javascript/read/arrays#whatisanarray