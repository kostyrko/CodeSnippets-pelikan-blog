Title: Bootstrap: wprowadzenie + formularze
Author: mkostyrko
Date: 2020-12-16 12:00
Updated:
Category: css
Tags: bootstrap
Slug: css-bootstrap
related_posts: css-rwd, html-css-bem



![css-bootstrap](https://mdbcdn.b-cdn.net/wp-content/uploads/2020/06/bootstrap-5.jpg)

[Bootstrap](https://getbootstrap.com/) - jest biblioteką CSSwą Twittera, jej możliwości oparte są na 3 podstawowych cechach 1) responsywnym układzie (opartym na grid + flex) strony 2) na elementach, z których może powstać strona (np. formularze, komponenty(np. buttons, carousel, dropdowns, navs), oraz narzędziach(np. scrollspy, tooltips)) - stworzonych z html/css/js (dla v < 5.0 również jQuery) 3) gotowych układach/motywach oraz ikonach

Linki: [Bootstrap - cheatsheet](https://getbootstrap.com/docs/5.0/examples/cheatsheet/#one), [IKONY](https://icons.getbootstrap.com/),[MOTYWY](https://themes.getbootstrap.com/)

----

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




### Kontenery i responsywność

Punkty graniczne na których jest oparta responsywność Bootstrapa dostępne są w postaci mapy w [**_variables.scss**](https://github.com/twbs/bootstrap/blob/99379f3843ddd5bd66ce6559ab91ef68c744fbd7/scss/_variables.scss#L118), w których kolejno przypisane są klucze reprezentujące nazwy klas

    $grid-breakpoints: (
      xs: 0,
      sm: 576px,
      md: 768px,
      lg: 992px,
      xl: 1200px,
      xxl: 1400px
    );


W przypadku pracy z Sassem deklaracja własnych styli powinna odbywać się poprzez odwołanie się do @mixina w sposób następujący (pierwsza deklaracja dotyczy przedziału xs) 

    .custom-class {
      display: none;
    }
    @include media-breakpoint-up(sm) {
      .custom-class {
        display: block;
      }
    }

To na CSS zostanie "przełożone" w następujący sposób (576px odpowiada **sm**):

    .custom-class {
      display: none;
    }
    @media (min-width: 576px) { ... }

Powyższa deklaracja jest dla **min-width** w przypadku **max-width** ostatnim słowem tworzącym nazwę @mixina jest słowo **down** (zamiast up) np. `@include media-breakpoint-down(sm) {...}`


#### Kontenery

Kontenery są podstawowym blokiem budującym strony oparte na bootstrapie, to w ramach konteneru tworzony jest układ oparty na siatce/grid (który jest podzielony na kolumny (pion) i rzędy (poziom))

Bootstrap oferuje 3 rodzaje kontenerów -> `.container` , `.container-fluid`, `container-{breakpoint}` (breakpoint tj nazwa klasy)

`.container-fluid` - szerokość jest zawsze równa 100% (`width: 100%`)


W przypadku `.container` ich maksymalna szerokość jest mniejsza od punktów granicznych związanych z responsywnością


||Extra small <576px|Small ≥576px	|Medium ≥768px	|Large ≥992px	|X-Large ≥1200px	|XX-Large ≥1400px|
|---|---|---|---|---|---|---|
.container|	100%	|540px	|720px	|960px	|1140px	|1320px|


`container-{breakpoint}` - podana klasa reprezentująca punkt graniczny/media query określa ten od którego kontener nie wynosi 100% - przykładowo 

`container-lg` oznacza, że dla xs,sm i md kontener będzie `width: 100%` natomiast dla lg już będzie wynosił **960px** dla xl i xxl również wg. powyżeszj tabeli (jak dla `.container`)

    <div class="container-md">100% wide until medium breakpoint</div>

Podobnie jak w przypadku tzw. breakpointów mapa szerokości kontenerów znajduje się w pliku [**_variables.scss**](https://github.com/twbs/bootstrap/blob/99379f3843ddd5bd66ce6559ab91ef68c744fbd7/scss/_variables.scss#L118)

    $container-max-widths: (
      sm: 540px,
      md: 720px,
      lg: 960px,
      xl: 1140px,
      xxl: 1320px
    );



### Bootstrap Grid czyli część dalsza RWD

Our grid supports six responsive breakpoints.

1 - Bootstrapowa siatka oparta jest na systemie 6 punktów przełomowych zw. z szerokością ekranu (tzw. breakpoints zw. z media-queries)

2 - Kontenery wyśrodkowują treść (pion i w poziomie paddingują)

3 - Rzędy opakowują kolumny

4 - kolumny są elastyczne

5 - marginesy pomiędzy kolumnami/rzędami są responsywne i konfigurowalne

Gutters are also responsive and customizable.

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



więcej informacji na temat: [Bootstrapowego grida](https://getbootstrap.com/docs/5.0/layout/grid/)

### Gutters - marginesy 

"Marginesy" gutters w wersji podstawowej wynoszą 1.5 rem (24px) jednak ich zakres faktyczny zaczyna się od 0 i dochodzi do 3rem -> [**_variables.scss**](https://github.com/twbs/bootstrap/blob/99379f3843ddd5bd66ce6559ab91ef68c744fbd7/scss/_variables.scss#L118)

    $spacer: 1rem !default;
    $grid-gutter-width: 1.5rem;
    $gutters: (
      0: 0,
      1: $spacer * .25,
      2: $spacer * .5,
      3: $spacer,
      4: $spacer * 1.5,
      5: $spacer * 3,
    );

`.gx-*` - horyzontalne "marginesy" np. `.gx-5`

`.gy-*` - wertykalne "marginesy

`.g-5` - horyzontalne + wertykalne

podobnie sprawy się mają w przypadku paddingów:

`.px-*` - horyzontalne paddingi np. `.px-3`

`.p-3` - padding x 3

więcej na ten temat tutaj: [getbootstrap.com -> utilities -> spacing](https://getbootstrap.com/docs/5.0/utilities/spacing/)

---
### Komponenty i narzędzia

Poznawanie komponentów oraz ich możliwości najlepiej zacząć od przeglądania tzw. ściągi [Bootstrap - cheatsheet](https://getbootstrap.com/docs/5.0/examples/cheatsheet), która z powodzeniem może funkcjonować jako ich wizualny spis treści.


---
### Formularze

Zachowanie inputy w bootstrapowym formularzu (podobnie jak i w zamym html) jest zależne od zdefiniowanego typu (np. email,password, number) 

|Klasa|zastosowanie|Przykład|
|---|---|---|
|`.form-control`|podstawowa klasa elementu formularza w Bootstrapie| `<input type="email" class="form-control" [..]/>`|
|`.form-control-{rozmiar}`|kontroluje wielkość elementu formularza|`.form-control-lg`|
|`.form-control-plaintext"`|w miejscu formularza pojawia się tekst|`<input class="form-control-plaintext" [..]/>`|
|`.form-text`|tekst będący częścią formularza (np. komentarz p/div/span)||
|`disabled`|dodanie `disabled` do html powoduje, że pole jest niedostępne|`<input [..] disabled/>`|
|`readonly`|pole jedynie do odczytu|`<input [..] readonly/>`|
|`type="file"`|input pozwalający na załadowanie pliku/ścieżki|`<input class="form-control" type="file">`|
|`form-control-color`|umożliwia wybóru koloru (istnieje możliwość zdefiniowania koloru wyjściowego)|`<input type="color" class="form-control form-control-color" value="#563d7c" [...]>`|
|`.form-select"`|klasa dla elementu formularza typu select|`<select class="form-select" [...]>`|
|`selected`|wybrany element||
|`multiple`|definiuje select wielokrotnego wyboru|`<select class="form-select" multiple [...]>`|
|`form-check`|klasa opakowująca dla checkbox'a lub radio w zależności od zdefinowanego typu|`<div class="form-check">``<input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">`|
|`form-check-input`|input dla checboxa lub radio w zal. od zdef. typu||
|`.form-check`+`.form-switch`|input typu switch|`<div class="form-check form-switch"> <input class="form-check-input" type="checkbox"/>`|

#### Walidacja

W kontekście walidacji istotne są 2 pesudo-klasy `:invalid` (NIEprawidłowy) and `:valid` (prawidłowy) które należy zaaplikować do elementów `<input>`,` <select>` oraz `<textarea>`

Klasa `.was-validated` (powinna zostać naddana po walidacji) odnosi się do rodzica, zwykle elementu `<form>`, po przesłaniu należy ją usunąć aby formularz powrócił do poprzedniego stanu.

Klasy `.is-invalid` and `.is-valid` mogą zostać użyte zamiast wyżej wymienionych pseudo-klas w przypadku walidacji następującej po str. serwera i on nie wymagają zastosowania `.was-validated` u rodzica.

Dodając `novalidate` (atrubut typu logicznego) do `<form>` powoduje zablokowanie domyślnej walidacji ze str przeglądarki oraz pojawiania się jej tzw. tooltipów (dymków z informacją zwrotną). 

Przykład walidacji (źródło: [getbootstrap.com -> validation](https://getbootstrap.com/docs/5.0/forms/validation/))

    <form class="row g-3 needs-validation" novalidate>
      [...]
    </form>

    (function () {
      'use strict'

      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      const forms = document.querySelectorAll('.needs-validation')

      // Loop over them and prevent submission
      Array.prototype.slice.call(forms)
        .forEach(function (form) {
          form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
              event.preventDefault()
              event.stopPropagation()
            }

            form.classList.add('was-validated')
          }, false)
        })
    })()

Więcej na temat walidacji formularzy (min. na temat walidacji przez serwer/informacja zwrotna): [getbootstrap.com -> validation](https://getbootstrap.com/docs/5.0/forms/validation/)

---
### Layoutit!

[Layoutit!](https://www.layoutit.com/build) - aplikacja do budowy stron przy pomocy Bootstrapa


---
Źródła:

[Bootstrap](https://getbootstrap.com/)

[Bootstrap 4 Tutorial](https://www.w3schools.com/bootstrap4/default.asp)

YT

[Bootstrap 5 Beta - a game changer?](https://www.youtube.com/watch?v=oOtWMEl9Uyg&feature=emb_title&ab_channel=MDB-justcodeit)

[Bootstrap 5 tutorial - crash course for beginners in 1.5H (December 2020)](https://www.youtube.com/watch?v=c9B4TPnak1A&feature=emb_title&ab_channel=MDB-justcodeit)