Title: JavaScript: json i json-server
Author: mkostyrko
Date: 2020-07-19 10:00
Updated:
Category: nodejs
Tags: js, javascript, json, json-server, readFile, require, node, stringify, parse
Slug: js-json-server
related_posts: js-promises, js-xhr-rest, js-xhr, js-asynchronicznosc-ajax, js-fetch-api

![json](http://www.webcyou.com/wp-content/uploads/2017/07/json-logo.png){: max-height="300px"}



### JSON - JavaScript Object Notation

Format JSON zbliżony jest do obiektów znanych z JS,  z tą zasadą, że `nazwy kluczy wpisuje się w PODWÓJNY cudzysłów`, kolejne wpisy oddzielone są przecinkami a same pliki JSON przechowują jedynie dane/zmienne (żadnych funkcji/kodu wykonywalnego). Praca z plikami typu JSON przypomina te znane z obiektów JS,  stąd odwołujemy się do obiektów oraz ich poszczególnych części stosując klucze. Wartości zawarte w JSONie mogą być zapisane w postaci **łańcucha znaków, liczby lub wartości logicznej** (false, null, true), te natomiast mogą składać się na **tablicę** lub **obiekt**, które mogą być dowolnie zagnieżdżone

Przykład (za [wikipedia.org](https://pl.wikipedia.org/wiki/JSON))


        {
            "menu": {
                "id": "file",
                "value": "File",
                "popup": {
                "menuitem": [
                    {"value": "New", "onclick": "CreateNewDoc()"},
                    {"value": "Open", "onclick": "OpenDoc()"},
                    {"value": "Close", "onclick": "CloseDoc()"}
                ]
                }
            }
        }


#### stringify i parse

Dwie istotne metody w kontekście JSONa, które są warte zapamiętania to `JSON.stringify()` oraz `JSON.parse()`

**JSON.stringify()** - zmienia obiekt JS w do łańcucha znaków JSON (przyjmuje również argumenty jeśli jakieś wymiana określonych wartości jest wymagana)

        console.log(JSON.stringify(new Date(2020, 07, 20, 15, 4, 5)));
        // >> ""2020-07-20T15:04:05.000Z""

**JSON.parse()** - zmienia/parsuje łańcuch znaków JSON tworząc wartość JS lub obiekt JS

        const json = '{"name": "BB-8", "class": "Astromech droid"'};
        const obj = JSON.parse(json);

        console.log(obj.name);
        // >> BB-8

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

[Serwer lokalny i json-server](http://kursjs.pl/kurs/ajax/server-lokalny.php)

[Reading json files in NodeJS: require() vs fs.readFile()](https://blog.codingblocks.com/2018/reading-json-files-in-nodejs-require-vs-fs-readfile/)


[JSON - wszystko co musisz o nim wiedzieć](https://www.youtube.com/watch?v=haY)