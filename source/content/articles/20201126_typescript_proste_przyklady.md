Title: TypeScript: proste przykłady
Author: mkostyrko
Date: 2020-11-26 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-proste-przyklady
related_posts: typescript-wprowadzenie

![typescript-logo](https://www.positronx.io/wp-content/uploads/2018/11/positronx-banner-1152-1.jpg)


### Przykład 1 - deklarowanie typów

1.1. Number
TS - podkreśli num2 w wywołaniu (res) ze względu na to, że nie spełnia zdefiniowanego typu number (po transpilacji w JS (TS jej nie zablokuje) problem nie będzie sygnalizowany i wynik będzie wynosił "12" /np. zamiast oczekiwanego 3) - wynika to ze statycznego i dynamicznego typowania

    function addDroids(n1:number, n2:number) {
        return n1 + n2
    }

    const num1= '1'
    const num2 = 2
    const droids = addDroids(num1,num2)
    console.log(droids);

1.2. Number + String + Boolean

    function addDroids(n1:number, n2:number, showRes: boolean, comment: string) {
            const result = n1 + n2 // typ: number / stworzenie "nie/zmiennej" aby zachować typ: number
            if (showRes) {
                console.log(comment + result) // string + number = string
            } else {
                return result // zwraca typ number
            }
        }

    const num1= 1
    const num2 = 2
    const showResult = true
    const comment = 'The number of droids is: '

    addDroids(num1, num2, showResult, comment)

1.3. Objects




---

Źródła:



[TypeScript Course for Beginners 2020 - Learn TypeScript from Scratch!](https://www.youtube.com/watch?v=BwuLxPH8IDs)

[TypeScript Tutorial - TypeScript for React - Learn TypeScript [2020]](https://www.youtube.com/watch?v=NjN00cM18Z4&ab_channel=ProgrammingwithMosh)

