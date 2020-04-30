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

Zwracają kolekcję HTML albo node-list


| selektor | funkcja | przykładowe zastosowanie
|---|---|---|
| `document.getElementById()` | zwraca element w podanym Id | `document.getElementById('button-4')` |
| `document.querySelector()`| zwraca pierwszy element spełniający podany warunek/ wpisany składnią znaną z CSS | `document.getElementById('#button-4')` |


### Przechodzenie pomiędzy elementami DOM

### Tworzenie elementów

### Usuwanie i wymiana elementów


### Ćwiczenia

[GRA](ttps://mtomchuck.github.io/monster-village/dist/)

---

Źródła:

