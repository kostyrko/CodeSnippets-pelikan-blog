Title: Angular: cykle życia komponentu
Author: mkostyrko
Date: 2020-02-01 10:00
Updated:
Category: angular
Tags: angular
Slug: angular-lifecycle-hooks
related_posts: 

![angular](https://wpblog.semaphoreci.com/wp-content/uploads/2019/01/Testing-Components-in-Angular-2-with-Jasmine-776x320.png)

Tabela przedstawiająca life cycle hooki (wg kolejności ich życia)

|Haki cykli życia|Interfejs|Wykrywa zmianę?*|
|---|---|---|
|ngOnChanges|OnChanges|Tak|
|ngOnInit|OnInit|Nie|
|ngDoCheck|DoCheck|Tak|
|ngAfterContentInit|AfterContentInit|Nope|
|ngAfterContentChecked|AfterContentChecked|Ja|
|ngAfterViewInit|AfterViewInit|Nej|
|ngAfterViewChecked|AfterViewChecked|Yup|
|ngOnDestroy|OnDestroy|Nope|

***Uruchamiane wielokrotnie**

Dyrektywy podobnie jak komponenty mogą korzystać z haków cykli życia (life cycle hooks)


### ngOnChanges

Uruchamia się jako 1 ze wszystkich hooków oraz za każdym razem kiedy zmienia się property (referencja, zatem jeśli referencja nie ulega zmianie, ew zmiany w ramach obiektu nie będą zauważone  referencja przecież zostaje ta sama) tego komponentu (zmienia się zawsze kiedy zmianie ulegnie property zw z input). Uruchamia się gdy powstaje komponent.

    export class ChildComponent implements OnChanges {
      @Input() name
      ngOnChanges(changes: SimpleChanges) {
        for (const prop of Object.keys(changes)) {
          console.log(changes[prop])
        }
      }
    }

źródło: [Sposób na śledzenie zmian property @Input – ngOnChanges i Angular](https://zacznijprogramowac.net/angular/ngonchanges-w-angularze-sposob-na-sledzenie-zmian-property/)

[ngOnChanges best practice - always use SimpleChanges - always](https://dev.to/nickraphael/ngonchanges-best-practice-always-use-simplechanges-always-1feg)

### OnInit

Uruchamia się jednokrotnie (zaraz po ngOnChange), pełni rolę konstruktora dla obiektu [zwykły konstruktor komponentu jest powiązany z TS a nie Angularem]. Dobre do inicjalizowania danych, uruchomienie logiki startowej, w metodzie ngOnInit należy się odwołać do wstrzykniętych zależności

ngOnInit jest szybsze od konstruktora (który może nie mieć dostępu do wszystkich właściwości komponentu), dlatego ten jest wykorzystywany jedynie wstrzykiwania zależności, duża ilość logiki w konstruktorze spowalnia komponent i utrudnia testowanie.


### DoCheck

Hook ten uruchamia się po to by sprawdzić czy nastąpiły zmiany w danych i czy należy zmienić szablon html. Może wykonywać się wiele razy, przez to również trzeba uważać przy jego wykonywaniu. W odróżnieniu od innych hooków (ngOnChanges) ngDoCheck sprawdza min. również wnętrza obiektów (dane) i rozpozna zmianę oraz wywoła zdarzenie - podobnie będzie to wyglądało np. w przypadku wpisywania tekstu do inputu. Uwaga: powoduje wykonanie wywołanie również we wszystkich komponentach położonych niżej, obciąża również aplikację.

    export class ChildComponent DoCheck {
      @Input() dog: Dog;
      // Uruchomi się zawsze z Change Detection
      ngDoCheck(): void {
        console.log('Uruchamiam się zawsze :smile:')
      }
    }

[DoCheck wykrywanie zminan – Angular i ngDoCheck](https://zacznijprogramowac.net/angular/docheck-wykrywanie-zminan-angular-ngdocheck/)

### AfterContentInit

Wywołuje się raz, po tym jak wykona się ngDoCheck - ma dostęp do komponentów wyświetlanych przez <ng-content></ng-content>

### AfterContentChecked

Uruchamia się za każdym razem jak zostaje uruchomiony changeDetection -> Oznacza, że komponent został już sprawdzony i zaraz zostanie wyrenderowany z nowymi danymi (np. do pobrania najnowszych/końcowych danych)

### AfterViewInit

Uruchomi się raz w cyklu życia komponentu. Ma dostęp do komponentów, które zostały wstrzyknięte przy pomocy ViewChild.

### AfterViewChecked

Uruchamia się po detekcji zmiany - gdy widok komponentu lub jego dziecka zostanie sprawdzony przez *change detection* -> czy zmiany nastąpiły?/czy należy je zmienić?

### OnDestroy

Wywołuje się tylko gdy Angular będzie niszczony przez Angulara (np przy pomocy ngIf, inaczej rzecz ujmując gdy likwidowana jest logika, aplikacji która zajmuje pamięć przeglądarki).

@HostListener('window:beforeunload') - listener zakładany na metodę, który wykona się przy wpisanej w argument akcji


---

Źródła:

[Hooking into the component lifecycle](https://angular.io/guide/lifecycle-hooks)


