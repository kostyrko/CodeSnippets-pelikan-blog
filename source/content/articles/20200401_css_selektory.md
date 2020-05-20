Title: CSS - składnia selektory
Author: mkostyrko
Date: 2020-04-01 09:00
Updated:
Category: css
Tags: css, selektory, znaczniki, potomek, dziecko
Slug: css-selektory
related_posts: css-pseudo-elementy


Schemat

    Lista dyrektyw

    selektor { 
    właściwość - wartość właściwości; /* razem tworzą deklarację */
    }

    ang. rule set

    Selector {
      property: property value; /* declaration */
    }

Selektor znacznika np `strong`
Selektor klasy poprzedzony jest kropką `.`

Selektor id poprzedzony jest haszem `#`

Selektor id nadaje priorytet regule ważniejszy od niż ten posiadający klasę, a selektor znacznika/typu ma najmniejszy priorytet.

---

### Selektory elementów

**`*`** - każdy element/ selektor uniwersalny

**`e p`** - element "p" będący **potomkie**m elementu "e"

**`e > p`** - element "p" będący **dzieckiem** elementu "e"

**`e + p`** - element "e" bezpośrednio poprzedzony elementem "e"

**`e ~ p`** - element "e" poprzedzany przez element "p"

Przykładowe zastosowanie

  li .taskBtn ~ .taskBtn {
  color: white;
  background-color: green;
  }

::: wszystkie elementy będące dzieckiem elementu li poprzedzone elementem z klasą .taskBtn
---

### Selektory atrybutów

**`e[atrybut]`** - element zawierający wybrany atrybut

    a[target] {
      background-color: yellow;
    }

    <a href="http://www.wikipedia.org" target="_top">wikipedia.org</a>

**`e[atrybut="wartość"]`** - element posiadający atrybut z konkretną wartością

    a[target="_blank"] {
      background-color: yellow;
    }

    <a href="http://www.wikipedia.org" target="_top">wikipedia.org</a>
    <a href="http://www.w3schools.com" target="_blank">w3schools.com</a>

**`e[atrybut~="konkretna_wartość"]`** - element zawierający atrybut, którego częścią jest konkretna wartość

    [title~="flower"] {
      border: 5px solid yellow;
    }

    <img src="img_flwr.gif" title="flower" width="224" height="162">

[Pełna lista](http://www.kurshtml.edu.pl/css/selektory.html)

---

**Gra selektory**

http://flukeout.github.io/

---

### Moce selektorów

![Star Wars Selectors](https://stuffandnonsense.co.uk/archives/images/css-specificity-wars.png)



Źródło i polecane linki:

https://the-awwwesomes.gitbooks.io/html-css-step-by-step/content/pl/css-advanced-selectors/index.html

https://developer.mozilla.org/pl/docs/Web/CSS/Na_pocz%C4%85tek/Selektory

https://stuffandnonsense.co.uk/archives/css_specificity_wars.html

https://developer.mozilla.org/pl/docs/Learn/Getting_started_with_the_web/CSS_basics

