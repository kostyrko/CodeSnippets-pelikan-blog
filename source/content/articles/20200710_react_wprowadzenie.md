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

Przygotowanie **webpack.config.js** więcej na ten temat patrz: [Webpack - krótkie wprowadzenie](https://kostyrko.github.io/zfrontu/js-webpack.html)

        const path = require("path");
        const entryPath = "1_hello_world/js";
        const outPath = "1_hello_world";
        const entryFile = "app.js";

        module.exports = {
        watch: true,
        entry: `./${entryPath}/${entryFile}`,
        output: {
            filename: "out.js",
            path: path.resolve(__dirname, `${outPath}/build`) // folder wyjściowy/zapisu
        },
        devServer: {
            contentBase: path.join(__dirname, `${outPath}`),    // ścieżka gdzie znajduje się statyczna treść np. index.html (path.join by stworzyć absolutną ścieżkę)
            publicPath: "/build/",
            compress: true,
            port: 3001
        },
        module: {
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

Aby zobaczyć aplikację na webpackowym serverze należy wpisać w terminalu

        npm start

Lub aby wykorzystać stworzyć bundle.js        

        npm run-script build

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

<<zamiast>>

    React.createElement(
      "span",
      {id: "droid"},
      "This is not the droid you are looking for!"
    );

Atrybuty w JSX różnią się od HTML używają 1) camelCase 2) wykorzystując nieco zmienione słowa kluczowe np. **class** -> **className** / **background-color** -> **backgroundColor**

#### Wyrażenia

##### Zmienne

W atrybutach mogą się również znaleźć wyrażenia JS zamknięte w **nawiasach klamrowych -> {}** ale mogą się tam również znaleźć **atrybuty styli** -> ich właściwości powinny być zamknięte w cudzysłowach, a kolejne deklaracje oddzielone przecinkami

    const style {
      backgroundColor: 'red',
      width: '100px',
      height: '100px'
    }

    <div style = {style}></div>

    <div padding = {2+2}></div>

##### Funkcyjne


        function yodaTalk(name){
            return `${firstName}, you are the one, looking for, are we.`;
        }
        const name = 'Wookie';

        <span>{ yodaTalk(name) }</span>


##### Tagi JSX w zmiennych


    const name = 'Wookie';

    const greeting = <span> { firstName }, you are the one, looking for, are we.</span>
    
    <div>{ greeting }</div>


##### Tagi JSX w funkcjach - funkcja zwracająca element

    function yodaTalk(name){
            return <span> {firstName}, you are the one, looking for, are we.</span>;
        }
        const name = 'Wookie';

        <div>{ yodaTalk(name) }</div>

##### Tagi JSX na podstawie wyrażeń logicznych


        const dagobah = true

        if (dagobah){
            info = <span> Luke, you are the one, looking for, are we.</span>;
        } else {
            info = <a href="/login">Let's go to Dagobah, but first Log In</a>;
        }

        <div>{ info }</div>


#### Opis procesu

Element tworzony przy pomocy tagów JSX -> w trakcie kompilacji jest zmieniany na React.createElement -> wywołanie zwraca obiekt -> React tworzy wewnętrzne wirtualne drzewo DOM -> React tworzy drzewo DOM i wstawia je do dokumentu

---

### React.Fragment -> o fragmentach słów parę{#fragmenty}

JSX może przyjąć tylko jeden element -> stąd aby wyrenderować wiele elementów należy je opakować w jeden nadrzędny np. div, ale od React 1.6 można wykorzystywać tzw. Fragmenty, które same w sobie są pewnego rodzaju elementem "klamrowym", który nie generuje kolejnego elementu `<> element1 element2 ...element </>`

Można zaimportowania modułu "Fragment" z biblioteki "react"

    import React, {Fragment} from "react";

Wówczas wykorzystanie fragmentu wygląda następująco -> `<Fragment> element1 element2 ...element </Fragment>`

Fragmenty pozwalają na zgrupowanie wielu elementów bez konieczności dodawania dodatkowego węzła DOM (np. div) 


    class HelloDroid extends Component {
      render() {
        return (
          <>
            <h1>I am a Wookiee!</h1>;
            <h2>I am the planet Kashyyyk!</h2>;
          </>
        )
      }
    }

---

### Notacje obiektów w ES6 w kontekście JSX

Notacje w JS dostępnych od ES6 - ten system zapisu pozwala, na oszczędność kodu - JS potrafi odczytać zmienną jako deklarację CSS 

    const color = "red"

    button {       <<zamiast>>      button {
      color                         color: color;
    }                               }


Inną cechą, o której warto sobie przypomnieć w kontekście JSX jest operator spread/rozproszenia,
który nie tylko pozwala na tworzenie tablic, ale również na ich rozpraszanie, tak samo jak i obiektów np.

    const divSize = {
        width: '100px',
        marginTop: '20px'
    }

    const  blue = {                 <<zamiast>>         const blue = {
            backgroundColor:'blue',                     backgroundColor:'blue',
            ...divSize                                  width: '100px',
        }                                               marginTop: '20px'
                                                        }

---

Źródła:

[Podstawowe informacje](https://pl.reactjs.org/docs/getting-started.html)

[Samouczek: Wstęp do Reacta](https://pl.reactjs.org/tutorial/tutorial.html)

[How to set up React with Webpack and Babel [Tutorial]](https://www.robinwieruch.de/minimal-react-webpack-babel-setup)

[A Complete Webpack Setup for React - Build a React project with Webpack 4 and Babel 7](https://medium.com/swlh/a-complete-webpack-setup-for-react-e56a2edf78ae)

YT: 

[Wprowadzenie do biblioteki React.js](https://www.youtube.com/watch?v=DN73tm89cgU)

[React JS - kurs w 60 minut](https://www.youtube.com/watch?v=Qz7swLxNS0Y)

