Title: Angular: przekazanie danych pomiędzy komponentami cz. 2 -> serwis
Author: mkostyrko
Date: 2021-04-11 10:00
Updated: 2021-07-24 10:00
Category: angular
Tags: angular, serwis, service, subscribe, unfinished
Slug: angular-serwisy
related_posts: angular-komunikacja-komponentow

![angular](https://i.stack.imgur.com/E8ItT.png)

### Angular serwisy

#### Wstęp

Klasa TyperScriptowa - stworzona do centralizacji danych/zarządzania danymi (a docelowo stanem aplikacji). Jej zadaniem jest - dostarczania danych na potrzeby komponentów (np. poprzez komunikacja z API, komunikacja pomiędzy komponentami, przechowywanie stanu aplikacji).


Serwis posiada swój dekorator **@Injectable** - ten wskazuje na to, że dana klasa jest serwisem i jej logikę można wstrzyknąć do innego komponentu przy pomocy **dependecy injection**  poprzez zadeklarowanie providera (dostarczyciela) + dane określające w jaki sposób działa serwis + użycie innych serwisów. 

Warto pamiętać : dekorator **@Injectable** nie jest warunkiem koniecznym do implementacji serwisu, jest natomiast warunkiem niezbędnym do wstrzyknięcia serwisu w serwis (wówczas serwis, do którego inny jest wstrzykiwany musi posiadać taki dekorator).)

---
Przykładowa **deklaracja tworząca klasę serwisu** (np. **loggerService.service.ts**)

    import { Injectable } from '@angular/core';
    @Injectable()
    export class LoggerService {
      log(msg: any) {
        console.log(msg);
      }
    }

