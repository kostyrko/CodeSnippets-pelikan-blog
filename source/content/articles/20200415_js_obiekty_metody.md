Title: JavaScript - Obiekt.metoda()
Author: mkostyrko
Date: 2020-04-15 10:00
Updated:
Category: javascript
Tags: javascript, js, array
Slug: js-obiekt-metody
related_posts: js-podstawowe-typy, js-tablice

**`Object.assign()`** - kopiuje/klonuje wszystkie elementy jednego lub więcej elementu do określonego elementu

Schemat:

    returnedTarget = Object.assign(target, source);

Przykłady

    const obiekt = { a: 1 };
    const kopia = Object.assign({}, obiekt);
    // kopia = { a: 1 }

    const o1 = { a: 1 };
    const o2 = { b: 2 };
    const o3 = { c: 3 };

    const obj = Object.assign(o1, o2, o3);
    // obj = { a: 1, b: 2, c: 3 }

:::Właściwości nieprzeliczalne oraz te z łańcucha prototypów nie są kopiowane :::

---

[**`Object.create()`**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create) - tworzy nowy obiekt, wykorzystując istniejący obiekt jako prototyp tworzonego obiektu

**`Object.defineProperty()`** - tworzy nowy właściwość bezpośrednio na obiekcie albo modyfikuje istniejącą wartość wewnątrz obiektu

**`Object.defineProperties()`** - definiuje nowe lub modyfikuje istniejące właściwości

**`Object.entries()`** - zwraca tablicę zawierającą par klucza-wartości w postaci stringa

**`Object.freeze()`** - zamraża obiekt, obiekt zamrożony nie może być zmieniany (nie można dodawać nowych właściwości/"elementów", zmieniać ich ani usuwać)

**`Object.fromEntries()`** - zmienia listę kluczy-wartości w obiekt

    const entries = new Map([
        ['foo', 'bar'],
        ['baz', 42]
    ]);

    const obj = Object.fromEntries(entries);

    console.log(obj);
    // expected output: Object { foo: "bar", baz: 42 }

`Object.getOwnPropertyDescriptor()`

`Object.getOwnPropertyDescriptors()`

`Object.getOwnPropertyNames()`

`Object.getOwnPropertySymbols()`

`Object.getPrototypeOf()`

`Object.is()`

`Object.isExtensible()`

`Object.isFrozen()`

`Object.isSealed()`

**`Object.keys()`** - zwraca tablicę kluczy danego obiektu

    Object.keys(object1)

`Object.preventExtensions()`

`Object.seal()`

`Object.setPrototypeOf()`

**`Object.values()`** - zwraca wartości danego obiektu w postaci tablicy


Źródła:

https://launchschool.com/books/javascript/read/objects#whatareobjects

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object

https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Obiekty/Object/