Title: Angular: komunikacja pomiędzy dzieckiem a rodzicem (input,output,eventEmitter, ViewChild)
Author: mkostyrko
Date: 2020-12-23 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-komunikacja-komponentow
related_posts: angular-wprowadzenie

---

![angular](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png)

### Dekorator @Input()

Łączy input z danym komponentem pozwalając mu na zewnętrzne użytkowanie - rozbicie logiki komponentu na mniejsze części (komponenty)

Wymaga importu z counterReducer

    import { Component, OnInit, Input } from '@angular/core';

Oraz zdefiniowania identyfikatora opatrzonego dekoratorem @Input() 

    @Input() hero: Hero;


Odwołanie się w komponencie posiadającym element, do którego następuje odwołanie (komponent rodzica) wygląda w sposób następujący (np. heroes.component.html -> selectedHero)

    <app-hero-detail [hero]="selectedHero"></app-hero-detail>

`[hero]="selectedHero"` - składnia definiująca połączenie jednostronne, w ramach właściwości elementu DOM (właściwość selectedHero komponentu HeroesComponent zostaje skopiowana/przeniesiona do właściwości hero celowego elementu, który jest zmapowany na podstawie danych z HeroDetailComponent). Kiedy użytkownik klika selectedHero ulega zmianie, a przez to również HeroDetailComponent (property bindig go odświeża)

Przykład

    ==== Usunięcie tego fragmentu =====
    <div *ngIf="selectedHero">
      <h2>{{ selectedHero.name | uppercase }} Details</h2>
      <div><span>id: </span>{{ selectedHero.id }}</div>
      <div>
        <label
          >name:
          <input [(ngModel)]="selectedHero.name" placeholder="name" />
        </label>
      </div>
    </div>
    ============ Zastąpienie go tym ========
    <app-hero-detail [hero]="selectedHero"></app-hero-detail>


    >>>>>>> Komponent dziecka zawierającego input <<<<<<<

    // HTML dziecka
    <div *ngIf="hero">

      <h2>{{hero.name | uppercase}} Details</h2>
      <div><span>id: </span>{{hero.id}}</div>
      <div>
        <label>name:
          <input [(ngModel)]="hero.name" placeholder="name"/>
        </label>
      </div>

    </div>

    // TS dziecka
    import { Component, OnInit, Input } from '@angular/core';
    import { Hero } from '../hero';

    @Component({
      selector: 'app-hero-detail',
      templateUrl: './hero-detail.component.html',
      styleUrls: ['./hero-detail.component.css']
    })
    export class HeroDetailComponent implements OnInit {

      @Input() hero: Hero;

      constructor() { }

      ngOnInit(): void {
      }

    }

## Template Reference


### @ViewChild

@ViewChild('odnośnikDoTemplateReference/nazwaKlasyDziecka/wieleObiektówDanegoTypuHTML') - dekorator pozwalający na wstrzyknięcie komponentu dziecka pozwalający na jego sterowanie z klasy rodzica. Ten dekorator może być również wykorzystany do sterowaniem html (pobranie) jak i funkcjonalnością dziecka.

W przypadku wielu takich samych komponentów przy odwołaniu się do klasy komponentu dziecka, zostanie wykorzystany pierwszy napotkany komponent (aby temu zapobiec można wykorzystać **template reference**)



<script src="http://gist-it.appspot.com/github.com/ZacznijProgramowac/template-reference-examples/blob/master/src/app/app.component.ts"></script>

<script src="http://gist-it.appspot.com/github.com/ZacznijProgramowac/template-reference-examples/blob/master/src/app/app.component.html"></script>

[Komunikacja pomiędzy komponentami w Angular 2](https://typeofweb.com/komunikacja-pomiedzy-komponentami-w-angular-2/)

---


Źródła:

