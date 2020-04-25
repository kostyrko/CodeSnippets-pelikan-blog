Title: JavaScript - metody tablic (array methods)
Author: mkostyrko
Date: 2020-04-12 10:00
Updated:
Category: javascript
Tags: javascript, js, array, tablica
Slug: js-tablice-metody
related_posts: 

### Tablice

Tablica wyjściowa

    const arr = [1,2,3,4]

#### Dodawanie elementów

**`push`** i **`unshift`** - pozwala na dodanie jednego lub więcej elementów na koniec/początek tablicy (zwraca nową długość tablicy a nie zmodyfikowaną tablicę)

    arr.push(1,null,'push')
    arr.unshift(0)

**`concat`** - [od concatenate] zwraca nową tablicę, która zawiera wszystkie elementy tablicy, na której zostałą zastosowana metoda oraz podanych argumentów

::: tablica nie jest modyfikowana :::

    arr.concat(2,'concatenate')

    brak modyfikacji -> stąd

    console.log(arr)
    > [0,1,2,3,4,1,null,"push"]

**`pop`** i **`shift`** - usuwa i zwraca ostatni/pierwszy element tablicy

:::tablica ulega modyfikacji:::

    arr.pop()
    >> push

**`indexOf`** - znajduje nr porządkowy (indeks) wybranego elementu
::: jeśli dany element nie jest obecny w tablicy to wówczas zwraca **`-1`** :::

    arr.indexOf(1)
    > 1


**`splice`** - usuwa obiekt z tablicy na podstawie pozycji/indeksu tworząc z niego nową tablicę (może przyjąć więcej niż jeden argument, tworząc ich zakres)

:::tablica ulega modyfikacji:::

    const arr1 = [1,2,3,4,5]
    let removedItems = arr1.splice(1,3)
    // arr1 = [1,5]
    // removedItems = [2,3,4]


**`slice`** - przyjmuje zero, 1 lub 2 argumenty / 0 - kopiuję tablicę, 1- tnie ją od wskazanego argumentu (indeks), 2 - w zakresie wskazanym przez argumenty (indeksy) - wyłącznie (argument końcowy nie będzie częścią)

**`sort`** - zwraca posortowaną tablicę, gdzie sortowanie jest oparte na pierwszej cyfrze składającej się na liczbę, podobnie sprawa wygląda w przypadku alfabetu gdzie 1. litera ma wpływ na kolejność pozycji i a potem następna etc.

:::tablica ulega modyfikacji:::

**`reverse`** - odwraca kolejność elementów znajdujących się w tablicy

**`includes`** - sprawdza czy tablica zawiera wpisany argument stosuje `===` i nie można szukać zagnieżdżonych list

---

`callback` - funkcja wywołująca się na każdym elemencie

**`forEach`** - tworzy pętlę przechodzącą przez zawartość tablicy - wymaga funkcji wywołania zwrotnego (callback), która tworzy akcję na każdym z elementów tablicy -> zwraca `undefined`, ale po drodze wywołuje wynik akcji

    let arrEach = [1, 2, 3, 4];
    arrEach.forEach(function (num) {
      console.log(num + 1);
    });
    > 2
    > 3
    ...

**`map`** - podobny do forEach ale zmienia elementy tablicy i zwraca nową tablicę ze zmienionymi wartościami

**`filter`** - zwraca **nową tablicę**, z elementami dla którego wskazany argument jest prawdziwy (= True)

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

:::tablica NIE ulega modyfikacji:::

**`reduce`** - funkcja przyjmuje cztery argumenty 1) wartość inicjalizującą tzw akumulator 2) obecną wartość Opcjonalnie: 3) obecny indeks 4) źródłową tablicę na której, reduce jest stosowane

Funkcja wywołania zwrotnego przyjmuje np. 2 argumenty - element tablicy oraz aktualną wartość akumulatora i zwraca wartość, która zostanie przypisana do akumulatora i będzie jako taki użyty w kolejnej iteracji.

Redukuję tablicę do pojedynczej wartości

:::tablica NIE ulega modyfikacji:::


      let arr = [2, 3, 5, 7]

      arr.reduce((accumulator, element) => accumulator + element, 0) //17
    
    // inny zapis

      arr.reduce(function(acc,element){
          return acc + element
      }, 0) // wartość początkowa akumulatora

---

<p class="codepen" data-height="450" data-theme-id="dark" data-default-tab="js,result" data-user="mkostyrko" data-slug-hash="abvZZBE" style="height: 450px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="tablice-metody">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/abvZZBE">
  tablice-metody</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

---

Ćwiczenia:

https://launchschool.com/books/javascript/read/arrays#exercises

Źródła:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

http://kursjs.pl/kurs/super-podstawy/tablice.php

https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Obiekty/Array/from#

https://launchschool.com/books/javascript/read/arrays#exercises

https://alligator.io/js/filter-array-method/