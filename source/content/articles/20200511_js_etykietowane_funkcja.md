Title: JavaScript - etykietowanie funkcji
Author: mkostyrko
Date: 2020-05-11 10:00
Updated:
Category: js
Tags: javascript, tag, function, funkcja, etykietowanie, tagged function
Slug: js-etykietowana-funkcja
related_posts: js-podstawowe-typy

*Template strings* lub też *literals* zwane po polsku *łańcuchami szablonowymi*

Łańcuchy szablonowe [wcześniej wspominałem o nich [w tym miejscu](https://kostyrko.github.io/zfrontu/js-podstawowe-typy.html)] pozwalają na podstawianie zmiennych wewnątrz informacji przeznaczonymi do druku i zawartymi pomiędzy apostrofami [ warto pamiętać o tym, że stosowanie tego formatu zapisu nie wymaga używania sekwencji ucieczkowej -> /n]

Przykładowo:

    const droid = "r2d2"
    const droid2 = "c3po"

    console.log(`Hello 
    ${droid}, 
    ${droid2}`)

    >>Hello 
    >>r2d2, 
    >>c3po

Funkcje mogą być również wywołane poprzez zastosowania `łańcucha szablonów` tzw `tag functions` - wówczas części tego łańcucha nie odwołujące się do zmiennych mogą być traktowane jako tablica (podzielona w miejscach gdzie znajdują się zmienne), która musi być  zawarta jako argument

    function droidGreeter (strings, droidName) {
    console.log(strings[0] + droidName + strings[1])
    return droidName + strings[0]
    };

    const droid = 'c3po';

    console.log(droidGreeter` I am ${droid} - and you? `); // array strings = [' I am ', ' - and you? ']

    >>  I am c3po - and you?
    >> c3po I am 

W ten sposób można tworzyć instancje różnego rodzaju informacji wynikowych przy pomocy jednej funkcji

    const droids = [
      {name: 'C3PO', height: '1.71'},
      {name: 'R2D2', height: '1.09'},
      {name: 'BB8', height: '0.67'},
      {name: 'L3-37', height: '1.79'},
      {name: 'K-2SO', height: '2.16'}
    ]

    function showSpecs (arr, n, h) {
      console.log(arr[0] + n + arr[1] + h + arr[2])
    }

    showSpecs`This ${droids[1].name} is ${droids[1].height}` 

    >> This R2D2 is 1.09

    showSpecs`This droid's name is ${droids[1].name} and he is ${droids[1].height} m high` 

    >> This droid's name is R2D2 and he is 1.09 m high

    droids.forEach(function(droids){
      showSpecs`This ${droids.name} is ${droids.height} high`; 
    })

    >> This C3PO is 1.71 high
    >> This R2D2 is 1.09 high
    >> This BB8 is 0.67 high
    >> This L3-37 is 1.79 high
    >> This K-2SO is 2.16 high

Patrz również [tutaj](https://playcode.io/602318) aby popracować na powyższej funkcji w edytorze i konsoli online

![image](https://pbs.twimg.com/media/EXpDjdDWsAE9D7D?format=jpg&name=large)

---

Źródła:
https://codeburst.io/javascript-what-are-tag-functions-97682f29521b
