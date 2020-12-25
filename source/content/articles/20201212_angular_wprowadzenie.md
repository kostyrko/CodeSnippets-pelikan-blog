Title: Angular: wprowadzenie
Author: mkostyrko
Date: 2020-12-12 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-wprowadzenie
related_posts: react-wprowadzenie

---

![angular](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png)

### Angular wprowadzenie

Angular został napisany w TypeScript

Aplikacje budowane są z modułów, które składają się komponentów (w przypadku małej aplikacji może istnieć jeden moduł - root module).

Moduły, komponenty oraz serwisy są klasami posiadającymi dekoratory. Dekoratory wskazują na ich typ oraz zapewniają ich metadane, które mają wpływ na zachowanie Angulara.


---

### Moduły (ngModules) - kontekts

ngModules - nazwa aby rozróżnić od JS modules.

Moduły tworzą kompilacyjny kontekst dla zbioru modułów (przez konwencję *root module* nazywa się *AppModule*)

Angular składa się z modułów -> app.module.ts (src/app/app.module.ts) splata wszystkie moduły w całość, poszczególny moduł natomiast zbudowana jest jako drzewo składające się z komponentów.

główny moduł posiada dekorator @NgModule, który skłąda się na aplikację Angularową.

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
        bootstrap: [AppComponent] // ! zadeklarowanie początku aplikacji
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

Metadane zawarte w dekoratorze odwołują się do -  definiuje selektor CSS komponentu, wskazuje na miejsce znajdowania się pliku zawierającego style, wskazuje lokację szablonu HTML

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
#### Operator Pipe

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
### Serwis - zaplecze/"back-end" aplikacji

serwis (klasa z dekoratorem @Injectable) - wykonuje zadanie związane z komunikowaniem (np. pobieraniem) danych dla komponentów  - dostarcza dane, pomaga w ich analizie oraz przetwarzaniu. Serwis również wspomaga komunikację pomiędzy komponentami (serwisy HTTP, logowanie błędów, logowanie użytkowników) - pozwala na wstrzyknięcie providerów jako zależności do klasy

serwis zadeklarowany w app.module.ts jest dostępny dla całej aplikacji, natomiast jeśli zadeklarowany w dekoratorze poszczególnego komponentu to wówczas jest jedynie widoczny dla danego komponentu oraz jego dzieci.

Dekorator serwisu `@Injectable()` przyjmuje jego metadane (podobnie jak `@Component` w przypadku komponentu)

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
### Biding

Event binding - pozwala aplikacji na reakcję na dane wprowadzone przez użytkownika

Property binding - pozwala na interpolację właściwości pozyskanych z aplikacji oraz wykorzystanie ich w HTML

#### Property binding

Pierwszy sposób na data-binging **heroes.component.html** -> `{{hero}}`, w nawiązaniu do **heroes.component.ts** -> gdzie hero zostało zadeklarowane jako właściwość klasy `hero = 'Windstorm';`

`[hero]="selectedHero"` - składnia definiująca połączenie jednostronne, w ramach właściwości elementu DOM (właściwość selectedHero komponentu HeroesComponent zostaje skopiowana/przeniesiona do właściwości hero celowego elementu, który jest zmapowany na podstawie danych z HeroDetailComponent)

    <app-hero-detail [hero]="selectedHero"></app-hero-detail>

#### Dwustronne połączenie

`[(ngModel)]` - składnia definiująca połączenie dwustronne

Przykład zastosowania (łączy input z elementem name obiektu hero zadeklarowanym jako właściwość komponentu)

    <input [(ngModel)]="hero.name" placeholder="name" />

