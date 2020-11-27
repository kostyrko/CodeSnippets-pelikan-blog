Title: TypeScript: klasy
Author: mkostyrko
Date: 2020-11-25 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-klasy
related_posts: react-wprowadzenie

![typescript-logo](https://refactoring.guru/images/patterns/languages/typescript.png)

Klasy w TypeScript nie różnią od klas w JS ES6

TS transpiluje do klasy jeśli wybrany jest standard ES6 lub nowszy albo do funkcja konstruktora dla ES5 i starszych (symuluje klasy choć jest funkcją (egzekucja podobna do klas))

---
### Przykładowa klasa

constructor - funkcja wykonywana w trakcie inicjalizacji/tworzenia obiektu

    class Droid {
      name: string; // tak samo w JS powyżej ES6

      constructor(message: string) {
        this.greeting = message;
      }

      greet(this: Greeter) { // odwołanie do instancji, które powstała na podstawie klasy Droid
        return "Hello, " + this.name;
      }
    }

    let r2d2 = new Droid("R2D2"); // -> arg zapisuje jako name

    const r2d2Copy = { name: 'C3PO', greet : r2d2.greet}

`this` - jest kontekstem, w zależności od miejsca, w którym się do niego odwołujemy może odnosić się do czegoś innego, w przypadku klas zwykle odnosi się do instancji klasy lub inaczej to ujmując do tego obiektu, na którym dana metoda jest wywoływana

---
### Dziedziczenie

    class Animal {
      move(distanceInMeters: number = 0) {
        console.log(`Animal moved ${distanceInMeters}m.`);
      }
    }

    class Dog extends Animal {
      bark() {
        console.log("Woof! Woof!");
      }
    }

    const dog = new Dog();
    dog.bark();
    dog.move(10);
    dog.bark();

---
### Prywatne pola (Private)


    class Planet {
        private name: string  // oznaczenie prywatności sposób prywatyzacji
        private droids: string[] = [] // to jest również oznaczenie prywatności
        
        constructor(name: string) {
            this.#name = name;
        }

        greet() {
            console.log(`This is ${this.#name}!`);
        }

        addDroid(droid: string){
          this.droids.push(droid);
        }

        printDroids() {
          console.log(this.droids)
        }
    }

    let coruscant = new person("Coruscant");
    coruscant.addDroid('Crime Scene Analysis Droid')

    coruscant.droids[1]=('Swtor MCR-99 Droid') // error - droids jest prywatnym polem i jego zmiana (dodanie nowej wartości to tablicy jest możliwe jedynie przy pomocy jednego sposobu, wywołanie odpowiedniej metody).

Prywatne poleca sprawia, że jego edycja jest możliwa jedynie przy pomocy przeznaczonej do tego metody. To może się przydać szczególnie w momencie gdy dana metoda zawiera w sobie zdefiniowaną walidację (bezpośrednia edycja może być jej pozbawiono). w JS wszystkie pola są `publiczne/public` w TS,  jeśli nie są inaczej oznaczone również takie są domyślnie. Prywatne pola są również ukryte po za klasą (nie są dostępne).


więcej na ten temat: [ECMAScript Private Fields](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8-beta/#ecmascript-private-fields)

---
### Chronione pola (protected)

    class Person {
      protected name: string;
      constructor(name: string) {
        this.name = name;
      }
    }

    class Employee extends Person {
      private department: string;

      constructor(name: string, department: string) {
        super(name);
        this.department = department;
      }

      public getElevatorPitch() {
        return `Hello, my name is ${this.name} and I work in ${this.department}.`;
      }
    }

    let howard = new Employee("Howard", "Sales");
    console.log(howard.getElevatorPitch());
    console.log(howard.name);
    Property 'name' is protected and only accessible within class 'Person' and its subclasses.

---
### Tylko do odczytu 


    class Octopus {
      readonly name: string;
      readonly numberOfLegs: number = 8;

      constructor(theName: string) {
        this.name = theName;
      }
    }

    let dad = new Octopus("Man with the 8 strong legs");
    dad.name = "Man with the 3-piece suit";
    Cannot assign to 'name' because it is a read-only property.


---

[TypeScript - Generics, klasy i zaawansowane typy](https://www.frontlive.pl/typescript-sredniozaawansowany/)

[The Catalog of TypeScript Examples](https://refactoring.guru/design-patterns/typescript)

JS

[SO - Javascript classes vs typescript classes](https://stackoverflow.com/questions/54841417/javascript-classes-vs-typescript-classes)

[JavaScript Object Constructors](https://www.w3schools.com/js/js_object_constructors.asp)