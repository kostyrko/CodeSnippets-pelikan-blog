Title: Migracja z JS do TS
Author: mkostyrko
Date: 2020-11-26 10:00
Updated:
Category: typescript
Tags: rts, typescript
Slug: typescript-migracja-js-ts
related_posts: typescript-wprowadzenie

![typescript-logo](https://www.positronx.io/wp-content/uploads/2018/11/positronx-banner-1152-1.jpg)

### Migracja z JS do TS
#### Przykład 1 - deklarowanie typów

1.1. Funkcja definiująca argumenty jako typ Number
TS - podkreśli num2 w wywołaniu (res) ze względu na to, że nie spełnia zdefiniowanego typu number (po transpilacji w JS (TS jej nie zablokuje) problem nie będzie sygnalizowany i wynik będzie wynosił "12" /np. zamiast oczekiwanego 3) - wynika to ze statycznego i dynamicznego typowania

    function addDroids(n1:number, n2:number) {
        return n1 + n2
    }

    const num1= '1'
    const num2 = 2
    const droids = addDroids(num1,num2)
    console.log(droids);

1.2. Funkcja zawierająca typu Number + String + Boolean

    function addDroids(n1:number, n2:number, showRes: boolean, comment: string) {
            const result = n1 + n2 // typ: number / stworzenie identyfikatora aby zachować typ: number
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


**Przykład zastosowania** - zastosowanie TS do wskazania oczekiwań typów (to info nie będzie już obecne w TS)


`!` - informacja dla TS, że nigdy nie zwróci Null, a zawsze znajdzie element

`as HTMLInputElement` - wskazanie na rodzaj elementu HTML (type casting)

    const button = document.querySelector('button');
    const input1 = document.querySelector('num1')! as HTMLInputElement;
    const input2 = document.querySelector('num2')! as HTMLInputElement;

    function addDroids(n1:number, n2:number) {
            return n1 + n2;
        }

    button.addEventListener('click', function(){
      console.log(addDroids(+input1.value, +input2.value)));
    })

---

### Migracja z JS do TS

[Migrating from JavaScript](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)



---

Źródła:


[TypeScript Course for Beginners 2020 - Learn TypeScript from Scratch!](https://www.youtube.com/watch?v=BwuLxPH8IDs)

[TypeScript Tutorial - TypeScript for React - Learn TypeScript [2020]](https://www.youtube.com/watch?v=NjN00cM18Z4&ab_channel=ProgrammingwithMosh)

[How to move your project to TypeScript - at your own pace](https://www.twilio.com/blog/move-to-typescript)

[Node.js: Migration from JavaScript to TypeScript](https://www.youtube.com/watch?v=qFMMOJucqTw&feature=emb_title&ab_channel=JavaScriptRoom)

