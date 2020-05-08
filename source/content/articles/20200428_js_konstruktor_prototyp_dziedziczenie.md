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

Aby zmieniać właściwości konstruktorów można  słowo kluczowe `.prototype ` (będzie to miało wpływ na wszystkie stworzone na jego podstawie obiekty - jego instancji!!!) i edytować prototyp danej funkcji

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
      >> Person {name:"mike"} // brak właściwości `type` chociaż w konsoli zwróci również info następującego typi ->
       __proto__ :
            type: "human"

      console.log(mike.type);
      >> human

Pojawić się również powinna wiadomość na temat prototypu obiektu

      __proto__: Object
      np. hasOwnProperty: f

      console.log(mike.hasOwnProperty('name'))
      >> true

Ale:

      console.log(mike.hasOwnProperty('type'))
      >> false // ponieważ należy do prototypu, a nie właściwości obiektu (konstruktora)



Dodawanie nowej metody

      Person.prototype.showName = function() { return this.name}

      console.log(mike.showName());
      >> mike // wywołuje funkcję
      console.log(mike.showName);
      >> function(){return this.name;} // zwraca funkcję


---

JS - zawiera wiele funkcji konstruktorów, które pozwalają na stworzenie obiektów według wcześniej zdefiniowanych prototypów

`new String()`, `new Boolean()`, `new Number()`, `new Array()`, `new Function()`, `new Object()`, `new RexExp()` - regular expression

::: warto pamiętać o tym, że w ten sposób tworzy się obiekty a nie typy prymitywne choć wywołanie go odbywa się w taki sam sposób jak przy typie prymitywnym/podstawowym :::

Wbudowana funkcja konstrukcyjna dla tablic

      const arr = new Array(22,33,44)
      console.log(arr) // [22,33,44]

Funkcji

      const func = new Function('x', 'y', 'return x + y')
      console.log(func(1,1))
      >> 2

Obiekt

      const obj = new Object({name: "r2d2"})

---

Prototypy - każdy obiekt ma swój prototyp, który również jest obiektem i dziedziczy z niego metody oraz właściwości

Object.prototype

Przykładowa funkcja konstruktora zawierająca funkcję liczenia wieku

      function Droid(name, constDate) {
      this.name = name;
      this.birthday = new Date(constDate);
      this.showAge = function(){
            const diff =  Date.now() - this.birthday.getTime();
            const ageDate = new Date(diff);
            return Math.abs(ageDate.getUTCFullYear() - 1970);
            }
      }

      const c3po = new Droid('C3PO', '2-2-2222');
      console.log(c3po.showAge());

Każdy ze stworzonych obiektów na podstawie tego konstruktora, również zawiera w sobie tą funkcję
aby tego uniknąć można zadeklarować funkcję po za konstruktorem, wówczas zostanie ona zapisana do prototypu ale nie przypisana do każdego utworzonego obiektu

      function Droid(name, constDate) {
      this.name = name;
      this.birthday = new Date(constDate);
      }

      Droid.prototype.showAge = function(){
            const diff =  Date.now() - this.birthday.getTime();
            const ageDate = new Date(diff);
            return Math.abs(ageDate.getUTCFullYear() - 1970);
      }

Standard ES6 wprowadza również możliwość zadeklarowania klasy, której skutek będzie zbliżony

      class Droid {
            constructor(name, constDate) {
                  this.name = name;
                  this.constDate = constDate
            }

            showName() {
                  return `Hello ${this.name}`
            }
      }

      const c3po = new Droid('c3po', '2222')

      console.log(c3po)

      >> Droid {name: "c3po", constDate: "2222"}
            constDate: "2222"
            name: "c3po"
                  __proto__:
                  constructor: class Droid
                  showName: ƒ showName()
                  __proto__: Object

---

### Dziedziczenie



      function Robot (name) {
            this.name = name;
      }

Dodanie funkcji w prototypie konstruktora Robot

      Robot.prototype.greeting = function(){
            return `hello ${this.name}`;
      }

Konstruktor droid, który dziedziczy właściwości konstruktora Robot

      function Droid(type) {
            Robot.call(this, name)
            this.type = type
      }

**:::`.call()` - funkcja call pozwala na wywołanie funkcji z innego kontekstu:::**

aby zapewnić dziedziczenie prototypie należy to zaznaczyć w innym przypadku nie będzie to możliwe

      Droid.prototype = Object.create(Robot.prototype)

**Object.create - metoda, która pozwala na przekazanie dziedziczenia prototypu, te mogą być nadpisana nową metodą o tej samej nazwie.**
**Ta metoda tworzy nowy obiekt, korzystając z istniejących obiektów jako jej prototypu stąd:**

Należy zdefiniować używanie konstruktora z Droida, w innym przypadku zostanie on odziedziczony

      Droid.prototype.constructor = Droid;

---

Źródła:

https://developer.mozilla.org/pl/docs/Web/JavaScript/Guide/Obsolete_Pages/Przewodnik_po_j%C4%99zyku_JavaScript_1.5/Tworzenie_nowych_obiekt%C3%B3w/Zastosowanie_konstruktor%C3%B3w_funkcji

http://kursjs.pl/kurs/obiekty/konstruktor.php

https://www.udemy.com/course/modern-javascript-from-the-beginning/