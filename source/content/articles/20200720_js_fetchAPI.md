Title: JavaScript i  Fetch API
Author: mkostyrko
Date: 2020-06-20 10:00
Updated:
Category: javascript
Tags: javascript, js, node.js, fetch, fetch api,
Slug: js-fetch-api
related_posts: js-promises, js-xhr-rest, js-xhr, js-asynchronicznosc-ajax

![fetch-api](https://css-tricks.com/wp-content/uploads/2018/07/dog-fetch.png){: max-height="300px"}


Fetch jest API/interfejsem należącym do przeglądarki, ale jest również dostępny przy pomocy node.js -> `import fetch from 'node-fetch'`, który pozwala na asynchroniczne pobieranie danych z serwera.

Fetch bazuje na *obietnicach* -> Zwraca zapytanie HTTP jako obietnicę tego zapytania. W momencie wykorzystania metody **fetch()** tworzony jest obiekt typu Promise - oznacza to, że umożliwia korzystania z metod związanych z obiektami Promise np. **.then()** i **.catch()**

Podstawową metodą *Fetch API* jest **fetch()** która przyjmuje adres parametr, przyjmując, że domyślną metodą jest **GET** (jeśli chcemy wykorzystać inną metodę, wówczas musimy skorzystać z opcji dodatkowych argumentów, które można przekazać do metody *fetch* - o tym niżej)

    fetch('https://jsonplaceholder.typicode.com/posts/2')
      .then(response => console.log(response));

Odpowiedź z serwera zawiera wiele informacji np. informacje o statusie odpowiedzi, headery, typ, url czy **body**

W pierwszej kolejności będzie to


    Promise {<pending>}
    __proto__: Response
    [[PromiseStatus]] : "fulfilled"
    [...]


Następnie...


    Response {
      body: (...),          <- ciało odpowiedzi
      bodyUsed: false
      headers: Headers {}
      ok: true
      status: 200,          <- status połączenia
      statusText: ""        <- status połączenia jako tekst
      type: "cors"          <- typo połączenia
      url: "https://jsonplaceholder.typicode.com/posts/2",
      __proto__: Response
    }




Knyf z **fetch** polega na tym, że error nie będzie przechwytywany automatycznie przez metodę **catch()** w momencie gdy serwer działa, stąd wymaga sprawdzenia/walidacji informacji zwrotnej przy pomocy funkcji warunkowej

    fetch('https://jsonplaceholder.typicode.com/posts/2')
      .then(response => {
        if (response.ok) {
          console.log(response)
        } else {
          console.log('not successful')
        }
      })

Właściwość **ok** metody **fetch()** zastosowana powyżej zwraca wartość logiczną (tylko odczyt) i zwraca **True** jeśli treść odpowiedzi zawiera się w przedziale **200-299**

Wyżej zaprezentowany zapis może również przyjąć formę wykorzystującą **obietnicę** i wówczas również możemy wykorzystać metodę **catch()**



    fetch("https://jsonplaceholder.typicode.com/posts/2")
    .then(response => {
        if (response.ok) {
            return response.json()
        } else {
            return Promise.reject(response)
        }
    })
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        if (error.status === 404) {
            console.log("ERROR 404");
        }
    });
 

---

### Body i jego metody

Body jest właściwością informacji zwrotnej (ang. response) fetch i w niej zawarte są dane, na których pozyskaniu może nam zależeć.

**.json()** - przyjmuje informację zwrotną zapytania i zwraca obietnicę jako rezultat sparsowanego ciała tekstu w formacie JSON

    fetch('https://jsonplaceholder.typicode.com/posts/2')
      .then(response => response.json())
      .then(json => console.log(json));

Przy pomocy powyższego kodu, przyjmujemy dane z serwera, odpowiedź zostaje ciało odpowiedzi zostaje przemienione na obiekt json a ten zostaje przekazany do konsoli

**.text()** - zwraca odpowiedź w formie tekstu

**.formData()** - zwraca odpowiedź w formie FormData

**.blob()** - zwraca odpowiedź jako dane binarne z tyułem

**arrayBuffer()** - zwraca odpowiedź jako ArrayBuffer ("buffer z surowymi danymi binarnymi o niezmiennej długości" -> [ArrayBuffer - developer.mozilla.org](https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Obiekty/ArrayBuffer))

---

### Fetch i POST/GET/PUT

Podobnie jak w przypadku XMLHttpRequest wysyłanie danych wymaga przekazanie **1)** słowa kluczowego wskazującego na konkterntą metodę (np. POST), **2)** odpowiedniego nagłówka/headers **3)** oraz przekazania treści w body, które zostanie zamienione w obiekt typu JSON (stringify())

    fetch('https://reqres.in.api.users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: 'User 1'
      })
    }).then(response => {
      return response.json()
    })
      .then(data => console.log(data))

Ten format można zapisać również w następujący sposób

    const url = 'https://reqres.in.api.users'

    const data = {
      name: 'User 1',
    }

    const options = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
          'Content-Type': 'application/json'
      }
    };

    fetch(url, options)
      .then(response => response.json())
      .then(data => console.log(data))


Fetch API posiada również interfejs Headers() -> [Headers - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Headers)


Istnieje również możliwość wysyłanie danych w postaci URL jeśli serwer, z którego korzystamy nie wymaga nagłówka wówczas...

Przykład za [kurjs.pl - Fetch API](http://kursjs.pl/kurs/ajax/fetch.php)

  fetch(url, {
        method: "post",
        body: uriEncode("name=Marcin&surname=Nowak")
    })
    .then(res => res.json())
    .then(res => {
        console.log("Dodałem użytkownika:");
        console.log(res);
    })


---

Źródła:

[Fetch API - kursjs.pl](http://kursjs.pl/kurs/ajax/fetch.php)

[Fetch API - devenv.pl](https://devenv.pl/fetch-api/#:~:text=Fetch%20API%20jest%20interfejsem%20pozwalaj%C4%85cym,z%20obiektu%20XMLHttpRequest%20(XHR))


[How to use the Fetch API in JavaScript - attacomsian.com](https://attacomsian.com/blog/javascript-fetch-api)

MDN web docs

[Response.ok](https://developer.mozilla.org/en-US/docs/Web/API/Response/ok)

[Body](https://developer.mozilla.org/en-US/docs/Web/API/Body)

Filmy

[Learn Fetch API In 6 Minutes](https://www.youtube.com/watch?v=cuEtnrL9-H0)
