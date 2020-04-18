Title: JavaScript - obiekty
Author: mkostyrko
Date: 2020-04-14
 10:00
Updated:
Category: javascript
Tags: javascript, js, array
Slug: js-obiekty
related_posts: js-podstawowe-typy, js-tablice


Programowani obiektowego uczyłem się na podstawie Pythona i początkowo miałem problem z uchwyceniem konceptu, zrozumienie obiektu w JavaScript okazało się być czymś prostszym (przypomina pythonowy słownik na sterydach - choć faktycznie bliżej mu do obiektu znanego mi z tego języka, sam jednak zapis jest mniej skomplikowany - tam tworzy się tzw klasy).

Obiekty zawierają właściwości, którymi są pary składające się z klucza i przypisanych im wartości, owymi wartościami mogą być wszystkie prymitywne typy, jak i tablice czy funkcje - te rozdzielone są przecinkami. Kolokacje te (key-value pairs) są rozdzielone dwukropkiem. Obiekt zadeklarowany jest poprzez użycie słowa kluczowego jak przy innych zmiennych `let` lub `const` oraz poprzez zastosowanie nawiasów klamrowych.

    const person = {
    name: 'Mikołaj',
    age: 99,
    animals : ["cat","dog"],
    sayHello: function() {
      console.log("hello Mikolaj")
    }
    };

    person.sayHello()
    > hello Mikolaj

    console.log(person.animals[1])
    > dog

Odwołujemy się do poszczególnej wartości poprzez przywołanie nazwy obiektu oraz właściwości po kropce lub funkcji otwierając i zamykając nawias. Alternatywnie można stosować kwadratowe nawiasy np. `person["animals"]`

Dodawanie nowych par klucza-wartości odbywa się w podobny sposób jak w przypadku tablic

    person.height = 1.8
    // lub:
    person['gender'] = "male"

    console.log(person)
    > {name: 'Mikołaj',age: 99,animals : ["cat","dog"],
    sayHello: function() {console.log("hello Mikolaj"), 
    height: 1.8, gender : "male"}

Poprzez odwołanie się do słów kluczowych `delete` istnieje możliwość usunięcia wybranych właściwości obiektu

    delete person.height
    > true // zwraca false - jeśli nie jest to możliwe
    delete person['gender']
    > true
    console.log(person)
    > {name: 'Mikołaj',age: 99,animals : ["cat","dog"],
    sayHello: function() {console.log("hello Mikolaj")}

Zmiana wartości, przypisanej do klucza odbywa jest prosta i również zbliżona do tego co znane jest z tablicy, jednak zamiast odwoływać się do pozycji indeksowej, należy odwołać się do klucza

    person.name = "Michał"
    console.log(person)
    > {name: 'Mikołaj',age: 99,animals : ["cat","dog"],
    sayHello: function() {console.log("hello Mikolaj")}

W wewnętrznej funkcji obiektu można odwołać się do wartości przypisanych do kluczy w niej zawartej w dwojaki sposób odwołując się do klucza lub słowa kluczowego `this` (który odwołuje się do obiektu okna)

    const person2 = {
      name: 'Mike',
      sayHello: function() {
        console.log(`hello ${this.name}`) // lub person2.name > hello Mike
      }
      };

---

### Prototypy

Obiekty mogą dziedziczyć elementy z innych obiektów. Prototypem nazywany wówczas jest obiekt, który jest "dawcą"

---


Źródła:

https://launchschool.com/books/javascript/read/objects#whatareobjects

https://www.youtube.com/watch?v=qs3F-z6ridc

https://dev.to/valentinogagliardi/the-secret-life-of-javascript-objects-2a33