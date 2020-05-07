Title: JavaScript - wydarzenia DOM cz. 2 - propagacja
Author: mkostyrko
Date: 2020-05-04 11:00
Updated:
Category: javascript
Tags: dom, js, javascript, dom, events, propagacja wydarzenia, selectors
Slug: js-wydarzenia-dom-2
related_posts: js-dom-elementy-selektory, js-obiekt-window-document

### Propagacja wydarzeń (w górę) - event bubbling

W DOM domyślnie wydarzenia są przenoszone od dziecka lub rodzeństwa do rodzica lub rodzeństwa - oznacza to, że jeśli rodzic oraz dziecko mają nastawioną ten sam rodzaj akcji wywołującej (np. click) oraz różne lub tą samą wydarzenie wywołane, oba z nich dojdą do skutku chyba, że dojdzie do przerwania propagacji - oznacza to również, że wydarzeni, do której doszło na dziecku może wywoływać akcję na rodzicu ( w takim przypadku wystarczy jedynie ustawienie eventListener na rodzicu), a propagacja zachodzi również pomiędzy rodzeństwem.

Przeciwieństwem *event bubbling* jest *event capturing* - przekazywanie danych w dół drzewa DOM (domyślna np. dla focus)

#### Metody zatrzymujące propagacje

`event.stopPropagation()` - zatrzymuje propagację w górę wydarzeń tego samego typu/ propagacja poziome (pomiędzy rodzeństwem) nadal jest aktywne

`event.stopImmediatePropagation()` - zatrzymuje wykonywanie wydarzeń pojedynczym elemencie, wywoływanie wydarzenia nie jest przenoszone na rodziców ani rodzeństwo

---

### Delegacja wydarzeń - event delegation

W przypadku delegacji wydarzeń dochodzi to propagacji innej niż w domyślny sposób - np.dziecko (oraz jego potomstwo etc.) dziedziczy po rodzicu lub rodzeństwie. np. akcja, która zachodzi na rodzicu może wywoływać zdarzenie na dziecku. Tego typu zachowanie można zdefiniować przy pomocy warunków. Oznacza to, że można nastawić 'nasłuchiwacz', który wykonuje określone zadanie na wybranym elemencie.

Rozwiązanie 1

    function deleteItem(e) {
      if(e.target.parentElement.className === 'delete-item') {
        console.log('delete-item')
      }
    }
::: jeśli celem jest obiekt posiadający rodzica, który posiada dokładnie w ten sposób przypisaną klasę lub klasy 'delete-item' to wówczas wykonaj wydarzenie:::

Rozwiązanie 2

    function deleteItem(e) {
      if(e.target.parentElement.classList.contains('delete-item') ) {
        e.target.parentElement.parentElement.remove())
      }
    }

::: jeśli celem jest obiekt posiadający rodzica, który posiada klasę lub klasy, której częścią jest podane wyrażenie 'delete-item' to wówczas wykonaj wydarzenie:::

---

Źródła:

