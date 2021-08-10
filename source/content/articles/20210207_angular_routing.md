Title: Angular: routing
Author: mkostyrko
Date: 2021-02-07 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-routing
related_posts:

![angular](https://wpblog.semaphoreci.com/wp-content/uploads/2019/01/Testing-Components-in-Angular-2-with-Jasmine-776x320.png)

Client-side rendering - bez zapytania do serwera (wymaga konfiguracji serwera tak aby zwracał index.html skąd angular przejmuje tworzenie ścieżki)

app.component.html - wykorzystanie `<router-outlet></router-outlet>` dyrektywy w celu wskazania, w którym miejscu powinien pojawić sie komponent związany z routingiem

    <div class="container">
        [...]
        <div class="row">
            <div class="col-xs-12">
                <!-- load router here -->
                <router-outlet></router-outlet>
            </div>
        </div>
    </div>

app-routing.module.ts - zdefiniowanie ścieżek routingu


    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    import { CreateCharacterComponent } from './create-character/create-character.component';
    import { TabsComponent } from './tabs/tabs.component';

    const routes: Routes = [ 
      {path: '', component: TabsComponent},
      {path: 'new-character', component: CreateCharacterComponent}
    ];

    @NgModule({
      // registers routes in the angular router module
      imports: [RouterModule.forRoot(routes)],
      exports: [RouterModule]
    })
    export class AppRoutingModule { }

app.module.ts - zaimportowanie do głównego modułu

    import { BrowserModule } from '@angular/platform-browser';
    [...]

    @NgModule({
      declarations: [
        ...
      ],
      imports: [BrowserModule, AppRoutingModule, FormsModule],
      [...]
    })
    export class AppModule {}


header.component.html - gdzie routing jest stosowany po str html ->  `routerLinkActive="active"` oraz `[routerLinkActiveOptions]="{exact: true}"`

    <ul class="nav nav-pills">
        <!-- add active class when link active -->
        <!-- active only when exactly and not only part of the path -->
      <li class="nav-item" routerLinkActive="active"
      [routerLinkActiveOptions]="{exact: true}">
        <a class="nav-link" routerLink="/">Star Wars Characters</a>
      </li>
      <li class="nav-item" routerLinkActive="active">
        <a class="nav-link" routerLink="/new-character"> New Character</a>
      </li>
    </ul>

  
### Zastosowanie routingu w małej aplikacji

    import { BrowserModule } from '@angular/platform-browser';
    import { NgModule } from '@angular/core';

    import { AppComponent } from './app.component';
    import { CrisisListComponent } from './crisis-list/crisis-list.component';
    import { HeroesListComponent } from './heroes-list/heroes-list.component';

    import { RouterModule } from '@angular/router';
    import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

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
          {path: 'crisis-list', component: CrisisListComponent},
          {path: 'heroes-list', component: HeroesListComponent},
          {path: '', redirectTo: '/heroes-list', pathMatch: 'full'},
          {path: '**', component: PageNotFoundComponent}
        ]),
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }

Router-outlet w app.component.html odpowiada za wyświetlenie elementów przypisanych do konkretnej ścieżki (alternatywnie można stosować ngIf)

app.component.html

    <h1>Angular Router Sample</h1>

    <nav>
      <a class="button" routerLink="/crisis-list" routerLinkActive="activebutton">Crisis Center</a> |
      <a class="button" routerLink="/heroes-list" routerLinkActive="activebutton">Heroes</a>
    </nav>

    <router-outlet></router-outlet>


### Większa aplikacja może wymagać odosobnienia logiki routingu

Założenie nowego pliku przechowującego/obsługującego Routing w folderze app
app-routing.modules.ts

    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';

    // import komponentów, które mają funkcjonować pod konkretną ścieżką

    import { MoviesComponent } from './pages/movies/movies.component';
    import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
    import { CategoriesComponent } from './pages/categories/categories.component';
    import { MovieDetailsComponent } from './pages/movies/movie-details/movie-details.component';

    // tablica przechowująca routing - ścieżki
    const routes: Routes = [
      // przekierowanie do movies od razu po załadowaniu ścieżki początkowej/pustego adresu
      // pathMatch: 'full' - ścieżka musi zgadzać się w 100%
      { path: '', redirectTo: '/movies', pathMatch: 'full' },
      { path: 'movies', component: MoviesComponent },
      // jako id (token) powinna być przekazana przy pomocy routingu wartość
      { path: 'movie/:id', component: MovieDetailsComponent},
      { path: 'categories', component: CategoriesComponent},
      // dopasuje się do każdej ścieżki, dlatego musi być na końcu ścieżek
      { path: '**', component: PageNotFoundComponent },
    ];

    // importowanie i eksportowanie
    @NgModule({
      imports: [RouterModule.forRoot(routes)],
      exports: [RouterModule],
    })
    export class AppRoutingModule {}