Przykład prostej aplikacji korzystającej z serwisu [star-wars-app](https://github.com/kostyrko/JS-sandbox/tree/angular-service/7_Angular/angular-service-app/star-wars-services/src/app) 

Przykład tej samej aplikacji, ale gdzie serwis (ServiceLog) został wstrzyknięty do serwisu (StarWarsService) [star-wars-app](https://github.com/kostyrko/JS-sandbox/tree/angular-service-into-service/7_Angular/angular-service-app/star-wars-services/src/app)

-> więcej na temat tej aplikacji [Udemy: Angular Essentials (Angular 2+ with TypeScript)](https://www.udemy.com/course/angular-essentials-angular-2-angular-4-with-typescript/)

---
**Wykorzystanie serwisu w ramach aplikacji**


Deklaracja serwisu (*dependency injection*) znajduje się w tablicy **providers** (dostarczycieli ===> `providers: [LoggerService]` w **app.module.ts**

**app.module.ts**

    // import serwisu
    import { LoggerService } from './shared/loggerService.service';
    // import komponentu wykorzystującego serwis
    import { LoggingComponent } from './logging/logging.component';

    @NgModule({
      imports: [BrowserModule],
      declarations: [AppComponent, LogTestComponent],
      bootstrap: [AppComponent],
      providers: [LoggerService] // jedna instancja dla całej aplikacji
    })
    export class AppModule { }


**Wykorzystanie serwisu w ramach komponentu**

W Angular analizuje argumenty w konstruktorze oraz zadeklarowane zależności (wyżej) i dokonuje wstrzyknięcia zależności (dependency injection) na podstawie wskazania w konstruktorze


    import { Component } from "@angular/core";
    import { LoggerService } from '../shared/loggerService.service';

    @Component({
        selector: "log-test",
        templateUrl: "./log-test.component.html",
    })
    export class LogTestComponent {

        loggerService : LoggerService // nowa właściwość klasy loggerService typu LoggerService

        constructor(
          loggerService: LoggerService // deklaracja argumentu
          ) { 
            this.loggerService = LoggerService // dependency injection
          }

        ngOnInit {
          testLog(): void {
            this.loggerService.log("Test the `log()` Method");
          }
        }
    }


**providedIn: 'root'**

zastosowanie providedIn: 'root' w ramach dekoratora `@Injectable()` powoduje, że deklarujemy jego dostępność w całym komponencie, wówczas nie ma potrzeby deklarowania go wśród providerów w **app.module.ts**


    import { Injectable } from '@angular/core';
    @Injectable(
      // declares that this service should be created
      // by the root application injector.
      providedIn: 'root',
    )
    export class LoggerService {
      log(msg: any) {
        console.log(msg);
      }
    }

#### Dekoratory

##### Injectable

`singleton` - serwis dzieli te same dane pomiędzy wszystkie zainteresowane komponenty

`providedIn: 'root'`  -> wskazanie gdzie dany serwis jest dotępny (root - cała aplikacja)

tożsame działanie: providers: [ LoggerService ] - również tworzy sinleton w całej aplikacji jeśli w module @NgModule({....

`providedIn: 'platform'`  -> singleton w całej platformie aplikacji

`providedIn: 'any'`  -> nowa instancja dla każdego modułu

`providedIn: 'moduleName'` -> wskazanie nazwy modułu, do którego przynależy serwis


providers: [ LoggerService ] w dekoratorze @Component({.... - dla komponentu oraz wszystkich jego dzieci powstanie nowa instancja serwisu // Dzieci już nie muszą deklarować tego serwisu w soich prowiderach. Tym samym również dochodzi do nadpisania globalnego serwisu.

#### Wykorzystanie serwisu w serwisie

Serwis może zostać zadeklarowany w **app.component.ts** (spaja aplikację) jednak aby faktycznie był widoczny (używalny) w innym serwisie musi on zostać zadeklarowany w głównym pliku modułowym angulara **app.module.ts**

Dodatkowo serwis korzystający z innego serwisu musi posiadać dekorator **@Injectable**!! (importowany z '@angular/core') [dependency injector w angularze współpracuje tylko z klasami, które posiadają dekorator **Injectable**]

---
#### Generowanie serwisu przy pomocy Angular CLI

ng g s services/serviceName (ng generate service)

        npm run ng g s core/services/loggerService

Wynik:

        import { Injectable } from '@angular/core';

        @Injectable({
          providedIn: 'root'
        })
        export class LoggerService {

          constructor() { }
        }

---

### Przykładowy projekt z zastosowaniem serwisu

Orginalne żródło poniższego projektu: [GH - ZacznijProgramowac/easy-words](https://github.com/ZacznijProgramowac/easy-words/tree/003-answer-component)

[Udemy -Angular - kompletny kurs od podstaw - edycja na rok 2021](https://www.udemy.com/course/angular-kompletny-kurs-od-podstaw)

---
**model danych** easy-words-app/src/app/data/models.ts

    export interface WordType {
      word: string;
      type: Type;
      correct?: boolean;
    }

    export enum Type {
      NOUN, VERB
    }

---
**dane/plik zastępujący bazę danych** easy-words-app/src/app/data/data-base.ts


    import { Type, WordType } from './models';

    export const WORDS: WordType[] = [
      {
        word: 'accept',
        type: Type.VERB,
      },
      {
        word: 'advice',
        type: Type.NOUN,
      },
      {
        word: 'blood',
        type: Type.NOUN,
      },
      {
        word: 'clear',
        type: Type.VERB,
      },
      {
        word: 'damage',
        type: Type.VERB,
      },
      {
        word: 'choice',
        type: Type.NOUN,
      },
      {
        word: 'educate',
        type: Type.VERB,
      },
    ];

---
**serwis** - easy-words-app/src/app/services/words.service.ts


    import { Injectable } from '@angular/core';
    import { WORDS } from '../data/data-base';
    import { WordType, Type } from '../data/models';

    @Injectable({
      providedIn: 'root'
    })
    export class WordsService {

      // zdefiniowanie tablic jako prywatnych i niewidocznych po za klasą (do ich wydobycia poniższe metody)
      private words: WordType[] = [];
      private nouns: WordType[] = [];
      private verbs: WordType[] = [];

      constructor() {
        // zainicjowanie zawartości tablicy przechowującej słowa
        this.words = WORDS;
      }

      getWords(): WordType[] {
        return this.words;
      }

      getNouns(): WordType[] {
        return this.nouns;
      }

      getVerbs(): WordType[] {
        return this.verbs;
      }

      addNoun(value: WordType): void {
        this.nouns.push(value);
      }

      addVerb(value: WordType): void {
        this.verbs.push(value);
      }

      check() {
        // word.correct true albo false jeśli typ słowa jest równy tej grupie do, której został przypisany
        this.nouns.map(word => (word.correct = word.type === Type.NOUN));
        this.verbs.map(word => (word.correct = word.type === Type.VERB));
      }
    }

---
**Komponent korzystający z serwisu** - easy-words-app/src/app/compontents/question/question.component.ts 


    import { Component, OnInit } from '@angular/core';
    import { WordType } from 'src/app/data/models';
    import { WordsService } from 'src/app/services/words.service';

    @Component({
      selector: 'app-question',
      templateUrl: './question.component.html',
      styleUrls: ['./question.component.css']
    })
    export class QuestionComponent implements OnInit {

      // przechowuje jedno słowo, wyświetlane w danym momencie
      // ma postać obiektu WordType zdefiniowane w models.ts
      word: WordType = null;

      constructor(
        // wstrzyknięcie komponentu (@Injectable({providedIn: 'root'})) więc tu nie musi być podany w tablicy providers
        // private - dostępny tylko w klasie komponentu // public - html również ma do niego dostęp
        private wordsService: WordsService
      ) { }

      ngOnInit(): void {
        // wywołanie metody w celu pobrania słowa
        this.fetchWord();
      }

      // pobiera element z listy oraz go usuwa (shift())
      private fetchWord(): void {
        this.word = this.wordsService.getWords().shift();
      }

      // dodanie słowa do zbioru (tablicy) nouns znajdującej się serwisie WordsService
      addToNouns(word: WordType): void {
        this.wordsService.addNoun(word);
        this.fetchWord();
      }

      // dodanie słowa do zbioru (tablicy) verbs znajdującej się serwisie WordsService
      addToVerbs(word: WordType): void {
        this.wordsService.addVerb(word);
        this.fetchWord();
      }

      // odwołanie się do metody sprawdzającej poprawność przypisani słów znajdującej się serwisie WordsService
      check(): void {
        this.wordsService.check();
      }
    }

---
easy-words-app/src/app/compontents/question/question.component.html

    <div class="row center">
      <div class="col s12">
        <div class="card blue-grey darken-1">
          <div class="card-content white-text">
            <!-- jeżeli obiekt word ma wartość to jest wyświetlane w innym przypadku koniec/ obiekt ten za każdym razem ulega zmianie w momencie użycia poniższych 2 pierwszych metod-->
            <h2>{{ word ? word.word : 'Koniec'}}</h2>
          </div>
          <div class="card-action">
            <button class="btn-large blue m5" (click)="addToNouns(word)" *ngIf="word">
              Noun
            </button>
            <button class="btn-large blue" (click)="addToVerbs(word)" *ngIf="word">
              Verb
            </button>
            <button class="btn-large black" (click)="check()" *ngIf="!word">
              Sprawdź
            </button>
          </div>
        </div>
      </div>
    </div>


**Komponent korzystający z serwisu 2 - główny komponent przekazujący dane do dziecka (dump komponentu)**


**easy-words-app/src/app/app.component.ts**


    import { Component } from '@angular/core';
    import { WordsService } from './services/words.service';

    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
    })
    export class AppComponent {
      title = 'easy-words-app';

      constructor(private wordsService: WordsService) {}

      // bezpośredni dostęp do zawartości serwisu
      // getter rzeczowników
      get nouns() {
        return this.wordsService.getNouns()
      }

      // 'getter' czasowników
      get verbs() {
        return this.wordsService.getVerbs()
      }
    }


**easy-words-app/src/app/app.component.html**


    <div class="row">
      <div class="col s12">
        <app-question></app-question>
      </div>
      <div class="col s6">
        <!-- property title oraz words - lista nouns/getter z komponentu rodzica (@Input) -->
        <app-answers title="Nouns" [words]="nouns"></app-answers>
      </div>
      <div class="col s6">
        <app-answers title="Verbs" [words]="verbs"></app-answers>
      </div>
    </div>


**Komponent przyjmujący dane od rodzica** 

**easy-words-app/src/app/compontents/answers/answers.component.ts**


    import { Component, Input, OnInit } from '@angular/core';
    import { WordType } from 'src/app/data/models';

    @Component({
      selector: 'app-answers',
      templateUrl: './answers.component.html',
      styleUrls: ['./answers.component.css']
    })
    export class AnswersComponent {

      // nazwa listy verbs albo nouns
      @Input() title: string;
      // przechowuję listę przypisanych słów
      @Input() words: WordType[];

      constructor() { }

    }


**easy-words-app/src/app/compontents/answers/answers.component.html**

  
    <ul class="collection with-header">
      <li class="collection-header">
        <h4>{{ title }}</h4>
      </li>
      <!-- word?.correct zawiera ? ponieważ nie jest obowiązkowe i jest przypisywane dopiero w momencie sprawdzania -->
      <li
        class="collection-item"
        *ngFor="let word of words"
        [ngClass]="{ incorrect: word?.correct === false}"
      >
        {{ word.word }}
      </li>
    </ul>



---

Źródła:

[SO - Angular 2, How to Share Array Data Between components using service?](https://stackoverflow.com/questions/43585998/angular-2-how-to-share-array-data-between-components-using-service)

[Types of AngularJS Services with Examples – Creating/Registering Services](https://data-flair.training/blogs/angularjs-services/)

[ANGULAR 2 – Bidirectional Service](https://www.angular.love/2016/12/28/angular-2-bidrectional-service-komunikacja-komponentow-poprzez-serwis/)

[Czym jest serwis w Angularze?](https://zacznijprogramowac.net/angular-pytania/czym-jest-serwis-w-angularze/)

[Jak pozbyć się singletonów w Angularze?](https://www.p-programowanie.pl/angular/jak-pozbyc-sie-singletonow-w-angularze)

[angular.io -> Add services](https://angular.io/tutorial/toh-pt4)

[angular.io -> Dependency injection in Angular](https://angular.io/guide/dependency-injection)

[Logging in Angular Applications](https://www.codemag.com/article/1711021/Logging-in-Angular-Applications)