Title: Angular: formularze wstęp + reactive forms
Author: mkostyrko
Date: 2020-12-23 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-formularze
related_posts:

---

![angular](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHghCEZH5gPt3yGwrsP2c5hHAFfEHgysQdxQ&usqp=CAU)

Angular umożliwia stworzenie 2 rodzajów formularzy tzw. **reaktywnych** (reactive) oraz **szablonowych** (template-driven)

**Reaktywne formularze** -zapewniają bezpośredni dostęp do obiektów modelu. Są bardziej skalowalne i łatwiejsze w ponownym użytkowaniu. [forma walidacji: funkcja, przewidywalność: synchroniczna, model danych: ustrukturyzowany i niezmienny]

**Szablonowe formularze** - uzależnione są od dyrektyw w tworzeniu i manipulowaniu obiektu modelu. Są proste w implementacji w przypadku małych form. [forma walidacji: dyrektywy, przewidywalność: asynchroniczna, model danych: nieustrukturyzowany i mutowalny]

Zarówno formy **reaktywne** jak i **szablonowe** korzystają z poniższych klas, które stanowią o ich funkcjonowaniu

**FormControl** - śledzi wartość oraz status walidacji pojedynczego elementu formularza

**FormGroup** - śledzi wartości oraz status walidacji zbioru elementów formularza

**FormArray** - śledzi wartości oraz status zbioru walidacji tablicy zawierającej formularze

**ControlValueAccessor** - tworzy pomost pomiędzy instancjami Angular FormControl oraz natywnymi elementami drzewa DOM.

---

### Dyrektywy

**ngModel**

dyrektyra **ngModel** jest częścią '@angular/forms' i jest z formularzami właśnie powiązana. Pozwala na dwustronne powiązanie `[()]`, ale kiedy jest używana w pojedynce, wskazuje Angularowi, na element HTML, który ma kontrolować/ którego powinien być świadomy, w kontekście formularza oraz jego obsługi (patrz **ngSubmit**) - tworzy obiekt związany z formularzem.


    <input type="text" id="name" name="name" class="form-control" ngModel>

    <input
      class="col s8"
      type="text"
      placeholder="Dodaj zadanie i datę wykonania"
      [(ngModel)]="taskName"
    />


**ngSubmit**

dyrektywa **ngSubmit** pozwala na połączenie z wydarzeniem, które ma zostać wykonane w trakcie wysyłania formularza - zapobiega wysłaniu formularza i wywołuje właściwe zdarzenie.

    <form (ngSubmit)="onSubmit()">


**ngModelChange**


### Lokalna referencja

`#form = "ngForm"` - tworzy lokalną referencję (#form) do szablonu formularza poprzez wykorzystanie słowa kluczowego (ngForm) oraz obiektu formularza utworzony przez Angular (patrz **ngModel**).

    // html
    <form (ngSubmit)="onSubmit(form)" #form="ngForm">

    // ts
    onSubmit(submittedForm: {}) {
     console.log(submittedForm);
   } 


---

**Przykład reactive form** - model formularza jest bezpośrednio definiowany w klasie (wyraźny model formularza) - dyrektywa [formControl] łączy instancję **FormControl**
do konkretnego elementu formy (widoku) poprzez wewnętrzną wartość "akcesorium" / **model formularza jest źródłem prawdy**

    import { Component } from '@angular/core';
    import { FormControl } from '@angular/forms';

    @Component({
      selector: 'app-reactive-favorite-color',
      template: `
        Favorite Color: <input type="text" [formControl]="favoriteColorControl">
      `
    })
    export class FavoriteColorComponent {
      favoriteColorControl = new FormControl('');
    }

**Przykład template-driven form** - model formularza jest domniemany, dyrektywa NgModel tworzy i zarządza instancją FromControl dla danego elementu HTML / **źródłem prawdy jest szablon html**

    import { Component } from '@angular/core';

    @Component({
      selector: 'app-template-favorite-color',
      template: `
        Favorite Color: <input type="text" [(ngModel)]="favoriteColor">
      `
    })
    export class FavoriteColorComponent {
      favoriteColor = '';
    }

Do przeczytania -> Przepływ danych w formularzach: [angular.io - Data flow in forms](https://angular.io/guide/forms-overview#data-flow-in-forms)

---

![reactive-form](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSZShqRsNi1Z6zK-hmfGRqgEW9lU1D8y5qgA&usqp=CAU)

### Reaktywne formularze

1 - Postawowy formularz reaktywny

Importowanie modułu ReactiveFormsModule do app.module.ts

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/app.module.ts"></script>

Komponent name-editor -> name-editor.component.ts

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/name-editor/name-editor.component.ts
"></script>

name-editor.component.html

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/name-editor/name-editor.component.html"></script>

2- Zarządzanie formularzem z wieloma elementami oraz zagnieżdżone formularze

Zarządzanie **wieloma instancjami** Kontroli Formularza (**form control**) w pojedynczej grupie -> wykorzystanie `FormGroup`

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor/profile-editor.component.ts"></script>

<script src="http://gist-it.appspot.com/github/kostyrko/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor/profile-editor.component.html"></script>

Przykładowy zwracany obiekt ->

    {firstName: "mike ", lastName: "tyson", address: {street: "uluru", city: "rock", state: "tn", zip: "0000"}}

Istnieją dwa sposoby na aktualizację wartości:

**setValue()** - zmienia całą wartość w odniesieniu do struktury grupy formularza

**patchValue()** - zmienia właściwość zdefiniowaną w obiekcie, który uległ zmianie w modelu formularza

**setValue()** pozwala na przechwycenie błędów w złożonych formularzach, podczas gdy **patchValue** nie przekazuje o nich informacji/nie reaguje na nie.

3 - Tworzenie formularza przy pomocy **FormBuildera** + Walidacja

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor-form-builder/profile-editor-form-builder.component.ts"></script>

Szablon HTML z dodaną walidacją

<script src="http://gist-it.appspot.com/github/kostyrko/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor-form-builder/profile-editor-form-builder.component.html"></script>

4 - Dynamicznie modyfikowany formularz przy pomocy FromArray (alternatywa dla FromGroup)

<script src="http://gist-it.appspot.com/github/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor-dynamic-form/profile-editor-dynamic-form.component.ts"></script>

Szablon HTML wykorzystujący **\*ngFor**

<script src="http://gist-it.appspot.com/github/kostyrko/kostyrko/JS-sandbox/blob/master/7_Angular/angular-reactive-forms-example/src/app/profile-editor-dynamic-form/profile-editor-dynamic-form.component.html"></script>

Przykładowe dane zwrotne ->

    Value: { "firstName": "Mike", "lastName": "Tyson", "address": { "street": "Bronson", "city": "Tyson City", "state": "Nebula", "zip": "0000" }, "aliases": [ "mike@tyson.usa", "tyson@usa.mike", "bronson@tyson.mike" ] }

---

Istotne/dalsze informacje:

więcej na temat walidacji formularzy można dowiedzieć się tutaj [angular.io Validating form input](https://angular.io/guide/form-validation)

Lista Klas oraz Dyrektyw formularza Angular.io [reactive-forms-api](https://angular.io/guide/reactive-forms#reactive-forms-api-summary)

---

Źródła:

[angular.io - Reactive forms](https://angular.io/guide/reactive-forms)

[angular.io - forms overview](https://angular.io/guide/forms-overview)
