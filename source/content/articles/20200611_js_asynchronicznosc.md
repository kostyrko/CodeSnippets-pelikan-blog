Title: JavaScript: asynchroniczność i XML -> AJAX
Author: mkostyrko
Date: 2020-06-05 10:00
Updated:
Category: javascript
Tags: javascript, js, asynchroniczność, call stack, Web Api, obietnice, promises
Slug: js-asynchronicznosc
related_posts:

### Wstęp

JavaScript w swoim założeniu jest jednowątkowa, kod wywoływany jest w sposób synchroniczny (linia po linii), w zestawieniu z node.js lub przeglądarką internetową może stać się asynchroniczna (kod dalej jest wywołany po kolei, ale jego elementy nie zatrzymają wywołania się reszty kodu np. w przypadku obiektu Window i metody setTimeout(opóźnienie wywołania się bloku kodu))- jest to przydatne w przypadku odwołań do serwerów, gdzie zwrócenie określonych danych może trwać dłuższy moment np. w przypadku Fetch API (kod odpowiedzialny za funkcjonowanie strony będzie dalej funkcjonował poprawnie w trakcie wysyłania i odbierania zapytania)

**Stos wywołań**/*Call stack* - miejsce, w które trafiają wywołania funkcji (kolejność, w której tam trafiają ma znaczenie na ich wywoływanie) i z którego są ściągane w momencie ich ukończenia.

**Web API** - tu trafiają asynchroniczne operacje (np. setTimeout) i są wykonywane - po wykonaniu trafia do **kolejki wywołań zwrotnych**/*Callback queue* oraz czeka na moment, w którym może zostać wprowadzony na stronę internetową.

**Pętla wydarzeń**/*Event loop* - funkcja sprawdzająca czy Stos wywołań jest pusty i w momencie, gdy ten warunek zostaje spełniony przenosi wywołania z kolejki **wywołań zwrotnych** do *stosu wywołań* i wówczas funkcja jest wywoływana

![event-loop](https://www.oreilly.com/library/view/learning-nodejs-development/9781788395540/assets/74fbf540-71b8-499a-a7cf-2da14ed034de.jpg)


### Obietnice/Promises

*Promises* zostały wprowadzone wraz z ES6, wcześniej  asynchroniczność opierano na `callbackach`/*wywołaniach zwrotnych* (funkcjach zagnieżdżonych w funkcjach) - wywołanie się funkcji wewnętrznej było uzależnione od wywołania funkcji wyższego rzędu. Obiekty *promises* (obietnice) zakładają wykonanie pewnej czynności oraz zwrócenie rezultatu lub poinformowania o błędzie i może znajdować się w jednym stanie jednocześnie: `Pending` (wywołane i oczekuje), `Fulfilled` (wykonane z powodzeniem), `Rejected` (odrzucone z niepowodzeniem)

Schemat kodu w przypadku Fulfilled


    Promise(.treść-obietnicy.).then(result=>{
        //rezultat do wykonania
    })

Schemat kodu w przypadku Fulfilled

    Promise(.treść-obietnicy.).catch(error=>{
        //zwraca błąd
    })

### Async oraz await

`async` oraz `await` wprowadzono w ES7 i ich zadaniem jest dalszy rozwój asynchroniczności w JavaScript -> pozwala na zapis asynchronicznego kodu w sposób przypominający synchroniczny

`async` oznacza funkcję, która zwraca obietnicę/promise

`await` słowo kluczowe stosowane wewnątrz funkcji `async` - program czeka z wywołaniem kolejnej linii do spełnienia warunku związanego z zakończeniem akcji asynchronicznej znajdującej się po za słowem kluczowym `await`



---

Źródła:

Duckett, Jon. Javascript and jquery: Interactive front-end web development. Wiley Publishing, 2014.

[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

[Jak działa asynchroniczność w JavaScript](https://www.youtube.com/watch?v=MD1euJQQkLQ)

[Event Loop a kolejność wykonywania kodu w JavaScript](https://bit.ly/3cUHuT0)


[Asynchroniczność w JavaScript](https://fsgeek.pl/post/asynchronicznosc-w-javascript/)

http://jsdn.pl/asynchronicznosc-javascript-dla-poczatkujacych/



