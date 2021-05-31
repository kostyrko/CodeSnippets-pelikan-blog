Title: Angular: wprowadzenie
Author: mkostyrko
Date: 2020-12-22 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-wprowadzenie
related_posts: react-wprowadzenie, typescript-klasy

---

![angular](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png)

### Angular wprowadzenie

Angular został napisany w TypeScript

Aplikacje budowane są z modułów, które składają się komponentów (w przypadku małej aplikacji może istnieć jeden moduł - root module). Każdy z komponentów składa się z klasy pisanej w TS oraz szablony w HTML. Pierwszy z nich odpowiada za informacje, które powinny być widoczne w kodzie html, natomiast informacje zapisane w html powinny odpowiadać za wyświetlanie danych i umożliwienie interakcji z użytkownikiem.

Moduły, komponenty oraz serwisy są klasami posiadającymi dekoratory. Dekoratory wskazują na ich typ oraz zapewniają ich metadane, które mają wpływ na zachowanie Angulara.


---

### Moduły (ngModules) - kontekts

ngModules - nazwa aby rozróżnić od JS modules.

Moduły tworzą kompilacyjny kontekst dla zbioru modułów, które składają się na aplikację (przez konwencję *root module* nazywa się *AppModule*) - tu deklarujemy moduły, z których aplikacja się składa.

Angular składa się z modułów -> app.module.ts (src/app/app.module.ts) splata wszystkie moduły w całość, poszczególny moduł natomiast zbudowana jest jako drzewo składające się z komponentów.

główny moduł posiada dekorator @NgModule, który skłąda się na aplikację Angularową (nie mylić z dyrektywą **NgModel**).

Na moduły składają się komponenty (w przypadku małej aplikacji może istnieć jeden moduł - root module)


      import { BrowserModule } from '@angular/platform-browser';
      import { NgModule } from '@angular/core';

      import { AppComponent } from './app.component';

      @NgModule({
        declarations: [ // ! deklaracja użytych komponentów
          AppComponent
        ],
        imports: [ // ! deklaracja inne moduły, zewnętrzne i dostępne w ramach Angulara
          BrowserModule
        ],
        providers: [LoginService], // ! serwis zadeklarowany dla całej aplikacji - jeśli zadeklarowany w dekoratorze poszczególnego komponentu to wówczas jest jedynie widoczny dla danego komponentu oraz jego dzieci
        bootstrap: [AppComponent] // ! zadeklarowanie początku aplikacji lub tzw root - na podstawie tego "komponentu" Angular tworzy aplikację.
      })
      export class AppModule { }

czytaj dalej [Introduction to modules](https://angular.io/guide/architecture-modules)

---
### Komponenty - wyświetlanie i komunikacja z użytkownikiem

Komponent jest klasą posiadającą dekorator - wyświetla/tworzy html i obsługuje zdarzenia,
komponenty muszą być zadeklarowane w module (środowisku/kontekście). Komponenty służą do wyświetlania danych i komunikacji z użytkownikiem.

Komponent można stworzyć przy pomocy Angular 

    ng generate component nazawaKomponentu
    ng generate component heroes

To spowoduje powstanie folderu o podanej nazwie w folderze src/app zawierającego 4 pliki, **dodatkowo** doda nowo utworzony komponent jako deklarację w dekoratorze **NgModule** (@NgModule) w głównym pliku app (**src/app/app.module.ts**)

Komponent składa się z 3-4 (ts,css,html,ts) plików zawartych we wspólnym folderze (np. heroes ): 1) pliku "klasowego" zawierającego logikę komponentu np. **heroes.component.ts**, 2) szablonu HTML np. **heroes.component.html**, 3) specyficznych styli komponentu **heroes.component.css** oraz opcjonalnie 4) plik z testami **heroes.component.spec.ts**

W pliku TS (np. heroes.component.ts) zawarta jest klasa z dekoratorem komponentowym, który należy zaimportować z **@angular/core** a następnie podpiąć pod niego odpowiednio klasę

Metadane zawarte w dekoratorze odwołują się do -  definiuje selektor CSS komponentu, wskazuje na miejsce znajdowania się pliku zawierającego style, wskazuje lokację szablonu HTML.

Selektor komponentu jest referencją do danego komponentu. Przykładowo jeśli selektor został w komponencie zdefiniowany w sposób następujący `selector: 'app-name-editor',` aby go "zawrzeć" w ramach innego komponentu (wyświetlić/html) należy się do niego odwołać w sposób następujący: `<app-name-editor></app-name-editor> `

