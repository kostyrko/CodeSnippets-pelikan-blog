Title: TypeScript: wprowadzenie + podstawowe typy
Author: mkostyrko
Date: 2020-11-19 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-wprowadzenie
related_posts: react-wprowadzenie

![typescript-logo](https://raw.githubusercontent.com/basarat/typescript-book/master/images/venn.png)

TypeScript jest supersetem (nadzbiorem) JavaScript - oznacza to, że jest swego rodzaju "rozszerzeniem" JS posiadającym własne reguły (nowe możliwości) ale ulega kompilacji do JS.

**TS wprowadza/charakteryzuje**

1. Statyczne typowanie - kompilator sprawdza błędy przed wykonaniem kodu (jest to opcjonalne, dopiero gdy typowi )

2. Możliwość stosowania/definiowania typów

3. Wprowadza elementy dokumentacji/klarowności kodu np. poprzez zastosowanie tzw. *silnego typowania*

4. Statycznie typowany - typy są zadeklarowane na początku i nie zmieniają się w trakcie wykonywania kodu w sposób dynamiczny (co cechuje JS)

5. Wprowadza nowe typy: **tuple (krotki), enum (wyliczeniowy typ danych), any, void**

6. Warto pamiętać że: typy prymitywne w TS pisane są małą literą np. stringa oraz number zamiast String czy Number

### Instalacja i konfiguracja

    // terminal
    npm i -g typescript

Należy stworzyć plik **index.ts**

    // index.ts
    console.log('Hello world');

Następnie w terminalu wywołać komendę odwołującą się do TS i wskazującą na plik

    tsc index.ts

W folderze pojawi się nowy plik js po transpilacji -> `index.js` jego zawartość jest w JS/ES3 (w tym przypadku treść będzie taka sama)

W celu wprowadzenia zmian w zachowaniu kompilatora można dodać flagi do komendy do niego się odwołującej w terminalu lub zawrzeć odpowiednie informacje w osobnym pliku `tsconfig.json` (plik można utworzyć poprzez komendę `tsc --init` - tworzy plik z zakomentowanymi opcjami kompilatora -> po wpisaniu `tsc` kompiluje wszystkie pliki ts/ tworzy analytics.ts i .js)

        //tsconfig.json
        {
            "compilerOptions": {
                "target": "esnext", // kompilacja do najnowszej wersji JS
                "watch": true, // nasłuchiwanie na zmiany i kompilacja
                "lib": ["dom", "es2017"], // biblioteki np. "pilnujące" poprawności z klasami/obiektami DOM - trakcie pisania kodu
                "sourceMap": true // Source Map
            },
            "exclude" [ // pliki ts z tych folderów nie będą branę pod uwagę
              "node_modules
            ]
        }

!! W terminalu należy zainicjować "kompilację po wykryciu zmiany" poprzez

    tsc --watch

---

### TypeScript Playground

[Onlinowy edytor TS](http://www.typescriptlang.org/play/index.html)

---

### 1. Pisanie kodu w sposób domniemany (implicit)

    let num = 23 // type: number

    // nie jest możliwe bo wcześniej zadeklarowane jest number
    num = '22'

Podobnie

    let num
    num = 22
    num = '33' // będzie niepoprawne ponieważ inny typ został wyżej przypisany

### 2. Pisanie kodu w sposób wskazany (explicit)

    let num:number // wskazanie typu bez przypisania wartości

let może odnosić się jedynie do liczb jeśli typ został zadeklarowany

### Obiekty

Wskazanie na obiekt

    const droid: object = {
        name: 'C3PO',
        class: 'Protocol'
    }

Albo wykorzystując `{}`

    const droid: {} = {
        name: 'C3PO',
        class: 'Protocol'
    }

Może to przyjąć jeszcze bardziej rozbudowaną formę -> wskazanie na reprezentację obiektu

    const droid: {
        first: string;
        class: string;
    } = {
        name: 'C3PO',
        class: 'Protocol'
    }

Innym sposobem z którym pracujemy z obiektami i jego wzorami są tzw **interfejsu** (więcej na ten temat poniżej).

---

### 3. "Strong typing"/Silne typowanie tworzenie własnych typów

Tworzenie własnego **typu** - Zmienna

    type Style = 'bold' | 'italic'

    let font: Style;

    font = 'cursive' // błąd ponieważ może być jedynie 'bold' albo 'italic'




**Interface** - tworzenie typu **Obiektów**

Interfejs powinien być poprzedzony słowem **interface**

    interface Droid {
        first: string; // wypełnienie podanych tutaj kluczy jest obowiązkowe
        class: string;
        [key: string]: any // pozostawia furtkę na dodanie ew. kluczy wykorzystując typ: any
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

Interfejs jest przykładem tzw. duck typing” albo “structural subtyping” (to pojęcie nie jest zarezerwowane dla TS) - "rozpoznawanie typu obiektu nie na podstawie deklaracji, ale przez badanie metod udostępnionych przez obiekt. Technika ta wywodzi się z powiedzenia: „jeśli chodzi jak kaczka i kwacze jak kaczka, to musi być kaczką”." (za wikipedia) - innymi słowy należy sprawdzić metody przypisane do obiektu/jego "zachowanie".

Kolejny przykład - zawierający "funkcję"

    interface Droid {
      name: string;
      moviesNum: number;

      greet(phrase: string): void;
    }

    let droid1: Droid;

    droid1 = {
      name: 'C3PO',
      age: 9,
      greet(phrase: string) {
        console.log(phrase + ' ' + this.name);
      }
    };

    droid1.greet('Hi there - I am'); // Hi there - I am C3PO


`Interface` przypomina `type` - jednak interface odnosi się jedynie do obiektu, interface może zostać również zaimplementowany w klasie - staje się wówczas swego rodzaju "kontraktem", który klasa jest zmuszona wypełnić.



**Funkcje**

*więcej na temat funkcji również poniżej*

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

Tablica może przechowywać dane jednego typu (strict) lub wielu (flexible)

Wskazanie tablicy przechowującej jedynie liczby

    const arr:number[] = []
    arr.push(1)
    arr.push('23') // error
    arr.push(false) // error

// wskazanie tablicy, która przyjmuje jedynie obiekty powstałe na podstawie wcześniej wskazanego wzoru Droid/interfejsu

    const arr: Droid[] = []

---

### 4. Nowe typy - Tuple, Union, Any, Void, Never, Enum, unknown

W przypadku typów własnych (np. enum) konwencja nakazuje **nazwę z dużej litery**

**Krotki/Tuple**

Nowy typ, który nie występuje w JS. Krotki mogą przechowywać informacje posiadające różne typy, ale mają ograniczoną długość (length)

Definicja krotki (różne typy), w ramach obiektu ograniczonej do 2 wpisów gdzie 1. zawsze numerem a 2. łańcuchem znaków

    interface Droid {
        first: string;
        class: string;
        planet: [number, string] // krotka
    }

TS wyłapie jeśli będzie planowali przypisać do 2. atrybutu wartość o typie number (`droid.planet[1]=1`), nie pozwoli jednak na (nie wykrywa) pushowanie atrybutu do tablicy `droid.planet.push('comment')` nie pozwoli jednak na `droid.planet[1, 'Coirsant', 'comment']` zastąpienie tablicy inną niż ta, która spełnia określony wzórd

// dodanie **znaku zapytania -> ?** sprawia, że są to wartości opcjonalne

    type MyList = [number?, string?, boolean?]

więcej na ten temat: [TypeScript - Tuples](https://www.tutorialsteacher.com/typescript/typescript-tuple)

---

**Enum - wyliczeniowy typ danych**

Enums to "zbiór nazwanych, określonych wartości liczbowych", gdzie początkowa liczba domyślnie jest równa 0 a każda kolejna jest +1

    enum Status {
        Running,
        Timeout,
        Disabled
    }

    console.log(Status.Timeout) // >> 1

Poszczególnym wartościom mogą być przypisane inne liczby np.

    enum Status {
        Running = 5,
        Timeout = 10,
        Disabled // domyślnie jest +1 więc = 11
    }

Często nazwy poszczególnych wartości w enum pisanę są wyłącznie dużymi literami np. `RUNNING` zamiast `Running`


źródła:

[kamilmysliwiec.com - TypeScript – typ wyliczeniowy, enum](https://kamilmysliwiec.com/typescript-typ-wyliczeniowy-enum)

[solutionchaser.com - Zrozumieć enumy w TypeScriptcie](https://solutionchaser.com/typescript-enum/)

---

**Union**

Typ który określa przyjęcie więcej niż jednego podanego typu (przy użyciu symbolu "pipe") - przypomina JS "or" -> || i cechuje się zbliżoną semantyką

    let droids: number | string[]

TS nie analizuje typów, stąd może nie pozwalać na np. sumowanie typu **union** z **number** (można obejść walidacją lub odwołując się do metody .toString())


---

**Literal types - dosłowny typ**

Wykorzystywane w momencie gdy ma przechowywać określoną wartość lub ograniczoną ilość możliwych wartości np.

    let droid: 'C3PO' | 'R2D2'

---

**Type Aliases/Custom types**

Definiowanie własnych typów (na początku kodu) poprzedzone słowem kluczowym **type** - nazwa nie może pokrywać się z żadnym ze znanych obiektów z JS np. Date. Istnieje możliwość przypisania pojedynczego typu do nowego typu jednak nie miało by to praktycznego zastosowania, stąd ta możliwość wykorzystywana jest najczęściej w przypadku typu **Union**

    type StingsNums = number | string

    type OldDroid: 'C3PO' | 'R2D2'

    type Droid = { name: string; firstAppearance: number };

    let input1: StringsNums // przechowuje tylko liczby i ciąg łańcucha znaków

    let input2: OldDroid // przechowuje tylko 'C3PO' lub 'R2D2'

    const droid1: Droid = { name: 'C3PO', firstAppearance: 1977 };

---
**Any**

Użycie typu **any** w trakcie deklarowania tablicy, zmiennej etc. w efektywny sposób likwiduje benefity płynące z używania TS, ponieważ **any** (oznacza **jakikolwiek**) oznacza, że można stosować dowolny typ np. tablica może przechowywać dane pod dowolnym typem

    let droids: any[]


---
**unknown**

*Unknown* jest stosowane w momencie kiedy nie mamy pewności jaki typ powinien,będzie używany - przyjmie każdy typ danych. Typ *unknown* nie może być jednak przypisany do innego typu (*any* już na to pozwala)

    let userInput: unknown

    let anotherInput: string

    userInput = anotherInput // error


Zastosowanie -> nie wiem co będzie wpisane ale jeśli będzie to *string* to chciałbym to wykorzystać (jednak o ile jest to możliwe warto korzystać z typu *union* ze względu na to, że jest precyzyjniejszym rozwiązaniem)

    if (typeof userInput === 'string') {
        anotherInput = userInput
    }

---
**never**

funkcja może zwracać *never* w przypadku, gdy funkcja nie tworzy wartości/value tylko powoduje "zatrzymanie skryptu" (never= nigdy nic nie zwraca i taka jest intencja tej funkcji)

    function constError(message: string, code: number): never {
        throw {message: message, errorCode:code}
    }

    constError('Such droid does not exist', 404)

---


--
### 5. Funkcje jako typy

Deklarowanie zmiennej z typem **Function** pozwala nam na zapewnienie tego, że będzie ona przechowywać jedynie funkcję,a nie coś innego dodatkowo istnieje możliwość wskazania wzoru (typu) tej funkcji

Przykład bez wskazania

    function addDroids(n1:number, n2:number): number {
        return n1 + n2
    }

    let sumDroids: Function;
    sumDroids = 5 // error
    sumDroids = addDroids // ok

Przykład ze wskazaniem typu funkcji np. `()=> number` nie przyjmuje żadnych arg. i zwraca liczbę albo `(a:number, b:number)=> number` powinien przyjąć jakąkolwiek funkcję która przyjmuje 2 arg. będące liczbami i zwraca liczbę

    function addDroids(n1:number, n2:number): number {
        return n1 + n2
    }

    function sumUpDroids(n1:number, n2:number): void {
        console.log(n1+n2)
    }

    let sumDroids: (a:number, b:number)=> number; // definiowanie typu zwracanego
    
    sumDroids = addDroids // ok - spełnia definicję wyżej wskazaną
    sumDroids = sumUpDroids // error - nie spełnia wskazanego typu

### Funkcje - zwracanie typów + 'void' & 'undefined'

Istnieje możliwość typu zwracanej wartości funkcji -> poprzez zastosowanie po argumentach dwukropka oraz podania odpowiedniego typu (stosowane jedynie w przypadku potrzeby)

w wyniku tej funkcji zostanie zwrócona liczba/numbers

    function addDroids(n1:number, n2:number): number {
        return n1 + n2
    }

typ **void** oznacza brak wartości zwrotnej (nie trzeba tego definować, ale taki typ jest przypisany przez TS) - funkcji brakuje konkretnego **returna** (w JS zwrócony zostanie **undefined** a nie **void**) [samotny return bez przypisanej wartości również będzie spójny z tym konceptem]

    function sumDroids(n1:number, n2:number): void {
        console.log(n1+n2)
    }

TS pozwala również na przypisanie typu **undefined**, funkcja wykorzystująca ten typ musi jednak posiadać **return**

    function addDroids(n1:number, n2:number): undefined {
        console.log(n1+n2);
        return;
    }



**callaback jako funkcja**

Jednym z argumentów w ramach funkcji może być inna funkcja - istnieje możliwość wskazania jej wzoru/typu.
Wskazanie `void` może oznaczać, że z wartością zwróconą nic nie będzie wykonywane - nie oznacza to jednak, że ta funkcja nie musi nic zwracać (innymi słowy **void** nie jest zobowiązujące)

    function addMoreDroids(n1:number, n2:number, callB: (num: number)=> void) {
        const result =  n1 + n2
        callB(result)
    }

    addMoreDroids(1,2, (result)=>{ // result:number
        console.log(result)
    })




---

Źródła:

[TypeScript for JavaScript Programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)

[The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

[Basic Types](https://www.typescriptlang.org/docs/handbook/intro.html)

[A beginner’s guide to TypeScript (with some history of the TypeScript)](https://medium.com/jspoint/typescript-a-beginners-guide-6956fe8bcf9e)

[Co to TypeScript](https://clockworkjava.pl/2019/07/co-to-typescript/)

[The Catalog of TypeScript Examples](https://refactoring.guru/design-patterns/typescript)

YT

[Fireship -> TypeScript - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM&t=1s&ab_channel=Fireship)

[React i TypeScript - jak zacząć? | Przeprogramowani.ts #7](https://www.youtube.com/watch?v=nRdR6xAgGvw)

[TypeScript Course for Beginners 2020 - Learn TypeScript from Scratch!](https://www.youtube.com/watch?v=BwuLxPH8IDs)

[TypeScript Tutorial - TypeScript for React - Learn TypeScript [2020]](https://www.youtube.com/watch?v=NjN00cM18Z4&ab_channel=ProgrammingwithMosh)

[Rebased - Kurs TypeScript 1: Wprowadzenie](https://www.youtube.com/watch?v=IU1yUVtxEMI&ab_channel=Rebased)

Podcast

[DevTalk #116 – O TypeScript z Tomaszem Ducinem](https://devstyle.pl/2020/05/18/devtalk-116-o-typescript-z-tomaszem-ducinem/)
