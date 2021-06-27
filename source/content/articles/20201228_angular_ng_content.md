Title: Angular: referencje szablonów i ng-content
Author: mkostyrko
Date: 2020-12-28 10:00
Updated: 2021-06-27 10:00
Category: angular
Tags: angular, unfinished
Slug: angular-ng-content
related_posts: 

![angular ng-content](https://cdn-media-1.freecodecamp.org/images/1*mFnAxpS3I_lpRPnIyevxKw.png)

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



