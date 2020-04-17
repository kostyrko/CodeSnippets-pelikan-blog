Title: JavaScript - właściwości i metody łańcuch znaków
Author: mkostyrko
Date: 2020-04-10 10:00
Updated:
Category: javascript
Tags: javascript, js, string, łańcuch znaków, metody
Slug: js-metody-lancucha-znakow
related_posts: 

Jedną z podstawowych i często stosowanych właściwości stringów jest `length` który zwraca długość łańcucha znaków

    const fu = "bar"
    console.log(fu.length)
    >> 3

Metod, które można zastosować wobec stringów jest o wiele więcej - poniżej przedstawię tylko część z nich.
Wszystkie metody łańcucha zwracają nową wartość nie zmieniając oryginalnej

`charAt()` - zwraca znak znajdujący się na wskazanym indeksie

`concat()` - łączy ze sobą ciągi znaków

`endsWith()` - sprawdza czy ciąg znaków kończy się wskazanym znakiem

`includes()` - sprawdza czy ciąg znaków zawiera wskazany znak

`indexOf()` - zwraca pozycję indeksową (pierwszego) wskazanego znaku

`lastIndexOf()` - zwraca pozycję indeksową (ostatniego) wskazanego znaku

`match()` - sprawa ciąg znaków w poszukiwaniu wskazanego wyrażenia

`repeat()` - zwraca ciąg znaków który jest wielokrotnym powtórzeniem danego ciągu

`replace()`  - przeszukuje ciąg znaków w poszukiwaniu znaku lub wyrażenia i zwraca nowy string gdzie wskazany wcześniej ciąg lub znak jest zmieniony

    let str = "Visit Microsoft!";
    res = str.replace("Microsoft", "W3Schools");
    >> str = "Visit W3Schools!";

`search()` - przeszukuje ciąg znaków w poszukiwaniu znaku lub wyrażenia i zwraca ich indeks

`slice()` - wyciąga część łańcucha znaków i zwraca nowy na tej podstawie

`split()` - tnie łańcuch znaków i tworzy z niego tablicę

    const str = "How are you doing today?";
    let res = str.split(" ");
    >> res = ["How","are","you","doing","today?"]

`toLowerCase()`/`toUpperCase()` - zwraca łańcuch zmieniając wszystkie litery na małe/duże

`trim()` - pozbywa się spacji z końca i początku łąńcucha znaków


Źródła:

https://www.w3schools.com/jsref/jsref_obj_string.asp