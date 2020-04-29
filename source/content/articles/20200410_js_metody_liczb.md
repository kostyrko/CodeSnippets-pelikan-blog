Title: JavaScript - metody liczb
Author: mkostyrko
Date: 2020-04-10 11:00
Updated:
Category: javascript
Tags: javascript, js, liczby, numbers
Slug: js-metody-liczb
related_posts: js-metody-lancucha-znakow

Typ liczbowy (Numbers) posiada przypisane sobie metody - poniżej przedstawiona została część z nich

`toString()` - dokonuje konwersji na string

    (100 + 20).toString();   // '120' - zwraca sumę

`toFixed()` - pozwala na określenie ilości znajków liczbowych po kropce

    const x = 9.656;
    x.toFixed(0);           // 10
    x.toFixed(2);           // 9.66
    x.toFixed(4);           // 9.6560

`toPrecision()` - określa ilość znaków w wyrażeniu (łącznie)

    const x = 9.656;
    x.toPrecision();        // 9.656
    x.toPrecision(2);       // 9.7
    x.toPrecision(4);       // 9.656


`MAX_VALUE`/`MIN_VALUE` - zwraca największą/najmniejszą możliwą liczbę

    const x = Number.Number.MAX_VALUE/MIN_VALUE

`parseInt()`/`parseFloat()` - zmienia string w integer/float

    parseInt('123.32') // 123

    parseFloat('123.32') // 123.32


Źródła:

https://www.w3schools.com/js/js_number_methods.asp