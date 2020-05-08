Title: JavaScript - konstruktor, prototyp i dziedziczenie
Author: mkostyrko
Date: 2020-04-28 10:00
Updated:
Category: javascript
Tags: javascript, js
Slug: js-konstruktor-prototyp-dziedziczenie
related_posts: js-this

Funkcja konstruktora pozwala na stworzenie wielu obiektów według zdefiniowanego schematu, który jest nazywany prototypem

Nazwa funkcji konstruktora często zaczyna się od dużej litery

Schemat:

      function NazwaFunkcji (właściwość) { // zdefiniowanie konstruktora, przekazanie właściwości
            this.atrybut1 = właściwość; //
            this.atrybut2 = function(argument) {  // funkcja zawarta w ramach obiektu stająca się metodą obiektu
                  console.log(this.atrybut1); // przykłądowe wyrażenie/wywołujące obiekt
            }
      }

Korzystanie z funkcji - tworzenie nowego obiektu (musi być poprzedzonę słowem kluczowym `new`)

      const nazwaZmiennej = new nazwaFunkcji('argument')

      console.log(nazwaZmiennej)

      >> nazwaFunkcji { atrybut1:"argument", atrybut2: {...}}

      console.log(nazwaZmiennej.atrybut2()) // wywołanie metody

      >> właściwość // wartość przypisana do atrybut1 tego wywoływanego obiektu


Przykładowa funkcja konstruktora - tworzenie obiektu Person

      function Person (name) {
            this.name = name;
      }

słowo kluczowe `this` odwołuje się do aktualnej instancji/wywołania obiektu

Wywołanie funkcji

      const mike = new Person(mike)
      console.log(mike)
      >> Person{name:"mike"}

---

Słowo kluczowe `this` odwołuje się do aktualnej instancji/wywołania obiektu. Przykładowo w tym przypadku this jest wywoływanym obiektem `mike`

      function Person (name) {
            this.name = name;
            console.log(this);
      }

      const mike = new Person(mike)
      >> Person{name:"mike"}

`this` wywołane po za funkcją zwraca obiekt window

      console.log(this)
      >> Window { frames, Window....}

---

Aby zmieniać właściwości prototypów należy wykorzystać słowo kluczowe `.prototype ` (będzie to miało wpływ na wszystkie stworzone na jego podstawie obiekty - jego instancji!!!)

Dodawanie nowej przypisanej właściwości

Funkcja wyjściowa

      function Person (name) {
            this.name = name;
      }

Dodanie właściwości

      Person.prototype.type = "human"
      console.log(mike.type) // wywołanie
      >> human

Ale -> 

      console.log(mike)
      >> Person {name:"mike"} // brak właściwości `type`
      console.log(mike.type);
      >> human


Dodawanie nowej metody

      Person.prototype.showName = function() { return this.name}

      console.log(mike.showName());
      >> mike // wywołuje funkcję
      console.log(mike.showName);
      >> function(){return this.name;} // zwraca funkcję

---
Przykładowa funkcja konstruktora zwracająca wiek

      function Droid(name, constDate) {
      this.name = name;
      // this.age = age;
      this.birthday = new Date(constDate);
      this.calculateAge = function(){
      const diff =  Date.now() - this.birthday.getTime();
      const ageDate = new Date(diff);
      return Math.abs(ageDate.getUTCFullYear() - 1970);
      }
      }

      const c3po = new Droid('C3PO', '2-2-2222');
      console.log(c3po.calculateAge());

---

JS - zawiera wiele funkcji konstruktorów, które pozwalają na stworzenie obiektów według wcześniej zdefiniowanych prototypów

new String(), new Boolean(), new Number(), new Array()

Wbudowana funkcja konstrukcyjna dla tablic

      const arr = new Array(22,33,44)
      console.log(arr) // [22,33,44]



Źródła:

https://developer.mozilla.org/pl/docs/Web/JavaScript/Guide/Obsolete_Pages/Przewodnik_po_j%C4%99zyku_JavaScript_1.5/Tworzenie_nowych_obiekt%C3%B3w/Zastosowanie_konstruktor%C3%B3w_funkcji

http://kursjs.pl/kurs/obiekty/konstruktor.php

https://www.udemy.com/course/modern-javascript-from-the-beginning/