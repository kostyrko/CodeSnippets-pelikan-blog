Title: Angular: przekazywanie danych pomiędzy kompenentami (input, output, eventEmitter, ViewChild)
Author: mkostyrko
Date: 2020-12-23 10:00
Updated: 2021-07-24 10:00
Category: angular
Tags: angular, input, output, eventEmitter, ViewChild, unfinished
Slug: angular-komunikacja-komponentow
related_posts: angular-serwisy

---

![angular](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png)

#### @Input oraz @Output {#inputOutput}

**1) przekazanie danych 'w dół' (od rodzica do dziecka)**


**@Input** - Dekoratory pozwalające na rozbicie logiki aplikacji na mniejsze części/komponenty i komunikowanie się danymi pomiędzy nimi. Dekorator **@Input** można porównać do właściwość (property/props) komponentu w React tzn. pozwala na przekazanie do komponentu danych np.

    // rodzic
    <app-user [name]="Mike"></app-user>

gdzie komponent `app-user` przy pomocy dekoratora @Input ma zdefiniować właściwość `name`.

    @Input() name: string;


**2) przekazanie danych 'w górę' (od dziecka do rodzica)**


**@Output** - pozwala na przekazanie informacji DO rodzica, aby tego dokoną należy stworzyć nową instancję klasy **EventEmmiter** (poprzez wywołanie funkcji konstruktora). 1) W klasie dziecka przy pomocy dekoratora `@Output`  rejestrujemy EventEmmiter, który będzie przekazywał dane do rodzica - jego zmiana wywołana jest poprzez dedykowaną metodę klasy/komponentu dziecka.

    @Output() nameChanged = new EventEmmiter<string>(); // typ generyczny odpowiadający typowi przesyłanych danych

    onUserInput(event){
      this.nameChanged.emit(event.target.value);
    }

    // rodzic:
    //html
    <app-user (nameChanged)="onNameChanged($event)"></app-user>

    // ts
    [...]
    // wartość która ulegnie zmianie
    name = "Mike"
    
    onNameChanged(newName) {
      this.name = newName;
    }

Przykładowa aplikacja wykorzystująca tzw. Event Binding i wyżej wymienione dekoratory w sposób bezpośredni [star-wars-angular-service-app (etap prze implementacą serwisu)](https://github.com/kostyrko/JS-sandbox/tree/angular-event-binding/7_Angular/angular-service-app/star-wars-services/src/app)


### @ViewChild

Zapisanie w zmiennej referencji do dziecka danego elementu (dowolny jego element html jak i cały komponent). Pozwala na odwołanie się do publicznych pól dziecka przez rodzica. Rodzic decyduje z jakich pól dziecka będzie potrzebował.

Zadeklarowanie przy pomocy dekoratora - `@ViewChild` w klasie rodzica może wyglądać następująco:
    

"[...] Chcąc obserwować konkretny komponent deklarujesz typ zmiennej zgodny z klasą tego komponentu. Dzięki temu masz dostęp do publicznych pól i metod tej klasy. Odtąd, w dowolnym momencie możesz używać this.child jak zwykłego pola klasy rodzica."    

    @ViewChild(ChildComponent) child: ChildComponent;


"W przypadku tagów HTML musisz oznaczyć ten tag poprzez dowolny string z przedrostkiem ‚#’. Potem tu używasz tego stringa jako identyfikator, na podstawie którego angular namierzy tag i przypisze do zmiennej. Inny jest też deklarowany typ – ElementRef, czyli referencja lokalna na konkretny element HTML [...]"

Lub w przypadku html


    @ViewChild('ref') child: ElementRef;


Gdzie element html wygląda następującego


    <div #ref></div>


Uwaga końcowa:


"Propercja klasy dziecka rodzica na początku jest undefined. Możesz odwoływać się do niej, dopiero po zainicjalizowaniu widoku i wystąpieniu zdarzenia ngAfterViewInit()."

Cytowane fragmenty tekstu za: [@ViewChild(). Komunikacja komponentów](https://a-frontman.pl/viewchild-komunikacja-komponentow/)]


Sięgnięcie do listy dzieci jest możliwe przy pomocy `QueryList`


    @ViewChildren(ChildComponent) children: QueryList<ChildComponent>;

---

Źródła:

[viewchild-komunikacja-komponentow](https://a-frontman.pl/viewchild-komunikacja-komponentow/)