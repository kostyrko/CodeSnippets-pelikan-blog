Title: Angular i RxJS oraz Observable
Author: mkostyrko
Date: 2021-04-18 10:00
Updated:
Category: angular
Tags: angular,rxjs, observable, unfinished
Slug: angular-rxjs-observable
related_posts:

![angular+rxjs](https://miro.medium.com/max/5872/1*rcewo8BQLzUc_fI-_O7S_w.png)

### Bilbioteka RxJS

Programowani reaktywne - paradygmat programowani oparty na zdarzeniach (strumieniach danych oraz zmianach zachodzących w tych strumieniach - min. wymiana danych przy pomocy równoległych strumieni).

RxJs - biblioteka do reaktywnego programowania, w Angularze wykorzystywana (domyślnie) w kontekście routingu, zapytań do bazy danych (HTTP), formularzy. Pełni istotną funkcję w kontekście obsługi asynchroniczności oraz eventów. Jej składową jest obiekt **Observable**

**Observable** (strumień danych) różni się od Promise tym, że może być zwracany wielokrotnie, udostępnia metody do filtrowani i operowania przesyłanymi danymi (metody pipe -  do modyfikowania).


### Observable

Obiekt observable **wymaga subskrypcji** aby otrzymywać od niego dane. Na obiekcie observable należy wywołać metodę **subscribe** w ramach, której można przekazać funkcję (callbecki, które wykonają się w momencie gdy dostaną dane). **Subscribe** - może zwrócić wiele wyników rozłożonych w czasie.
Funkcja **of()** tworzy z tablicy/listy obiekt typu Observable - przeciwieństwem jest funkcja **from()**, która rozbija listę i przekazuje elementy pojedynczo.

W ten sposób stworzony observable będzie dla każdego subskrybenta nowym obiektem (każdy komponent dostaje te same dane). W przypadku **subject** (przedstawione poniżej) jest to jeden obiekt przekazywany wielu obserwatorom (część elementów może nie zdążyć przyjąć danych).

    import { of, form, Observable} form "rxjs";

    const droids = ['c3po', 'r2d2', 'bb8']

    const observable: Observable<string[]> = of(droids);

    observable.subscribe(x => console.log(x))


(Observable - rxjs-dev.firebaseapp.com)[https://rxjs-dev.firebaseapp.com/api/index/class/Observable]


(from - www.learnrxjs.io)[https://www.learnrxjs.io/learn-rxjs/operators/creation/from]


### Observable w Angularze

[**Operatory**](https://rxjs-dev.firebaseapp.com/guide/operators) RxJs pozwalają na pracę z danymi (ale nie ich modyfikację) w obiekcie [**Observable**](https://rxjs-dev.firebaseapp.com/guide/observable)

W środku metody [pipe](https://rxjs-dev.firebaseapp.com/api/index/function/pipe) wstawia się operatory, istnieje możliwość dodania kolejnych obserwatorów po przecinku.


    observable.pipe(
      filter(x => x.length > 0 ),
      toArray() // zmienia dane w listy
    ).subscribe( x => console.log(x))

### Subject (typ Observable)

Subject jest typem Observable i pozwala dzielić dane na wiele elementów (np. pomiędzy komponenty i serwisy).
Dostarczenie (seedowanie) danych do obiektu **subject** można przy pomocy metody **next()**

    // nowy obiekt subject oraz typ, na którym będzie pracował
    const subject = new Subject<number>();
    // subskrypcja z obiektu subject
    subject.subscribe( x => console.log('Subject: ', x));
    // dostarczenie danych, powyższy kod zareaguje na pojawienie się danych
    subject.next(0);

Może zdążyć się tak, że informacje inicjalizacyjne zostają przekazane do komponentu zanim ten się zbuduje, a po jego stworzeniu brak danych (dane nie są przekazane). Alternatywnie można użyć **Behavior subject** gdzie komponenty nawet gdy później załadowane będą otrzymywać dane.

##### Behavior subject

**Behavior subject** wymaga zainicjowania z określoną już wartością (null lub undefined również jest możliwe). W odróżnieniu od zwykłego subjectu oznacza to, że otrzymuje się wartość startową. **Behavior subject** przekaże zawsze ostatnią wartość jaka się pojawiła.

    const subjectBehavior = new BehaviorSubject<string>('r2d2');
    subject.subscribe( x => console.log('Subject: ', x));

Inne subjecty: **ReplaySubject** (def buforu), **AsynSubject** (ostatnia wartość wykonania obserwacji jest przekazana ale dopiero po jej wykonaniu)

#### Subscribe

Obiekt **subscribe** jest otrzymywany po wywołaniu metody subscribe na **Observable** // przechwytywanie poprzez przypisanie zmiennej i przypisanie tego co zwraca metoda subscribe

    // zwraca obiekt subscribe (isStopped: false // subskrypcja trwa)
    const subscribe = subjectBehavior.subscribe(x => console.log('BehaviorSubject: ', x));

#### Unsubscribe

Unsubscribe - metoda służąca do anulowania/zaprzestania subskrypcji (w przypadku Angulara np na ngOnDestroy)

**Observable** z formularzy, routingu, subjectu bez anulowania subskrypcji będą zajmowały pamięć (z HTTP kończą działanie jak przekażą dane). Observable stworzony wykorzystując metodę **from()** nie muszą być usuwane (subskrypcja jest zamknięta), przy pomocy **interval()** będzie tego wymagał.

    subscribe.unsubscribe();

-----------

### Przykładowy projekt z zastosowaniem serwisu wykorzystujący obiekt 'subject'

::: Orginalne żródło poniższego projektu: [GH - ZacznijProgramowac](https://github.com/ZacznijProgramowac/)

[Udemy -Angular - kompletny kurs od podstaw - edycja na rok 2021](https://www.udemy.com/course/angular-kompletny-kurs-od-podstaw)

#### Projekt porównujący zachowanie **subject** oraz **Behavior subject** => [peoples-list-subjects-app](https://github.com/kostyrko/JS-sandbox/tree/master/7_Angular/peoples-list-subjects-app)


#### Projekt easy-words bazujący na Subjects:

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/bcommit/7150e1ce3b29825f61b5a2320250c74ca1c9bfdf?branch=7150e1ce3b29825f61b5a2320250c74ca1c9bfdf&diff=split"></script>

**model danych** easy-words-app/src/app/data/models.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/data/models.ts"></script>


**dane/plik zastępujący bazę danych** easy-words-app/src/app/data/data-base.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/data/data-base.ts"></script>


**serwis** - easy-words-app/src/app/services/words.service.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/services/words.service.ts"></script>

**Komponent korzystający z serwisu** - easy-words-app/src/app/compontents/question/question.component.ts 

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/question/question.component.ts"></script>

easy-words-app/src/app/compontents/question/question.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/question/question.component.html"></script>


**Komponent korzystający z serwisu 2 - główny komponent przekazujący dane do dziecka (dump komponentu)**

easy-words-app/src/app/app.component.ts

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/app.component.ts"></script>

easy-words-app/src/app/app.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/app.component.html"></script>


**Komponent przyjmujący dane od rodzica**  - easy-words-app/src/app/compontents/answers/answers.component.ts 

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/answers/answers.component.ts"></script>


easy-words-app/src/app/compontents/answers/answers.component.html

<script src="http://gist-it.appspot.com/github.com/kostyrko/JS-sandbox/blob/master/7_Angular/angular-easy-words/easy-words-app/src/app/compontents/answers/answers.component.html"></script>


---

Źródła:

[RxJS - dokumentacja](https://rxjs-dev.firebaseapp.com/guide/overview)

[GH - ReactiveX/rxjs](https://github.com/ReactiveX/rxjs)


[RxJS z Angularem - programowanie reaktywne aplikacji frontendowej](shorturl.at/nqP46)


[RxJS w Angular – co wypada wiedzieć](https://www.angular.love/2018/07/04/rxjs-w-angular-co-wypada-wiedziec/)

[https://kamilmysliwiec.com/rxjs-hot-vs-cold-observable-operator-create](https://kamilmysliwiec.com/rxjs-hot-vs-cold-ob