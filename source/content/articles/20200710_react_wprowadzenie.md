Title: JavaScript: wprowadzenie do React'a
Author: mkostyrko
Date: 2020-07-10 10:00
Updated:
Category: reactjs
Tags: notacje obiektów, react
Slug: react-wprowadzenie
related_posts: 

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}



### Konfiguracja środowiska

Inicjalizacja projektu

    npm init -y

Przygotowanie Webpacka

    npm i webpack@4 --save-dev
    npm i webpack-cli@3 --save-dev
    npm i webpack-dev-server --save-dev

Dodanie do package.json skrótu uruchamiającego webpack-serwer

    "scripts": {
    [..],
    "start": "webpack-dev-server --hot -d"
  },

Przygotowanie Babel (core/preset-env/loader)
Babel loader pozwala na transpilację przy pomocy Webpacka -> [npm: babel-loader](https://www.npmjs.com/package/babel-loader)

    npm install -D babel-loader @babel/core @babel/preset-env webpack


Instalacja bable pod Reacta (nie jest wymagany jeśli nie używamy JSX)

    npm i @babel/preset-react --save-dev

Konfiguracja pliku konfiguracyjnego dla Bable -> .babelrc 

    {
    "presets": ["@babel/preset-env", "@babel/preset-react"]
    }

Instalacja Reacta (już nie jako deweloperska zalażność)

    npm i react@16.11.0 react-dom@16.11.0

Przygotowanie **webpack.config.js**

        const path = require("path");
        const entryPath = "sciezka_folderu";
        const entryFile = "sciezka_pliku.js";

        module.exports = {
        watch: true,
        entry: `./${entryPath}/${entryFile}`,
        output: {               // miejsce i nazwa zapisu pliku wyjściowego
            filename: "out.js",
            path: path.resolve(__dirname, `${entryPath}/build`)
        },
        devServer: {            // konfiguracja webpack serwera
            contentBase: path.join(__dirname, `${entryPath}`),
            publicPath: "/build/",
            compress: true,
            port: 3001
        },
        module: {               // dodanie babel-loader'a
            rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            }
            ]
        }
        };

---

Przygotowanie index.html do wczytania apki

        <!DOCTYPE html>
        <html lang="pl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>React</title>
        </head>
        <body>
            <div id="app"></div>
            <script src="build/out.js"></script>
        </body>
        </html>

---

Konfiguracja aplikacji pliku js

Import (app.js)

    Import React from "react"
    import ReactDOM from "react-dom" // tylko w głównym pliku aplikacji i tylko 1 raz

ReactDOM - renderuje/tworzy stronę

Schemat:
ReactDOM.render(element, miejsce)

    np.

      ReactDOM.render(
      <h1>This is not the droid you are looking for!</h1>,  // JSX
      document.getElementById("app")  // Miejsce
    );

Całość pliku przechowującego react-app np. app.js może wyglądać następująco 

    
    import React from "react";
    import ReactDOM from "react-dom";

    ReactDOM.render(
    <h1>This is not the droid you are looking for!</h1>,
    document.getElementById("app")
    );

---------

#### React i VSC

Dla tych co korzystają z VSC polecam dodać również bardzo przydatną informację do settings.json, która powoduje, że emmet działa również w plikach js

    "emmet.includeLanguages": {
        "javascript": "javascriptreact"
    }

---

### CDN

Alternatywnie do stosowania się do powyższej konfiguracji, można skorzystać z linków CDN, które wystarczy dodać do heada w pliku html
Warto jednak pamiętać, że są to zminifikowana wersja biblioteki React przygotowana jedynie do produkcji

    React ->

    <script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>

    Babel ->

    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

W takim przypadku należy pamiętać, że JS opakowany w tag scriptu powinien być posiadać typ -> text/bable `<script type="text/babel">`

Więcej na ten temat można przeczytać tutaj [React - CDN Links](https://reactjs.org/docs/cdn-links.html)

oraz w tym wpisie na blogu - gdzie jest pokazany bardziej rozbudowany przykład bez JSX [The 2-minute React app](https://frontarm.com/james-k-nelson/single-file-react-app/)

a tutaj o [UNPKG](https://unpkg.com/)

Przykładowe zastosowanie

<script src="https://gist.github.com/kostyrko/b9cff28fdb8a5dd45f106152ebacf15c.js"></script>

---

### Parę słówo o JSX

JSX nie jest ekskluzywny dla Reacta, ale został stworzony przez developerów z nim związanych - jest rozszerzeniem możliwości JS w tworzeniu HTML. Jest bardzo do niego zbliżony, ale też wybacza mniej błędów przy pisaniu tagów -> przykładowo każdy z nich musi być zamknięty a wartości muszą znajdować się pomiędzy apostrofami.

    <span id="droid">This is not the droid you are looking for!</span>

zamiast

    React.createElement(
      "span",
      {id: "droid"},
      "This is not the droid you are looking for!"
    );

Atrybuty w JSX różnią się od HTML używają 1) camelCase 2) dodają kolejny wyraz określający np. **class** -> **className** / **background-color** -> **backgroundColor**
W atrybutach mogą się również znaleźć wyrażenia JS zamknięte w nawiasach klamrowych 

    const style {
      backgroundColor: red;
    }

    <div style= {style}></div>

    <div padding={2+2}></div>


### React.Fragment -> o fragmentach słów parę 

JSX może przyjąć tylko jeden element -> stąd aby wyrenderować wiele elementów należy je opakować w jeden nadrzędny np. div, ale od React 1.6 można wykorzstywyać tzw Fragmenty, które są elementem "klamrowym", który nie generuje kolejnego elementu **<> element1 element2 ...element </>**

Można zaimportowania modułu "Fragment" z biblioteki "react"

    import React, {Fragment} from "react";

Wówczas wykorzystanie fragmentu wygląda następująco -> **<Fragment> element1 element2 ...element </Fragment>**

---

### Notacje obiektów w ES6 w kontekście JSX

Notacje w JS dostępnych od ES6 - ten system zapisu pozwala, na oszczędność kodu - JS potrafi odczytać zmienną jako deklarację CSS 

    const color = "red"

    button {       zamiast      button {
      color                         color: color;
    }                            }


Inną cechą, o której warto sobie przypomnieć w kontekście JSX jest operator spread/rozproszenia,
który nie tylko pozwala na tworzenie tablic, ale również na ich rozpraszanie, tak samo jak i obiektów np.

    const divSize = {
        width: '100px',
        marginTop: '20px'
    }

    const  blue = {                 zamiast         const blue = {
            backgroundColor:'blue',                     backgroundColor:'blue',
            ...divSize                                  width: '100px',
        }                                               marginTop: '20px'
                                                    }

---

Źródła:

[Podstawowe informacje](https://pl.reactjs.org/docs/getting-started.html)

[Samouczek: Wstęp do Reacta](https://pl.reactjs.org/tutorial/tutorial.html)

YT: 

[Wprowadzenie do biblioteki React.js](https://www.youtube.com/watch?v=DN73tm89cgU)

[React JS - kurs w 60 minut](https://www.youtube.com/watch?v=Qz7swLxNS0Y)
