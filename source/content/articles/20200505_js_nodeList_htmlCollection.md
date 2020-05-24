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

Uporządkowana lista wszystkich węzłów DOM, obiekty można uzyskać poprzez odwołanie się do indeksu

Kolekcja jest odświeżana automatycznie w momencie gdy DOM ulega zmianie.

document.`querySelectorAll('div')`

### HTML Collection

Lista węzłów będących **elementami** - węzeł może być użyty poprzez odwołanie się do nr indeksu, nazwy węzła lub id atrybutu.

Kolekcja jest odświeżana automatycznie w momencie gdy DOM ulega zmianie.

Atrybuty: length
Metody: 
`item()` - jako argument przyjmuje nr indeksu i zwraca obiekt, zwraca `null` gdy jest po za zasięgiem (brak elementu o podanym indeksie)
`nameItem()` - przyjmuje nazwę obiektu lub jego id i zwraca zwraca obiekt lub `null` w przypadku braku

---

Źródła:

https://stackoverflow.com/questions/15763358/difference-between-htmlcollection-nodelists-and-arrays-of-objects

https://www.w3.org/TR/DOM-Level-2-HTML/html.html#ID-75708506

https://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-536297177

https://www.w3schools.com/jsref/prop_node_nodetype.asp