**ngModel** jest częścią modułu odpowiedzialnego za zachowanie sie formularza **FormsModule**, zatem aby z niego skorzystać należy zaimportować odpowiedni moduł w ramach dekoratora **@NgModule**, który powinien znajdować się w ramach AppModule (**src/app.module.ts**)

    [...]
    import { FormsModule } from '@angular/forms';

    @NgModule({
      declarations: [
        AppComponent,
        HeroesComponent
      ],
      imports: [
        BrowserModule,
        FormsModule
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }

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

---
### *ngIF - dyrektywa warunku istnienia

Kolejną dyrektywą jest `*ngIF` która w przypadku gdy `warunek = undefined` nie tworzy elementu

Przykład zastosowania (jeśli selectedHero = undefined nie twórz tego elementu / np na początku gdy nie został jeszcze wybrany)

    <div *ngIf="selectedHero">
      [...]
    </div>
    
---
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

---
### Class binding

Powiązania pozwalają również na połączenie klasy oraz powiązanych z nią styli wraz ze zdefiniowanym warunkiem

Składnia: `[class.jakaś-klasa-css]="jakiś-warunek"`

   // heroes.component.html 
    <li *ngFor="let hero of heroes"
      [class.selected]="hero === selectedHero"
      (click)="onSelect(hero)">
      <span class="badge">{{hero.id}}</span> {{hero.name}}
    </li>

---
### Dekorator @Input()

Łączy input z danym komponentem pozwalając mu na zewnętrzne użytkowanie - rozbicie logiki komponentu na mniejsze części (komponenty)

Wymaga importu z counterReducer

    import { Component, OnInit, Input } from '@angular/core';

Oraz zdefiniowania identyfikatora opatrzonego dekoratorem @Input() 


    @Input() hero: Hero;


Odwołanie się w komponencie posiadającym element, do którego następuje odwołanie (komponent rodzica) wygląda w sposób następujący (np. heroes.component.html -> selectedHero)

    <app-hero-detail [hero]="selectedHero"></app-hero-detail>

`[hero]="selectedHero"` - składnia definiująca połączenie jednostronne, w ramach właściwości elementu DOM (właściwość selectedHero komponentu HeroesComponent zostaje skopiowana/przeniesiona do właściwości hero celowego elementu, który jest zmapowany na podstawie danych z HeroDetailComponent). Kiedy użytkownik klika selectedHero ulega zmianie, a przez to również HeroDetailComponent (property bindig go odświeża)

Przykład

    ==== Usunięcie tego fragmentu =====
    <div *ngIf="selectedHero">
      <h2>{{ selectedHero.name | uppercase }} Details</h2>
      <div><span>id: </span>{{ selectedHero.id }}</div>
      <div>
        <label
          >name:
          <input [(ngModel)]="selectedHero.name" placeholder="name" />
        </label>
      </div>
    </div>
    ============ Zastąpienie go tym ========
    <app-hero-detail [hero]="selectedHero"></app-hero-detail>


    >>>>>>> Komponent dziecka zawierającego input <<<<<<<

    // HTML dziecka
    <div *ngIf="hero">

      <h2>{{hero.name | uppercase}} Details</h2>
      <div><span>id: </span>{{hero.id}}</div>
      <div>
        <label>name:
          <input [(ngModel)]="hero.name" placeholder="name"/>
        </label>
      </div>

    </div>

    // TS dziecka
    import { Component, OnInit, Input } from '@angular/core';
    import { Hero } from '../hero';

    @Component({
      selector: 'app-hero-detail',
      templateUrl: './hero-detail.component.html',
      styleUrls: ['./hero-detail.component.css']
    })
    export class HeroDetailComponent implements OnInit {

      @Input() hero: Hero;

      constructor() { }

      ngOnInit(): void {
      }

    }


[Komunikacja pomiędzy komponentami w Angular 2](https://typeofweb.com/komunikacja-pomiedzy-komponentami-w-angular-2/)

--

### Routing 

Routing pozwala na zdefiniowanie ścieżki nawigacji (pomiędzy stanami aplikacji)


### Glossary


[Słownik z najważniejszymi pojęciami dla Angulara (ENG)](https://angular.io/guide/glossary)

---


### Instalacja Angular i pierwszy projekt przy pomocy Angular CLI

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
### Wtyczka dla Angulara

[**Augury**](https://chrome.google.com/webstore/detail/augury/elgalmkoelokbchhkhacckoklkejnhcd/related)

---


Źródła:

[Introduction to Angular concepts](https://angular.io/guide/architecture)

[TypeScript - tsc CLI Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

[Angular workspace configuration](https://angular.io/guide/workspace-config)
