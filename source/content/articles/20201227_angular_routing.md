Title: Angular: routing - podstawy
Author: mkostyrko
Date: 2020-12-27 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-routing
related_posts: 

---

![angular](https://blog.knoldus.com/wp-content/uploads/2020/05/Angular-Routing.png)

Narzędzie routingu pozwala na nawigację pomiędzy różnymi komponentami (stanami pojedynczej strony) aplikacji

1 - należy zaimportować **RouterModule** w **app.module.ts** oraz w importach go zastosować łącznie z metodą **forRoot()**, która iteruje przez tablicę zawierającą obiekty, zawierające informacje o ścieżce (warunku) oraz komponencie, który ma być wyświetlony w momencie gdy warunek jest spełniony.

    // app.module.ts
    import { BrowserModule } from '@angular/platform-browser';
    import { NgModule } from '@angular/core';
    import { AppComponent } from './app.component';
    import { CrisisListComponent } from './crisis-list/crisis-list.component';
    import { HeroesListComponent } from './heroes-list/heroes-list.component';
    import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
    import { RouterModule } from '@angular/router';


    @NgModule({
      declarations: [
        AppComponent,
        CrisisListComponent,
        HeroesListComponent,
        PageNotFoundComponent
      ],
      imports: [
        BrowserModule,
        RouterModule.forRoot([
          {path: 'crisis-list', component: CrisisListComponent}, // wskazanie na ścieżkę oraz na komponent, który ma być wyświetlony w jej przypadku
          {path: 'heroes-list', component: HeroesListComponent},
          {path: '', redirectTo: '/heroes-list', pathMatch: 'full'}, // podstawowa ścieżka przekierowuje do adresu '/heroes-list', gdy ten w całości pasuje do wskazanego (pathMatch)
          {path: '**', component: PageNotFoundComponent} // "dzika karta" - niezawarty powyżej link
        ]),
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }

2 - router-outlet oraz nawigacja

`<router-outlet></router-outlet>` - dyretkywa ta oznacza przestrzeń w której wynik pracy routera ma swój skutek.

**routerLink** - dyrektywa łącząca ścieżki wraz ze zdefiniowanymi szablonami html


**routerLinkActive** - korzystając z tej dyrektywy wskazujemy Angularowi na przypisanie zdefiniowanej klasy do elementu HTML, która oznacza aktywną ścieżkę

    <nav>
      <a class="button" routerLink="/crisis-list" routerLinkActive="activebutton">Crisis Center</a> |
      <a class="button" routerLink="/heroes-list" routerLinkActive="activebutton">Heroes</a>
    </nav>

    <router-outlet></router-outlet>

Całość kodu powyższej aplikacji [angular-router-sample](https://github.com/kostyrko/JS-sandbox/tree/master/7_Angular/angular-router-sample)

----

Źródła:

Więcej informacji na temat routingu: [In-app navigation: routing to views](https://angular.io/guide/router)