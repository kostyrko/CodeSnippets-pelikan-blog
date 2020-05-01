Title: JavaScript - pętle (for/while loop)
Author: mkostyrko
Date: 2020-04-18 10:00
Updated:
Category: javascript
Tags: javascript, js, funkcja
Slug: js-for-while-loop
related_posts: js-funkcje

Pętle `for` lub `while` pozwalają na wielokrotne wykonywanie się tego samego kodu

schemat pętli **`for`**:

    const y = 5 // zmienna będąca wyznacznikiem granicznym wykonywania pętli
 
    // wykonaj pętlę do momentu w którym i jest nadal mniejsze niż y 
    
    for (i=0; i < y; i++) { // i - akumulatorem; moment do którego wykonuje się pętla; zmiana dokonywana na akumulatorze po przejściu pętli
      let x = y + 1; // wykonujący się kod
      return x;
    };

Przykład pętli dekrementacyjnej (wykonuj pętlę w przypadku gdy i jest większe od 5): 

    for (let i = 10; i > 5 ; i-- ) {
      console.log(i)
    }

**`while`** - tworzy pętle, która wylicza wyrażenie `i` - dopóki jest ono prawdą wykonuje blok poleceń

    while (warunek) {
    polecenia
    }

    n = 0;
    x = 0;
    while(n < 3) {
      n ++;
      x += n;
    }

---

**`for...in`** - - przechodzi przez wszystkie policzalne właściwości obiektu, których kluczem jest string / ignoruje te, których kluczem jest symbol

    const object = {a: 1, b: 2, c: 3};

    for (let property in object) {
      console.log(`${property}: ${object[property]}`);
    }

    >> a: 1
    >> b: 2
    >> c: 3

**`for...of`** - tworzy pętlę przechodząc przez iteracyjne obiekty (string,tablica/array)

    const array1 = ['a', 'b', 'c'];

    for (const element of array1) {
      console.log(element);
    }

**`for each ..in`**  - przestarzałe wyrażenie - obecnie stosuje się `for..of`

    for each (variable in object) {
      statement
    }

**`for await...of`** - asynchroniczny iterator -> więcej na ten temat [tutaj](https://www.youtube.com/watch?v=I5oDbp_U-fQ)

    for await (zmienna iteracyjna) {
      polecenie
    }


**`do...while`** - wykonuje polecenie dopóki warunek jest spełniony

    do {
      polecenia
    } while(warunek);

    do {
    i+=1;
    document.write(i);
    } while (i<5);
  


Źródła:

http://kursjs.pl/kurs/super-podstawy/funkcje.php

http://jsdn.pl/samowywolujace-sie-anonimowe-funkcje/

http://jsdn.pl/funkcje-tworzenie-funkcji-w-javascripcie/

https://www.modestprogrammer.pl/wyrazenia-funkcyjne-oraz-funkcje-anonimowe-w-javascript