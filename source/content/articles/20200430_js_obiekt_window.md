Title: JavaScript - obiekt window i document
Author: mkostyrko
Date: 2020-04-30 10:00
Updated:
Category: javascript
Tags: js, javascript, window, document
Slug: js-obiekt-window-document
related_posts: 

Obiekt *document* jest częścią obiektu *window* i został opisany poniżej. Wybrane metody obiektu window (globalny) ->

### Window

`alert()` - pokazuje się okienko z ostrzeżeniem

    window.alert('Hello world') 

lub po prostu

  alert('Hello world')

`prompt()` - wyskakuje okienko z informacją

`confirm()` - przyjmuje parametr

    if(confirm('Are you sure?')) {
      console.log('Yes)
    }

`window.outerHeight`/`Width` - zwraca wysokość/szerokość okna

`window.innerWidth`/`Height` - zwraca wewnętrzną szerokość/wysokość okna


`window.scrollY` - ukazuje poziom (miejsce na stronie) scroll w pionie `scrollX` - w poziomie
pozwala na korelację z długością strony oraz animacją ukazującą ilość przeczytanej treści

---
#### Obiekt lokacyjny

`window.location` -> jest właściwością obiektu window i jest referencją do obiektu Location/lokacji

`window.location.hostname`
`window.location.port`
`window.location.href`
`window.location.search`

// Redirect

`window.location.href = 'http://google.com'` - będzie odsyłać do strony google
`window.location.reload()` - będzie przeładowywać stronę

---
#### Obiekt historii

Daje możliwość przeglądania historii korzystania przeglądarki

`window.history.go(-1)` - odsyła do poprzedniej strony/ jako argument kolejność w odwiedzonych stronach
`window.history.length` - ilość pozycji w historii

---

#### Obiekt Navigatora

Odwołuje się do właściwości przeglądarki

`window.navigator` - zwraca informacje na temat przeglądarki np. geolokalizację

`window.navigator.appVersion` - wersja przeglądarki

`window.navigator.platform` - zwraca system operacyjny

`window.navigator.vendor` - provider internetu

`window.navigator.language` - język przelądarki

---
### Obiekt document i jego właściwości

Obiekt `document` zawiera całą zawartość przeglądanego pliku HTML

Część właściwości zwraca w postaci tzw node-list przypominającej tablicę, choć nią nie są [wymaga konwersji do tablicy by używać ich metod]

`document.all` - zwraca całość w postaci node-listy wszystkie elementy  
`document.all.length` - zwraca liczbę 
`document.head` - elementy z head
`document.body` - elementy z body
`document.doctype` - rodzaj dokumentu
`document.domain` - domenę
`document.url` - url
`document.characterSet` 
`document.contentType` - np. text/html

`document.forms` - zwraca wszystkie formy z html
`document.forms[0]` - można traktować jak listę i wydobyć po indeksie
`document.forms[0].id` - zwraca id
`document.forms[0].method` - zwraca dostępną metodę
`document.forms[0].action` - zwraca przypisaną akcję

`document.links` - zwraca linki [a]
`document.links[0].id/.className/.classList` - zwraca id, klasy, listę klas

`document.images` - zwraca obrazy

`document.scripts` - zwraca wszystkie skrypty js

`document.scripts[2].getAttribute(`src') - treść atrybutu source

#### Przypisanie elementów document do tablicy

    let scripts = document.scripts
    let arr = Array.from(scripts)

    arr.forEach(function(script){
      console.log(script.getAttribute(`src'))
    })

---

Źródła:

https://developer.mozilla.org/en-US/docs/Web/API/Window/location