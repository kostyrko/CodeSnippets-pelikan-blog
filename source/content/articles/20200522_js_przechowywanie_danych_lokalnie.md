Title: JavaScript - przechowywanie danych lokalnie oraz w sesji
Author: mkostyrko
Date: 2020-05-22 10:00
Updated: 2020-06-04 10:00
Category: javascript
Tags: js, javascript, local storage, przechowywanie danych lokalnie
Slug: js-przechowywanie-danych-lokalnie
related_posts: js-dom-elementy-selektory

Lokalna pamięć przeglądarki pozwala na przechowywanie danych przy pomocy JavaScript bezterminowo.

Dane przechowywane w lokalnej pamięci przeglądarki nie mogą przekroczyć 5mb i nie powinny znajdować się w nich dane poufne.
Lokalna pamięć przeglądarki działa w sposób synchroniczny (odpowiada na zapytania po kolei).


Aby korzystać z tzw `local storage` (LS) można wykorzystać jedną z 5 dostępnych metod.


| Metoda | główna cecha
|---|---|
| setItem() | Dodaj element (klucz oraz wartość)|
| getItem() | Zwraca element po kluczu|
| removeItem() | Usuwa element po kluczu |
| clear() | Czyści pamięć LS|
| key() | pozwala na pozyskanie klucza z obiektu znajdującego się z LS |

Przykładowe zastosowanie

    window.localStorage.setItem('droid', 'r2d2');

    window.localStorage.getItem('droid');

    >> "r2d2"

Istotne jest to że pamięć lokalna przeglądarki może przechowywać jedynie łańcuchy znaków (stringi) w tym również stringi JSON
stąd często stosuje się metody interpolujące obiekty lub tablice do tego formatu stosując metody `JSON.stringify()` zmień w JSON string oraz `JSON.parse()` (tworzy obiekt opisany przez JSON string)

    const newDroid = {
      name: "r2d2",
      type: "Astromech droid",
    }

    window.localStorage.setItem('newDroid', JSON.stringify(newDroid));

    window.localStorage.getItem('newDroid');

    >> "{"name":"r2d2","type":"Astromech droid"}"


Konwersja w obiekt

    JSON.parse(window.localStorage.getItem('user'));

    >> {name: "r2d2", type: "Astromech droid"}
        name: "r2d2"
        type: "Astromech droid"
        __proto__: Object


Przykładowe zastosowanie w aplikacji - zapisanie elementu jako częsci tablicy `tasks`

źródło kodu: [org repo](https://github.com/bradtraversy/modern_js_udemy_projects/blob/master/tasklist_project/app.js)

  function storeTaskInLocalStorage(task) {
    let tasks;
    if(localStorage.getItem('tasks') === null){
      tasks = [];
    } else {
      tasks = JSON.parse(localStorage.getItem('tasks'));
    }
    tasks.push(task);

    localStorage.setItem('tasks', JSON.stringify(tasks));
  }

usunięcie elementu z lokalnej pamięci

    function removeTaskFromLocalStorage(taskItem) {
      let tasks;
      if(localStorage.getItem('tasks') === null){
        tasks = [];
      } else {
        tasks = JSON.parse(localStorage.getItem('tasks'));
      }

      tasks.forEach(function(task, index){
        if(taskItem.textContent === task) {
          tasks.splice(index, 1);
        }
      });

      localStorage.setItem('tasks', JSON.stringify(tasks));
    }

---

Źródła:

http://kursjs.pl/kurs/storage/storage.php

https://blog.logrocket.com/the-complete-guide-to-using-localstorage-in-javascript-apps-ba44edb53a36/

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse