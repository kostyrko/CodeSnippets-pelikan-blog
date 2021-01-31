Title: Angular CLI
Author: mkostyrko
Date: 2021-01-25
 12:00
Updated:
Category: angular
Tags: bootstrap, angular, javascript
Slug: angular-cli
related_posts: 



![angular-bootstrap](https://angular.io/assets/images/logos/angular/angular.svg)

### Podstawowe komendy

Proste generowanie komponentu

    ng generate component nazwaKomponentu

    np. ng generate component menu
    > informacja o wygenerowanych plikach oraz o aktualizacji app.module.ts


--skiTests true // generowanie bez pliku testów


Zapis tej komendy można wykorzystać również w skróconej wersji

    ng g c nazwaKomponentu

    ng g c navbar --skipTests true
    CREATE src/app/navbar/navbar.component.css (0 bytes)
    CREATE src/app/navbar/navbar.component.html (21 bytes)
    CREATE src/app/navbar/navbar.component.ts (275 bytes)
    UPDATE src/app/app.module.ts (455 bytes)

Generowanie serwisu wersja skrócona

  ng g s nazwaSerwisu

Generowanie komponentu w już istniejącym folderze komponentu

    ng generate component nazwaKatalogu/nazwaKomponentu

Generowanie komponentu Inline (zawarty w jednym pliku/ lub jedynie jego część)

   ng generate component nazwaKomponentu --inlineStyle true --inlineTemplate true


--flat // generowanie komponentu bez dodatkowego katalogu -> generuje pliki komponentu bez katalogu -> przydatne przy serwisach










---
Źródła:

[Angular -CLI](https://angular.io/cli)

[Angular - kompletny kurs od podstaw - edycja na rok 2021](https://www.udemy.com/course/angular-kompletny-kurs-od-podstaw/)

