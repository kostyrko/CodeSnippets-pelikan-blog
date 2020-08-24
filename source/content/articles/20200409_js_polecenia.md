Title: JavaScript - polecenia
Author: mkostyrko
Date: 2020-04-09 08:00
Updated:
Category: javascript
Tags: javascript, js, polecenia
Slug: js-polecenia
related_posts: 

### Kontroli przepływu

block

break

continue

empty

if/if else/else - podstawowa instrukcja warunkowa 

swith - instrukcja warunkowa biorąca pod uwagę zachowanie się kodu zależnego od wariacji zmiennej



throw - ma za zadanie zwrócić zdefiniowane przez użytkownika wyjątek i zatrzymuje wykonywanie się kodu

Przykładowe zastosowanie: 


    fetch("https://jsonplaceholder.typicode.com/posts/2")
        .then(response => {
            if (response.ok) {
                return response.json()
            } else {
                throw new Error("Błąd sieci")
            }
        })


**try...catch** - instrukcja obsługi wyjątków - instrukcja **try** pozwala na zdefiniowanie wykonywania się kodu w przypadku przypadku jego nie powodzenia wykonywanie się programu powinno zostać wyłapane przez instrukcję **catch** i zostanie wywołany kod w niej zawarty

---

### Deklaracje

**var**/**const**/**let** - słowa kluczowe poprzedzające deklarację zmiennej oraz definiujące jej rodzaj

---

### Funkcji i klas

**function** - słowo kluczowe poprzedzające deklarację funkcji


**async function** - funkcja asynchroniczna - wykorzystuje obiekt Promise do zwrócenia wyniku

**return** 

**class** - słowo kluczowe wstępujące przez zdefiniowaniem klasy (od JS >= ES6) -> więcej na ten temat: [JavaScript - klasy](https://kostyrko.github.io/zfrontu/js-klasy.html)

---

### Iteracji

[Patrz tutaj](https://kostyrko.github.io/zfrontu/js-for-while-loop.html)

---

### Inne

**debugger** - wyrażenie uruchamiające funkcjonalność debuggowania/ kod przestaje się wywoływać gdy dotrze do instrukcji debuggera

**export** - słowo kluczowe poprzedzające deklarację eksport części kodu

**import**  - słowo kluczowe poprzedzające deklarację importu części kodu z pliku

**lable**

---


Źródła:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

https://mathjs.org/

