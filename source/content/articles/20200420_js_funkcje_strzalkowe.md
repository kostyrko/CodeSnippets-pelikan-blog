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

::: jeśli funkcja jedynie zwraca to można pominąć instrukcję `return` - tzw. domniemany zwrot/return :::

::: można również pominąć `{}` w przypadku gdy istnieje tylko jedna linia kodu :::

        const multiply = function(a) {
            return a * a;
        }
        
        const multiply = a => a * a;

        const waterPlant = day => day === 'Tuesday' ? true : false;

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


Przykłady:

        function getNumber (num,arr) {
        const newArr = arr.filter((item)=> {return item === num});
        return (newArr[0] === num ? true : false);
        }
        
        zamiast

        function getNumber (num,arr) {
                const newArr = arr.filter(function(item) {
                return item === num;
                });
                if (newArr[0] === num) {
                        return true
                }
                else {
                        return false
                }
        };

**::: warto pamiętać żę funkcja strzałkowa jest zadeklarowana poprzez wyrażenie funkcyjne i oznacza, to że zmienia kontekst `this` co może być szczególnie istotne w kontekście manipulowania elementami DOM (wówczas `this` jest obiektem `window`) :::**



---

Źródła:

http://kursjs.pl/kurs/es6/funkcja-strzalkowa.php


https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html

http://www.algosmart.pl/powtorka-przed-reactjs-1-funkcje-strzalkowe

