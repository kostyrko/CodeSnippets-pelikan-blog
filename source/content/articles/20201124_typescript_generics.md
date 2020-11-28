Title: TypeScript: typy generyczne
Author: mkostyrko
Date: 2020-11-24 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-generics
related_posts: typescript-wprowadzenie

![typescript-logo](https://miro.medium.com/max/700/1*Sy-lk-CZlnc2szy0SPsLEQ.jpeg)


### Typy generyczne ("dynamiczne") wprowadzenie

Tablica w TS również jest typem (podobnie jak np. obiekt) i do tego **generycznym** (dopasowuje się do danych, które przechowuje)

`const names: Array = []` // Array<T>/ przedstawiony tutaj zapis faktycznie nie zostanie przyjęty przez TS, który będzie domagał się podania jakiegokolwiek typu np. **any** -> `const names: any[] = []` ten zapis jednak można przedstawić również w następujący sposób `const names: Array<any> = []`

### Typy generyczne <T>

Typ generyczny (generować/tworzyć) - jest typem o szerokim polu zastosowania/akceptuje różne typy argumentów.

Funkcja identyfikacyjna typu generycznego. Przyjmuje określony dowolny typ i zwraca ten sam typ ( w przypadku zastosowania **eny** typ zwracany mógłby być inny niż ten, który jest argumentem - tracona jest informacja o typie)

    function identity<T>(arg: T): T {
      return arg;
    }

**Funkcja identyfikacyjna** - zwraca to co zostało podane jako argument

**<T>** litera **T** zamknięta w nawiasach kątowych jest zwyczajowa (T-type) faktycznie może być inna i w niektórych przypadkach jest ona inna (reprezentuje konkretny typ, zatem w przypadku stosowania 2 typów, potrzebne są 2 symbole, wg konwencji kolejnym z nich jest **U**) - reprezentuje ona zmienną, która pozwala przechwycić typ.


**Wywołanie funkcji identyfikacyjnej typu generycznego**

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


Wskazanie argumentów o różnych typach / w przypadku wskazania jedynie typu obiekt TS nie połączy obiektów tylko stworzy inny

    function join<T, U> (objX: T, objY: U) {
      return Object.assign(objX, objY)
    }

    // jako arg używane są obiekty zawierające string i nr a nie wartość "string" i "number"
    const jointObj = join({name: 'C3PO'}, {moviesNum: 9})

    // można to również zapisać w tej postaci - jest to jednak o tyle zbędne,  że TS sam za nas odczyta strukturę wpisanych obiektów
    const jointObj = join<{name: string},{movies: number}>({name: 'C3PO'), {moviesNum: 9})

---
### Constrains - ograniczenie


    // funkcja join przyjmuje jedynie obiekty, za to ich zawartość nie jest zdefiniowana
    function join<T extends object, U extends object> (objX: T, objY: U) {
          return Object.assign(objX, objY)
        }

    // funkcja join przyjmuje jedynie obiekty
    const jointObj = join({name: 'C3PO'}, {moviesNum: 9})


Tworzenie ograniczenia na podstawie interfejsu

    interface Droid {
      length: number
    }

    zwraca krotkę/tuple
    function count<T extends Droid> (elem: T): [T, number]  {
      return [element, elem.length]
    }

    console.log(['R2D2';'C3PO']) // Array,2



`keyof` - jakikolwiek klucz z T


    function getKey<T extends object, U extends keyof T> (obj: T, key: U) {
      return obj[key]
    }

    // funkcja join przyjmuje jedynie obiekty
    const jointObj = join({name: 'C3PO'}, {moviesNum: 9})

    getKey({name: 'C3PO'}, 'name')


---

### Typ/funkcja Generyczne

Tworzenie funkcji/typu generycznego jest zbliżone do interfejsów


    function droid<T>(arg: T): T {
      return arg;
    }

    let myDroid: <T>(arg: T) => T = droid;


Typ generyczny napisany przypisany do postaci obiektu (patrz niżej interfejs)

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

Stworzenie klasy generycznej pozwala na dynamiczne przypisanie typu do jej instancji

    class GenericNumber<T> {
      zeroValue: T;
      add: (x: T, y: T) => T;
    }

    // przypisanie typu do instancji
    let myGenericNumber = new GenericNumber<number>();

    // przypisanie wartości
    myGenericNumber.zeroValue = 0;
    
    // przypisanie metody do instancji
    myGenericNumber.add = function (x, y) {
      return x + y;
    };


Kolejny przykład

    class DataArr<T extends string | numbers> {
      private data: T[]: [];

      addItem(item:T){
        this.data.push(item)
      }

      getItems() {
        return [...this.data]
      }
    }

    instancja-1
    const textStorage = new DataArr<string>();
    textStorage.addItem('C3PO')

    instancja-2
    const numberStorage = new DataArr<number>();
    textStorage.addItem(1)


---

Źródło: 

[TypeScript - Generics](https://www.typescriptlang.org/docs/handbook/generics.html)

[TypeScript: Tworzenie podtypów warunkowych](https://bulldogjob.pl/articles/1019-typescript-tworzenie-podtypow-warunkowych)

[TypeScript - Generics, klasy i zaawansowane typy](https://www.frontlive.pl/typescript-sredniozaawansowany/)

[TypeScript – pierwsze kroki. Typy generyczne.](http://jsdn.pl/typescript-typy-generyczne/)

[TypeScript – typy generyczne](https://kamilmysliwiec.com/typescript-typy-generyczne)