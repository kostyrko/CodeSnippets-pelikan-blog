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

    class Greeter {
      greeting: string;

      constructor(message: string) {
        this.greeting = message;
      }

      greet() {
        return "Hello, " + this.greeting;
      }
    }

    let greeter = new Greeter("world");

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


    class Person {
        #name: string
        
        constructor(name: string) {
            this.#name = name;
        }

        greet() {
            console.log(`Hello, my name is ${this.#name}!`);
        }
    }

    let jeremy = new Person("Jeremy Bearimy");

    jeremy.#name
    //     ~~~~~
    // Property '#name' is not accessible outside class 'Person'
    // because it has a private identifier.

Private fields start with a # character. Sometimes we call these private names.
Every private field name is uniquely scoped to its containing class.
TypeScript accessibility modifiers like public or private can’t be used on private fields.
Private fields can’t be accessed or even detected outside of the containing class – even by JS users! Sometimes we call this hard privacy.

    class Animal {
      private name: string;

      constructor(theName: string) {
        this.name = theName;
      }
    }

    new Animal("Cat").name;
    Property 'name' is private and only accessible within class 'Animal'.

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