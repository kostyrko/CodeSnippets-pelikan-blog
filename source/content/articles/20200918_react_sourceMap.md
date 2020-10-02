Title: React: Create React App i sourceMap w trakcie produkcji
Author: mkostyrko
Date: 2020-09-18 10:00
Updated:
Category: reactjs
Tags: react, sourceMap, Create React App, CRP
Slug: react-sourceMap
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://user-images.githubusercontent.com/27288406/47966049-b13a5700-e056-11e8-808e-45f2ffd4719c.png)

Jedną z moich ulubionych wtyczek w Gulpie/Webpacku bez wątpienia jest ta przy pomocy której jestem wstanie w szybki sposób dojść do tego, w którym pliku/linijce znajduje się frapująca mnie deklaracja stylu -> **sourceMap**


Wykorzystując opcję tworzenia aplikacji przy pomocy narzędzie Create React App nie mamy jednak możliwości skorzystania z **sourceMapa** - referencje do plików źródłowych tworzone są dopiero na końcowym etapie wdrożenia/diplojmentu

Istnieje jednak możliwość zmiany tego stanu, chociaż faktycznie też wymaga zmian plików znajdujących się w *react-scripts*



W pierwszej kolejności należy stworzyć folder o nazwie `scripts` w folderze projektu

A następnie stworzenie pliku `enable-css-sourcemaps.js` oraz wpisanie w niego treści wyszukującej środowiska produkcyjnego -> `isEnvProduction && shouldUseSourceMap` w kontekście definicji `sourceMap` i zamianę na środowisko developerskie -> `isEnvDevelopment && shouldUseSourceMap` w pliku `webpack.config.js` (można zrobić to ręcznie ale... jest z tym zdecydowanie więcej roboty)


    const { writeFileSync, existsSync, readFileSync } = require('fs');

    const path = 'node_modules/react-scripts/config/webpack.config.js';

    const find = /(sourceMap: isEnvProduction && shouldUseSourceMap)/g;
    const replace = 'sourceMap: isEnvDevelopment && shouldUseSourceMap';

    if (existsSync(path)) {
      const buffer = readFileSync(path)
        .toString()
        .replace(find, replace);

      try {
        writeFileSync(path, buffer);
        console.info('enable-css-sourcemaps: active');
      } catch (e) {
        console.error(`enable-css-sourcemaps: ${path} manipulation failed!`);
      }
    } else {
      console.warn(`enable-css-sourcemaps: ${path} does not exist`);
    }


[źródło tego fragmentu kodu poniżej]


Następnie package.json w części *scripts* należy dodać def. postinstall


    "postinstall": "node ./scripts/enable-css-sourcemaps.js"


A w ostatnim kroku należy wykorzystać `npm install` aby zmiana została zaczytana i weszła w życie

    npm install



---

Źródło:

[create-react-app sass sourcemaps not working #5707](https://github.com/facebook/create-react-app/issues/5707#issuecomment-569836264)

