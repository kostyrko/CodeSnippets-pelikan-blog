Title: TypeScript: typy generyczne
Author: mkostyrko
Date: 2020-11-24 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-generics
related_posts: typescript-wprowadzenie

![typescript-logo](https://miro.medium.com/max/700/1*Sy-lk-CZlnc2szy0SPsLEQ.jpeg)

### Typy generyczne <T>

Typ generyczny (generować/tworzyć) - jest typem o szerokim polu zastosowania/akceptuje różne typy argumentów.

Funkcja identyfikacyjna typu generycznego. Przyjmuje określony dowolny typ i zwraca ten sam typ ( w przypadku zastosowania **eny** typ zwracany mógłby być inny niż ten, który jest argumentem - tracona jest informacja o typie)

    function identity<T>(arg: T): T {
      return arg;
    }

**Funkcja identyfikacyjna** - zwraca to co zostało podane jako argument

**<T>** litera **T** zamknięta w nawiasach kątowych jest zwyczajowa (T-type) faktycznie może być inna i w niektórych przypadkach jest ona inna (reprezentuje konkretny typ, zatem w przypadku stosowania 2 typów, potrzebne są 2) - reprezentuje ona zmienną, która pozwala przechwycić typ.


Wywołanie funkcji identyfikacyjnej typu generycznego

    // explicit - w sposób sprecyzowany
    let output = identity<string>("myString");

    // explicit - w sposób domyślny
    let output = identity("myString");

---

Typ generyczny może określać przyjęcie tablicy (wówaczas w funkcji istnieje możliwość odwołania się do metod, które są przypisane tablicom np. length). Funkcja przyjmuje jako argument tablicę, która składa się z określonych typów

    function loggingIdentity<T>(arg: T[]): T[] {
      console.log(arg.length);
      return arg;
    }

Powyższą funkcję można również zapisać w następujący sposób

    function loggingIdentity<T>(arg: Array<T>): Array<T> {
      console.log(arg.length); // Array has a .length, so no more error
      return arg;
    }

---

### Typ/funkcja Generyczne

Tworzenie funkcji/typu generycznego jest zbliżone do interfejsów


    function droid<T>(arg: T): T {
      return arg;
    }

    let myDroid: <T>(arg: T) => T = droid;


Typ generyczny napisany przypisany do postaci obiektu (patrz niżej intefejs)

    function identity<T>(arg: T): T {
      return arg;
    }

    let myIdentity: { <T>(arg: T): T } = identity;


**generyczny interfejs**

    interface GenericIdentityFn {
      <T>(arg: T): T;
    }

    function identity<T>(arg: T): T {
      return arg;
    }

    let myIdentity: GenericIdentityFn = identity;


Przesunięcie generycznego parametru całości interfejsu


    interface GenericIdentityFn<T> {
      (arg: T): T;
    }

    function identity<T>(arg: T): T {
      return arg;
    }

    let myIdentity: GenericIdentityFn<number> = identity;

---

### Klasy Generyczne

    class GenericNumber<T> {
      zeroValue: T;
      add: (x: T, y: T) => T;
    }

    let myGenericNumber = new GenericNumber<number>();

    myGenericNumber.zeroValue = 0;
    
    myGenericNumber.add = function (x, y) {
      return x + y;
    };



---

Źródło: 

[TypeScript - Generics](https://www.typescriptlang.org/docs/handbook/generics.html)

[TypeScript: Tworzenie podtypów warunkowych](https://bulldogjob.pl/articles/1019-typescript-tworzenie-podtypow-warunkowych)

[TypeScript - Generics, klasy i zaawansowane typy](https://www.frontlive.pl/typescript-sredniozaawansowany/)

[TypeScript – pierwsze kroki. Typy generyczne.](http://jsdn.pl/typescript-typy-generyczne/)

[TypeScript – typy generyczne](https://kamilmysliwiec.com/typescript-typy-generyczne)