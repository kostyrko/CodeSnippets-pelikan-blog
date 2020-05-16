Title: JavaScript i DOM - tworzenie, usuwanie i pozyskiwanie informacji z elementów
Author: mkostyrko
Date: 2020-05-02 11:00
Updated:
Category: javascript
Tags: js, javascript, selektory, dom, elementy dom, 
Slug: js-dom-manipulowanie-elementami 
related_posts: js-dom-elementy-selektory


### Tworzenie elementów DOM

`.createElement()` - stwórz element

    const li = document.createElement('li')
    li.innerText = `To jest tekst dodanego elementu`


`.cloneNode(true)` lub `.cloneNode(false)` - klonowanie elementu true = deep /false != deep
 -> tzw głębokie klonowanie zakłada tworzenie takiej samej kopii wraz z dziećmi 

    const div2 = div1.cloneNode(true)

Klonowanie pozwala na replikację elementu i może być przydatne w sytuacji, w której chcemy stworzyć element taki sam do elementu istniejącego a następnie go zmienić. Element wyjściowy (wzór) może być stworzony w HTML i może mieć ustawiony display = none lub może powstać na podstawie funkcji tworzącej

---

`.appendChild()` - dodanie elementu jako dziecka dziecka

    li.appendChild(document.createTextNode('Hello World')) // dodanie węzła tekstowego zamkniętego pomiędzy tagami *li*

    e.target.nextElementSibling.appendChild(li) // dodanie dziecka li następnego rodzeństwa elementu na którym wykonał się dany event/wydarzenie

Przykładowy łańcuch zdarzeń

    const link = document.createElement('a')

    link.className = 'nav-link'

    link.innerHTML = '<i class=fa fa-remove></i>'

    li.appendChild(link)


Dodanie wygenerowanego elementu do innego

    document.querySelector('ul').appendChild(li)

`.insertBefore(nowyElement, dziecko)` - wstawienie nowego elementu przed wybranym dzieckiem

**::: Jeśli argumentem w powyższych metodach stanie się element już istniejący zostanie on wycięty (z całym dobrobytem/dziećmi) i wklejony w nowe miejsce :::**

Przykładowo (appendChild - wkleja z nowe miejsca jak i usuwa w poprzednim // dochodzi do kopiowania przez wartość ale nie referencje - zatem powstaje nowy obiekt):

    function move() {
        let elemParent = this.parentElement;
        if (elemParent.id === 'list1') {
            document.getElementById('list2').appendChild(this);
        } else {
            document.getElementById('list1').appendChild(this);
        }
    };

---

### Usuwanie i wymiana elementów

Zmiana elementu odbywa się **na JEGO rodzicu**

`.replaceChild(nowyElement, staryElementDziecko)` - wymiana elementu

`.replace(nowyElement, dziecko)` - zamiana wybranego dziecka na inny element

Przykładowy ciąg zdarzeń

    const newTitle = document.createElement('h2'); //tworzymy element

    newTitle.id = 'title-id' // nadajemu mu id

    newTitle.appendChild(document.createTextNode('Nowy tytuł')) // dodajemy do niego tekst

    const oldTitle = document.getElementById('title-id'); // "złapanie" elementu podlegającego wymianie

    const parentDiv = document.querySelector('div.nav-bar') // "złapanie rodzica"

    parentDiv.replaceChild(newTitle,oldTitle)

`.remove()` - usuwa podany element

`.removeChild()` - usuwa dziecko podanego elementu

    const listItems = document.querySelectorAll('li')

    listItems[0].remove() // usuwa pierwszy element

    list = document.querySelectorAll('ul')

    list.removeChild(listItems[0]) // usuwa pierwsze dziecko mające tag *li*

**Usuwanie elementu poprzez odwołanie się do rodzica**

    const deleteDroid = document.querySelector('#c3po')

    deleteDroid.parentElement.removeChild(deleteDroid)

---

**Zmiana klasy i atrybutu**

Dodawanie atrybutów

    element.setAttribute('attribute', 'właściwość')

`.setAttribute(atrybut, jego właściwość)` - pozwala na zdefiniowanego atrybutu

    link.getAttribute('href') //złap atrybutem

    link.setAttribute('href','http://google.com') // dodaj atrybut i jego właściwość

    link.hassAttribute('title') // zwraca true albo false jeśli taki posiada lub nie

`.removeAttribute()` - usuwa atrybut

    link.removeAttribute('title')

`.className` - dodawanie klasy

    element.className = 'list-item' // można również dodać id w podobny sposób

`.add()` - dodaje klasę do listy klas
`.remove()` - usuwa klasę

    const link = document.querySelector('li:first-child').children[0]

    let classLink = link.className //zwraca klasy w postaci stringu

    let listOfClasses = link.classList // zwracam listę klas w postaci DOMTokenList - zbliżone do tablicy - posiada indeksy

    link.classList.add('second-class') // dodaje klasę

    link.classList.remove('second-class') // usuwa klasę

---

### Wydobywanie informacji

`.tagName` - zwraca informację o tagu/etykiecie w formie stringa (wszystkie litery duże)

    element.tagName

    document.getElementById("IdOfLink").tagName;
    >> "A"

`.id` - zwraca id danego elementu

    document.querySelectorAll("a")[10].id // id 11. elementu będący linkiem

 w podobny sposób można uzyskać `.innerHTML` `.innerText`

#### Z formularza (form i input)

##### form

`.action` - zwraca URL do którego prowadzi wysłany formularz

`.method` - metoda którą wysyłany jest formularz GET lub POST

`.elements` - zwraca elementy formularza

`.elements.name.value` - zwraca zawartość elementu będącego dziecka noszącego nazwę name

    form.elements.email.value // zwraca wartość elementu który zawiera (name = 
    "email")

Formularz posiada specjalne zdarzenie

`submit` - wywoływane przy wysłaniu formularza

`reset` - wywoływane przy zresetowaniu formularza

##### input

`.value` - zwraca właściwość inputu/ to co zostało w niego wpisane/podane

`.type` - zwraca typ elementu input/pozwala również na jego ustawienie

`.disabled` - zwraca boolean, jeśli false to znaczy, że jest możliwe wprowadzenie danych jeśli ustawimy na true to wówczas będzie on nieaktywny

    input.disabled = "true" 

`.checked` - zwraca wartość logiczną *true* jeśli input jest typu *checkbox* i został on zaznaczony

`.selected` zwraca wartość logiczną *true* jeśli input jest typu *select* (rozwijana lista) i został on wybrany

### Stosowanie funkcji oraz iteracje

W kontekście stosowanie iteracji poprzez elementy DOM należy zwrócić uwagę na dwa kluczowe aspekty 

1) czy zbiór, na którym planujemy iterację pozwala na to no NodeList posiada metodę forEach (a HTML-collection już jej nie posiada) czy wymaga konwersji np. poprzez zastosowanie metody tablic np `Array.from(HTML-collection)` lub spread operatora np. `const arr = [...HTML-collection]`

2) czy funkcja, z którą będziemy pracować pozwala na skuteczne stosowanie słowa kluczowego `this` czy wymaga pracy z `event.target`. Funkcja strzałkowa albo inna deklarowana przez wyrażenie funkcyjne sprawi, że `this` będzie obiektem `window` podczas gdy deklaracja poprzedzona słowem kluczowym `function` gwarantuje, że `this` jest elementem, na którym dokonuje się event.



### Ćwiczenia

[GRA](ttps://mtomchuck.github.io/monster-village/dist/)

---

Źródła:

https://developer.mozilla.org/en-US/do