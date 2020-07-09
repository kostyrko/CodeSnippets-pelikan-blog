Title: CSS konwencje nazewnictwa klas -> OOCSS, BEM i BEMIT
Author: mkostyrko
Date: 2020-06-18 10:00
Updated:
Category: css
Tags: css, html, klasy, bem, bemit, oocss
Slug: html-konwencje-klas
related_posts: 

![BEM](https://www.e-accent.com/images/blog/bem.png#center){: max-height="300px"}


### Podstawowe zasady nazewnictwa

Nazewnictwo klas CSS zaczyna się od... wybrania odpowiedniego taga HTML a później...

#### Podział na 3 sposoby nazywania klas

* funkcjonalność (Functional class names) -> połączenie klasy z elementem ze względu na jego znaczenie `selected-button`, `important-text`

* zawartość (Content-based class names) -> klasy wskazujące na zawartość elementu `submit-button`, `intro-text`

* prezencja (Presentational class names) -> klasy zorientowane na sposób prezentacji elementu `round-image` `green-button`

więcej na ten temat przeczytasz tutaj [Naming CSS Stuff Is Really Hard](https://seesparkbox.com/foundry/naming_css_stuff_is_really_hard)

---

### OOCss/ Object Oriented CSS

Metodyka OOCSS jest zorientowana na stworzenie modularnego CSS zorientowanego obiektowo - elementy strony postrzegane są jako obiekty

Podstawowe zasady:

* **separacja struktury od stylu** (tworzenie klas globalnych a następnie niższego rzędu odpowiedzialne za stany obiektów oraz wielkość/prezencję obiektów `.btn` -> `.btn-clicked`, `btn-primary`)

* **separacja kontenerów i zawartości** (wygląd obiektu nie powinien być zależny od elementu, w którym się znajduje - jego ewentualna modyfikacja powinna być uzależniona od osobnej klasy przypisanej tej danej modyfikacji `.article-header` zamist `.article h1`)

![others-css](https://ach-te-internety.pl/wp-content/uploads/2016/07/bem-css-768x432.png){: height="250px"}

---

#### Podstawowe zasady, o których warto pamiętać

**Zasada 1** Dwuczłonowe nazwy klas rozdzielać należy myślnikiem `-` (w przypadku JS stosowany jest camelCase) `secondaryButton` -> `secondary-button`

**Zasada 2** - Nazwa klasy powinna być na najniższym poziomie elementu, który ma zostać wystylizowany lub inaczej rzecz ujmując bezpośrednio na danym elemencie.

**Zasada 3** - wykorzystaj zawartość danego elementu html np. klasa `header-logo`

**Zasada 4** - nie wykorzystuj zawartości jeśli to kształt w łatwiejszy sposób przekazuje (jest czytelniejszy) czym jest dany element.

======================

**Zasada 5** - jeśli dany element jest podobny do czegoś ale tym nie jest można stosować przyrostek `-like` np. `h1-like`

**Zasada 6** - jeśli chcesz klasę wykorzystać jako element związany z JS możesz klasie nadać przedrostek `js-` np. `js-click-me`

**Zasada 7** - należy unikać klas dłuższych niż dwa słowa

**Zasada 8** - można używać przedrostków is- lub has- dla klas opisujących dany stan np `.activate` -> `.is-activate`

---

![BEM-batman](https://res.cloudinary.com/indysigner/image/fetch/f_auto,q_auto/w_1600/https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/3a93b95e-3e4e-4367-86cb-0606ace15af3/sign-theme-batman.png){: height="300px"}

### [BEM](http://getbem.com/)

Jedna z najpopularniejszych koncepcji nazewnictwa CSS

### Podstawa

**Block/Blok** - sam w sobie określa własne znaczenie -> `header`, `menu`, `button`, `input`, `aside`

**Element** - element bloku -> `header__title`

**Modifier/Modyfikator** - zmienia wygląd lub zachowanie danego elementu -> `input–-disabled`

![BEM-blok](https://en.bem.info/kFetIbKxQdABHhUecbic45Il0Bg.png){: width: "500px"}

#### Istotne: 

Rozgraniczenie wyrazów w nazwie klasy podwójnym myślnikiem oznacza wariację elementu **`--`** (`input–-disabled`, `header--blue`)

Podwójnym podkreślnikiem oznacza dziecko elementu **`__`** (`menu__item`)


#### Blokowisko

Strona internetowa może być rozumiana poprzez podział na bloki, gdzie każdy kolejny poziom albo poszerza poprzedni albo go nadpisuje własnym stylem

![gw](https://en.bem.info/kqvCO2ZXeivuLHCbn2to5chFZrM.png)



---

### BEMIT

BEM + ITCSS (Inverted Triangle CSS) = BEMIT.

Inverted Triangle CSS -> Odwrócony trójkąt CSS, którego podstawowym założeniem jest strukturyzacja projektu zgodnie z trzema założeniami

1) zaczyna się od szczegółu i przechodzi do ogółu

2) zaczyna się od deklaracji używających jak najmniejszą ilość selektorów (mniej konfliktów na koniec)

3) selektory zastosowane na początku powinny mieć jak najszerszy zasięg np. reset

tu można przeczytać na temat 7 warstw projektu (Saas) -> [The Inverted Triangle Architecture: how to manage large CSS Projects](https://www.freecodecamp.org/news/managing-large-s-css-projects-using-the-inverted-triangle-architecture-3c03e4b1e6df/)

![Inverted Triangle CSS](https://cdn-media-1.freecodecamp.org/images/1*4oGYOCrfBqsjnqGwZ_GaHg.jpeg){: height="300px"}


[**BEMIT Cheatsheet**](https://gist.github.com/kostyrko/54aa8c4fd5ab64e2ea81b5d69f8183e3)

---

#### Znaczeniowe przedrostki - akronimy (Namespaces)

| litera | znaczenie
|---|---|
|`c`| Components/element |
|`o`| Objects/obiekt |
|`u`| Utilities/narzędzie |
|`is/has`| stan bycia/posiadania |
|`t`| theme/skórka |
|`s`| styling/stylizacja |
|`js`| powiązanie z JS |


Przykładowe zastosowanie

    <p class="o-media__body  c-user__bio">...</p>

Więcej na ten temat tutaj: [More Transparent UI Code with Namespaces](https://csswizardry.com/2015/03/more-transparent-ui-code-with-namespaces/)

---

#### Responsywne Przyrostki


#### Responsywne Przyrostki

Tu kluczowy jest znak `@` (ang. at ~ w) i oznacza, w którym momencie (media query) dana klasa się aktywuje (w zależności od tzw break pointów / punktów załamania) 

`o-layout@md` - obiekt układu w momencie średniego (middle) punktu załamania

`u-1/4@lg` - narzędzie gdy media-query large spełnia swój warunek posiada 1/4 szerokości

`scss`

        $lg = 1240px

        @media screen and (min-width:${lg}){
            deklaracja: właściwość;
        }

#### Wizualizacja wielu podobnych

Stosowanie nazewnictwa klas według jednego schematu pozawala na i późniejsze debugowanie lub wizualizaję elementów zbliżonych do siebie cechami w celu sprawdzenia poprawności deklaracji/ funkcjonowania strony

                /**
        * Ukazuje wszystkie klasy.
        */
        [class] {
        outline: 5px solid lightgrey;
        }

        /**
        * Ukazuje wszystkie elementy BEM - wszystkie które posiadają "__".
        */
        [class*="__"] {
        outline: 5px solid grey;
        }

        /**
        * Modyfikatory.
        */
        [class*="--"] {
        outline: 5px solid darkgrey;
        }

        /**
        * klasy obiektów.
        */
        [class^="o-"],
        [class*=" o-"] {
        outline: 5px solid orange;
        }

        /**
        * klasy składnikowych elementów.
        */
        [class^="c-"],
        [class*=" c-"] {
        outline: 5px solid cyan;
        }

        /**
        * klasy związane z responsywnością.
        */
        [class*="@"] {
        outline: 5px solid rosybrown;
        }

        /**
        * Wszystkie klasy przypisane do Hack classes.
        */
        [class^="_"] {
        outline: 5px solid red;
        }

        /**
        * Poprzez dodanie klasy hakowej do warstwy html (scss zagnieżdżenie powyższych w s-healthcheck)
        */
        
        <html class="s-healthcheck">

---

### Na zakończenie

::: Należy pamiętać o pisaniu komentarzy w kodzie CSS ::: przejrzystość i czytelność priorytetem nr 1

---

Źródła


[How to name css classes](http://bdavidxyz.com/blog/how-to-name-css-classes/)

[BEMIT: Taking the BEM Naming Convention a Step Further](https://csswizardry.com/2015/08/bemit-taking-the-bem-naming-convention-a-step-further/)


[Metodyki CSS #1 - OOCSS](https://www.nafrontendzie.pl/metodyki-css-1-oocss)

[Metodologia BEM. Jak pisać dobry kod CSS. Praktyczne przykłady.](https://www.nafrontendzie.pl/metodyki-css-2-bem)

[Metodyki CSS #2 – BEM](https://www.nafrontendzie.pl/metodyki-css-2-bem)

[css-naming-conventions-that-will-save-you-hours-of-debugging](https://www.freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849/)


[BEM - naming conventions](https://en.bem.info/methodology/naming-convention/)



