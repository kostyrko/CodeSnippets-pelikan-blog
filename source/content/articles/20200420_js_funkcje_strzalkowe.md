Title: JavaScript -> funkcje strzałkowe
Author: mkostyrko
Date: 2020-04-20 10:00
Updated:
Category: javascript
Tags: javascript, js, arrow functions, funkcja strzałkowa
Slug: js-funckja-starzalkowa
related_posts: js-funkcja

Funkcja starzałkowa skaraca zapis i.. nie zmienia kontekstu `this`

* słowo kluczowe `function` zmienia się w strzałkę `=>`

schemat:

        const show = function () {...};

        const show = () => {...};

* w przypadku **tylko** jednego parametru można pominąć nawiasy / nawis pozostaje gdy funkcja nie ma parametru lub więcej niż 1
* jeśli funkcja jedynie zwraca to można pominąć instrukcję `return`

        const multiply = function(a) {
            return a * a;
        }
        
        const multiply = a => a * a;

* jeżeli funkcja zwraca jedną instrukcję można pominąć klamry

        const multiply = (a,b) => {
                const result = a * b;
                return result
            }

* jeżeli funkcja zwraca literał obiektu należy zamknąć ją w nawiasie

        const retObject = function() {
        return { team : "Kasztany", score : 0 }
        }

        const retObject = name => ({ team : "Kasztany", score : 0 })
        const retObject = () => ({ team : "Kasztany", score : 0 })


Źródła:

http://kursjs.pl/kurs/es6/funkcja-strzalkowa.php


https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html

http://www.algosmart.pl/powtorka-przed-reactjs-1-funkcje-strzalkowe

