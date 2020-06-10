Title: Sass - wprowadzenie
Author: mkostyrko
Date: 2020-05-29 10:00
Updated:
Category: saas
Tags: sass, scss, css, javascript, gulp, gulpfile
Slug: saas-wprowadzenie
related_posts: js-gulp, css-rwd

CSS na sterydach - czyli **Syntactically Awesome Style Sheets**

![Sass](https://sass-lang.com/assets/img/logos/logo-b6e1ef6e.svg)

Sass jest językiem skryptowym rozszerzającym możliwości CSS i wymaga kompilacji na CSS tak aby mógł być interpretowany przez przeglądarki w tym celu można wykorzystać Gulpa (odpowiedniej wtyczki) lun wtyczki VSC.

Sass pozwala na:

[* definiowanie **zmiennych**](#zmienne)

[* pisanie składni opartej na **zagnieżdżaniu** selektorów w selektorach](#zagnieżdżanie)

[* organizację projektu w sposób **modułowy** (przechowywanie deklaracji w wielu plikach)](#moduły)

[* umożliwia tworzenie **@mixins** - grupowanie deklaracji oraz ich wielokrotne użytkowanie](#mixins)

[* pozwala na **dziedziczenie** deklaracji @extend](#dziedziczenie)

[* umożliwia tworzenie obiektów typu **map**](#obiekt-map) i [**list**](#obiekt-list)

[* stosowanie **operatorów** matematycznych/stingów/relacji/logicznych](#operatory)

[* stosowanie pętli warunkowych **if**](#if)

[* stosowanie pętli **for** i **each**](#for)

[* definiowanie i użytkowanie **funkcji**](#funkcje)

[* stosowanie wbudowanych modułów oraz ich **metod**](https://kostyrko.github.io/zfrontu/saas-moduly-metody.html)

Pliki sassowe mają rozszerzenie `.sass` lub `.scss`. Starsza wersja Sass nie zwierała nawiasów klamrowych i nie posiadała średników te wprowadzono od v. 3

Sass

    nav
        ul
            color: blue
        ul
            color: red

wersja Scss

    nav{
        ul {
            color: blue;
        }
        li {
            color: red;
        }
    }

W wyniku kompilacji z Sass na CSS kod może być przedstawiony w 4 następujących formatach

* `nested` - styl domyślny, bliski do Sassa gdzie CSS odzwierciedla strukturę obiektów HTML poprzez wcięcia

* `expanded` - najbliższy CSS, wcięte są jedynie właściwości

* `compact` - właściwości w miarę możliwości kompresowaną, tak aby *deklaracja* (np. właściwości z z fontem) zajmowała pojedynczą linię

* `compressed` - wszystko jest kompresowane do poszczególnych linii, kolejne elementy oddziela spacja - jakiekolwiek komentarze zawarte w scss NIE będą kompilowane do css -> najlżejsza forma zapisu deklaracji, która ma pozytywny wpływ na prędkość ładowania strony

Style definiuje się poprze użycie parametru `outputStyle` lub parametr `style`

    .pipe(sass({
        outputStyle: 'expanded',
        sourceComments: 'map' // mapowanie pliku
    }))

    sass({
        style: 'expanded'
    })

W terminalu poprzez flagę `--style`

    sass input.scss output.css --style compressed

`sourceComments: 'map'` - w css pojawia się komentarz odwołujący się do danego pliku scss

Przykładowe zastosowanie

        const gulp = require("gulp");
        const sass = require("gulp-sass");

        gulp.task("sass", function() {
        return gulp.src("scss/main.scss")
        .pipe(sass({
            outputStyle: 'compressed',
            sourceComments: 'map' 
        }).on("error", sass.logError))
        .pipe(gulp.dest("css"))
        });

Wynik w CSS (expanded)

        /* line 1, scss/main.scss */
        body {
        background-color: #692626;
        }

CSS (compressed)

        /* line 1, scss/main.scss */body{background-color:#ce4242}

=============================

#### Mapowanie SCSS

Proces *mapowania* pozwala na wskazanie przeglądarce interpretującej css z którego miejsca w pliku sass pochodzi dana deklaracja. Wymaga to dodania pakietu oraz dodania odpowiedniej komendy `init` i `write`

Przykładowe zastosowanie

    const gulp = require("gulp");
    const sass = require("gulp-sass");
    const sourcemaps = require('gulp-sourcemaps'); // wskazanie zależności

    gulp.task("sass", function() {
    return gulp.src("scss/main.scss")
    .pipe(sourcemaps.init()) // inicjalizacja
    .pipe(sass({
        outputStyle: 'expanded',
        sourceComments: 'map' 
    }).on("error", sass.logError)) // alternatywnie .pipe(sass({errLogToConsole: true}))
    .pipe(sourcemaps.write()) // zapis
    .pipe(gulp.dest("css"))
    });

    gulp.task("watch", function(){
    gulp.watch("scss/**/*.scss", gulp.series("sass"));
    });

Mapa źródłowa jest wytworzona przy pomocy zakodowanego komentarza poprzedzonego /*# - teraz przeglądając narzędzia programistyczne w przeglądarce będziemy wiedzieć w którym miejscu pliku scss (a nie css) doszło do danej deklaracji - !! przy pracy z sassem nie modyfikujemy pliku CSS, ponieważ ten będzie tworzony przez kompilator

    /* line 1, scss/main.scss */
    body {
    background-color: #994f4f;
    }

    /*# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWFpbi5jc3MiLCJzb3VyY2VzIjpbIm1haW4uc2NzcyJdLCJzb3VyY2VzQ29udGVudCI6WyJib2R5e1xuICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMTUzLCA3OSwgNzkpO1xufVxuIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7QUFBQSxBQUFBLElBQUksQ0FBQTtFQUNGLGdCQUFnQixFQUFFLE9BQWdCO0NBQ25DIn0= */

================

`Komentarze`

`/* */` - komentarz znajdzie się w pliku wynikowym CSS

`//` ten komentarz znajdzie się jedynie w pliku Sass

================

#### @debug 

Sassowy console.log ;) - pozwala na proste debuggowanie -> wypisuje w terminalu podaną frazę

    $colors: red, blue

    @debug "colors', $colors;

#### @error i @warn

użycie @warn ma za zadanie informowaniu o zajściu pewnego warunku granicznego jednak nie przerywa wykonywania się kodu jak to powinno nastąpić w przypadku @error

    @warn "Unknown prefix #{$prefix}.";


---
#### Zmienne {#zmienne}

`Zmienne` są poprzedzone znakiem dolara $ (pozwala na szeroki zakres przetrzymywanych danych). Zmienne należy nazywać ze względu na semantykę (opis do czego ona służy) i wg jednej zasady np. main-color lub color-main

    $font-stack: Helvetica, sans-serif;
    $primary-color: #333;

    body {
        font: 100% $font-stack;
        background-color: $primary-color;
    }

CSS

    /* line 2, scss/main.scss */
    body {
        font:Helvetica, sans-serif;
        background-color: #333;
    }

Zmienne można przechowywać w odmiennym pliku np "variables" i wówczas stosuje się
    
    @import "variables"

---

#### Zagnieżdżanie {#zagnieżdżanie}

`Zagnieżdżenie` - Sass pozwala na odwzorowanie hierarchii znanej z HTML przy pisaniu styli
::: stosowanie zagnieżdżeń do 3-4 poziomów

*Sass*

    nav {
        ul {
            margin: 0;
            padding: 0;
            list-style: none;
            > li { display: inline-block; }
        }

        a {
            display: block;
            padding: 6px 12px;
            text-decoration: none;
        }
    }

*CSS*

    nav ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    nav ul > li {
        display: inline-block;
    }

    nav a {
        display: block;
        padding: 6px 12px;
        text-decoration: none;
    }

`&` - jest stosowane w przypadku pseudoklas (zapewnia powtórzenie selektora => rodzica sassowego)

Scss

    a{
        &:visited{
            color: blue;
        }
        &:hover{
            color: green;
        }
    }

CSS

    a:visited{
        color:blue;
    }

    a:hover{
        color:green;
    }


---

Partials/Cząstkowość - Saas pozwala na rozbicie "CSS" na mniejsze pliki tworzące większą całość (np. jeden plik może odpowiadać za wszystkie buttony albo jedną dużą tabelę) - modularność
Wszystkie pliki cząstkowe powinny być poprzedzone podkreślaniem np. `_buttons.scss` importowany do `main.scss`

---

#### Modułowość - wprowadzenie {#moduły}

Sass pozwala na odwołanie się do zmiennych z zawartych w innych modułach/plikach (`@import` + nazwa pliku/ dąży się do zastąpienia @import przez `@use` i `@forward`)

Różnice pomiędzy `@use` a `@import` -> 1) use zapewnia pojedyncze importowanie w projekcie, 2) mixiny i funkcje (członkowie) zaczynające się na `_` lub `-` są postrzegane jako prywatne wyjątki i nie są importowane 3) import członków odbywa się jedynie lokalnie i nie jest przekazywany do dalszych importów 4) `@extends` - pozwoli na aplikację dalszą importów w kolejnych etapach łańcuch łączników 5) tworzy `namespace `(przestrzeń nazwy)

Zwykle stosuje się main.scss do scalania (importowania) zawartości innych plików scss (mogą się znajdować w folderach tematycznych)

bazowy plik Saas (nazwa `_base.sass`)

        // _base.sass
        $font-stack:    Helvetica, sans-serif
        $primary-color: #333

        body
        font: 100% $font-stack
        color: $primary-color

::: poprzedzenie podkreślnikiem nazwy pliku sprawia, że nie będzie on automatycznie wczytany przez przeglądarkę, ale zawartość plink znajdzie się w CSS :::

plika zawierający style i odwołujących się do zmiennych zdefiniowanych w pliku bazowym - wymaga odwołania się do nazwy pliku przed wymianą nazwy zmiennej tu `elements/_base.scss`

        @import 'elements/base'

        .inverse
        background-color: base.$primary-color
        color: white

CSS wygląda następująco

        body {
        font: 100% Helvetica, sans-serif;
        color: #333;
        }

        .inverse {
        background-color: #333;
        color: white;
        }

(źódło przykładu: https://sass-lang.com/guide)

---

#### Mixins {#mixins}

Pozwalają na użycie kodu, który jest powtarzany (może ale nie musi przyjmować jeden lub więcej argumentów - argumenty oddzielone są przecinkami) - argument może odnosić się zarówno do właściwości (np. display/padding) jak i przypisanej do niej wartości (np. flex/40px) danego obiektu - jest to tzw. **interpolacja**. W przypadku właściwości stosuje się zapis `#{$nazwa_właściwości}` w przypadku wartości `$wartość`. Istnieje również możliwość deklaracji tzw. argumentów opcjonalnych - bez ich podania danej właściwości zostanie przypisana domyślna wartość (domyślną wartość wpisuje się po dwukropku! --> `$y: 50%`)

Zmienna która pozwala na przetrzymywanie wielu deklaracji styli.

$value... - trzykropek pozwala na dodanie listy jako argumentu, która ma być traktowana jako jeden parametr

    @mixin boxShadow($color){
        box-shadow: 10px $color;
    }

`@include` - słowo kluczowe, które pozwala na wykorzystanie mixina

    .box {
        @include boxShadow(red);
    }


    @mixin divMixin($color, $font-size: 1rem, $translate){
            box-shadow: 10px $color;
            font-size: $font-size;
            #{$translate} : $translate-val;
        }

    div {
        @include divMixin(black, translate-Y, 10px)
    }



https://sass-lang.com/documentation/at-rules/mixin

---

#### Dziedziczenie {#dziedziczenie}

Dziedziczenie pozwala na stworzenie stylu, który przejmuje deklaracje innego stylu - selektory będą miały te same właściwości

Dziedziczenie do prostszych rzeczy związanych z powielaniem styli, jednak w przypadku jego wariacji @mixin jest lepszy.

::: Różnica pomiędzy dziedziczeniem a Mixinem jest również widoczna w przypadku wielu klas współdzielących style zapisane w Mixinie lub dziedziczone - w przypadku dziedziczenia nie powiela się stylu tylko jest przypisany do jednego selektora oznaczającego elementy w postaci listy rodzielonej przecinkami, w przypadku Mixina kod jest powielany wielokrotnie - dla każdego selektora jest tworzony unikalny styl - ze względu na to, że Mixin może być parametryzowany :::

`@extend`

    a {
        color: red;
    }

    error {
        @extend a; // color: red; dziedziczy również a:hover {color: black}
    }

    a:hover{
        color: black;
    }

Problemy z ilością selektorów w dziedziczeniu! - te są przypisywane automatycznie


`%` - *placeholder* - wirtualny selektor, który zapobiega replikacji selektorów w przypadku dziedziczenie

Pozwala na wytworzenie stylu do replikacji bez powielania klas w CSS (różnica jest widoczna na poziomie CSS)

    %a {
        color: red;
    }

    error {
        @extend %a; // color: red;
    }

https://sass-lang.com/documentation/at-rules/extend

---

#### Listy {#obiekt-list}

Zbiór elementów wykorzystywanych wyłącznie wewnątrz Saas [ nawiązują do tablic z JS - jednak sposób ich rozdzielenia nie jest zdefiniowany - może być spacja, przecinek] - jej numeracja zaczyna się od 1!

posiada metodę `length($nazwa_listy)`

nth() - wyciąga n-ty element z listy

    $colors: red, blue

    nth($colors, 1)

---

#### Mapa {#obiekt-map}

Przypomina obiekt z JS - posiada klucze oraz wartości - również nie jest kompilowana do CSS

$mapa-kolorow: (klucz1: wartość1, klucz2: wartość2);
map-get($mapa, klucz1) -> zwraca wartość1

    .footer {
        background-color: map-get($mapa-kolorow, klucz1); // zwraca wartość1
    }

`map-values()` - metoda zmieniająca wartości znajdujące się w mapie w listę

---
#### Operatory {#operatory}

Sass pozwala i przyjmuje klasyczne operatory kontekście **liczb/wyrażeń matematycznych** (+,/,-...) łącznie z modulo `%`

Należy pamiętać, że jednostki wprowadzają pewne ograniczenia wynikające z ich logiki.

W przypadku dzielenia może pojawić się problem gdy wartość dzielona może być częścią atrybutu np w przypadku fontu: 20px/10px aby temu zapobiec należy wykorzystać zmienne np font: $primary-size/10px

Zastosowanie okrągłych nawiasów pozwala na wymuszenie kolejności działań

Pozwala również na stosowanie operatorów w kontekście **stringów** - 

np. dodawanie ze sobą stringów skutkuje w ich łączeniu

    b + -zmien  = b-zmien

https://sass-lang.com/documentation/operators/string

Z operatorów moża korzystać również w kontekście sprawdzania **równości** oraz **relacji**

 `==` jest takie samo `!=` nie jest takie samo 

    @debug 1px != 1em; // true
    @debug "Helvetica" == Helvetica; // true - w przypadku stringów zastosowanie cudzysłowu nie ma znaczenia
    @debug hsl(34, 35%, 92.1%) == #f2ece4; // kolory również są tłumaczone
    @debug (5px 7px 10px) != [5px 7px 10px]; // true - nawiasy są rozpoznawane

    $theme: ("venus": #998099, "nebula": #d2e1dd);
    @debug $theme != ("venus": #998099, "iron": #dadbdf); // true - zawartość zmiennych jest sprawdzana

    @debug null != false; // true - null występuje jako false

Operatory stosowane przypadku **wyrażeń logicznych** -> `not`, `and`, `or`

    @debug not true; // false
    @debug not false; // true
    @debug true or false; // true
    @debug true and true; // true

---

#### Instrukcja warunkowa @if {#if}

    $type: droid;
    p {
        @if $type == c3po {
            color: gold;
        } @else if $type == r2d2 {
            color: blue;
        } @else if $type == d-o {
            color: green;
        } @else {
            color: black;
        }
    }

#### Pętla @for i @each {#for}

Generacja selektorów z powtarzalną wartością

    @for $var from <start> through <end> // wartość końcowa jest wliczana

    @for $var from <start> to <end> // wartość końcowa jest pomijana

    Przykład 1:

    @for $i from 1 through 3 {
        h#{$i} {
            font-size: 120px;
        }
    }

        WYNIK CSS:

            h1 {
            font-size: 100px;
            }

            h2 {
            font-size: 100px;
            }

            h3 {
            font-size: 100px;
            }

    Przykład 2

    @for $i from 1 through 3 {
        .item-#{$i} { width: 2em * $i; }
    }

    Przykład 3

    $font-color: (
        color1: red,
        color2: green,
        color3: blue
    );

    @for $i from 1 through 3 {
        h#{$i} {
            color: nth(map-values($font-color), $i);
        }
    }


Pętla @each pracuje na zbiorze danych - iteruje po liście wartości

    @each $var in <lista> {
    }

    // PRZYKŁAD 1

    @each $num in 1,2,3 {
    h#{$num} {
        font-size: 100px;
    }
    };

        // WYNIK CSS:

            h1 {
            font-size: 100px;
            }

            h2 {
            font-size: 100px;
            }

            h3 {
            font-size: 100px;
            }



    // PRZYKŁAD 2

    @each $animal in puma, sea-slug, egret, salamander {
        .#{$animal}-icon {
            background-image: url('/images/#{$animal}.png');}
    }

        // WYNIK-1 CSS:
        .puma-icon { background-image: url("/images/puma.png");}

Istnieje pętla `@while` wykorzystywana jest wtedy gdy nie mamy pewności kiedy dany warunek się skończy

#### @funkcje {#funkcje}

Funkcje wbudowane i zdefiniowane

https://sass-lang.com/documentation/at-rules/function

Zdefiniowane

Funkcja wyznacza i zwraca zdefiniowaną wartość

    @funkcja nazwa_funkcji($parametr) {
        @return $parametr/2;
    }

---

##### Wtyczka do VSC - Live Sass Complier !

Wtyczka Live Sass Complier dokonuje translację z Sass na CSS automatycznie

strona projektu: https://github.com/ritwickdey/vscode-live-sass-compiler


---
Źródła:

https://sass-lang.com/

https://sass-lang.com/documentation

VSC:

https://github.com/ritwickdey/vscode-live-sass-com