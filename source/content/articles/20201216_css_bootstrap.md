Title: CSS - Bootstrap
Author: mkostyrko
Date: 2020-12-16 12:00
Updated:
Category: css
Tags: bootstrap
Slug: css-biblioteki
related_posts: css-rwd, html-css-bem



![css-bootstrap](https://mdbcdn.b-cdn.net/wp-content/uploads/2020/06/bootstrap-5.jpg)

[Bootstrap](https://getbootstrap.com/) - główna strona Bootstrapa CSSwoej biblioteki Twittera

Bootstrap = Grid+Komponenty

Istnieją 3 możliwości dodania Boostrapa do projektu 1) poprzez pobranie Bootsrapowych plików i podłączenia ich do głównego pliku index.html lub 2) poprzez podłączenia linków CDN (content delivery network) 3) pobranie/zainstalowanie bootstrapa przy pomocy np. NPM jako zależności `npm install bootstrap`

W obu przypadkach musimy podlinkować ścieżkę do Bootastrapowych styli (CSS) oraz połączonych z nimi logiki (JS)

W przypadku **Bootstrapa v. 5**, jQuery już nie jest wykorzystywane a CDN składa się z zaledwie 2 linków. 1. z nich wklejamy do heada a kolejny tuż przed zamkncięciem tagu odpowiedzialengo za ciało strony`</body>`


    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width= , initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
      <title>Document</title>
    </head>


    [...]

      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    </body>
    </html>


### Podstawy Bootstrap

### Kontenery i responsywność

https://getbootstrap.com/docs/4.0/layout/overview/

Granice dla media queries

    // Small devices (landscape phones, 576px and up)
    @media (min-width: 576px) { ... }

    // Medium devices (tablets, 768px and up)
    @media (min-width: 768px) { ... }

    // Large devices (desktops, 992px and up)
    @media (min-width: 992px) { ... }

    // Extra large devices (large desktops, 1200px and up)
    @media (min-width: 1200px) { ... }


Media-queries są również dostępne jako mixiny Sassowe

    @include media-breakpoint-only(xs) { ... }
    @include media-breakpoint-only(sm) { ... }
    @include media-breakpoint-only(md) { ... }
    @include media-breakpoint-only(lg) { ... }
    @include media-breakpoint-only(xl) { ... }


### Bootstrap Grid System klucz do RWD

Bootstrapowy grid jest oparty na podziale 12 kolumn, jeśli ich liczba w ramach klasy nie jest wskazana wówczas przestrzeń jest liczona po równo.


    <div class="container">
      <div class="row">
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
        <div class="col-sm">
          One of three columns
        </div>
      </div>
    </div>

||Extra small < 576px|Small ≥ 576px|Medium ≥ 768px|Large ≥ 992px |Extra large ≥ 1200px|
|---|---|---|---|---|---|
|**Maksymalna szerokość kontenera**|Brak|540px|720px|960px|1140px|
|**Prefix klasy**|.col-|.col-sm-|.col-md-|.col-lg-|.col-xl-|

Przykład zastosowania


    <div class="row">
      <div class="col-12 col-md-8">.col-12 .col-md-8</div>
      <div class="col-6 col-md-4">.col-6 .col-md-4</div>
    </div>


`col-{breakpoint}-auto` - zmienia rozmiar kolumny w zależności od jej zawartości (dopasowuje szerokość kolumny do jej zawartości)

`class="w-100"` - klasa odpowiadająca html `</br>`


    <div class="row">
      <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
      <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>

      <!-- Force next columns to break to new line -->
      <div class="w-100"></div>

      <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
      <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
    </div>


#### Wyrównanie

Wyrównanie odbywa się na podstawie flexboxa -> np. dzieci `align-items-start`, `align-items-center` lub własne wyrównanie elementu np. `align-self-start`. Sprawa ma się podobnie w przypadku poziomego wyrównania -> np. `justify-content-start `

    <div class="row align-items-start">
        <div class="col">
          One of three columns
        </div>
    [...]

    <div class="row align-items-center justify-content-start">
        <div class="col">
          One of three columns
        </div>
        <div class="col align-self-start">
          One of three columns
        </div>
    [...]

#### Zmiana kolejności

Istnieje możliwość odwołania się do klasy z prefiksem `.order-`

    <div class="container">
      <div class="row">
        <div class="col">
          First, but unordered
        </div>
        <div class="col order-12">
          Second, but last
        </div>
        <div class="col order-1">
          Third, but first
        </div>
      </div>
    </div>


#### Margines -> Offset

Uzyskanie stałego marginesu od poprzedzającego elementu (lub granicy) można osiągnąć poprzez wykorzystanie klasy z prefixem `.offset-` oraz bazując na liczbie kolumn.


    <div class="row">
      <div class="col-md-4">.col-md-4</div>
      <div class="col-md-4 offset-md-4">.col-md-4 .offset-md-4</div>
    </div>



https://getbootstrap.com/docs/4.0/layout/grid/




### Komponenty

https://getbootstrap.com/docs/4.0/components/buttons/





---
### Layoutit!

[Layoutit!](https://www.layoutit.com/build) - aplikacja do budowy stron przy pomocy Bootstrapa


---
Źródła:

[Jak dodać Bootstrapa 4 – bootstrap i Angular](https://zacznijprogramowac.net/angular/jak-dodac-bootstrapa-4-do-angulara/)

YT

[Bootstrap 5 Beta - a game changer?](https://www.youtube.com/watch?v=oOtWMEl9Uyg&feature=emb_title&ab_channel=MDB-justcodeit)

[Bootstrap 5 tutorial - crash course for beginners in 1.5H (December 2020)](https://www.youtube.com/watch?v=c9B4TPnak1A&feature=emb_title&ab_channel=MDB-justcodeit)