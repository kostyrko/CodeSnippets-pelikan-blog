Title: Sass - wbudowane moduły i ich metody
Author: mkostyrko
Date: 2020-05-31 10:00
Updated:
Category: saas
Tags: sass, scss, css, javascript, gulp, gulpfile
Slug: saas-moduly-metody
related_posts: js-gulp, saas-wprowadzenie


Sass oferuje następujące wbudowane moduły `color`, `list`, `map`, `math`, `meta`, `selector`, `string`

Używanie modułu odbywa się poprzez jego zaimportowanie na początku poprzez odowłanie się do słowa kluczowego `@use` nazwy modułu oraz użycia gwiazdki lub bez użycia gwiazdki - wówczas każda metoda musi być poprzedzona nazwą modułu

    @use 'sass:math';
    $half: math.percentage(1/2);

    @use 'sass:math' as *;
    $half: percentage(1/2);

### String

Obecnie jedynie Dart Sass wspiera nazewnictwo bez odwołania się do modułów w sposób globalny

| metoda | funkcja | 
|---|---|---|
| string.quote($string)/quote() | zwraca string w cudzysłowiu | 
| string.index($string, $substring)/str-index() | Zwraca pierwszy indeks fragmentu stringu znajdującego się w stringu lub null |
|string.insert($string, $insert, $index)/str-insert()| zwraca kopię zmodyfikowanego string - przyjmuje string do wstawienia i indeks (miejsce)|
|string.length($string)/str-length()| zwraca liczbę reprezentującą długość łańcucha znaków|
|string.index("")| zwraca indeks podanego ciągu znaków lub 0|
|string.slice($string, $start-at, $end-at: -1) / str-slice()|zwraca fragment stringu zależnego od podanych parametrów (początkowej i końcowej wartości/indeks/łącznie)|
|string.to-upper-case($string) /to-upper-case()| wszystkie litery zmienia na wielkie|
|string.to-lower-case($string)/to-lower-case()| zmienia litery na małe|
|string.unique-id()/unique-id()| zwraca randomowo generowany ciąg znaków i unikatowy w ramach obecnej kompilacji Sass|
|string.unquote($string)/unquote()| zwraca ciąg znaków niezamknięty w cudzysłów|

Przykłady zastosowania:

    @debug string.insert("Roboto", " Bold", 100); // "Roboto Bold" - wstawia na końcu
    @debug string.insert("Bold", "Roboto ", -100); // "Roboto Bold" - wstawia na sam początek

---
Źródła:

https://sass-lang.com/

https://sass-lang.com/documentation

https://www.webski.com.au/what-is-sass-how-to-install-start-using-sass/

https://css-tricks.com/introducing-sass-modules/