Title: Sass - wbudowane moduły i ich metody
Author: mkostyrko
Date: 2020-05-31 10:00
Updated:
Category: saas
Tags: sass, scss, css, javascript, gulp, gulpfile
Slug: saas-moduly-metody
related_posts: js-gulp, saas-wprowadzenie


Sass oferuje następujące wbudowane moduły [color](#color), [list](#list), [map](#map), [math](#math), [meta](#meta), [selector](#selector), [string](#string)

Używanie modułu odbywa się poprzez jego zaimportowanie na początku poprzez odowłanie się do słowa kluczowego `@use` nazwy modułu oraz użycia gwiazdki lub bez użycia gwiazdki - wówczas każda metoda musi być poprzedzona nazwą modułu

    @use 'sass:math';
    $half: math.percentage(1/2);

    @use 'sass:math' as *;
    $half: percentage(1/2);

Obecnie jedynie Dart Sass wspiera nazewnictwo bez odwołania się do modułów w sposób globalny

**Indeks w SAAS zaczyna się od 1 !! a nie 0**

### Color {#color}

https://sass-lang.com/documentation/modules/color

Wybrane

| metoda | funkcja
|---|---|
| **adjust**($color, $red: null, $green: null, $blue: null, $hue: null, $saturation: null, $lightness: null, $alpha: null)/adjust-color(...) | zmniejsza lub zwiększa jedną lub więcej właściwości koloru | 
|**change**($color, $red: null, $green: null, $blue: null, $hue: null, $saturation: null, $lightness: null, $alpha: null)/change-color(...) | zmienia jedną lub więcej właściwości koloru|
| **alpha($color)/opacity($color)** | pozwala na zmianę kanału alpha (0-1) | 
| color.blue($color)/color.red($color)/color.green($color) | zwraca niebieskie/czerwony/zielony kanał| 
| **darken($color, $amount)**| przyciemnia kolor, przyjmuje kolor i wartość przyciemnienia (0-100%) |
| **scale($color,$red: null, $green: null, $blue: null, $saturation: null, $lightness: null, $alpha: null)**/scale()|  skalowanie koloru wobec poprzedniej jego wartości wykorzystując jedną lub więcej jego właściwości|
| **desaturate($color, $amount)**| pozwala zmienić nasycenie koloru |
|**grayscale($color)**| zwraca szary kolor przyjmujący balans bieli od koloru wprowadzonego |
|**hue($color)**| zwraca odcień koloru w skali 0-360 stopni|
|**invert($color, $weight: 100%)**| zwraca inwersję kolorystyczną podanej barwy|
|**lighten($color, $amount)**| rozjaśnia|
|**saturate($color, $amount)**| zmienia nasilenie barwy koloru|
|**transparentize($color, $amount)**| wpływa na przezroczystość koloru|

[A visual guide to Sass & Compass Color Functions](http://jackiebalzer.com/color)

---

### List {#list}

Wybrane

| metoda | funkcja
|---|---|
| **append($list, $val, $separator: auto)**/quote() | zwraca kopię listy z dodanym elementem | 
|**index($list, $value)**| zwraca indeks wybranej wartości w liście/null jeśli nie istnieje|
|**is-bracketed($list)**| zwraca wartość logiczną - czy jest w kwadratowych nawiasach|
|**join($list1, $list2, $separator: auto, $bracketed: auto)**| łączenie list|
|**append($list, $val, $separator: auto)**| dołączenie wartości do listy |
|**length($list)**|zwraca długość listy|
|**separator($list)**|zwraca nazwę separatora|
|**nth($list, $n)**/nth($list, $n)| zwraca element listy na n-tym miejscu indeksu|
|**set-nth($list, $n, $value)**|zwraca kopię listy z podmienionym elementem|


    @debug append((blue, red), green); // blue, red, green
    @debug append(10px 20px, 30px 40px); // 10px 20px (30px 40px)
    @debug index((map-values($font-sizes)), 50px) //

---

### Map {#map}

Wybrane

| metoda | funkcja
|---|---|
|**get($map, $key)**| zwraca element mapy wg. podanego klucza | 
|**has-key($map, $key)**| sprawdza czy mapa posiada podany klucz| 
|**keys($map)**| zwraca klucze mapy w postaci listy|
|**merge($map1, $map2)**| łączy mapy|
|**remove($map, $keys...)**| zwraca kopię mapy bez wartości połączonych z podanymi kluczami|
|**values($map)**| zwraca listę wszystkich wartości mapy|

### Math {#math}

| metoda | funkcja
|---|---|
| **$pi** | zwraca wartość PI |
| **round($number)** | zwraca zaokrągloną liczbę |
| **ceil($number)** | zwraca zaokrągloną liczbę w górę do najbliższej pełnej |
| **clamp($min, $number, $max)** | ograniczę liczbę do podanego zakresu min-max |
| **floor($number)** | zwraca zaokrągloną liczbę w dół do najbliższej pełnej |
| **clamp($min, $number, $max)** | zwraca string w cudzysłowie |
| **max($number...)**  | zwraca najwyższą z podanych wartości |
| **min($number...)**  | zwraca najniższą z podanych wartości |
| **max($number...)**  | zwraca najwyższą z podanych liczb |
|**sqrt($number)**| zwraca pierwiastek kwadratowy|
|**abs($number)**| zwraca wartość absolutną podanej liczby|
| **percentage($number)**| konwertuje liczbę w procent |
| **random($limit: null)**| zwraca liczbę przypadkową pomiędzy 0 a 1, jeśli limit powyżej 1 to wówczas jest od 1 do limitowej liczby |

    @debug math.abs(-10px); // 10px

---

### Meta {#meta}

| metoda | funkcja
|---|---|
| **load-css($url, $with: null)** | --- Mixins |
| **call($function, $args...)**| --- Functions |
| **content-exists()**| --- Functions |
| **feature-exists($feature)**/feature-exists($feature)| --- Functions |
| **get-function($name, $css: false, $module: null)**/get-function($name, $css: false, $module: null)| --- Functions |
|**global-variable-exists($name, $module: null)**|--- Functions|
|**inspect($value)**|zwraca podaną wartość jako string|
|**keywords($args)**|zwraca słowa kluczowe podane w mixie lub funkcje, które przyjmują słowa kluczowe|
|**mixin-exists($name, $module: null)**|sprawdza czy mixin o podanej nazwie istnieje|
|**module-functions($module)**|--- Functions|
|**module-variables($module)**|zwraca zmienne zadeklarowane w module|
|**type-of($value)**| zwraca typo podanej zmiennej/wartości|
|**variable-exists($name)**| sprawdza czy podana zmienna znajduje się w obecnym za
---

### Selector {#selector}

https://sass-lang.com/documentation/modules/selector

| metoda | funkcja
|---|---|
| **is-superselector($super, $sub)** | sprawdza czy selektor $super pokrywa się z selektorem $sub  |
| **append($selectors...)** | łączy selektory |
| **extend($selector, $extendee, $extender)**/ | rozszerza selektor o podaną regułę |
| **nest($selectors...)** | łączy selektory w taki sposób jak by były zagnieżdżone |
| **parse($selector)** | rozdziela selektory w formacie selektora wartości |
| **replace($selector, $original, $replacement)** | podmienia selektor / przyjmuje org. selektor, element do podmiany oraz ten, który go zastąpi |
| **unify($selector1, $selector2)** | łączy selektory - zwraca selektor będący połączeniem wprowadzonych selektorów |
| **simple-selectors($selector)** | zwraca listę selektorów zawartych w selektorze |
|**unquote(".main")**| pozbywa wprowadzony string cudzysłów|

    @debug (unquote(".main") unquote("aside:hover"))// .main aside:hover|

    @debug is-superselector("a", "a.disabled"); // true

    @debug append("a", ".disabled"); // a.disabled

    @debug extend("a.disabled", "a", ".link"); // a.disabled, .link.disabled

    #{$extender} {
        @extend #{$extendee};
        }

    @debug parse(".main aside:hover, .sidebar p");
    // ((unquote(".main") unquote("aside:hover")),
    //  (unquote(".sidebar") unquote(
    @debug replace("a.disabled", "a", ".link"); // .link.disabled

    @debug simple-selectors("a.disabled"); // a, .disabled
    
---

### String {#string}

https://sass-lang.com/documentation/modules/string

| metoda | funkcja
|---|---|
| **quote($string)**| zwraca string w cudzysłowie | 
| **index($string, $substring)** | Zwraca pierwszy indeks fragmentu stringu znajdującego się w stringu lub null |
|**insert($string, $insert, $index)** | zwraca kopię zmodyfikowanego string - przyjmuje string do wstawienia i indeks (miejsce)|
|**length($string)**| zwraca liczbę reprezentującą długość łańcucha znaków|
|**index("")**| zwraca indeks podanego ciągu znaków lub 0|
|**slice($string, $start-at, $end-at: -1)**|zwraca fragment stringu zależnego od podanych parametrów (początkowej i końcowej wartości/indeks/łącznie)|
|**to-upper-case($string)** | wszystkie litery zmienia na wielkie|
|**to-lower-case($string)**| zmienia litery na małe|
|**unique-id()**| zwraca randomowo generowany ciąg znaków i unikatowy w ramach obecnej kompilacji Sass|
|**unquote($string)**| zwraca ciąg znaków niezamknięty w cudzysłów|

Przykłady zastosowania:

    @debug insert("Roboto", " Bold", 100); // "Roboto Bold" - wstawia na końcu
    @debug insert("Bold", "Roboto ", -100); // "Roboto Bold" - wstawia na sam początek


---



---

Źródła:

https://sass-lang.com/

https://sass-lang.com/documentation

https://css-tricks.com/introducing-sass-modules/