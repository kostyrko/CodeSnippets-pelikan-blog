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

### Komponenty - wyświetlanie i komunikacja z użytkownikiem

Komponent jest klasą posiadającą dekorator - wyświetla/tworzy html i obsługuje zdarzenia,
komponenty muszą być zadeklarowane w module (środowisku/kontekście). Komponenty służą do wyświetlania danych i komunikacji z użytkownikiem.

`@Component()` - dekorator komponentu identyfikuje pierwszą klasę znajdującą się pod nim jako przynależną do komponentu i zapewnia metadane dla tego komponentu.

czytaj więcej: [Introduction to components and templates](https://angular.io/guide/architecture-components)

### Serwis - zaplecze/"back-end" aplikacji

serwis (klasa z dekoratorem @Injectable) - wykonywanie zadań dla komponentów (dostarcza dane, pomaga w ich analizie oraz przetwarzaniu), wspomaga komunikację pomiędzy komponentami (serwisy HTTP, logowanie błędów, logowanie użytkowników) - pozwala na wstrzyknięcie providerów jako zależności do klasy

serwis zadeklarowany w app.module.ts jest dostępny dla całej aplikacji, natomiast jeśli zadeklarowany w dekoratorze poszczególnego komponentu to wówczas jest jedynie widoczny dla danego komponentu oraz jego dzieci.


---
### Events/Data oraz Property Biding

Event binding - pozwala aplikacji na reakcję na dane wprowadzone przez użytkownika

Property binding - pozwala na interpolację właściwości pozyskanych z aplikacji oraz wykorzystanie ich w HTML

pipe - transformacja danych na wyświetlenie

---

### Routing 

Routing pozwala na zdefiniowanie ścieżki nawigacji (pomiędzy stanami aplikacji)


### Glossary


[Słownik z najważniejszymi pojęciami dla Angulara (ENG)](https://angular.io/guide/glossary)

---

### Wtyczka dla Angulara

[**Augury**](https://chrome.google.com/webstore/detail/augury/elgalmkoelokbchhkhacckoklkejnhcd/related)

### Instalacja Angular i pierwszy projekt przy pomocy Angular CLI

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



---


Źródła:

[Introduction to Angular concepts](https://angular.io/guide/architecture)

[TypeScript - tsc CLI Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

[Angular workspace configuration](https://angular.io/guide/workspace-config)

