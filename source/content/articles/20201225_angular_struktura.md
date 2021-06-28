Title: Angular: struktura aplikacji i komponentów
Author: mkostyrko
Date: 2020-12-25 11:00
Updated: 2021-06-28 10:00
Category: angular
Tags: angular
Slug: angular-struktura-komponenty
related_posts: react-wprowadzenie, typescript-klasy, angular-serwisy

---

![angular](http://www.tutorialspark.com/AngularJS/MVC.png)

### Angular i model MVC

Angular działa wg modelu MVC (Model/View/Controler)


Model - logiczna struktura danych w aplikacji (struktura kodu reprezentująca dane)


View - struktura kodu, która reprezentuje Interface aplikacji, z którym styka się użytkownik (wygląda aplikacji)


Controller - pośredniczy pomiędzy widokiem a modelem (reprezentuje logię działania aplikacji)


Inne pojęcia zw. z logiąką działania angularowej aplikacji


Scope - inaczej kontekst pomiędzy modelem oraz zdefiniowanymi funkcjami. Kontroler ustawia model oraz funkcje w ramach kontekstu.


Directives - dyrektywy pozwalające na dynamiczne zarządzanie HTML


Expression - pozwalają na dostęp do kontekstu modelu oraz funkcji (interpolację danych)


### Konstrukcja Komponentu

Klasa jako interface (implements NazwaKlasy)


konstruktor - pozwala na inicjalizowanie zależności (w postaci argumentów), choć faktycznie nie wszystkie argumenty podane w konstruktorze muszą być faktycznie wykorzystane w ramach funkcji konstruktora (np. różnego rodzaje zależności w postaci serwisów), a mogą być użyte w dalszej części klasy tworzącej komponent.


        [...]
        items: ToDoItems[]

        constructor (logService: LogService, itemsToDo: ToDoItems[]) {
            this.items = itemsToDo
        }
        [...]
        onClick() {
            logService.log('Hello World')
        }






---


Źródła:

[AngularJS : Application Anatomy](http://www.tutorialspark.com/AngularJS/AngularJS_App_Anatomy.php)