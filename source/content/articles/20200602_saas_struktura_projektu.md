Title: Sass - struktura projektu
Author: mkostyrko
Date: 2020-06-02 10:00
Updated:
Category: saas
Tags: sass, scss, css, javascript, gulp, gulpfile
Slug: saas-struktura-projektu
related_posts: js-gulp, saas-wprowadzenie

![struktura-projektu-scss](https://miro.medium.com/max/1400/1*MCiNLBzUI-LWK_PhVwq0xA.png#center){:height="75%" width="100%"}

Wraz z wzrostem wielkości projektu, większą rolę odgrywać będzie odpowiedni sposób strukturyzacji oraz modularyzacji plików zdefiniowanych w ramach niego stylów. Podział na odpowiednie moduły umożliwia również ponowne wykorzystanie wybranych części kodu w innych projektach.

Zwyczajowo przyjęło, się że plik, który importuje moduły (partials) a staje się łącznikiem pomiędzy nimi nazwany jest `main.scss`. W ramach tego pliku importuje się moduł używając relatywnej ścieżki do oraz nazwy danego pliku z pominięciem rozszerzenia zawartej w apostrofach/cudz. poprzedzonej słowem kluczowym `@import`/`@use`

Pliki modułów, które nie muszą być importowane przez kompilator bezpośrednio poprzedzone są podkreślaniem.

Nazwy plików oraz ich zawartość powinna w sposób semantyczny odzwierciedlać układ strony np. w pliku _header.scss powinny znaleźć się deklaracje związane z nagłówkiem/headerem.

#### Struktura małego projektu ...
... może zamknąć się w 3-4 plikach 

    _base.scss // zawiera zmienne, mixins, resety
    _layout.scss // deklaracje związane z układem - grid, flex, kontenery
    _compontents.scss // elementy (również przedstawione w taki sposób by mogły zostać ponownie użyte) => przyciski, navy
    
    main.scss // zawiera jedynie importy modułów

**:::zaprezentowana struktura w momencie rozrostu projektu może zostać rozszerzona w taki sposób, że foldery przyjmują nazwy wymienionych plików zawierające pliki rozbijające deklaracje na jeszcze bardziej podstawowe części :::**

Może również przyjąć bardziej rozbudowaną formę (nazwy folderów oraz poszczególnych plików są samowyjaśniające)

    main.scss
      abstracts
        | _variables.scss
        | _functions.scss
        | _mixins.scss
      base
        | _reset.scss
        | _typography.scss
      components
        | _buttons.scss
        | _sliders.scss
      layout
        | _navigation.scss
        | _grid.scss
        | _header.scss
        | _footer.scss
        | _forms.scss
      pages
        | _home.scss
        | _about.scss
      themes
        | _theme.scss
      vendors
        | _bootstrap.scss

Więcej na temat typografi można przeczytać [tutaj](https://css-tricks.com/six-tips-for-better-web-typography/) i [tutaj](https://css-tricks.com/typography-for-developers/)


![stuktura-projektu](https://entwickler.de/wp-content/uploads/2013/12/kurm_style1.png)

Przykładowa struktura folderów zawierająca pliki saasowe



---
Źródła:

https://itnext.io/structuring-your-sass-projects-c8d41fa55ed4

https://github.com/Automattic/_s/issues/1215

http://dualeoblog.com/structure-sass-project/

