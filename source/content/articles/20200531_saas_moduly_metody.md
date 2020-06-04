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
| **color.adjust**($color, $red: null, $green: null, $blue: null, $hue: null, $saturation: null, $lightness: null, $alpha: null)/adjust-color(...) | zmniejsza lub zwiększa jedną lub więcej właściwości koloru | 
|**color.change**($color, $red: null, $green: null, $blue: null, $hue: null, $saturation: null, $lightness: null, $alpha: null)/change-color(...) | zmienia jedną lub więcej właściwości koloru|
| **color.alpha($color)**/alpha($color)/opacity($color) | pozwala na zmianę kanału alpha (0-1) | 
| color.blue($color)/color.red($color)/color.green($color) | zwraca niebieskie/czerwony/zielony kanał| 
| **darken($color, $amount)**| przyciemnia kolor, przyjmuje kolor i wartość przyciemnienia (0-100%) |
| **color.scale($color,$red: null, $green: null, $blue: null, $saturation: null, $lightness: null, $alpha: null)**/scale()|  skalowanie koloru wobec poprzedniej jego wartości wykorzystując jedną lub więcej jego właściwości|
| **desaturate($color, $amount)**| pozwala zmienić nasycenie koloru |
|**color.grayscale($color)**/grayscale($color)| zwraca szary kolor przyjmujący balans bieli od koloru wprowadzonego |
|**color.hue($color)**/hue($color)| zwraca odcień koloru w skali 0-360 stopni|
|**color.invert($color, $weight: 100%)**| zwraca inwersję kolorystyczną podanej barwy|
|**lighten($color, $amount)**| rozjaśnia|
|**saturate($color, $amount)**| zmienia nasilenie barwy koloru|
|**transparentize($color, $amount)**/fade-out($color, $amount)| wpływa na przezroczystość koloru|


### List {#list}

Wybrane

| metoda | funkcja
|---|---|
| **list.append($list, $val, $separator: auto)**/quote() | zwraca kopię listy z dodanym elementem | 
|**list.index($list, $value)**| zwraca indeks wybranej wartości w liście/null jeśli nie istnieje|
|**list.is-bracketed($list)**| zwraca wartość logiczną - czy jest w kwadratowych nawiasach|
|**list.join($list1, $list2, $separator: auto, $bracketed: auto)**| łączenie list|
|**list.append($list, $val, $separator: auto)**| dołączenie wartości do listy |
|**list.length($list)**|zwraca długość listy|
|**list.separator($list)**|zwraca nazwę separatora|
|**list.nth($list, $n)**/nth($list, $n)| zwraca element listy na n-tym miejscu indeksu|
|**list.set-nth($list, $n, $value)**|zwraca kopię listy z podmienionym elementem|


    @debug list.append((blue, red), green); // blue, red, green
    @debug list.append(10px 20px, 30px 40px); // 10px 20px (30px 40px)

---

### Map {#map}

Wybrane

| metoda | funkcja
|---|---|
|**map.get($map, $key)**| zwraca element mapy wg. podanego klucza | 
|**map.has-key($map, $key)**| sprawdza czy mapa posiada podany klucz| 
|**map.keys($map)**| zwraca klucze mapy|
|**map.merge($map1, $map2)**| łączy mapy|
|**map.remove($map, $keys...)**| zwraca kopię mapy bez wartości połączonych z podanymi kluczami|
|**map.values($map)**| zwraca listę wszystkich wartości mapy|

---

### Math {#math}

| metoda | funkcja
|---|---|
| **math.$pi** | zwraca wartość PI |
| **math.round($number)**/round($number) | zwraca zaokrągloną liczbę |
| **math.ceil($number)**/ceil() | zwraca zaokrągloną liczbę w górę do najbliższej pełnej |
| **math.clamp($min, $number, $max)** | ograniczę liczbę do podanego zakresu min-max |
| **math.floor($number)**/ceil() | zwraca zaokrągloną liczbę w dół do najbliższej pełnej |
| **math.clamp($min, $number, $max)** | zwraca string w cudzysłowie |
| **math.max($number...)** max($number...) | zwraca najwyższą z podanych wartości |
| **math.min($number...)** min($number...) | zwraca najniższą z podanych wartości |
| **math.max($number...)** max($number...) | zwraca najwyższą z podanych liczb |
|**math.sqrt($number)**| zwraca pierwiastek kwadratowy|
|**math.abs($number)**| zwraca wartość absolutną podanej liczby|
| **math.percentage($number)** percentage($number) | konwertuje liczbę w procent |
| **math.random($limit: null)** random($limit: null)| zwraca liczbę przypadkową pomiędzy 0 a 1, jeśli limit powyżej 1 to wówczas jest od 1 do limitowej liczby |

    @debug math.abs(-10px); // 10px

