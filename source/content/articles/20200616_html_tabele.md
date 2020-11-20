Title: HTML: podstawy tabel
Author: mkostyrko
Date: 2020-06-16 10:00
Updated:
Category: html
Tags: css, html, semantyczny html, semantic
Slug: html-tabele
related_posts: html-semantyczny



![html-tabele](https://i.imgur.com/uIwzEfS.png)

|Sekcje Tabeli| HTML|
|---|---|
|Sekcja nagłówka| `<table></table>`|
|Sekcja nagłówka| `<thead></thead>`|
|Sekcja główna|`<tbody></tbody>` |
|Stopka|`<tfoot></tfoot>` |
| ---- | ---- |
|Wiersz|`<tr></tr>` |
|Komórka|`<td></td>` |
|Nagłówek tabeli|`<th></th>` |
| ---- | ---- |
| Zasięg | `<th scope="col/row">` |

---
### Przykładowa tabelka

<table>
    <thead>
        <tr>
            <th></th>
            <th scope="col">Model</th>
            <th scope="col">Planet</th>
            <th scope="col">Class</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">1</th>
            <td>R2D2</td>
            <td>Naboo</td>
            <td>Droid</td>
        </tr>
        <tr>
            <th scope="row">2</th>
            <td>C3PO</td>
            <td>Tatooine</td>
            <td rowspan="2">Protocol droid</td>
        </tr>
        <tr>
            <th scope="row">3</th>
            <td>ME-8D9</td>
            <td>Takodana</td>
        </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="4"> Star wars</td>
            </tr>
        </tfoot>
</table>

    <table>
        <thead>
            <tr>
                <th></th>
                <th scope="col">Model</th>
                <th scope="col">Planet</th>
                <th scope="col">Class</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th scope="row">1</th>
                <td>R2D2</td>
                <td>Naboo</td>
                <td>Droid</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>C3PO</td>
                <td>Tatooine</td>
                <td rowspan="2">Protocol droid</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td>ME-8D9</td>
                <td>Takodana</td>
            </tr>
        </tbody>
            <tfoot>
                <tr>
                    <td colspan="4"> Star wars</td>
                </tr>
            </tfoot>
    </table>

---
**Przykładowa tabela z zagnieżdżonymi tabelami**


<p class="codepen" data-height="265" data-theme-id="light" data-default-tab="html,result" data-user="mkostyrko" data-slug-hash="dyXEKGL" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Neste Table">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/dyXEKGL">
  Neste Table</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>


---

Źródła

[Kurs Html5 - tabela HTML](http://how2html.pl/tabela-html/)


