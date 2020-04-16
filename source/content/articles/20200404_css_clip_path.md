Title: CSS - rysowanie poligonów (clip-path: polygon())
Author: mkostyrko
Date: 2020-04-04 11:00
Updated:
Category: css
Tags: css, clip-path, poligon, rysowanie, polygon
Slug: css-clip-path
related_posts: css-neumorphism


Deklaracja `clip-path:` z przypisaną wartością `polygon()` pozwala na rysowanie poligonów o dowolnych kształtach.
W ramach niej wpisane są pary procentów oddzielone przecinkami określającymi miejsce znajdowanie się węzła.


* 0% 0% - górny lewy róg
* 100% 0% - górny prawy róg
* 0% 100% - dolny lewy róg
* 100% 100% - dolny prawy róg

zatem:

* 50% 0 - środek górnej granicy
* 50% 100% - środek dolnej granicy
* 0% 65% - 65% licząc od góry lewej krawędzi

Poniżej znajdziesz również link do on-linowego generatora poligonów, z którego można skopiować css

Przykładowa zawartość klasy style.css

          header {
            background-color: red;
            text-align: center;
            clip-path: polygon(50% 0%, 100% 0, 100% 65%,50% 100%, 0 65%, 0 0);


Tutaj jak wygląda to w praktyce: 

<p class="codepen" data-height="400" data-theme-id="light" data-default-tab="css,result" data-user="mkostyrko" data-slug-hash="oNjvavK" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="clip-path: poligon()">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/oNjvavK">
  clip-path: poligon()</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

Przy pomocy narzędzi deweloperskich FireFox lub Chrome można również manipulować ręcznie wartościami tak jak to jest przedstawione na poniższym filmie: 
Zobacz 30 sekund tego filmu, żeby się przekonać jakie to proste:

<iframe width="560" height="315" src="https://www.youtube.com/embed/rXuHGLzSmSE?start=297" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Generator poligonów

[http://www.cssplant.com/clip-path-generator](http://www.cssplant.com/clip-path-generator)

---
### Inne dopuszczalne wartości oraz ich funkcje

**circle()** - tworzy koło/wartość wpisywana w pikselach

**ellipse()** - twrzoy elipeś/piksele

**inset()** - wcięcie lub też wycięcie obiektu wewnątrz/procenty

**inset-rectangle()** - podobnie jak inset

---

Źródło:

https://youtu.be/rXuHGLzSmSE?t=276

https://developer.mozilla.org/en-US/docs/Web/CSS/clip-pat