`@Component()` - dekorator komponentu identyfikuje pierwszą klasę znajdującą się pod nim jako przynależną do komponentu i zapewnia metadane dla tego komponentu.

`ngOnInit(`) - ng on initialization -> funkcja wywoływana zaraz po stworzeniu("zamontowaniu") komponentu


    import { Component, OnInit } from '@angular/core'; // import dekoratora

    @Component({ // metadane
      selector: 'app-heroes', // selektor CSS komponentu
      templateUrl: './heroes.component.html', // szablon HTML
      styleUrls: ['./heroes.component.css'] // CSS style dla komponentu
    })
    export class HeroesComponent implements OnInit {

      constructor() { }

      ngOnInit() { // tzw. lifecycle hook 
      }

    }

Wykorzystując selektor komponentu możliwe jest zagnieżdżenie komponentu w innym komponencie

    <app-heroes></app-heroes>

czytaj więcej: [Introduction to components and templates](https://angular.io/guide/architecture-components)

---

## Wprowadzenia do składni szablonów - zagadnienia podstawowe

---
Wytłumaczenie podstawowych znaków: 

`{{ }}` - **interpolacja** wyświetla wszystko na stronie w postaci tekstu, wyświetla typy proste, pozwala na wywołanie metod
`[ ]` - łączenie wartości
`( )` - łączenie wydarzenia
`#` - odwołanie do zmiennej/referencji szablonu zmiennych (elementu HTML)
`*` - dyrektywa strukturalna

### Interpolacja

Interpolacja jest podstawowym narzędziem Angulara, które pozwala na wymianę danych pomiędzy klasą a szablonem HTML
(stosowane jest w html ale odwołuje się do informacji zawartych w klasie komponentu)

Przykłady zastosowania interpolacji

`{{ droid }}` - zmienna zawarta w komponencie (ts) // jeśli jest to obiekt zwróci `[object Object]`

`{{ droid.name }}` - odwołanie się do właściwości name obiektu droid

`{{ getDroid().name }}` - interpolacja danych `name` z obiektu zwracanego przez funkcję `getDroid()`

`{{ getDroid }}` - interpolacja funkcji działa na nią metod toString() , wyjątkiem jest jeśli ta jest poprzedzona słowem kluczowym `get`, wówczas przedstawiony zostanie wynik wywołania funkcji// w takim przypadku zastosowania `{{ getDroid() }}` zwróci jedynie informacje o typie 

`{{ 2+2 }}` - interpolacja wyrażenia matematycznego

---

### Operator Pipe

1 - Operator `pipe` -> `|` pozwala na pracę z danymi przed ich wyświetlaniem - wpływa na zachowanie/wygląd elementu. Istnieją wbudowane rury (metody) angulara oraz istnieje możliwość stworzenia włąsnych [wszystkie rury angulara: [Pipes - api list](https://angular.io/api?type=pipe)]

`{{ droid | uppercase }}` // spowoduje że dana zmienna wyświetlać się będzie dużymi literami

**JSON** pipe (pozwala na wyświetlanie obiektów), **KeyValuPipe** (pozwala na iterowanie po obiektach za pomocą klucza), **slice** pipe (tnie)

`{{getDate() | date: 'yyyy'}}` // zastosowanie operatora pipe - date wraz z parametrami więcej: [DatePipe](https://angular.io/api/common/DatePipe)

    {{ num | number: '1.0-0'}} // wyświetlanie jako liczby całkowitej

    {{ num | number: '2.4-5'}} // wyświetlanie 2 liczb przed i 4-5 po przecinku

2 - Część pipów działa w oparciu o lokalizację (język, czas, miejsce)

    {{ price | currency }}

    {{ price | currency: 'PLN': 'symbol':'':'pl'}} // nadpisanie ustawień lokalnych korzystając z argumentów

Nadpisanie lokalizacji

    import localePl from '@angular/common/locales/pl'

    registerLocaleData(localePL)

    {{ '07-15-1410' | date: 'fullDate':'':'pl'}}

3 - Istnieje możliwość łączenia Pipów

    {{ '07-15-1410' | date: 'fullDate' | uppercase }}


Biblioteka **nxg pipes**


---
### *ngFor - dyrektywa powtórzenia

**#ngFor** jest dyrektywą powtórzenia dla Angulara i powtarza dany element (gospodarza) dla każdego elementu z listy // gospodarzem jest ten element w który dyrektywa jest wpisana. Innymi słowy **ngFor** powiela elementy **html** tyle razy ile jest elementów w danej liście.

    let (zdefiniowanie zmiennej) item of (z) items (lista np. tablica)

`*ngFor="let hero of heroes"` - dla każdego bohater z bohaterów gdzie w pliku **heroes.components.ts** heroes został zadeklarowany jako właściwość klasy definiującej komponent `heroes = HEROES;`

    // heroes.components.html
    <ul class="heroes">
      <li *ngFor="let hero of heroes">
        <span class="badge">{{hero.id}}</span> {{hero.name}}
      </li>
    </ul>

**ngFor** pozwala również na odwołanie się do właściwości indeksowej danego elementu, w tym celu można stworzyć kolejną zminną **i**, którą można następnie wykorzystać w interpolacji - `*ngFor="let hero of heroes, let i = index"`

    <li class="collection-item row" *ngFor="let task of tasks, let i = index">
          <span class="col s10"> {{i + 1 }} {{task.name}} - {{task.deadline}}</span>

Patrz pipe: [KeyValuePipe](https://angular.io/api/common/KeyValuePipe) od pobierania informacji (klucza)

    @Component({
      selector: 'keyvalue-pipe',
      template: `<span>
        <p>Object</p>
        <div *ngFor="let item of object | keyvalue">
          {{item.key}}:{{item.value}}
        </div>
        <p>Map</p>
        <div *ngFor="let item of map | keyvalue">
          {{item.key}}:{{item.value}}
        </div>
      </span>`
    })
    export class KeyValuePipeComponent {
      object: {[key: number]: string} = {2: 'foo', 1: 'bar'};
      map = new Map([[2, 'foo'], [1, 'bar']]);
    }


---
### *ngIF (then,else, ngSwitch) - dyrektywa warunku istnienia

Kolejną dyrektywą jest `*ngIF` która w przypadku gdy `warunek = undefined` nie tworzy elementu, natomiast jeśli warunek jest spełniony to tworzy dany element.

**:::** ***alternatywnie :*** visibility -> hidden `<button (click)="btn.style.visibility = 'hidden">`  - element nie znika z drzewa DOM, a do tego nie zwalania miejsca na stronie **:::**

Przykład zastosowania (jeśli selectedHero = undefined nie twórz tego elementu / np na początku gdy nie został jeszcze wybrany)

    <div *ngIf="selectedHero">
      [...]
    </div>

#### *ngIF, else i ng-template

**else** podobnie jak w innych elementach JS oznacza możliwość alternatywną. Np. można wskazać odwołujący się do lokalnej referencji zawarty w znacznikach `<ng-template></ng-template>` który jest wykorzystywany w tym kontekście - opakowuje element, który ma się pojawić gdy dany warunek wcześniej postawiony nie zostaje spełniony (znaczniki te nie tworzą same w sobie elementu - nie istnieją w drzewie DOM)

    <p *ngIf="day == 6"; else otherDay>sobota</p>

    <ng-template #otherDay>
      <p>dziś nie jest sobota</p>
    </ng-template>


#### *ngIF, then, else i ng-container

`ng-container` - jest znacznikiem/kontenerem, który pozwala na skonstruowanie bardziej złożonej logiki związanej z dyrektywą warunku istnienia ( w ten sposób unikamy tworzenia dodatkowego elementu DIV lub innego dodatkowego elementu drzewa DOM) - pełni rolę elementu do obsługi logiki

**ngIf** i **ngFor** - nie mogą być ustawione na tych samych elementach

    // Przykład 1
    <ng-container *ngIF="day === 6; then saturday; else notSaturday">
    </ng-container>

    <ng-template #saturday>
      <p>dziś nie jest sobota</p>
    </ng-template>
    
    <ng-template #notSaturday>
      <p>dziś nie jest sobota</p>
    </ng-template>

    // Przykład 2
    <ng-container *ngIf="true">
      <span *ngFor="let i of [1,2,3]">{{ i }}</span>
    </ng-container>


#### ngSwitch + ngSwitchCase - wyświetlanie warunkowe

**ngSwitch** - sprawdza warunek i jeśli jest on spełniony to wówczas dany element jest tworzony 

    <ng-container [ngSwitch]="day">
      <span #ngSwitchCase="1">Poniedziałek</span>
      <span #ngSwitchCase="2">Wtorek</span>
      <span #ngSwitchCase="3">Środa</span>
      <span #ngSwitchDefault>Każdy inny dzień</span>
    </ng-container>


---
### Biding - łączenie

** Podstawy **

Event binding - pozwala aplikacji na reakcję na dane wprowadzone przez użytkownika - łączenie elementu DOM poprzez wydarzeniem z właściwościami komponentu (ts).

Property binding - pozwala na interpolację właściwości pozyskanych z aplikacji oraz wykorzystanie ich w HTML - pozwala na połączenie właściwości komponentu z właściwością elementu drzewa dom.

Two way binding - połączenie zwrotne, gdzie właściwość elementu drzewa dom jest połączony z właściwoscią komponentu, a ten jest połączony za pomocą wydarzenia z elementem drzewa DOM.

** Wyjaśnienie działania/ Podsumowanie **

Obiekty HTML posiadają Atrybuty // Obiekty DOM posiadają właściwości (property)

Atrybuty inicjalizują właściwości (property) w drzewie DOM, łaczenie/bindowanie w Angularze bezpośrednio wpływa na stan właściwości obiektu z drzewa DOM (łączenie/bindowanie wartości do właściwości/property), które mają wpływ na wyświetlanie się obiektów.

Rodzaje bindingu (powiązań) - `One-way binding:` **Event binding ()**, **Property binding (Data binding) []** (np. poprzez interpolację), `Two-way binding [()]:` => patrz !! **Dyrektywa ngModel**


#### Przykłady

**Event binding ()**

    <button (click)="clearList()"></button>
    <button (click)="taks = []"></button>

**Property binding ()**

    <input type="text" [value]="task.name">
    <button [disabled]="true">Submitt</button>

**Two-way binding /event binding+property binding**

    <input type="text" [(value)]="task.name">


#### Property binding

Pierwszy sposób na data-binging **heroes.component.html** -> `{{hero}}`, w nawiązaniu do **heroes.component.ts** -> gdzie hero zostało zadeklarowane jako właściwość klasy `hero = 'Windstorm';`

`[hero]="selectedHero"` - składnia definiująca połączenie jednostronne, w ramach właściwości elementu DOM (właściwość selectedHero komponentu HeroesComponent zostaje skopiowana/przeniesiona do właściwości hero celowego elementu, który jest zmapowany na podstawie danych z HeroDetailComponent)

Schemat wygląda następująco:

  [nazwa_właściwości_z_którą_się_łączy]="pole_klasowe/funkcja/wyrażenie"

Przykłady:

    <input [value]="Wpisz danej tutaj">

    <textarea [style.background]="color"></textarea>

    <img [src]="imgUrl"/>

    <button [disabled]="counter > 1"></button>

    <app-hero-detail [hero]="selectedHero"></app-hero-detail>

Wywołanie zadarzenia asynchronicznego np. `(keyup)="0"` albo `(change)="(0)"` w przypadku gdy to jest np. oparte na walidacji 

    <button [disabled]="nameInput.value === '' || dateInput.value === ''" />

`[innerHTML] `-  pozwala na wyświetlanie kodu HTML

    export class SomeComponent {
      htmlStr: string = '<strong>The Tortoise</strong> &amp; the Hare';
    }

    <div [innerHTML]="htmlStr"></div>

źródło przykładu: [innerHTML Property Binding in Angular](https://www.digitalocean.com/community/tutorials/angular-innerhtml-binding-angular)



### Events binding

Składnia -> (nasłuchujTegoWydarzenia)="wykonajTąFunkcję(zTymArgumentem")

Przykład

    // heroes.component.html 
    <li *ngFor="let hero of heroes" (click)="onSelect(hero)">

Funkcja ta jest metodą przypisaną do klasy komponentu

    // heroes.component.ts
    [...]
    export class HeroesComponent implements OnInit {

      selectedHero: Hero;
      
      onSelect(hero: Hero): void {
        this.selectedHero = hero;
      }

    [...]


W trakcie generowania się eventu/wydarzenia powstaje również obiekt przechowujące dane o danym wydarzeniu -> aby przechwycić dany obiekt należy wykorzystać zmienną `$event`

    (keyup) = "onKeyUp($event)"

    // w pliku TS
    onKeyUp(event: KeyboardEvent) {
      const target = event.target as HTMLInputElement // rzutowanie typu
      console.log(target.value);
    }

Spis wydarzeń: [Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)

[Przykłady event binging](https://github.com/ZacznijProgramowac/event-binding-examples/blob/master/src/app/app.component.html)

---


### Class binding

Powiązania pozwalają również na połączenie klasy oraz konkretnych styli wraz ze zdefiniowanym warunkiem

Składnia: `[class.jakaś-klasa-css]="jakiś-warunek"`

    // heroes.component.html
    <li *ngFor="let hero of heroes"
      [class.selected]="hero === selectedHero"
      (click)="onSelect(hero)">
      <span class="badge">{{hero.id}}</span> {{hero.name}}
    </li>

---

### Dyrektywa ngModel - Dwustronne połączenie (property+event binding)

`[(ngModel)]` - składnia definiująca połączenie dwustronne i można je rozumieć jako połączenie **property** oraz **event binding**

Przykład zastosowania (łączy input z elementem name obiektu hero zadeklarowanym jako właściwość komponentu)

    <input [(ngModel)]="hero.name" placeholder="name" />

**ngModel** jest częścią modułu odpowiedzialnego za zachowanie sie formularza **FormsModule**, zatem aby z niego skorzystać należy zaimportować odpowiedni moduł w ramach dekoratora **@NgModule**, który powinien znajdować się w ramach AppModule (**src/app.module.ts**)

Dyrektywa **ngModel** pozwala na dwustronne powiązanie pomiędzy zmiennymi klasy a właściwościami html (połączenie event binding z property binding `[()]`). Korzystając z tej dyrektywy nie musimy korzystać z referencji oraz "sztucznego" wywoływania wydarzenia wspomagającego asynchroniczność wydarzeń.


1 - import FormsModule z app.module.ts

    import { FormsModule } from '@angular/forms';

    registerLocaleData(localePl);

    @NgModule({
      declarations: [AppComponent],
      imports: [BrowserModule, FormsModule],
      [...]

2 - deklaracja zmiennych w klasie (app.component.ts)

    export class AppComponent {
      taskName = 'Tu wpisz zadanie'; // deklaracja zmiennej
      taskDate = '';
      [...]

      createTask() {
      const task: Task = {
        name: this.taskName,
        deadline: this.taskDate,
        done: false,
      };
      this.tasks.push(task);
      this.taskName = ''; // czyszczenie input'u
      this.taskDate = '';
    }


3 - app.component.html

    [...]
    <input
      class="col s8"
      type="text"
      placeholder="Dodaj zadanie i datę wykonania"
      [(ngModel)]="taskName"
    />
    [...]

    // zamiast zastosowania event oraz property binding
    [value]="name"
    (input)="name = $event.target.value"

istnieje jeszcze event `(ngModelChange)` dostępny dla formularzy


---
### Serwis - zaplecze/"back-end" aplikacji

serwis (klasa z dekoratorem @Injectable) - wykonuje zadanie związane z komunikowaniem (np. pobieraniem) danych dla komponentów  - dostarcza dane, pomaga w ich analizie oraz przetwarzaniu. Serwis również wspomaga komunikację pomiędzy komponentami (serwisy HTTP, logowanie błędów, logowanie użytkowników) - pozwala na wstrzyknięcie providerów jako zależności do klasy

serwis zadeklarowany w app.module.ts jest dostępny dla całej aplikacji, natomiast jeśli zadeklarowany w dekoratorze poszczególnego komponentu to wówczas jest jedynie widoczny dla danego komponentu oraz jego dzieci.

Dekorator serwisu `@Injectable()` przyjmuje jego metadane (podobnie jak `@Component` w przypadku komponentu)

---

## Zagadnienia zaawansowane - wyjaśnione w kolejnych postach

#### @Input oraz @Output

Dekoratory pozwalające na rozbicie logiki komponentu na mniejsze części/komponenty i komunikowanie się danymi pomiędzy nimi -> **@Input** działa niczym właściwość komponentu w React (props) tzn. pozwala na przekazanie do komponentu danych np.

    // rodzic
    <app-user [name]="Mike"></app-user>

gdzie komponent app-user musie mieć przy pomocy dekoratora @Input zdefiniową właściwość

    @Input() name: string;


**@Output** - pozwala na przekazanie informacji do rodzica, aby tego dokoną naleŻy stworzyć nową instację klasy EventEmmiter // wywołanie funkcji konstruktora

    @Output() nameChanged = new EventEmmiter<string>(); // typ generyczny moŻe być róŻnego rodzaju

    onUserInput(event){
      this.nameChanged.emit(event.target.value);
    }

    // rodzic:
    <app-user [name]="name" (nameChanged)="onNameChanged($event)"></app-user>

    name = "Mike"
    
    onNameChannged(newName) {
      this.name = newName;
    }

--
### Routing 

Routing pozwala na zdefiniowanie ścieżki nawigacji (pomiędzy stanami aplikacji)

---
#### Injector/wtryskiwacz

[Angular Injector, @Injectable & @Inject](https://www.tektutorialshub.com/angular/angular-injector-injectable-inject/)

[Angular InjectionToken - www.angular.love](https://www.angular.love/2018/03/09/angular-injectiontoken/)

---

#### RxJS - asynchroniczność w serwisie

Observable.subscribe() is the critical difference

The new version waits for the Observable to emit the array of heroes—which could happen now or several minutes from now. The subscribe() method passes the emitted array to the callback, which sets the component's heroes property.

This asynchronous approach will work when the HeroService requests heroes from the server.


[Observable data](https://angular.io/tutorial/toh-pt4#observable-data)



---


## Instalacja Angular i stworzenie pierwszego projektu przy pomocy Angular CLI

[Angular CLI Cheat Sheet: The best Commands to boost your productivity](https://malcoded.com/posts/angular-fundamentals-cli/)

ng - next generation (Angular reprezentuje kolejną generację HTML)

    npm install -g @angular/cli

Użycie -> Stworzenie pierwszego projektu

:: Istotne: nazwa projektu nie może zaczynać się od liczby ani zawierać podkreślników lub myślników :::

    ng new PierwszyProjekt

Odpowiedzenie na parę początkowych pytań

    ? Do you want to enforce stricter type checking and stricter bundle budgets in the workspace?
      This setting helps improve maintainability and catch bugs ahead of time.
      For more information, see https://angular.io/strict Yes
    ? Would you like to add Angular routing? No
    ? Which stylesheet format would you like to use? CSS

Uruchomienie projektu

    ng serve

Zawartość folderu projektowego

    nazwaProjektu
        |
        |-e2e // testy end to end
        |-node modules // zależności
        |-src // zawiera projekt
        |-.editconfig // uniwersalna konfiguracja dla edytorów
        |-.gitignore 
        |-.angular.json // główny plik konfiguracyjny dla projektu (budowanie, testowanie, skryptyścieżki...)
        |-browserslist // wspierane narzędzia dla przeglądarek
        |-karma.conf.js // konfiguracja testów
        |-package.json  // komendy CLI
        |-package-lock.json
        |-README.md
        |-tsconfig.app.json // konfiguracja TS dla aplikacji
        |-tsconfig.json // globalna konfiguracja TS dla workspace
        |-tsconfig.spec.json // TS do kompilowanie testów
        |-tslint.json // reguły dla TS

**src**

    nazwaProjektu
            |
            [...]
            |
            |-src // zawiera pliki aplikacji
            |   |
            |   |-app // komponenty,serwisy
            |   |-assests // statyczn pliki (fonty,obrazy)
            |   |-environments // rozróżnienie pomiędzy środowiskiem developerskim a produkcyjnym
            |   |-index.html //
            |   |-main.ts // punkt startowy (nie zmieniany)
            |   |-polyfills.ts // polifile dla angulara (zapewnia kompatybilność z przeglądarkami)
            |   |-styles.ts // (style dla aplikacji)
            |   |-test.ts // konfiguracja testów
            |
            [...]


Przykładowy projekt wykonany przy pomocy Angulara dostępny na stackblitz.com: [angular-nstnfl](https://stackblitz.com/edit/angular-nstnfl?file=src/app/app.component.ts) źródło projektu [Getting started with Angular](https://angular.io/start)

---

## Na zakończenie
### Wtyczka dla Angulara

[**Augury**](https://chrome.google.com/webstore/detail/augury/elgalmkoelokbchhkhacckoklkejnhcd/related)

### Glossary

[Słownik z najważniejszymi pojęciami dla Angulara (ENG)](https://angular.io/guide/glossary)


---


Źródła:

[Introduction to Angular concepts](https://angular.io/guide/architecture)

[TypeScript - tsc CLI Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

[Angular workspace configuration](https://angular.io/guide/workspace-config)

[Udemy - Angular - kompletny kurs od podstaw - nowa edycja 2020](https://www.udemy.com/course/angular-kompletny-kurs)

[angular.io - template-syntax](https://angular.io/guide/template-syntax)