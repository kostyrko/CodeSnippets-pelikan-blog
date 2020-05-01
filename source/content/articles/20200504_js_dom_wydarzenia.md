Title: JavaScript - wydarzenia DOM
Author: mkostyrko
Date: 2020-05-04 10:00
Updated:
Category: javascript
Tags: dom, js, javascript, dom, events, wydarzenia, selectors
Slug: js-wydarzenia-dom
related_posts: js-dom-elementy-selektory, js-obiekt-window-document

### Nasłuchiwacz wydarzeń ;)

Aby dodać interakcji do strony internetowej przy pomocy JS należy do wybranego przez siebie elementu dołączyć tzw. 'nasłuchiwacz wydarzeń' (ang. event listener)

**`.addEventListener(wydarzenie, funkcja)`** - ta metoda przyjmuje dwa argumenty rodzaj 1) rodzaj wydarzenia np. 'click' (kliknięcie myszy) oraz 2) funkcję jaka ma się wywołać w momencie jego zajścia/bez nawiasów.

Przykładowe zastosowanie

    function helloWorld (e) {
      console.log('Hello World');
      e.preventDefault();
    }

    document.querySelector('button').addEventListener('click', helloWorld)

`.preventDefault()` - zapobiega domyślnemu zachowaniu się elementu, np. w przypadku linku jest to przejście na kolejną stronę etc.

funkcja wywołująca obiekt *event*

    function onClick(event) {
      console.log(event)
    }

    document.querySelector('button').addEventListener('click', event)

Obiekt event zawiera zbiór informacji na temat wydarzenia, do którego doszło np. *target* - zawierający informację, na temat obiektu, na którym doszło do danego wydarzenia

**`.target`**

    event.target.id  - zwraca id elementu, który był celem
     
    event.target.className/.classList - zwraca nazwę klasy/listę klas elementu, który jest targetem

    event.target.innerText - zwraca tekst elementu celowego

**`.type`** - zwraca typ wydarzenia

    event.type - z  np. mouseover

`.timeStamp` - czas w którym doszło do wydarzenia

`.clientY`/`.clientX` - miejsce wydarzenia relatywnie do granic okna przeglądarki / zwraca wartość w px

`.offsetY`/`.offsetX` - miejsce wydarzenia relatywne wobec elementu, na którym dochodzi do danego wydarzenia, gdzie punktem wyjściowym jest lewy górny róg / zwraca wartość w px

---

### Typy wydarzeń

#### Mysz

`click` - pojedyncze kliknięcie

`dblclick` - podwójne kliknięcie

`mousedown` - kliknięcie i przytrzymanie

`mouseup` - puszczenie po mousedown

`mouseenter` - najechanie kursorem na obiekt / dotyczy jedynie obiektu ale nie jego dzieci

`mouseleave` - opuszczenie kursorem obszaru obiektu

`mouseover` - takie samo jak `mouseenter` ale dotyczy również elementów zawartych w danym elemencie/całości

`mouseout`- takie samo jak `mouseout` ale dotyczy również elementów zawartych w danym elemencie/całości

`mousemove` - ruch wewnątrz obiektu, zwraca koordynaty w px znajdowania się myszki (offsetX,offsetY)

#### Input i formularze

`.type` - zwraca typ wydarzenia

Przykładowe zastosowanie

    const form = document.querySelector('form')

    const input = document.querySelector('input')

    form.addEventListener('submit', runEvent);

    function runEvent(e){
      console.log(`typ wydarzenia:` ${e.type})
    }

`submit` - nasłuchuje wysłania formularza // często używany z preventDefault() - aby powstrzymać przed domyślną akcją wywołaną przez dany element

`.value` - zwraca wartość wpisaną w formularz, pozwala również nadać wartość domyślną formularzowi np. po wykonanym przesłaniu

    let inputContent = input.value

    function runEvent(e){
      console.log(input.value);
      input.value = ''; // czyści formularz
    }

`keydown` - działa w momencie, w którym klawisz jest wciśnięty

`.target` - pozwala na wydobycie informacji z elementu, który jest targetem

    element.target.value

`keyup` - działa w momencie pozostawienia klawisza

`keypress` - działa w momencie wciśnięcia guzika

`focus` - focus na elemencie

`blur` - kliknięcie po za element (eliminacja focusa)

`cut` - rejestruje wycięcie treści

`paste` - rejestruje wklejenie

`input` - rejestruje każdy element związany z inputem (cut,paste,type)

`change` - działa na <select> list - rejestruje wybór w rozwijanej liście




---

Źródła:

