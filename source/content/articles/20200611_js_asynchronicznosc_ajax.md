Title: JavaScript: asynchroniczność i AJAX
Author: mkostyrko
Date: 2020-06-11 12:00
Updated:
Category: javascript
Tags: javascript, js, asynchroniczność, call stack, Web Api, obietnice, promises, callback, promise
Slug: js-asynchronicznosc-ajax
related_posts: js-xhr

![ajax](https://miro.medium.com/max/700/1*v3b022s2UAyhVAFLUtzhJg.png)


### Wstęp

JavaScript w swoim założeniu jest jednowątkowa, kod wywoływany jest w sposób synchroniczny (linia po linii), w zestawieniu z node.js lub przeglądarką internetową może stać się asynchroniczna (kod dalej jest wywołany po kolei, ale jego elementy nie zatrzymają wywołania się reszty kodu np. w przypadku obiektu Window i metody setTimeout(opóźnienie wywołania się bloku kodu))- jest to przydatne w przypadku odwołań do serwerów, gdzie zwrócenie określonych danych może trwać dłuższy moment np. w przypadku Fetch API (kod odpowiedzialny za funkcjonowanie strony będzie dalej funkcjonował poprawnie w trakcie wysyłania i odbierania zapytania). Patrz też dalej [ajax](#ajax)

**Podsumowując - asynchroniczność pozwala na:**

* Zmianę zawartości części strony bez konieczności jej odświeżenia

* Wysłanie żadania zwrotu danych na serwer

* Odebranie danych przesłanych przez serwer

* Wysłanie danych na serwer



#### Jak to działa? - istotne etapy/wyrażenia

**Stos wywołań**/*Call stack* - miejsce, w które trafiają wywołania funkcji (kolejność, w której tam trafiają ma znaczenie na ich wywoływanie) i z którego są ściągane w momencie ich ukończenia.

**Web API** - tu trafiają asynchroniczne operacje (np. setTimeout) i są wykonywane - po wykonaniu trafia do **kolejki wywołań zwrotnych**/*Callback queue* oraz czeka na moment, w którym może zostać wprowadzony na stronę internetową.

**Pętla wydarzeń**/*Event loop* - funkcja sprawdzająca czy Stos wywołań jest pusty i w momencie, gdy ten warunek zostaje spełniony przenosi wywołania z kolejki **wywołań zwrotnych** (ang. callback) do *stosu wywołań* i wówczas funkcja jest wywoływana

![event-loop](https://www.oreilly.com/library/view/learning-nodejs-development/9781788395540/assets/74fbf540-71b8-499a-a7cf-2da14ed034de.jpg)

----

### Wyjście z piekła wywołań zwrotnych/ callback hell

Callback jest informacją zwrotną wynikającą z wywołania funkcji, ta może posłużyć jako parametr/agrument wywołania kolejnej funkcji (funkcja zagnieżdżona w wywołaniu funkcji) umożliwia to uzależnienia kolejnego działania od zwrotu działania funkcji poprzedzającej - wywołanie się funkcji wewnętrznej było uzależnione od wywołania funkcji wyższego rzędu. Wielokrotne zagnieżdżenie wywołań zwrotnych (ang. callback), trudne do opanowania oraz utrzymania, nazywane jest `callback hell`

        function renderPage = function() {
            getFirstData(function(x) {
                getAnotherData1(x, function(y) {
                    getAnotherData2(y, function(z) {
                        getAnotherData3(z, function() {
                            [...]
                        });
                    });
                });
            });


Przykład za: [kursjs.pl - Callback i Promise](http://kursjs.pl/kurs/ajax/promise.php)

---

#### Obietnice/Promises

*Promises* zostały wprowadzone wraz z ES6, bez nich  asynchroniczność opierano na `callbackach`/*wywołaniach zwrotnych*. Obiekty *Promise* (obietnice) zakładają wykonanie pewnej czynności oraz zwrócenie rezultatu lub poinformowania o błędzie i może znajdować się w jednym stanie jednocześnie: `Pending` (wywołane i oczekuje), `Fulfilled` (wykonane z powodzeniem), `Rejected` (odrzucone z niepowodzeniem). Wprowadzenie *obietnic* pozwala na uniknięcie stosowania funkcji warunkowych.

Schemat kodu w przypadku Fulfilled


    Promise(treść-obietnicy).then(result=>{
        //rezultat do wykonania
    })

Schemat kodu w przypadku Rejected

    Promise(treść-obietnicy).catch(error=>{
        //zwraca błąd
    })

---

#### Async oraz await

`async` oraz `await` wprowadzono w ES7 i ich zadaniem jest dalszy rozwój asynchroniczności w JavaScript -> pozwala na zapis asynchronicznego kodu w sposób przypominający synchroniczny

`async` oznacza funkcję, która zwraca obietnicę/promise

`await` słowo kluczowe stosowane wewnątrz funkcji `async` - program czeka z wywołaniem kolejnej linii do spełnienia warunku związanego z zakończeniem akcji asynchronicznej znajdującej się po za słowem kluczowym `await`

[syntactic sugar]

---

#### Istotne wyrażenia:

Sposób łączenia się z serwerem tzw. WEB API: AJAX -> XMLHttp oraz Fetch API

Przykładowe sposoby/formaty przechowywania danych na serwerze: XML, JSON ... HTML, YAML

Standard łączenia się z serwerem oraz wymiany informacji: REST API

---
![ajax](https://i.pinimg.com/originals/e4/e9/fc/e4e9fc856f0ee78ce86696e5729ab1d2.png)

### AJAX {#ajax}


**AJAX - Asynchronous JavaScript And XML/ Asynchroniczny JS i XML** - umożliwia wykorzystanie XML (obiektów XMLHttpRequest) do komunikacji z serwerem - w ten sposób zbudowana strona internetowa może funkcjonować w sposób asynchroniczny (wcześniej serwer zwracał HTML + dane - w modelu AJAX XML+ dane jest przetwarzany na HTML + dane przy pomocy JS).

Początkowo (w momencie stworzenia AJAX) formatem, w którym dane przesyłano był XML (długi zapis - składnia może być dłuższa od przechowywanych danych, wydzielenie danych z XML przypomina ten z DOM), który z czasem został zastąpiony przez JSON (bardziej przyjazny format/przypomina obiekty JS)

**Protokół HTTP **- Hypertext Transfer Protocol - protokół zapewniający komunikację w sieci internet. [Zapytanie z przeglądarki (powtarzane w trakcie korzystania ze strony) trafiają na serwer DNS (Domain Name System) -> serwer w Internecie -> Zwracana odpowiedź (Składa się na nią Status odpowiedzi, 0 lub więcej nagłówków, Ciało odpowiedzi/body)

![HTTP/XML-Request](https://derivadow.files.wordpress.com/2007/01/ajax.png?w=506&h=309)

Możliwe statusy odpowiedzi (wybrane)

| Numer | Znaczenie
|---|---|
| **200** | połączenie zakończyło się sukcesem |
| **301** | strona przeniesiona na inny adres |
| **404** | strona nie istnieje |
| **500** | błąd serwera|


Typy połączenia

| Typ | Znaczenie
|---|---|
| **GET** | pobierani danych |
| **POST** | wysyłanie danych |
| **PUT** | zmiana obiektu w bazie danych |
| **PATCH** | edycja pojedynczej właściwości obiektu w bazie danych |
| **DELETE** | usunięcie danych |


---

Źródła:

Duckett, Jon. Javascript and jquery: Interactive front-end web development. Wiley Publishing, 2014.

[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

[Jak działa asynchroniczność w JavaScript](https://www.youtube.com/watch?v=MD1euJQQkLQ)

[Event Loop a kolejność wykonywania kodu w JavaScript](https://bit.ly/3cUHuT0)


[Asynchroniczność w JavaScript](https://fsgeek.pl/post/asynchronicznosc-w-javascript/)

[Jak pozbyć się callback hell za pomocą promisów?](https://www.nafrontendzie.pl/jak-pozbyc-sie-callback-hell)

[Callback i Promise](http://kursjs.pl/kurs/ajax/promise.php)

[Async / await](http://kursjs.pl/kurs/ajax/async-await.php)

[AJAX what is it? (it’s not DHTML)](https://derivadow.com/2007/01/05/ajax-what-is-it-its-not-dhtml/)

[How to Use Async/Await to Write Better JavaScript Code](https://www.freecodecamp.org/news/how-to-use-async-await-write-better-javascript/)

[AJAX - kursjs.pl](http://kursjs.pl/kurs/ajax/ajax.php)

[AJAX - getting started - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started)
