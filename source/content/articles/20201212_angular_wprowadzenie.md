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

### Instalacja Angular CLI

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

### Moduły

Angular składa się z modułów -> app.module.ts (src/app/app.module.ts) splata wszystkie moduły w całość, poszczególny moduł natomiast zbudowana jest jako drzewo składające się z komponentów.

główny moduł posiada dekorator @NgModule, który skłąda się na aplikację Angularową


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

### Komponenty - wyświetlanie i komunikacja z użytkownikiem

Komponent jest klasą posiadającą dekorator - wyświetla html i obsługuje zdarzenia,
komponenty muszą być zadeklarowane w module. Komponenty służą do wyświetlania danych i komunikacji z użytkownikiem.

### Serwis - zaplecze/"back-end" aplikacji

serwis (klasa z deklaratorem @Injectable) - wykonywanie zadań dla komponentów (dostarcza dane, pomaga w ich analizie oraz przetwarzaniu), wspomaga komunikację pomiędzy komponentami (serwisy HTTP, logowanie błędów, logowanie użytkowników)

serwis zadeklarowany w app.module.ts jest dostępny dla całej aplikacji, natomiast jeśli zadeklarowany w dekoratorze poszczególnego komponentu to wówczas jest jedynie widoczny dla danego komponentu oraz jego dzieci.


---

### Interpolacja


### Pipes


### Operator Question mark

### dyrektywa *ngFor

### Data Biding

### Event Biding

### Template reference

### Property binding

---

### Wtyczka dla Angulara

[**Augury**](https://chrome.google.com/webstore/detail/augury/elgalmkoelokbchhkhacckoklkejnhcd/related)




---


Źródła:

[TypeScript - tsc CLI Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

[Angular workspace configuration](https://angular.io/guide/workspace-config)


