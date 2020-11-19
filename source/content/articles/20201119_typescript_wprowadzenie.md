Title: TypeScript
Author: mkostyrko
Date: 2020-11-14 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-wprowadzenie
related_posts: react-wprowadzenie

![typescript-logo](https://www.positronx.io/wp-content/uploads/2018/11/positronx-banner-1152-1.jpg)

TypeScript jest supersetem JavaScript

1. Statyczne typowanie - kompilator sprawdza błędy przed wykonaniem kodu (jest to opcjonalne, dopiero gdy typowi )

### Instalacja i użytkowanie -> "Hello world"

    // terminal
    npm i -g typescript

Należy stworzyć plik **index.ts**

    // index.ts
    console.log('Hello world');

Następnie w terminalu wywołać komendę odwołującą się do TS i wskazującą na plik

    tsc index.ts

W folderze pojawi się nowy plik js po transpilacji -> `index.js` jego zawartość jest w JS/ES3 (w tym przypadku treść będzie taka sama)

W celu wprowadzenia zmian w zachowaniu kompilatora można dodać flagi do komendy do niego się odwołującej w terminalu lub zawrzeć odpowiednie informacje w osobnym pliku `tsconfig.json`

        //tsconfig.json
        {
            "compilerOptions": {
                "target": "esnext", // kompilacja do najnowszej wersji JS
                "watch": true, // nasłuchiwanie na zmiany i kompilacja
                "lib": ["dom", "es2017"] // biblioteki np. "pilnujące" poprawności z klasami/obiektami DOM - trakcie pisania kodu
            }
        }

### Pisanie kodu w sposób domniemany (implicit)

    let num = 23 // type: number

    // nie jest możliwe bo wcześniej zadeklarowane jest number
    num = '22'

Podobnie

    let num
    num = 22
    num = '33' // będzie niepoprawne ponieważ inny typ został wyżej przypisany

### Pisanie kodu w sposób wskazany

    let num:number // wskazanie typu bez przypisania wartości

let może odnosić się jedynie do liczb jeśli typ został zadeklarowany

### "Strong typing" tworzenie własnych typów

Tworzenie własnego **typu** - Zmienna

    type Style = 'bold' | 'italic'

    let font: Style;

    font = 'cursive' // błąd ponieważ może być jedynie 'bold' albo 'italic'

**Interface** - tworzenie wzoru Obiektów

    interface Droid {
        first: string; // wypełnienie podanych tutaj kluczy jest obowiązkowe
        class: string;
        [key: string]: any // pozostawia furtkę na dodanie ew. kluczy
    }

    const droid: Droid = {
        name: 'C3PO',
        class: 'Protocol'
    }

    const droid2: Droid = {
        name: 'R2-D2',
        type: 'Astromech droid',
        planet: 'Naboo'
    }

**Funkcje**

Pilnuje, żeby jako arg. podana była jedynie liczba

    function pow (x: number, y: number) {
        return March.pow(x,y)
    }

Pilnuje, żeby jako arg. podana była jedynie liczba ale zwraca wartość w postaci `stringa` - wymaga wskazania **toString()**

    function pow (x: number, y: number):string {
        return March.pow(x,y).toString()
    }


Używa się `void` w przypadku braku zwracania wartości

    function pow (x: number, y: number):void {
        March.pow(x,y).toString()
    }


**Tablice**

// wskazanie tablicy przechowującej jedynie liczby

    const arr:number[] = []
    arr.push(1)
    arr.push('23') // error
    arr.push(false) // error

// wskazanie tablicy, która przyjmuje jedynie obiekty powstałe na podstawie wcześniej wskazanego wzoru Droid/interfejsu

    const arr: Droid[] = []

**Krotki**

// dodanie **znaku zapytania -> ?** sprawia, że są to wartości opcjonalne

    type MyList = [number?, string?, boolean?]

**Generics**

Stosowane wtedy kiedy chcemy użyć typu albo funkcji wewnątrz klasy

    class Observable<T> {
        constructor(public value: T) {}
    }

    let x: Observable<number>

    let y: Observable<Droid>

    let z = new Observable(23)


---

Źródła:

[TypeScript for JavaScript Programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)

[The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

[Basic Types](https://www.typescriptlang.org/docs/handbook/intro.html)

[A beginner’s guide to TypeScript (with some history of the TypeScript)](https://medium.com/jspoint/typescript-a-beginners-guide-6956fe8bcf9e)

YT

[Fireship -> TypeScript - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM&t=1s&ab_channel=Fireship)

[React i TypeScript - jak zacząć? | Przeprogramowani.ts #7](https://www.youtube.com/watch?v=nRdR6xAgGvw)

[TypeScript Course for Beginners 2020 - Learn TypeScript from Scratch!](https://www.youtube.com/watch?v=BwuLxPH8IDs)