---

### Meta {#meta}

| metoda | funkcja
|---|---|
| **meta.load-css($url, $with: null)** | --- Mixins |
| **meta.call($function, $args...)**| --- Functions |
| **meta.content-exists()**| --- Functions |
| **meta.feature-exists($feature)**/feature-exists($feature)| --- Functions |
| **meta.get-function($name, $css: false, $module: null)**/get-function($name, $css: false, $module: null)| --- Functions |
|**meta.global-variable-exists($name, $module: null)**|--- Functions|
|**meta.inspect($value)**|zwraca podaną wartość jako string|
|**meta.keywords($args)**|zwraca słowa kluczowe podane w mixie lub funkcje, które przyjmują słowa kluczowe|
|**meta.mixin-exists($name, $module: null)**|sprawdza czy mixin o podanej nazwie istnieje|
|**meta.module-functions($module)**|--- Functions|
|**meta.module-variables($module)**|zwraca zmienne zadeklarowane w module|
|**meta.type-of($value)**| zwraca typo podanej zmiennej/wartości|
|**meta.variable-exists($name)**| sprawdza czy podana zmienna znajduje się w obecnym zakresie|


---

### Selector {#selector}

https://sass-lang.com/documentation/modules/selector

| metoda | funkcja
|---|---|
| **selector.is-superselector($super, $sub)** | sprawdza czy selektor $super pokrywa się z selektorem $sub  |
| **selector.append($selectors...)** | łączy selektory |
| **selector.extend($selector, $extendee, $extender)**/ | rozszerza selektor o podaną regułę |
| **selector.nest($selectors...)** | łączy selektory w taki sposób jak by były zagnieżdżone |
| **selector.parse($selector)** | rozdziela selektory w formacie selektora wartości |
| **selector.replace($selector, $original, $replacement)** | podmienia selektor / przyjmuje org. selektor, element do podmiany oraz ten, który go zastąpi |
| **selector.unify($selector1, $selector2)** | łączy selektory - zwraca selektor będący połączeniem wprowadzonych selektorów |
| **selector.simple-selectors($selector)** | zwraca listę selektorów zawartych w selektorze |
|**unquote(".main")**| pozbywa wprowadzony string cudzysłów|
|(unquote(".main") unquote("aside:hover"))|// .main aside:hover|

    @debug selector.is-superselector("a", "a.disabled"); // true

    @debug selector.append("a", ".disabled"); // a.disabled

    @debug selector.extend("a.disabled", "a", ".link"); // a.disabled, .link.disabled

    #{$extender} {
        @extend #{$extendee};
        }

    @debug selector.parse(".main aside:hover, .sidebar p");
    // ((unquote(".main") unquote("aside:hover")),
    //  (unquote(".sidebar") unquote("p")))

    @debug selector.replace("a.disabled", "a", ".link"); // .link.disabled

    @debug selector.simple-selectors("a.disabled"); // a, .disabled
    
---

### String {#string}

https://sass-lang.com/documentation/modules/string

| metoda | funkcja
|---|---|
| **string.quote($string)**/quote() | zwraca string w cudzysłowie | 
| **string.index($string, $substring)**/str-index() | Zwraca pierwszy indeks fragmentu stringu znajdującego się w stringu lub null |
|**string.insert($string, $insert, $index)**/str-insert()| zwraca kopię zmodyfikowanego string - przyjmuje string do wstawienia i indeks (miejsce)|
|**string.length($string)**/str-length()| zwraca liczbę reprezentującą długość łańcucha znaków|
|string.index("")| zwraca indeks podanego ciągu znaków lub 0|
|**string.slice($string, $start-at, $end-at: -1)** / str-slice()|zwraca fragment stringu zależnego od podanych parametrów (początkowej i końcowej wartości/indeks/łącznie)|
|**string.to-upper-case($string)** /to-upper-case()| wszystkie litery zmienia na wielkie|
|**string.to-lower-case($string)**/to-lower-case()| zmienia litery na małe|
|**string.unique-id()**/unique-id()| zwraca randomowo generowany ciąg znaków i unikatowy w ramach obecnej kompilacji Sass|
|**string.unquote($string)**/unquote()| zwraca ciąg znaków niezamknięty w cudzysłów|

Przykłady zastosowania:

    @debug string.insert("Roboto", " Bold", 100); // "Roboto Bold" - wstawia na końcu
    @debug string.insert("Bold", "Roboto ", -100); // "Roboto Bold" - wstawia na sam początek

---

Źródła:

https://sass-lang.com/

https://sass-lang.com/documentation

https://css-tricks.com/introducing-sass-modules/