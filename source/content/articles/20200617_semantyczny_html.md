Title: HTML: semantyczny HTML
Author: mkostyrko
Date: 2020-06-17 10:00
Updated:
Category: html
Tags: css, html, semantyczny html, semantic
Slug: html-semantyczny
related_posts: 

![semantyczny-html](https://www.jungledisk.com/blog/content/images/blog/div-soup-vs-semantic-html.png#center){: max-height="300px"}


Znaczniki semantyczne określają znaczenie treści, która jest w ramach nich zamknięta. Nie powinny być wykorzystywane do pozycjonowania (od tego `div`) a do określania treści.

| HTML - tag | znaczenie 
|---|---|
|`<alt>`| alternative/opis w przypadku braku elementu lub dla czytnika |
|`<article>`| artykuł - rozumiany jako przedmiot rzecz / niezależna i zamknięta część strony |
|| zawartość tego taga powinna stanowić treść samą w sobie / będzie miała sens też na innej stronie |
|`<aside>`| boczny pasek/treść boczna |
|`<details>`| detale / w przypadku inputu pozwala na dodanie opcji wyboru |
|`<figcaption>`| podpis obrazu |
|`<figure>`| obraz/rycina |
|`<footer>`| stopka |
|`<header>`| wstęp/metadane/ linki nawigacji |
|`<main>`| główna treść strony |
|`<mark>`| podkreślony tekst |
|`<nav>`| element nawigacyjny |
|`<section>`| sekcja - tematyczne grupowanie semantycznie wspólnej części np. wielu artykułów |
|| może też rozdzielać na mniejsze części artykułów / sekcja jest integralną częścią strony|
|`<summery>`| podsumowanie |
|`<time>`| podsumowanie |
| ----- | ------ |
|`<abbr>`| abbreviation/skrót |
|`<address>`| adres |
|`<code>`| kod|
|`<dfn>`| definicja|
|`<Hn>`| Nagłówek |
|`<em>`| emphasis/podkreślenie|
|`<ins>`| insertion/ treść wstawiona|
|`<progress>`| oznaczenie postępu |
|`<rel>`| relation- ma na celu wskazanie na relacje pomiędzy elementami |

---

### Przykłady użycia semantycznego HTML

#### `<section>` & `<article>`

> HTML Article Element (`<article>`) defines a piece of self-contained content. It does not refer to the main content alone and can be used for comments and widgets.
>HTML Section Element (`<section>`) defines a section of a document to indicate a related grouping of semantic meaning. (za [MDN web docs - Using HTML sections and outlines](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines#:~:text=HTML%20Article%20Element%20(,related%20grouping%20of%20semantic%20meaning.)))

Ten tag wyraźnie wprowadza małe zamieszanie i zauważalne są dwie strategie korzystania z niego 1) porcjuje `<article>` na mniejsze sekcji 2) grupuje wiele `<article>` - tworzy cześć wyższego rzędu strony niż `<article>` oba podejścia nie muszą się wykluczać ([Section vs Article HTML5 - Stack Overflow](https://stackoverflow.com/questions/7549561/section-vs-article-html5))


![site-layout-1](https://almosthumor.files.wordpress.com/2011/09/html5demo1.jpg){: height="400px"}

**oraz**

![site-layout-2](https://cdn.semrush.com/blog/static/media/62/de/62de85ae40932e6d41e2966b3af3ca8e/resize/885x666/semantic-html5-markup-related-aside-kalicube.webp){: height="400px"}

---

### Przykłady użycia semantycznego HTML 2

#### Input + Details

<p class="codepen" data-height="400" data-theme-id="dark" data-default-tab="html,result" data-user="mkostyrko" data-slug-hash="qBbqapZ" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="datalist">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/qBbqapZ">
  datalist</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

#### Progress

<p class="codepen" data-height=""400 data-theme-id="dark" data-default-tab="html,result" data-user="mkostyrko" data-slug-hash="PoZbGeQ" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="progressbar">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/PoZbGeQ">
  progressbar</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

### Semantyczny HTML

Semantyczny HTML jest istotny z perspektywy:

* dostępności (Accessibility) -> Czytniki ekranowe/syntezatory mowy oraz urządzenia z niewielkimi ekranami (np. Apple Watch) korzystają z pomocy semantycznego HTML.

* SEO -> roboty wyszukiwarek sieciowych wykorzystują semantyczny html do indeksowania/pozycjonowania strony/jej znaczenia

* HTML pozwala na prostą walidację `<input type="email">` np. w przypadku wpisywanie adresu email -> tym samym mniej JS 


---

Źródła

[Native image lazy-loading for the web!](https://addyosmani.com/blog/lazy-loading/)

[JSJ 421: Semantic HTML with Bruce Lawson](https://devchat.tv/js-jabber/jsj-421-semantic-html-with-bruce-lawson/)

[Semantyczny blog w HTML](https://tutorials.comandeer.pl/html5-blog.html)

[Znacznik label - semantyczny HTML by Comandeer](https://www.youtube.com/watch?v=hffiWUbbPFs)

[Kod poprawny semantycznie](http://www.kurshtml.edu.pl/html/kod_poprawny_semantycznie,tekst.html)

[An Overview of HTML5 Semantics](https://codepen.io/mi-lee/post/an-overview-of-html5-semantics)

[HTML5 Semantic Tags: What Are They and How To Use Them!](https://www.semrush.com/blog/semantic-html5-guide/)