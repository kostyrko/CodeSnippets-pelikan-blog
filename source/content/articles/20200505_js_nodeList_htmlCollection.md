Title: DOM: NodeList i HTML Collection
Author: mkostyrko
Date: 2020-05-05 10:00
Updated:
Category: javascript
Tags: javascript, js, dom, kolekcje węzłów DOM, kolekcja węzłów DOM, collection of DOM nodes
Slug: js-nodelist-htmlcollection
related_posts: js-wydarzenia-dom-1, js-wydarzenia-dom-2, js-dom-elementy-selektory, js-dom-manipulowanie-elementami


Kolekcje węzłów DOM

Typy węzłów

* element node
* attribute node
* text node
* comment node

### NodeList

Uporządkowana lista wszystkich węzłów DOM (w tym również węzłów tekstowych oraz bloków tekstowych), obiekty można uzyskać poprzez odwołanie się do indeksu

`querySelectorAll()`/`getElementsByName()` - - metody document zwracające NodeList

NodeList posiada metodę `forEach()` !!

NodeList, jest `static` - zwrócona lista nie jest odświeżana w przypadku zmian w DOM -> brak detekcji zmian


### HTMLCollection

Lista węzłów (wybranego typu) będących **elementami** - węzeł może być użyty poprzez odwołanie się do nr indeksu, nazwy węzła lub id atrybutu.

W większości przypadków kolekcja jest odświeżana automatycznie w momencie gdy DOM ulega zmianie.

`getElementsByTagName()` / `getElementsByClassName()` - metody document zwracające HTMLCollection

Posiada atrybut *length*

Metody: 
`item()` - jako argument przyjmuje nr indeksu i zwraca obiekt, zwraca `null` gdy jest po za zasięgiem (brak elementu o podanym indeksie)
`nameItem()` - przyjmuje nazwę obiektu lub jego id i zwraca zwraca obiekt lub `null` w przypadku braku

---

Sprawdź wynik poniższego kodu ([źródło](https://dev.to/jharteaga/difference-between-htmlcollection-and-nodelist-25bp))

Index.html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Demo</title>
      </head>
      <body>
        <ul id="list">
          <li class="item">Pierwszy Element</li>
          <li class="item">Drugi Element</li>
          <li class="item">Trzeci Element</li>
        </ul>
        <script src="script.js"></script>
      </body>
    </html>


script.js

    //złap element UL
    const list = document.getElementById('list');

    //Złam element wykorzystując dwie metody oraz jego klasę (two ways)
    const itemsByClassName = document.getElementsByClassName('item');
    const itemsByQuerySelector = document.querySelectorAll('.item');

    console.log('Pierwszy console log', itemsByClassName, itemsByQuerySelector);

    //dodaj czwarty element
    list.innerHTML += `<li class="item">Czwarty Element</li>`;

    console.log('Kolejny console log', itemsByClassName, itemsByQuerySelector);


**Tak, NodeList dalej będzie zawierało 3 elementy podczas gdy HTMLCollection zwróci 4 podczas kolejnego wywoływania zmiennych**

---

Źródła:

https://stackoverflow.com/questions/15763358/difference-between-htmlcollection-nodelists-and-arrays-of-objects

https://www.w3.org/TR/DOM-Level-2-HTML/html.html#ID-75708506

https://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-536297177

https://www.w3schools.com/jsref/prop_node_nodetype.asp


https://medium.com/@layne_celeste/htmlcollection-vs-nodelist-4b83e3a4fb4b