Title: JavaScript - metody tablic (array methods)
Author: mkostyrko
Date: 2020-04-12 10:00
Updated:
Category: javascript
Tags: javascript, js, array, tablica
Slug: js-tablice-metody
related_posts: 

### Tablice

Tworzenie tablicy

    const arr = [1,2,3,4]

::: istnieje możliwość również przez funkcję konstruktora `new Array()`

Sprawdzanie czy obiekt, do którego się odwołujemy jest tablicą

    Array.isArray(arr) // true (/false)

Dodawanie wartości do tablicy

    arr[2] = 20
    arr // [1,2,20,3,4]

Tablice można tworzyć również z obiektów do nich podobnych porzez wykorzystanie tzw. spread operatora [...obiektPodobnyDoArr] oraz **Array.from**(obiektPodobnyDoArr)

Często stosowanymi metodami tablic są [forEach/reduce/filter/map](#iteracje)

#### Podstawowe metody() tablic

**`push`** i **`unshift`** - pozwala na dodanie jednego lub więcej elementów na koniec/początek tablicy (zwraca nową długość tablicy a nie zmodyfikowaną tablicę)

    const arr = [1,2,3,4]
    arr.push(1,null,'push')
    arr.unshift(0)

**`concat`** - [od concatenate] zwraca nową tablicę, która zawiera wszystkie elementy tablicy, na której zostałą zastosowana metoda oraz podanych argumentów :::tablica wyjściowa NIE ulega modyfikacji:::

    arr.concat(2,'concatenate')

    brak modyfikacji -> stąd

    console.log(arr)
    > [0,1,2,3,4,1,null,"push"]

Pozwala na łączenie ze sobą 2 tablic

    const arr1 = [1,2,3]
    const arr2 = [4,5,6]
    let arr3 = arr1.concat(arr1)
    console.log(arr3)
    >> Array [1,2,3,4,5,6]

**`pop`** i **`shift`** - usuwa i zwraca ostatni/pierwszy element tablicy :::tablica ulega modyfikacji:::

    arr.pop()
    >> push

**`indexOf`** - znajduje nr porządkowy (indeks) wybranego elementu
::: jeśli dany element nie jest obecny w tablicy to wówczas zwraca **`-1`** :::

    arr.indexOf(1)
    > 1


**`splice`** - zwraca "wycięte" obiekt z tablicy na podstawie pozycji/indeksu tworząc z niego nową tablicę (może przyjąć więcej niż jeden argument, tworząc ich zakres):::tablica wyjściowa ULEGA modyfikacji:::

    const arr1 = [1,2,3,4,5]
    let removedItems = arr1.splice(1,3)
    // arr1 = [1,5]
    // removedItems = [2,3,4]


**`slice`** - przyjmuje zero, 1 lub 2 argumenty / 0 - kopiuję tablicę, 1- tnie ją od wskazanego argumentu (indeks), 2 - w zakresie wskazanym przez argumenty (indeksy) - wyłącznie (argument końcowy nie będzie częścią) :::tablica wyjściowa NIE ulega modyfikacji:::

**`sort`** - zwraca posortowaną tablicę w sposób leksykograficzny (słownikowo), gdzie sortowanie jest oparte na pierwszej cyfrze/literze składającej się na liczbę/wyraz,  gdzie 1. litera/cyfra ma wpływ na kolejność pozycji i a potem następna etc.

aby posortować ze sobą liczby w tablicy należy jest ze sobą porównać i do tego stosuje się funkcji porównawczej

    function compareNumbers(a,b) {
        return a-b
    }

::: jeśli wynik -1 to sortuje do lewej, jeśli 1 to do prawej w przypadku 0 pozostawia na miejscu :::

Przykładowe zastosowanie

    let arr1 = [7,1,2,3,4,5]
    arr1 = arr1.sort((a,b)=>a-b) // od najmniejszej
    arr1 = arr1.sort((a,b)=>b-a) // od największej

:::tablica ULEGA modyfikacji:::

**`reverse`** - odwraca kolejność elementów znajdujących się w tablicy

**`includes`** - sprawdza czy tablica zawiera wpisany argument stosuje `===` i nie można szukać zagnieżdżonych list

**`find`** jako argument można wpisać wyrażenie na podstawie, którego będzie wyszukiwać

    const arr = [50,51,7,1,2,3,4,5]

    // zwracaj wynik poniżej 50
    function under50(num) {
        return num < 50;
    }
    // zwraca pierwszy wynik
    const find = arr.find(under50);

    console.log(find)
    >> 7

alternatywny zapis (zwracaj pierwszy wynik poniżej 50)

    const find = arr.find(e => e < 50)

Przykładowe zastosowanie z projektu `To Do App`[z tablicy wszystkich zadań (allTasks) znajdź to, którego data-priority jest niższe od nowo tworzonego zadania(newTask)]

    const element = allTasks.find(e => 
      Number(newTask.dataset.priority) > Number(e.dataset.priority))

`.some()` - sprawdza czy w tablicy znajdują się wartość spełniające przypisany warunek (np. `console.log(array.some(even))`)

`.every()` - - sprawdza czy w tablicy wszystkie wartości spełniające przypisany warunek (np. `console.log(array.every(even))`)

<!-- [Repo całego kodu projektu](https://github.com/kostyrko/JS-apps/tree/master/1_task_list_app/2_task_app) -->

---

### forEach/reduce/filter/map {#iteracje}

`callback` - funkcja wywołująca się na każdym elemencie

**`forEach`** - tworzy pętlę przechodzącą przez zawartość tablicy - wymaga funkcji wywołania zwrotnego (callback), która tworzy akcję na każdym z elementów tablicy -> zwraca `undefined`, ale po drodze wywołuje wynik akcji

    let arrEach = [1, 2, 3, 4];

    arrEach.forEach(function (num) {
      console.log(num + 1);
    });
    > 2
    > 3
    ...

---

**`map`** - podobny do forEach ale zmienia elementy tablicy i zwraca nową tablicę ze zmienionymi wartościami

Przedstawiona poniżej funkcja zwróci nową tablicę o nazwie *birthYear* zwierającą aktualny rok umniejszony o każdy element z tablicy *years*, nowa tablica będzie miała tyle samo elementów co tablica *years*

        const years = [20,21,22]

        const currYear = new Date().getFullYear()

        const birthYear = years.map(function(elem){
            return currYear - elem
        })
        
        // przy założeniu, że jest rok 2020
        >> [2000,1999,1998]

---

**`filter`** - zwraca **nową tablicę**, z elementami dla którego wskazany argument jest prawdziwy (= True)
:::tablica wyjściowa NIE ulega modyfikacji:::

    const newArr = array.filter(function(item){
        return condition;
    });

    function getNumber (num,arr) {
    const newArr = arr.filter(function(item) {
        return item === num;
    });
    return (newArr[0] === num ? true : false)
    };

    // zapis przy pomocy funkcji strzałkowej
    
    function getNumber (num,arr) {
    const newArr = arr.filter((item)=> {return item === num});
    return (newArr[0] === num ? true : false);
    }

---

**`reduce`** - funkcja przyjmuje cztery argumenty 1) wartość inicjalizującą tzw akumulator 2) obecną wartość Opcjonalnie: 3) obecny indeks 4) źródłową tablicę na której, reduce jest stosowane

