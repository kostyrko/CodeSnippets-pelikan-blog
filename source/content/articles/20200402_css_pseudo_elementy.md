Title: CSS::pseudo-elementy
Author: mkostyrko
Date: 2020-04-02 07:00
Updated:
Category: css
Tags: css, pseudo-elementy, first-line, ::before, ::after
Slug: css-pseudo-elementy
related_posts: flexbox-wprowadzenie

Pseudo elementy pozwalają na zadeklarowanie wyglądu odmiennego dla wybranego fragmentu tekstu lub wstawienie z pozycji CSS dodatkowego elementu. Pseudo elementy poprzedzone są podwójnym dwukropkiem `::` np.   `::first-line`

Wzór zastosowania (za [developer.mozzilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements))

    selector::pseudo-element {
      property: value;
    }

    selektor::pseudo-element {
      właściwość: wartość;
    }

Innymi słowy pseudoelement jest słowem kluczowym, które w połączeniu z wybranym selektorem pozwala na stylowanie wybranej części wybranego elementu.

* stylowanie pierszej litery lub linii
* wstawianie nowego elementu (np. obrazu)

Przykładowe zastosowanie

    p::first-line {
      color: blue;
      text-transform: uppercase;
    }

`::first-line` - pozwala na zadeklarowanie konkretnych cech dla pierwszej linii wybranego tekstu
[na marginesie przykładowo do identacji tekstu nie trzeba stosować pseudo-elementów, wystarczy np `text-indent` ]

Do pseudo-selektorów można dodać odpowiednio np. - `font`, `color`, `word-spacing`, `background`, `text-decoration`, `line-height`

`::first-letter` - zadeklarowanie konkretnej cechy dla pierwszej litery

`::after` - reprezentuje ostatnie dziecko wybranego elementu/ podstawową właściwością jest `content` w ramach, której definiowana jest zawartość dodawanego elementu np. tekst lub link do obrazu

Przykładowe zastosowanie dodające określony tekst po tekście zawartym w wybranym paragrafie

    p::after {
      content: “this text will be added after”;
      color: blue;
    }


`::before `- tworzy pseudo-element, który reprezentuje pierwsze dziecko wybranego selektora HTML, posiada właściwość `content` analogiczną do `::after`

`::selection` - odwołuje się do podświetlenia wybranego tekstu znajdującego się w selekcji

Przykładowe zastosowanie

    p::selection {
      background-color: red;
    }

ale może zawierać również: `color`, `background-color`, `cursor`, `caret-color`, `outline`, `text-decoration`, `text-emphasis-color,` `text-shadow`

`::marker` - pozwala na stylowanie markera listy

Przykładowe zastosowanie 

    ul li::marker {
      color: red;
      font-size: 150%;
    }

`::placeholder` - pozwala na stylowanie fragmentu formularza który przyjmuje input 

Przykładowe zastosowanie

    input::placeholder {
    color: red;
    font-size: 1.2em;
    font-style: italic;
    }

Pełna lista (łącznie z jeszcze nie w pełni wdrożonymi pseudoelementeami) znajduje się [tutaj](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

---

Źródło i polecane linki:

https://blog.logrocket.com/a-guide-to-css-pseudo-elements/

https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements

https://www.w3schools.com/css/css_pseudo_elements.asp

https://css-tricks.com/almanac/selectors/a/after-and-before/

https://css-tricks.com/pseudo-element-roundup/
