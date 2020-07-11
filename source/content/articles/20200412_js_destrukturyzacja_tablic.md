Title: JavaScript - destrukturyzacja tablic i obiektów
Author: mkostyrko
Date: 2020-04-12 11:00
Updated:
Category: javascript
Tags: javascript, js, array, tablica, destrukturyzacja, obiekt, tablica
Slug: js-destrukturyzacja
related_posts: 

### Destrukturyzacja tablic

Destrukturyzacja tablic pozwala na przypisanie do zmiennych tworzących tablice kolejne elementy zawarte w tablicy (właściwości tablicy)

    let droids = ['r2d2', 'c3po']
    let [droid1, droid2] = droids
    console.log(droid2)
    >> c3po

    zamiast

    let droid2 = droids[1]

Istnieje również możliwość omijania pewnych elementów w trakcie destrukturacji poprzez pozostawienie wolnej spacji pomiędzy przecinkami

    ```JavaScript
      let droids = ['r2d2', 'c3po', 'bb8']
      let [droid1, , droid3] = droids
      console.log(droid3)
      >> bb8````

Przy pomocy operatora spread można również wydzielić jeden element zwracając z reszty tablicę

    ```JavaScript
      let droids = ['r2d2', 'c3po', 'bb8']
      let [droid1, ...droid2] = droids
      console.log(droid2)
      >> ['c3po', 'bb8']```
      console.log(droid1)
      >> r2d2````

---

### Destrukturyzacja obiektów

    const protocolDroid = {
        name:"ME-8D9",
        occupation:"Protocol droid",
        height:"1.72",
        homeWorld:"Takodana"
        }

    let {name, homeWorld} =  protocolDroid

    console.log(name)
    >> ME-8D9
    console.log(homeWorld)
    >> Takodana

Pozwala to na wykorzystanie w funkcji tylko tych elementów obiektu, które są nam potrzebne

    const createDroid = ({ name, homeWorld }) => {
      console.log(name, homeWorld);
    };

    createDroid(protocolDroid);

    const protocolDroid = {
        name:"ME-8D9",
        occupation:"Protocol droid",
        height:"1.72",
        homeWorld:"Takodana"
        address: {
          city: "Takodana"
          }
        }

    const {name, address: {city}} = protocolDroid;

    console.log(city)
    >> Takodana

Istnieje również możliwość nadpisania przypisania wartości do zmiennej/nadawanie zmiennej nowej wartości

    const droid = { name: "ME-8D9" };
    const { name: protocolDroid } = droid;
    console.log(protocolDroid); // >> ME-8D9