Funkcja wywołania zwrotnego przyjmuje np. 2 argumenty - element tablicy oraz aktualną wartość akumulatora i zwraca wartość, która zostanie przypisana do akumulatora i będzie jako taki użyty w kolejnej iteracji.

Redukuję tablicę do pojedynczej wartości
:::tablica NIE ulega modyfikacji:::

Wyliczanie sumy tablicy (dla każdego elementu dodaj go do akumulatora, który przyjmuje wartość poprzedniej iteracji, akumulator zaczyna od 0)

      let arr = [2, 3, 5, 7]

      arr.reduce((accumulator, element) => accumulator + element, 0) //17
    
    // inny zapis

      arr.reduce(function(acc,element){
          return acc + element
      }, 0) // wartość początkowa akumulatora

Wyliczanie średniej tablicy 

    let arr = [1,2,3]

    const arrAvg = arr = arr.reduce((a,b) => a + b, 0) / arr.length // ES6

    let arr = [1,2,3]


    function arrAvg(arr){
    let sum = arr.reduce(function(acc,element){
            return acc + element
        }, 0);
    return sum / arr.length
    }

    console.log(arrAvg(arr))

---

<p class="codepen" data-height="450" data-theme-id="dark" data-default-tab="js,result" data-user="mkostyrko" data-slug-hash="abvZZBE" style="height: 450px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="tablice-metody">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/abvZZBE">
  tablice-metody</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

---

![sort_method](https://i.stack.imgur.com/81miP.png)

---

Ćwiczenia:

https://launchschool.com/books/javascript/read/arrays#exercises

Źródła:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

http://kursjs.pl/kurs/super-podstawy/tablice.php

https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Obiekty/Array/from#

https://launchschool.com/books/javascript/read/arrays#exercises

https://alligator.io/js/filter-array-method/

https://www.freecodecamp.org/forum/t/arr-sort-a-b-a-b-explanation/167677

https://stackoverflow.com/questions/10359907/how-to-compute-the-sum-and-average-of-elements-in-an-array