Title: JavaScript - selektory DOM
Author: mkostyrko
Date: 2020-05-02 10:00
Updated:
Category: javascript
Tags: js, javascript, selektory, dom, elementy dom, 
Slug: js-dom-elementy-selektory
related_posts: js-obiekt-window-document

### Selektory pojedynczych elementów



| selektor | funkcja | przykładowe zastosowanie
|---|---|---|
| `document.getElementById()` | zwraca element w podanym Id | `document.getElementById('button-4')` |
| `document.querySelector()`| zwraca pierwszy element spełniający podany warunek/ wpisany składnią znaną z CSS | `document.getElementById('#button-4')` |

:::Istnieje możliwość łączenia selektorów z atrybutami :::

Przykładowe zastosowanie

  `document.getElementById('button-4').className` // zwraca klasę

  **const button = document.getElementById('button-4')**

  `button.style.background = 'red'` // zmienia tło na czerwone

  `button.style.display = 'none'` - element znika

  `button.style.display = " "` - element się pojawia

  `button.textContent = "tekst"` - wpisuje treść

  `button.innerText = "tekst"` - wpisuje treść

  `button.innerHTML = "<span style="color: red">tekst</span>"` - dodaje html

  `document.querySelector('#button')` - pierwszy element gdzie id='button'

  `document.querySelector('.button')` - pierwszy element gdzie class='button'

  `document.querySelector('.button .name')` - pierwszy element gdzie class='name' będący dzieckiem elementu gdzie class='button'

  `document.querySelector('h1')` - pierwszy element z tagiem h1

  `document.querySelector('h1 span')` - pierwszy dziecko *span* elementu *h1*

  `document.querySelector('li:last-child')` - pierwszy element typu *li* będący *ostatnim dzieckiem*

  `document.querySelector('li:nth-child(odd)').style.color = "red"` - pierwszy element typu *li* będzie czerwony (ponieważ pierwszy jest nieparzysty)

  `document.querySelector('[href = "google.com"]')` - pierwszy element z atrybutem href


### Selektory wielu elementów

Zwracają kolekcję HTML (HTML Collection) albo node-list


| selektor | funkcja | przykładowe zastosowanie
|---|---|---|
| `document.getElementsByClassName()` | zwraca wiele elementów na podstawie podanej nazwy klasy w postaci kolekcji html | `document.getElementsByClassName('buttons')` |
| `document.getElementsByTagName()` | zwraca wiele elementów na podstawie podanego tagu w postaci kolekcji html | `document.getElementsTagName('li')` |
| `document.querySelectorAll()` | zwraca wszystkie element spełniający podany warunek/składnia CSS jako NodeList | `document.querySelectorAll('ul.list li.list-item')` |

**::: Konwersja HTML collection :::**

    let arr = Array.from(document.getElementsTagName('li'))

    arr.forEach(function(elem, index){
      console.log(index, elem.className);
    });

**::: NodeList nie wymaga konwersji ponieważ ma metodę forEach() :::**

`document.querySelectorAll('li:nth-child(odd)')` - co 2. element listy, każde parzyste dziecko będące li - aby nadać styl należy użyć pętli `for` lub `forEach`

    const oddItem = document.querySelectorAll('li:nth-child(odd)')

    oddItem.forEach(function(elem){
      elem.style.background = 'red'
    });

Lub (działa również dla kolekcji html)
  
    for(let i = 0; i < oddItem.length; i++ ) {
      oddItem[i].style.background = 'red'
    }

Przykładowe zastosowanie

`document.getElementsByClassName('buttons')[3].style.color= 'red'` - zmieni 4 zwrócony element na czerwono

'document.querySelector('ul').getElementsByClassName('list-item') - zwróć wszystkie elementy mające klasę *list-item* będące się w elemencie *ul*



### Przechodzenie pomiędzy elementami DOM

### Tworzenie elementów

### Usuwanie i wymiana elementów


### Ćwiczenia

[GRA](ttps://mtomchuck.github.io/monster-village/dist/)

---

Źródła:

https://developer.mozilla.org/en-US/docs/Web/API/NodeList
