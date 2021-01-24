Title: Angular -> Mały projekt od podstaw
Author: mkostyrko
Date: 2021-01-23
 12:00
Updated:
Category: angular
Tags: bootstrap, angular, javascript
Slug: angular-projekt
related_posts: 



![angular-bootstrap](https://angular.io/assets/images/logos/angular/angular.svg)

### Mały projekt - cytaty z Gwiezdnych Wojen

Zainiscjowanie projekty przy pomocy Angular-CLI

    ng new star-wars-quotes-app

dodanie frameworku css-owego [**materialize-css**](https://materializecss.com/getting-started.html) do zależności

    npm install materialize-css@1.0.0

Konfigurowanie zależności stylowej w angular.json // wskazanie zarówno na styl css oraz na jego plik js

    "styles": [
        "src/styles.css",
        "./node_modules/materialize-css/dist/css/materialize.css"
      ],
      "scripts": [
        "./node_modules/materialize-css/dist/js/materialize.js"
      ]

Dodanie iko w sekcji head index.html

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

----
1. Dodanie folderu modeli -> /star-wars-quotes-app/src/models

`quotation.ts` -> zawiera interfejs pojedynczego cytatu

    export interface Quotation {
      author: string;
      sentence: string;
      votes: number;
    }

`database.ts` - przechowuje bazę cytatów

`app.component.html` - wyjściowy szkielet

`style.css` - podstawowe dodatki stylistyki

Pliki wyjściowe -> [ZacznijProgramowac/angular.json](https://gist.github.com/ZacznijProgramowac/af7de69c309236e466fd1c497f75408a)

---

2. Dodanie funkcjonalności

A. Dodawanie klasy do elementu

Szablon html

    \\ app.component.html
    <!-- dodanie klasy do komponentu gdy showForm będzie miła wartość true -->
    <!-- ten element jest stylowany -->
    <div class="row edit-row" [class.drawer]="showForm">
    </div>

    <!-- w tym elemencie (button) metoda jest wywoływana -->
    <button class="btn-floating teal add-button" (click)="onSwitchForm()">
      <i class="material-icons">add</i>
    </button>

Tym czasem po stronie ts należy dodać pole, które będzie przechowywać wartość, w zal. od której element będzie widoczny lub nie, do tego należy również dołączyć metodę, która obsługuje mechanizm zmiany.


    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
    })
    export class AppComponent {
      title = 'star-wars-quotes-app';

      // przechowuje wartość zw. z dodawaniem klasy
      showForm = false

      onSwitchForm(): void {
        this.showForm = !this.showForm;
      }
    }


B. Wyświetlanie cytatów (*ngFor)

a) zaimportowanie danych (QUOTES: Quotation[]/realizuje interfejs Quotation) oraz interfejs, który mają spełniać

    import { Component } from '@angular/core';
    import { QUOTES } from 'src/models/database';
    import { Quotation } from 'src/models/quotations';

    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
    })
    export class AppComponent {
      title = 'star-wars-quotes-app';

      quotes: Quotation[] = QUOTES

      // przechowuje wartość zw. z dodawaniem klasy
      showForm = false
      // metoda zmieniająca wartość przechowywaną w showForm
      onSwitchForm(): void {
        this.showForm = !this.showForm;
      }
    }

Wykorzystanie zaimportowanych danych po stronie szablonu HTML

    <div class="card teal hoverable"

            // dla każdego cytatu z cytatów -> *ngFor
              *ngFor="let quotation of quotes; let odd=odd"

            // uzależnienie klasy tego czy odd jest fale lub true
              [ngClass]="odd ? 'accent-4':'accent-5'"
              >

            // wykorzystanie zmiennych
                <div class="card-content white-text">
                  <span class="card-title">
                    {{quotation.sentence}}
                  </span>
                    {{quotation.author}}
                </div>
            [...]
    </div>

C. Dodawanie cytatów (*ngModel)

app.module.ts 
Importowanie modułu/dyrektywy formularza do app.module.ts -> FormsModule

    import { FormsModule } from '@angular/forms';

    @NgModule({
      declarations: [
        AppComponent
      ],
      imports: [
        BrowserModule, FormsModule
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }


Zainicjowanie pola w komponencie, w którym będą przechowywane dane/wykorzystuje wcześniej zdef. interfejs/ inicjalizacja obiektu z wstępnymi danymi w innym przypadku był by null.
Dodanie metody, która obsługuje dodane pole.

    import { Component } from '@angular/core';
    import { QUOTES } from 'src/models/database';
    import { Quotation } from 'src/models/quotations';

    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
    })
    export class AppComponent {
      title = 'star-wars-quotes-app';
      quotes: Quotation[] = QUOTES

      // stworzone pole
      quotation: Quotation = {author: '', sentence: '', votes: 0};
      showForm = false
      onSwitchForm(): void {
        this.showForm = !this.showForm;
      }

      //metoda,która dodaje quotation na początek listy, następnie resetuje obiekt przechowujący
      addQuotation() {
        this.quotes.unshift(this.quotation);
        this.quotation = {author: '', sentence: '', votes: 0};
      }
    }

Po str html należy zbindować 2 elementy w 2 str sposób przy pomocy ngModel + na buttonie zarejestrowanie event.click

    <div class="row edit-row" [class.drawer]="showForm">
      <div class="input-field col s4">
        <input type="text" placeholder="Autor" [(ngModel)]="quotation.author"/>
      </div>
      <div class="input-field col s6">
        <input type="text" placeholder="Cytat" [(ngModel)]="quotation.sentence"/>
      </div>
      <div class="input-field col s2">
        <button class="btn small" (click)='addQuotation()'>Dodaj</button>
      </div>
    </div>

D. Dodawanie głosowania

Dodanie metody obsługującej głosowanie po str TS do komponentu

    [...]
    addVote(quotation: Quotation, value: number){
        quotation.votes +=value
      }
    [...]

Użycie metody w widoku html - wstawienie elementu do szablonu przy pomocy interpolacji oraz na buttonach dodanie metody click

    <div class="card-action right-align">
      <span class="badge grey darken-2 left white-text">{{quotation.votes}}</span>
      <button class="btn blue mr-5" (click)="addVote(quotation, +1)">
        <i class="material-icons">exposure_plus_1</i>
      </button>

      <button class="btn brown" (click)="addVote(quotation, -1)">
        <i class="material-icons">exposure_neg_1</i>
      </button>
    </div>

E.  Implementacja Rankingu (założenie jest taki że te co mają więcej niż 0 są dobre a te co poniżej są słabe)

ngFor i ngIf nie może być razem dlatego wykorzystuje się ng-container. Tak przedstawia się fragment kodu przedstawiający element ukazujący ranking

      <ng-container *ngFor='let quotation of quotes' >
        <p class="collection-item" *ngIf="quotation.votes > 0">
          <span class="blue lighten-4 badge">{{quotation.votes}}</span>
          {{quotation.sentence}}<br />
          <span class="blue-text">{{quotation.author}}</span>
        </p>
      </ng-container>

---
Źródła:

[Angular - kompletny kurs od podstaw - edycja na rok 2021](https://www.udemy.com/course/angular-kompletny-kurs-od-podstaw/)

