Title: JavaScript: Webpack - krótkie wprowadzenie
Author: mkostyrko
Date: 2020-06-26 11:00
Updated:
Category: javascript
Tags: webpack, webpack@4, javascript, task runner, transpilacja
Slug: js-webpack
related_posts: js-babel

![webpack](https://miro.medium.com/max/1400/1*gdoQ1_5OID90wf1eLTFvWw.png)

### Wstęp

*Webpack* generuje tzw. pakiety (ang. bundles -> bundle.js) na podstawie wytworzonego tzw. drzewa zależności oraz dostosowanie ich do formatu czytelnego dla możliwie jak najszerszego zakresu przeglądarek internetowych - jest swego rodzaju kompilatorem powstałej treści na podstawie różnych formatów do takiego, który przyjmuje przeglądarka internetowa (js,html,css). W  tym sensie działą podobnie do innych tzw. *task runnerów* (narzędzie do automatyzacji działań dokonywanych na plikach) jak Gulp

Istotną zaletą korzystania z *Webpacka* jest to, że każdy plik jest traktowany jako moduł (obraz, css, font, js etc). ([CommonJS](https://flaviocopes.com/commonjs/) -> po stronie node.js i moduły z ES (klient) nie są dostępne dla wszystkich przeglądarek stąd potrzeba ich transpilacji)

Loader - przetwarza plik (nie-js) w ten sposób by mógł być dodane do drzewa zależności (np. css-loader, babel-loader, html-loader) -  etap transpilacji

np. **html-loader** pozwala na modułowe tworzenie plików HTML (więcej na ten temat:[SO - How can I provide parameters for webpack html-loader interpolation?](https://stackoverflow.com/questions/39374187/how-can-i-provide-parameters-for-webpack-html-loader-interpolation) )

Wtyczki - różnego rodzaju wtyczki pozwalają na osiągnięcie oczekiwanego efektu np. zapisanie reguł css do osobnego pliku css/po za plik bundle.js poprzez pracę na gotowych pakietach (np. extract text plugin [wydobywa css], webpack-uglify-js-plugin[miniaturyzuje js])

np. wtyczka **purge-css** pozbywa się nieużywanych klas CSS (więcej na ten temat: [GH-repo purgecss-webpack-plugin](https://github.com/FullHuman/purgecss/tree/master/packages/purgecss-webpack-plugin))


[![webpack w akcji](https://webmastah.pl/wp-content/uploads/2017/05/what-is-webpack-1024x512.png)](https://webmastah.pl/kurs-vue-js-krok-po-kroku-vue-loader/)

---

### Instalacja oraz użycie WebPacka

Inicjalizajca porojektu (stworzenie package.json) 

    npm init -y

Instalacja *Wepacka* w v.4 oraz cli v.4 jako developerska zależność

    npm i webpack@4 --save-dev
    npm i webpack-cli@3 --save-dev

Narzędzie nie jest dostępne globalnie zatem aby nie wywoływać go poprzez każdorazowe wprowadzeni ścieżki `./node_modules/.bin/webpack`
można dodać webpacka do sekcji scripts w `package.json` przypisując go do klucza np. start (powszechnie stosowana nazwa) + należy wskazać główny plik (wejścia) oraz nazwę pliku wyjścia (pod tą nazwą zostanie zapisany bundle)

    {
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "./node_modules/.bin/webpack app.js --output out.js"
      }
    }

Teraz wystarczy wpisać

    npm start

::: Istnieje możliwość przeprowadzenia globalnej instalacji Webpacka, ale ta nie jest polecana (wówczas powyższy krok jest zbędny) `npm i -g webpack` :::

Budowa paczki od punktu wejścia i dołącza odnaleziony kod do pliku wyjścia, a po drodze natrafia na instrukcję require(), która wskazuje na konkretne pliki i znajdujący się w nich kod -> w wyniku tego połączenia powstaje plik, który jest trudny do odczytu przez człowieka, ale jest czytelny dla node.js lub przeglądarki

Przykładowe użycie

    // package.json
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "./node_modules/.bin/webpack r2d2.js --output out.js"
      },


    // droidFinder.js
      function findDroid(droid) {
        console.log(`You: Is this ${droid}?\nObi Wan: This is not the droid you are looking for`);
      }

      module.exports = findDroid;


    // r2d2.js
      const findDroidFunc = require('./droidFinder');

      findDroidFunc("R2D2")


    //out.js
      !function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=0)}([function(e,t,n){n(1)("R2D2")},function(e,t){e.exports=function(e){console.log(`You: Is this ${e}?\nObi Wan: This is not the droid you are looking for`)}}]);

    -----------

    >> node out.js
    >> You: Is this R2D2?
      Obi Wan: This is not the droid you are looking for

---

### Tworzenie pliku konfiguracyjnego dla Webpacka

Istnieje możliwość konfiguracji `Webpacka` przy pomocy odpowiedniego do tego utworzonego pliku = `webpack.config.js` w którym należy zawrzeć informacje na temat wtyczek oraz zadań jakie powinny zostać przez to narzędzie wykonane

Prosta konfiguracja

Instalacja

    npm i webpack@4 --save-dev
    npm i webpack-cli@3 --save-dev


    // webpack.config.js
    const path = require('path');     // moduł node.js, który pozwala na pracę z module.exports

    module.exports = {    // konfiguracja eksportu
      entry: './src/index.js',    // wskazanie wejścia
      output: {     // wskazanie wyjścia
        filename: 'main.js',    // podanie nazwy pliku wyjściowego
        path: path.resolve(__dirname, 'dist'), // moduł node.js wskazujący na ścieżkę pliku wyjściowego __dirname (przechowuje ścieżkę katalogu, w którym znajduje się plik)
      },
    };

więcej info na [temat path.resolve()](https://nodejs.org/docs/latest/api/path.html#path_path_resolve_paths) - zwraca bezwzględny adres na podstawie przekazanych argumentów (__dirname - przechowuje ścieżkę katalogu, w którym znajduje się plik, "nazwa_katalogu")

---

Tworzymy własną konfigurację w `webpack.config.js`

    // package.json
    >> wersja 1 <<
    "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "webpack-dev-server --hot -d",     // flaga --hot pozwala na zmianę modułów w trakcie pracy bez konieczności odświeżania -d -> debug
    "build": "webpack -p" // webpack production [Minification using UglifyJsPlugin/Runs the LoaderOptionsPlugin]
    },
    =======================================
    >> wersja 2 <<
    "scripts": {
    "start": "webpack --mode development --watch",
    "build": "webpack --mode production",
    "server": "webpack-dev-server --inline --hot"
    },

    >> Zależności <<
    "devDependencies": {
        "@babel/core": "^7...",
        "@babel/preset-env": "^7...",
        "babel-loader": "^8...",
        "webpack": "^4...",
        "webpack-cli": "^3...",
        "webpack-dev-server": "^3...",
        "style-loader": "...", 
        "css-loader": "...",
        "saas-loader": "..."
      }


Umożliwia zastsowowanie komend -> **nmp start/ npm build/ npm server**


więcej info na [webpack production](https://webpack.js.org/guides/production/)


    //webpack.config.js
    const path = require("path");
    const entryPath = "sciezka/folderu/z_plikami";
    const entryFile = "nazwa_pliku.js";

    module.exports = {
      watch: true,                      // obserwuj zmiany
      entry: `./${entryPath}/js/${entryFile}`,      // plik wejściowy
      output: {                         // plik wyjściowy
        filename: "out.js",             // nazwa pliku wyjściowego
        path: path.resolve(__dirname, `${entryPath}/build`) // folder wyjściowy/zapisu
      },
      devServer: {                      // tworzenie sewera (tu użyta zależność "webpack-dev-server")
        contentBase: path.join(__dirname, `${entryPath}`), // informacja/ścieżka gdzie znajduje się statyczna treść np. index.html (path.join by stworzyć absolutną ścieżkę)
        publicPath: "/build/",         // stworzone pliki będą znajdować się w tym folderze
        compress: true,               // kompresja
        port: 3001                    // port na którym znajduje się serwer
      },
      module: { // właściwość modules z przypisanymi obiektami posiadającymi właściwość rules - te definiują sposób pracy z różnymi typami plików (tu użyta zależność "babel-loader"/"@babel/preset-env"/"@babel/core")
        rules: [
          {
            test: /\.js$/,      // zawiera wyrażenie regularne wskazujące na rodzaj pliku (rozszerzenia), które ma być objęte działaniem loadera
            exclude: /node_modules/,    // wykluczenie plików z folderu..
            loader: "babel-loader"
          },
          {
            test: /\.css$/,
            use: [ 'style-loader', 'css-loader' ]       // css-loader importuje kod css do JS a style-loader - wstrzykuje CSS do HTML
          },
          {
            test: /\.scss$/,
            use: [ 'style-loader', 'css-loader', 'sass-loader' ]      // saas-loader transpiluje saas na css
          }
        ]
      }
      plugins: [      // wtyczki
        new webpack.optimize.UglifyJsPlugin({   // wskazanie wtyczki 
            beautify: true,     // konfiguracja
            comments: false
        })
      ]
    };


opcjonalnie:


    [...]
          module: {
              rules: [
                  {
                      test: /\.m?js$/,
                      exclude: /(node_modules|bower_components)/,
                      use: {
                          loader: "babel-loader",
                          options: {
                              presets: ["@babel/preset-env"]
                          }
                      }
                  }
              ]
          }
    [...]


---
Źródła:

[Webpack 3 tutorial PL by Overment](https://www.youtube.com/watch?v=hE2XR4TdgXg&list=PLjHmWifVUNMJZZPBRtLRta-5zkc2SXDep)

[Podstawy konfiguracji Webpack](https://www.nafrontendzie.pl/podstawy-konfiguracji-webpack)

[webpack.js.org](https://webpack.js.org/)

[webpack-github repo](https://github.com/webpack/webpack)

[Zsh: command not found: webpack](https://stackoverflow.com/questions/35932000/zsh-command-not-found-webpack)

[webpack command not working](https://stackoverflow.com/questions/38788166/webpack-command-not-working)

[webpack-getting started](https://webpack.js.org/guides/getting-started/)

[webpack-configuration](https://webpack.js.org/configuration/)

[Webpack i Babel](http://kursjs.pl/kurs/es6/webpack.php)

[Konfiguracja Webpack 2+ - część #3: pluginy](https://www.nafrontendzie.pl/konfiguracja-webpack-2-czesc-3-pluginy)

[Konfiguracja Webpack 2+ – część #2: loadery](https://www.nafrontendzie.pl/konfiguracja-webpack-2-czesc-2-loadery)

[Webpack 4 – Jak go skonfigurować i zacząć pracę?](https://bedekodzic.pl/webpack-4/)