Zaimportowanie oraz implementacja w app.module.ts Routingu

    import { BrowserModule } from '@angular/platform-browser';
    import { NgModule } from '@angular/core';

    import { AppComponent } from './app.component';
    import { HttpClientModule } from '@angular/common/http';

    import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
    import { MovieCoverComponent } from './shared/movie-cover/movie-cover.component';
    import { MovieDetailsComponent } from './pages/movies/movie-details/movie-details.component';
    import { MoviesComponent } from './pages/movies/movies.component';
    import { CategoriesComponent } from './pages/categories/categories.component';
    import { MoviesInCategoryComponent } from './pages/categories/movies-in-category/movies-in-category.component';

    //  >> Import Routingu <<

    import { AppRoutingModule } from './app-routing.module';

    @NgModule({
      declarations: [
        AppComponent,
        MovieDetailsComponent,
        MoviesComponent,
        CategoriesComponent,
        PageNotFoundComponent,
        MoviesInCategoryComponent,
        MovieCoverComponent,
      ],

      //  >> Implementacja Routingu <<

      imports: [BrowserModule, HttpClientModule, AppRoutingModule],
      providers: [],
      bootstrap: [AppComponent],
    })
    export class AppModule {}

Router-outlet w app.component.html odpowiada za wyświetlenie elementów przypisanych do konkretnej ścieżki (alternatywnie można stosować ngIf)

    <nav>
      <div class="nav-wrapper black">
        <a class="brand-logo" routerLink="/">Best Movies</a>
        <ul class="right hide-on-med-and-down">
          // active - klasa (nazwa przykładowa), która przypisana jest do aktywnego linku
          <li><a routerLink="/movies" routerLinkActive="active">Movies</a></li>
          <li><a routerLink="/categories" routerLinkActive="active">Categories</a></li>
          <li><a>Years</a></li>
        </ul>
      </div>
    </nav>
    <router-outlet></router-outlet>


Przekazywanie id/tokena wartości przy pomocy Routingu

**movie-cover.component.html**

    <div class="grid__item">
      <div class="card">
        <div class="card-image">
          <img [src]="movie.poster" />
          <span class="card-title black">{{ movie.title }}</span>
        </div>
        <div class="card-content">
          <p>{{ movie.plot.slice(0, 100) }}...</p>
        </div>
        <div class="card-action">
          //  >> przekazanie id z obiektu movie  <<
          <a class="black-text" [routerLink]="['/movie', movie.id]">More >></a>
        </div>
      </div>
    </div>

Wykorzystanie przekazanego id


**movie-details.component.ts**

    import { Component, OnInit } from '@angular/core';
    import { Observable } from 'rxjs';
    import { HttpService } from '../../../services/http.service';
    import { Movie } from '../../../models/movie';
    import { ActivatedRoute, ParamMap } from '@angular/router';
    import { switchMap } from 'rxjs/operators';

    @Component({
      selector: 'app-movie-details',
      templateUrl: './movie-details.component.html',
      styleUrls: ['./movie-details.component.css'],
    })
    export class MovieDetailsComponent implements OnInit {
      movieDetails: Observable<Movie>;

      // wykorzystanie serwisu dzięki niemu zastosowanie id
      constructor(private http: HttpService, private route: ActivatedRoute) {}

      ngOnInit() {
      this.movieDetails = this.route.paramMap.pipe(
        // odwołanie się do serwisu // subskrypcja zachodzi po str frontendu przy pomocy async pipe
        switchMap((params: ParamMap) => this.http.getMovie(params.get('id')))
      )
      }

      goToMovies() {}
    }


**movie-details.component.html**


    <div class="row" *ngIf="movieDetails | async as movie">
      <div class="col s4"><img [src]="movie.poster" /></div>
      <table class="col s8">
        <tbody>
          [...]
      </table>
      <button class="btn black" (click)="goToMovies()">Back</button>
    </div>


ParamMap jako Observable pozwala na zmianę zawartości i re-renderowanie komponentu, również przy zmianie ścieżki

---

Źródła:

[Zachnij Programować - angular-movie-db-routing-example](https://github.com/ZacznijProgramowac/angular-movie-db-routing-example/blob/002-router-param/src/app/app-routing.module.ts)
