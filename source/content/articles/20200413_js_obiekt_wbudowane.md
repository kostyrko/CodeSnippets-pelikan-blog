Title: JavaScript - obiekty wbudowane
Author: mkostyrko
Date: 2020-04-13 08:00
Updated:
Category: javascript
Tags: javascript, js, obiekty wbudowane
Slug: js-obiekty-wbudowane
related_posts: js-obiekt-math

### Wartości

`Infinity`

`NaN`

`undefined`

`null`

---

### Funkcje

`eval()` - ocenia kod który jest stringiem (użycie tego nie jest bezpieczne jeśli ogólnodostępne)

    console.log(eval('2 + 2') === eval('4'));
    // expected output: true

    console.log(eval('2 + 2') === eval(new String('2 + 2')));
    // expected output: false

`uneval()` - tworzy string reprezentujący kod źródłowy obiektu

    uneval(function foo() {}); // returns "(function foo(){})"


`isFinite()` - sprawdza czy liczba podana (argument) jest liczbą skończoną

`isNaN()` - sprawdza czy podany argument jest liczbą

    console.log(milliseconds('100F'));
    // expected output: "Not a Number!"

`parseFloat()` - analizuje argument (string?) i zwraca go jako float

    function circumference(r) {
    return parseFloat(r) * 2.0 * Math.PI;
}

`parseInt()` - analizuje argument (string) i zwraca go jako integer

`decodeURI()` - dekoduje Uniform Resource Identifier wcześniej stworzony przez `encodeURI()`

`decodeURIComponent()`  - dekoduje Uniform Resource Identifier wcześniej stworzony przez `encodeURIComponent()`

`encodeURI()` - koduje URI poprzez zamianę każdej instancji na 1-4 wyjściowych sekwencji reprezentowanych przez symbol z UTF-8

`encodeURIComponent()` - jw

---


### Obiekty podstawowe

Object

Function

Boolean

Symbol

Error

EvalError

RangeError

ReferenceError

SyntaxError

URIError

----

### Liczby i daty

`Number` - pozwala pracować z wartościami liczbowymi, stosowany przy uzyskiwaniu dostępu do stałych właściwości. Posiada *właściwości*

Metody Numbers został przedstawione tutaj [tutaj](https://kostyrko.github.io/zfrontu/js-metody-liczb.html)

---
Obiekt Math został opisany [tutaj](https://kostyrko.github.io/zfrontu/js-math.html)

---

#### Date

`Date` - reprezentuje moment w czasie -> odowłując się do 1 January 1970 UTC

  **Metody**

  `Date.now()` - wartość liczbowa aktualnego czasu

  `Date.pars()` - "Zwraca liczbę milisekund, które upłynęły od 1 stycznia 1970, 00:00:00 czasu lokalnego do daty podanej jako argument string."

    Date.parse("Wed, 09 Aug 1995 00:00:00");
    // Zwraca 807937200000 w strefie czasowej GMT-0300, a inne wartości w innych

  `Date.UTC()` - "Zwraca liczbę milisekund, które upłynęły od 1 stycznia 1970, 00:00:00 czasu uniwersalnego do daty podanej jako zestaw liczb"

    const utcDate1 = new Date(Date.UTC(96, 1, 2, 3, 4, 5));
    console.log(utcDate1.toUTCString());
    // expected output: Fri, 02 Feb 1996 03:04:05 GMT


  **Instancje obiektu Date (wybrane)**

**Metody**

`Date.prototype.getDate()` - zwraca dzień miesiąca podanej daty

    const birthday = new Date('August 19, 1975 23:15:30');
    const date1 = birthday.getDate();

`.getDay()` - zwraca dzień tygodnia

`.getFullYear()` - rok

`.getHours()` - godzinę

`.getMinutes()` - minuty

`.getMonth()` - miesiąc

`.getTime()` - zwraca aktualny czas w milisekundach

*Setters - pozwalają na zdefiniowanie czasu*

`.setTime()`, `setMinutes()` etc

---

### Przetwarzanie tekstu

`String` - łańcuch znaków

`RegExp` - obiekt wyrażeń regularnych, zawiera wzór regularnego wyrażenia -> znalezienie lub zmianę ciągu znaków w innym ciągu znaków

### Indeksowanie kolekcji

Array

Int8Array

Uint8Array

Uint8ClampedArray

Int16Array

Uint16Array

Int32Array

Uint32Array

Float32Array

Float64Array

### Kolekcje z kluczami

Map

Set

WeakMap

WeakSet

---
### Kolekcje wektorowe

---

### Dane strukturalne

ArrayBuffer

SharedArrayBuffer 

Atomics 

DataView

JSON

---

### Kontrola obiektów abstrakcyjnych

Promise

Generator

GeneratorFunction

AsyncFunction

---

### Refleksy

### Internacjonalizacja

### WebAssembly

---

### Pozostał

arguments



Źródła:

https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Obiekty
