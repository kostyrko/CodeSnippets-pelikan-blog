Title: JavaScript: formularze
Author: mkostyrko
Date: 2020-01-02 12:00
Updated:
Category: javascript
Tags: bootstrap, angular, javascript
Slug: javascript-formularze
related_posts: 

![java-script-formularz](https://www.proformat.pl/wp-content/uploads/U%C5%BCyteczny-formularz-kontaktowy.jpg)

## Formularz

"Łapanie" formularza na 2 sposoby = poprzez odwołanie się do forms lub poprzez "klasyczne" selektory

    const firstForm1 = document.forms[0]
    const firstForm2 = document.querySelector("form")


### Właściwości formularza (wybrane)

|właściwość formularza|funkcja|Przykład zastosowania|
|---|---|---|
|formularz.elements|"zwraca kolekcję kontrolek zawartych" w formularzu|firstForm1.elements|
|formularz.length|"zwraca ilość kontrolek" w formularzu||
|formularz.name|"ciąg z nazwą bieżącego elementu" formularza||
|formularz.action|"pobiera/ustawia akcję dla" formularza||
|formularz.target|"pobiera/ustawia okno docelowe akcji formularza"||
|formularz.method|"Pobiera/ustawia metodę HTTP używaną do wysłania formularza."||

Pełna lista właściwości formularza i źródło: [HTMLFormElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement)/[developer.mozilla.org - właściwości formularza](https://developer.mozilla.org/pl/docs/Web/API/HTMLFormElement#W.C5.82asno.C5.9Bci)

### Metody formularza

|metoda formularza|funkcja|Przykład zastosowania|
|---|---|---|
|formularz.submit()|"wysyła formularz"||
|formularz.reset()|"przywraca formularz do jego stanu początkowego"||
|formularz.requestSubmit()|Wysyła żądanie aby formularz został zatwierdzony przez konkretny przycisk oraz, do którego jest przypisana konkretna konfiguracja||
|Walidacja|Walidacja|Walidacja|
|formularz.checkValidity()|Zwraca **true** jeśli walidacja elementów formularza przebiegła poprawnie||
|formularz.raportValidity()|Zwraca **true** jeśli walidacja elementów formularza przebiegła poprawnie||
|formularz.setCustomValidity()|Zwraca informację związaną z walidacją inputu o dowolnej wskazanej treści|

### Zdarzenia (events)

|metoda formularza|funkcja|
|---|---|
|formdata|wydarzenie **formdata** jest wywołany kiedy lista reprezentująca dane formularza są stworzone |
|reset|wydarzenie **reset** jest wywołany gdy formularz jest "zerowany"/resetowany|
|submit|wydarzenie **submit** jest wywołany gdy formularz jest wysłany|


#### Przykład zastosowania `formdata`

    // złapanie referencji do formularza
    const formElem = document.querySelector('form');

    // zgłoszenie obsługi zdarzeń
    formElem.addEventListener('submit', (e) => {
      // prevent default na wysłaniu
      e.preventDefault();

      // tworzy obiekt FormData, który odpala event formdata
      new FormData(formElem);
    });

    // formdata handler to retrieve data

    formElem.onformdata = (e) => {
      console.log('formdata fired');

      // Złapanie/wydobycie danych formularza z obiektu wydarzenia
      let data = e.formData;
      for (var value of data.values()) {
        console.log(value);
      }

      // wysyłanie danych przez XHR
      var request = new XMLHttpRequest();
      request.open("POST", "/formHandler");
      request.send(data);
    };

źródło przykładu: [GlobalEventHandlers.onformdata](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onformdata)

---
### Pola formularza

Główne zdarzenia - **change, focus/blur, keypress/keyup/keydown, input** (gdy wartość pola zostaje zmienione)
### Inputy

źródło lub inspiracja poniższych przykładów [kursjs.pl - formularze](https://kursjs.pl/kurs/formularze/formularze.php)

#### Text

Wydobycie informacji poprzez odwołanie się do właściwości **value** inputu

    const inputEmail = document.querySelector("#userEmail");
    input.addEventListener("input", e => {
        const val = input.value;
        const reg = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        
        // jeśli poprawnie dodaj klasę
        if (!reg.test(val)) {
            input.classList.add("field-error");
        } else {
            // jeśli niepoprawnie dodaj klasę
            input.classList.remove("field-error");
        }
    });

<p class="codepen" data-height="365" data-theme-id="light" data-default-tab="js,result" data-user="mkostyrko" data-slug-hash="YzGejNK" style="height: 365px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="JS_formularz_tekst/email">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/YzGejNK">
  JS_formularz_tekst/email</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

#### Radiobox i Checkbox

**checked** - sprawdza czy jest zaznaczone polecenia

**change** - nasłuchuje na zmiany w formularzu typu (radiobox/checkbox)


    for (const radio of exampleRadio) {
      radio.addEventListener("change", e => {
          for (const radio of exampleRadio) {
              if (radio.checked) {
                  console.log(radio.value)
              }
          }
      });
    }

<p class="codepen" data-height="365" data-theme-id="light" data-default-tab="js,result" data-user="mkostyrko" data-slug-hash="eYdMZJJ" style="height: 365px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="JS_formularz_radiobox/checkbox">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/eYdMZJJ">
  JS_formularz_radiobox/checkbox</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

#### Select

Właściwości elementu formularza typu select

**select.value** - wartość pola selected

**select.options** - zbiór elementów opcji

**select.selectedIndex** - indeks wybranej opcji

**select.options[selectedIndex]** - indeks wybranej opcji z formularza select

Przy tworzeniu opcji formularza select istnieje możliwość wykorzystania konstruktora **Option(text*, value*, defaultSelected*, selected*)**

    const option1 = new Option("Tekst", 102);

#### Color

Reaguje na zdarzenie **change**

    input.addEventListener("change", e => {
        console.log(input.value)
    });

#### Range
Reaguje na zdarzenia typu change(gdy zmienia się wartość) oraz input(w czasie zmiany wartości)

    input.addEventListener("change"/"input", e => {
        console.log(input.value)
    });

---
Źródła:

[Formularze w JavaScript](http://javascript-html5-tutorial.pl/ui-formularze-w-javascript.html)

[kursjs.pl -> Formularze - walidacja](https://kursjs.pl/kurs/formularze/formularze-walidacja.php)

[kursjs.pl - Formularze](https://kursjs.pl/kurs/formularze/formularze.php)