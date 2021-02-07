Title: Angular: referencje szablonów i ng-content
Author: mkostyrko
Date: 2020-12-28 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-ng-content
related_posts: 


Przy pomocy ng-content można przekazywać treść oraz różne komponenty

ng-content jest swego rodzaju wskaźnikiem/selektorem pozwalającym na opakowanie elementu komponentem, innymi słowy na zagnieżdżenie innego komponentu, fragmentu kodu html lub treści (stringa) w ramach innego komponentu.

    <button class="btn-floating teal add-button" (click)="clickButton.emit()">
      <ng-content></ng-content>
    </button>

zastosowanie

    <app-button (clickButton)="form.onSwitchForm()">
        <i class="material-icons">add</i>
    </app-button>


### Rozbudowane użycie ng-content

Nadawanie nazwy aby mieć większy wpływ na to, gdzie dany element jest wyświetlany

    select=[first]

Wstrzykiwanie ng-content

ngAfterViewInit() / @ContentChild / @ContentChildren

https://github.com/ZacznijProgramowac/ng-template-examples/tree/master/src/app

---

![angular](https://wpblog.semaphoreci.com/wp-content/uploads/2019/01/Testing-Components-in-Angular-2-with-Jasmine-776x320.png)


