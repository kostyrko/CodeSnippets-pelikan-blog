Title: Angular: serwisy
Author: mkostyrko
Date: 2021-04-11 10:00
Updated:
Category: angular
Tags: angular, serwis, service, subscribe, unfinished
Slug: angular-serwisy
related_posts:

![angular](https://i.stack.imgur.com/E8ItT.png)

### Angular serwisy

#### Wstęp

Dowolna klasa TS, wykonuje zadanie dostarczania danych na potrzeby komponentów (komunikacja z API, komunikacja pomiędzy komponentami, przechowywanie stanu aplikacji).
Serwis posiada swój dekorator @Injectable (wskauje na to, że jest serwisem + dane określające w jaki sposób działa serwis + użycie innych serwisów).


    @Injectable()
    export class LoggerService {
      log(msg: any) {console.log(msg);}
    }

Provider w deklaracji komponentu ===> providers: [LoggerService]

W kostruktorze -> dependency Injection (przygotowanie instancji obiektu i wstyrzknięcie jej do komponentu)


    @NgModule({
        imports: [ BrowserModule ],
        declarations: [ App, OtherComponent ],
        bootstrap: [ App ],
        providers: [ LoggerService ]
      })
      export class AppModule {
        constructor(private logger: LoggerService) {
        logger.log('Hello')
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


### Przykładowy projekt z zastosowaniem serwisu

Orginalne żródło poniższego projektu: [GH - ZacznijProgramowac/easy-words](https://github.com/ZacznijProgramowac/easy-words/tree/003-answer-component)

[Udemy -Angular - kompletny kurs od podstaw - edycja na rok 2021](https://www.udemy.com/course/angular-kompletny-kurs-od-podstaw)


<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/bcommit/7150e1ce3b29825f61b5a2320250c74ca1c9bfdf?branch=7150e1ce3b29825f61b5a2320250c74ca1c9bfdf&diff=split"></script>

**model danych** easy-words-app/src/app/data/models.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/data/models.ts"></script>


**dane/plik zastępujący bazę danych** easy-words-app/src/app/data/data-base.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/data/data-base.ts"></script>


**serwis** - easy-words-app/src/app/services/words.service.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/services/words.service.ts"></script>

**Komponent korzystający z serwisu** - easy-words-app/src/app/compontents/question/question.component.ts 

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/question/question.component.ts"></script>

easy-words-app/src/app/compontents/question/question.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/question/question.component.html"></script>


**Komponent korzystający z serwisu 2 - główny komponent przekazujący dane do dziecka (dump komponentu)**

easy-words-app/src/app/app.component.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/app.component.ts"></script>

easy-words-app/src/app/app.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/app.component.html"></script>


**Komponent przyjmujący dane od rodzica**  - easy-words-app/src/app/compontents/answers/answers.component.ts 

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/answers/answers.component.ts"></script>


easy-words-app/src/app/compontents/answers/answers.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/easy-words-app-noSubjects/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/answers/answers.component.html"></script>





---

Źródła:

[SO - Angular 2, How to Share Array Data Between components using service?](https://stackoverflow.com/questions/43585998/angular-2-how-to-share-array-data-between-components-using-service)

[Types of AngularJS Services with Examples – Creating/Registering Services](https://data-flair.training/blogs/angularjs-services/)

[ANGULAR 2 – Bidirectional Service](https://www.angular.love/2016/12/28/angular-2-bidrectional-service-komunikacja-komponentow-poprzez-serwis/)

[Czym jest serwis w Angularze?](https://zacznijprogramowac.net/angular-pytania/czym-jest-serwis-w-angularze/)

[Jak pozbyć się singletonów w Angularze?](https://www.p-programowanie.pl/angular/jak-pozbyc-sie-singletonow-w-angularze)

[angular.io -> Add services](https://angular.io/tutorial/toh-pt4)

[angular.io -> Dependency injection in Angular](https://angular.io/guide/dependency-injection)