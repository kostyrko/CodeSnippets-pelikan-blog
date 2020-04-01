Title: CSS - pozycjonowanie
Author: mkostyrko
Date: 2020-03-30 08:00
Updated:
Category: css
Tags: css, pozycjonowanie, static, relative, absolute, fixed, sticky
Slug: css-pozycjonowanie
related_posts: flexbox-wprowadzenie, css



Podstawowe właściwości **`position`**

**`static`** - wartość domyślna, pozycja zgodna z układem strony

**`relative`** - relatywnie do swojej domyślnej pozycji przesunięty o zdefiniowaną właściwość/wartość

* `top`, `right`, `bottom`, `left` 

Przykładowe zastosowanie

      div.relative {
        position: relative;
        left: 30px;
        border: 3px solid #73AD21;
        }


**`fixed`** - pozycja relatywna do wyświetlacza (viewport) - zawsze w tym samym miejscu

* `top`, `right`, `bottom`, `left`


**`absolute`** - pozycja relatywna do najbliższego spozycjonowanego rodzica (rodzic musi mieć zdefiniowaną właściwość `position: relative/fixed`)


Przykładowe zastosowanie

    .container {
      position: relative;
    }

    .center {
      position: absolute;
      left: 0;
      top: 50%;
      width: 100%;
      text-align: center;
      font-size: 18px;
    }

**`sticky`** - pozycja zależna od pozycji scrolla i łączy w sobie cechy `relative` oraz `fixed`. Element jest pozycjonowany w sposób `relative` do momentu, w którym określone kryterium (scrolla) nie jest spełnione, wówczas spełnia cechy `fixed`

**`inherit`** - pozycja jest dziedziczona / domyślnie nie jest

Przykładowe zastosowanie

    div.sticky {
      position: -webkit-sticky; /* Safari */
      position: sticky;
      top: 0;
      background-color: green;
      border: 2px solid #4CAF50;
    }

![display-position](https://i2.wp.com/www.tutorialbrain.com/wp-content/uploads/2019/03/CSS-Position.png?resize=640%2C640&ssl=1)


**Bonus**

`z-index` - wskazuje na której pozycji ma się wyświetlić dany element - ma to szczególne znaczenie w kontekście obiektów które się zakrywają lub częściowo pokrywają

Przykładowe zastosowanie, obiekt ustawiony na pozycję -1 będzie pod spodem

    img {
      position: absolute;
      left: 0px;
      top: 0px;
      z-index: -1;
    }



Źródła i polecane linki:

Przykłady:

https://www.w3schools.com/css/css_positioning.asp

https://css-tricks.com/almanac/properties/p/position/

Opis:

https://dzone.com/articles/css-position-relative-vs-position-absolute

https://css-tricks.com/absolute-relative-fixed-positioining-how-do-they-differ/

https://www.tutorialbrain.com/css_tutorial/css_position/