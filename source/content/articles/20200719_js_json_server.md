Title: JavaScript: json i json-server
Author: mkostyrko
Date: 2020-07-19 10:00
Updated:
Category: javascript
Tags: js, javascript, json, json-server, readFile, require, node
Slug: react-wprowadzenie
related_posts: 

![json](http://www.webcyou.com/wp-content/uploads/2017/07/json-logo.png){: max-height="300px"}



### JSON - JavaScript Object Notation

Format JSON zbliżony jest do obiektów znanych z JS,  z tą zasadą, że `nazwy kluczy wpisuje się w PODWÓJNY cudzysłów`, kolejne wpisy oddzielone są przecinkami a same pliki JSON przechowują jedynie dane (żadnych funkcji). Praca z plikami typu JSON przypomina te znane z obiektów JS,  stąd odwołujemy się do obiektów oraz ich poszczególnych części stosując klucze. Można np. stosować na nie destrukturyzacji.

#### stringify i parse

---

### JSON-server

JSON-server jest narzędziem pozwalające na stworzenie lokalnego serwera przy pomocy, którego można symulować REST API. Rozwiązanie to w całości oparte jest na zapisanym lokalnie pliku typu JSON

Instalacja (globalna - może wymagać -> sudo)

        npm install json-server -g

Wykorzystanie - uruchomienie. W terminalu należy wpisać słowo kluczowe json-server dodać flagę watch oraz podać ścieżkę zapisu pliku json

        json-server --watch sciezka/do/pliku.json


Przykładowo


        json-server --watch ./jsServer/starWars.json


Użytkowanie. W przeglądarce należy uruchomić adres

    http://localhost:3000/
    lub 
    http://localhost:3000/nazwa_obiektu


Przykładowo


    http://localhost:3000/droids
    http://localhost:3000/planets


gdzie zawartość pliku json wygląda przykładowo:

        {
            "droids" : [
                {
                    "id" : 0,
                    "name" : "D-O",
                    "class" : "unknown"
                },
                {
                    "id" : 1,
                    "name" : "BB-8",
                    "class" : "Astromech droid"
                }
            ],
            "planets" : [
                {
                    "id" : 0,
                    "planet" : "Tatooine",
                    "sector" : "Arkanis sector"
                },
                {
                    "id" : 1,
                    "planet" : "Coruscant",
                    "sector" : "Coruscant subsector"
                }
            ]
        }



---

### JSONPlaceholder

Na bazie JSON-servera działa onlinowe REST API stworzone również do testowania aplikacji -> JSONPlaceholder

więcej na temat jego działania można przeczytać tutaj [JSONPlaceholder - Guide](http://jsonplaceholder.typicode.com/guide.html)

---

Źródła:

Rauschmayer, A. (2014). Speaking JavaScript: an in-depth guide for programmers. " O'Reilly Media, Inc.".

Duckett, Jon. Javascript and jquery: Interactive front-end web development. Wiley Publishing, 2014.

[](http://kursjs.pl/kurs/ajax/server-lokalny.php)

[](https://blog.codingblocks.com/2018/reading-json-files-in-nodejs-require-vs-fs-readfile/)


[JSON - wszystko co musisz o nim wiedzieć](https://www.youtube.com/watch?v=haY