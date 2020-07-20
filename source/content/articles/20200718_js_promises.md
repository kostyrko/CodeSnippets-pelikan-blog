Title: JavaScript: promises
Author: mkostyrko
Date: 2020-07-18 10:00
Updated:
Category: nodejs
Tags: js, javascript, promises, ajax
Slug: js-promises
related_posts: js-xhr-rest, js-xhr, js-asynchronicznosc-ajax, js-fetch-api

![promises](https://bitsofco.de/content/images/2016/06/Creating-Promises.png){: max-height="300px"}


#### Obietnice/Promises

*Promises* zostały wprowadzone wraz z ES6, bez nich  asynchroniczność opierano na `callbackach`/*wywołaniach zwrotnych*. Obiekty *Promise* (obietnice) zakładają wykonanie pewnej czynności oraz zwrócenie rezultatu lub poinformowania o błędzie. Pozwala to na stworzenie takiego łańcucha kodu, który uzależnia wykonanie kolejnej funkcji od wyniku zwrotnego poprzedniej. Obiekt Promise może znajdować się w jednym stanie jednocześnie: `Pending` (wywołane i oczekuje), `Fulfilled` (wykonane z powodzeniem), `Rejected` (odrzucone z niepowodzeniem). Wprowadzenie *obietnic* pozwala na uniknięcie stosowania dużej ilości funkcji warunkowych.

**Użytkowanie.** 

W pierwszej kolejności należy stworzyć obiekt *Promise* (odwołując się do konstruktora obiektu Promise) w ramach, którego zachodzi asynchroniczność zwracająca jedną z dwóch funkcji. W przypadku sukcesu należy wywołać funkcję **resolve**, natomiast niepowodzenia **reject** (w niej zostaną przekazane błędne dane).

źródło poniższych przykładów: [kursjs.pl - Callback i Promise](http://kursjs.pl/kurs/ajax/promise.php)


        const load = new Promise((resolve, reject){
            if (readData) {
                resolve(data)
            } else {
                reject('error')
            }
        })


Po stworzeniu obiekt/instancji *Promise* znajduje się w stanie **Pending**, natomiast po wywołaniu się funkcji przechodzi w stan **Settled**, który w zależności wyniku przejdzie w status **Fulfilled** lub **Rejected**


Następnie na zwróconą funkcję należy zareagować (ang. consume), w tym celu można wykorzystać metod **.then()** **.catch()** [opisane poniżej]


        load
            .then(result => {
                console.log(result)
            })
            .catch(err => {
                console.log(err)
            })

---

### Metody .then() i .catch()

Metoda **.then()** pozwala na *zakolejkowanie* reakcji na status zwróconych danych (dowolnie pozytywny, negatywny lub oba). Innymi słowy jest to kod, który ma się wywołać po wywołaniu się funkcji będącej częścią obiektu *Promise* lub jeszcze inaczej po tym jak *obietnica* (Promise) zostanie zwrócona. *Then* można w tym kontekście przetłumaczyć jako *potem*.

        load.then(
            result => console.log(result),
            error => console.error(error)
        );


Metoda **.catch()** stosowana jest najczęściej do reakcji/przechwytywaniu ew. negatywnej odpowiedzi z serwera (reject)

        loadData()
            .then(result => console.log(result))
            .catch(error => console.error(error));

![promises-advanced](https://i.stack.imgur.com/UX8JM.png){: max-height="400px"}

---

### Metody .all() .race() i finally()

Metoda **.all()** pozwala na wywołanie reakcji po zwróceniu wszystkich *obietnic*


        Promise.all([
            checkData1(),
            checkData2()
        ])
            .then(resp => {.....}



Metoda **.race()** zwraca pierwszą zakończoną *obietnicę*



Metoda **.finally()** wywołuje działanie niezależnie od statusu zwróconej *obietnicy*


        .then(res => console.log(res))
            .catch(err => alert(err))
            .finally(() => {
                btnLoadMore.classList.remove("loading");
                btnLoadMore.disabled = false;
            });

---

Źródła:

[JavaScript Promises 101](https://bitsofco.de/javascript-promises-101/)

[kursjs.pl - Callback i Promise](http://kursjs.pl/kurs/ajax/promise.php)

