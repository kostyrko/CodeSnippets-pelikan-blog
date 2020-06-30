Title: JavaScript: XMLHttpRequest - wstęp (GET)
Author: mkostyrko
Date: 2020-06-30 10:00
Updated:
Category: javascript
Tags: javascript, js, ajax, rest, XMLHttpRequest, github, github api, api
Slug: js-xhr
related_posts: js-asynchronicznosc-ajax

![XMLHttpRequest](https://domscripting.com/presentations/fowa07/slides/images/page_xhr_server.jpg)

### XMLHttpRequest

XMLHttpRequest (XHR) służy do wykonywania dynamicznych (asynchronicznych) połączeń z serwerem
i jest wykorzystywany do 1) aktualizacji informacji zawartych na stronie internetowej 2) wysłania żadania danych do serwera po załadowaniu strony 3) przyjęcia informacji przesłanej przez serwer - po załadowaniu strony 4) przesłania danych do serwera (w tle).

Obecnie XHR został zastąpiony Fetch API.

---

### Wysyłanie żądania nastawione na odbiór danych

W pierwszej kolejności należy utworzyć obiekt XMLHttpRequest() odwołując się do notacji konstruktora typu XHR

    const xhr = new XMLHttpRequest();

Zastosowanie

    function seekUser() {
        const xhr = new XMLHttpRequest();
        [.........]
        }

A następnie zdefiniować połączenie za pomocą metody `open()` przygotowującej żadanie i przyjmującej 3 atrybuty 1) typ (połączenia -get, post, put, patch, delete), 2) url (adres) obsługujący żądanie, 3) definicję rodzaju połączenia (synchroniczne/false lub asynchroniczne/true)

    xhr.open('GET',`https://api.github.com/users/${inputTxt.value}`, true);

Konfigurację należy zakończyć metodą `send()` -> xhr.send(), która wysyła żądanie połączenia z serwerem, gdy dane nie są wysyłane (np. GET) wówczas argument domyślnie jest `null` / można również taką wartość wpisać, w przypadku wysyłania danych (POST) treść danych znajdzie się zamknięta pomiędzy nawiasami

    xhr.send(null)

Zastosowanie

    function seekUser() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://api.github.com/users/${inputTxt.value}`, true);
        [......]
        xhr.send(null);
    }

---

### Oczekiwanie

Oczekiwanie na informację zwrotną może trwać mniej lub więcej czasu, ale informacja zwrotna nie jest dostępna natychmiast

Po przesłaniu zapytania wywołana zostaje zdarzenie `onload` (w trakcie ładowania), do którego jest przypisana funkcja anonimowa odpowiedzialna za reakcję na zwróconą informację.

        xhr.onload = function() {
            if(this.status === 200) {...
        }

Istotnymi zdarzeniami są `load` (połączenie zakończone pozytywnie, zostały dane zwrócone), `error` (błąd w połączeniu), `progress` (połączenie trwa) + **abort**(anulowanie połączenia) **timeout**(przekroczenie czasu połączenia) **loadstart/loadend**(rozpoczęcie/zakończenie połączenia)

Zwrócone dane z serwera nie koniecznie muszą oznaczać jednoznacznie pozytywny wynik -> może zostać zwrócony status błędu 404(brak strony), 500(błąd serwisu), 401(forbidden), stąd walidacje. W przypadku zwrócenia danych o które zapytano status połączenia powinien wynosić **200**. Praktykowana jest prosta walidacja oparta na **if**

Zastosowanie

    gdzie ${inputTxt.value} nazwa użytkownika np. https://api.github.com/users/kostyrko

    function seekUser() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://api.github.com/users/${inputTxt.value}`, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
            [...]
            }
        }
        xhr.send(null);
    }

Oczekując na odpowiedź można skorzystać z typu odpowiedzi metod `onreadystatechange` (wyłapuje kiedy *readyState* ulega zmianie) i `readyState`, która wskazuje na stan przesyłania danych/komunikacji z serwerem - gdzie:

- 0 - oznacza zapytanie niewysłane (open() nie zostało wywołane)
- 1 - oznacza zapytanie wysłane (open() zostało wywołane)
- 2 - nagłówki zostały odebrane (send() zostało wywołane, są dostępne taka samo jak status połączenia)
- 3 - trwa pobieranie odpowiedzi (responseText - zawiera częściowe informacje),
- 4 - Operacja została zakończona

Zastosowanie

    function seekUser() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://api.github.com/users/${inputTxt.value}`, true);
        xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                [....]
                }
        }
        xhr.send(null);
    }

---

### Odpowiedź

Jeśli load dokona się z sukcesem (dojdzie do połączenia z serwerem) wówczas możemy wykorzystać istniejące metody obiektu **xml**:

- **response** - treść odpowiedzi (na ogół w formie tekstowej)
- **responseText** - zwraca odpowiedź jako tekst
- **responseXML** - - zwraca odpowiedź jako XML
- **status** - status połączenia
- **statusText** - status połączenia w formie tekstowej

Treść odpowiedzi w formie tekstowej pozwala np. na konwersję do postaci JSON (**JSON.parse**) 

Zastosowanie


    function seekUser() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://api.github.com/users/${inputTxt.value}`, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
            console.log(typeof xhr.response); // >> string
            console.log(xhr.response); // <dane>
            console.log(typeof xhr.responseText); // >> string
            console.log((JSON.parse(xhr.responseText)).email); // <email>
            }
        }
        xhr.send(null);
    }

---

#### Przykład zastosowania na podstawie GitHub API

<script src="https://gist.github.com/kostyrko/fa29df00eba1d3a044323150214c73e1.js"></script>


---

Źródła:

Duckett, Jon. Javascript and jquery: Interactive front-end web development. Wiley Publishing, 2014.

[kursjs.pl](http://kursjs.pl/kurs/ajax/xmlhttprequest.php)

[MDN-Using XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)

[How to make HTTP requests using XMLHttpRequest (XHR)](https://attacomsian.com/blog/http-requests-xhr#)

[Online Multimedia Tutorial 02 – AJAX, Ludwig-Maximilians-Universität München](http://www.medien.ifi.lmu.de/lehre/ws1920/omm/uebung/folien/OMM-02-AJAX.pdf)
