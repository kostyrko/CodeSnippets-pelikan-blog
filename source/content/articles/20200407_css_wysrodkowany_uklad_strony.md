Title: CSS - wyśrodkowany układ strony
Author: mkostyrko
Date: 2020-07-02 10:00
Updated:
Category: css
Tags: css, flex, flexbox, layout, układ
Slug: css-wysrodkowany-uklad-strony
related_posts: css-flexbox

Jednym popularniejszych obecnie stosowanych układów stron internetowych jest oparty na wyśrodkowanej treści - dzięki temu treść strony nie rozjeżdża się na boki przy większych ekranach.

Taki układ można łatwo osiągnąć przy użyciu `flexboxa`, odpowiednio zagnieżdżonego `div`'a oraz przypisanej mu klasy określającej jego szerokość

Przyjmę, że będziemy operować na 3 częściach -> Headerze - gdzie potencjalnie można znajdować się nawigacja, Main - zawiera główną zawartość strony, oraz Footer - gdzie znajdować się mogą informacje kontaktowe. Dalsze komentarze znajdują się kodzie zamieszczonym poniżej

`index.html`

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="style.css">
      <title>Centralized layout</title>
    </head>
    <body>
      <!-- zajmuje 100% body (a body 100vw i wh) -->
      <header>
      <!-- zajmuje tyle szerokości ile zdefiniowane przez css -->
        <div class="container"> 
          <p class="header-text text">Top within header and container div</p>
        </div>
      </header>
      <main>
        <div class="container">
          <p class="main-text text">Main within main and container div 1</p>
          <p class="main-text text">Main within main and container div 2</p>
          <p class="main-text text">Main within main and container div 3</p>
        </div>
      </main>
      <footer>
        <div class="container">
          <p class="footer-text text">Bottom within header and container div</p>
        </div>
      </footer>
    </body>
    </html>

style.css

    /* importowanie fontów */
    @import url('https://fonts.googleapis.com/css2?family=Baloo+Thambi+2:wght@500&family=Indie+Flower&family=Shadows+Into+Light&display=swap');

    /* reset */
    * {
      padding: 0;
      margin: 0;
    }

    html {
      font-size: 1.5rem;
    }

    /* kontener zawierający wyśrodkowaną treść */
    .container {
      width: 60%;
      min-width: 200px;
      background-color: white;
      border: 2px solid rgb(10, 10, 10);
      margin: 5px 0 5px 0;
      /* wyśrodkowanie zawartości kontenera */
      display: flex;
      align-items: center;
      justify-content: space-evenly;
      flex-wrap: wrap;
    }

    /* header wyśrodkowujący kontener */
    header {
      display: flex;
      justify-content: center;
      background: green;
      border-bottom: 1px solid;
      height: 10vh;
    }

    /* mian wyśrodkowujący kontener */
    main {
      display: flex;
      justify-content: center;
      background-color: blue;
      height: 80vh;
    }

    /* footer wyśrodkowujący kontener */
    footer {
      display: flex;
      justify-content: center;
      background-color: orange;
      border-top: 1px solid;
      height: 10vh;
    }

    .text {
      font-family: 'Indie Flower', cursive;
      border: 1px dashed;
      background-color: rgb(255, 115, 0);
      width: 65%;
      text-align: center;
    }

    /* .header-text lub */
    header .text {
      font-family: 'Baloo Thambi 2', cursive;
      height: 60%;
    }

    .main-text {
      width: 250px;
      height: 25%;
    }
    .footer-text {
      font-family: 'Shadows Into Light', cursive;
    }

    .main-text:first-of-type {
      background-color: chartreuse;
    }

    .main-text:nth-of-type(2) {
      background-color: yellow;
    }

    .main-text:last-of-type {
      color: white;
      background-color: black;
    }

Efekt można obejrzeć tutaj

<p class="codepen" data-height="400" data-theme-id="light" data-default-tab="css,result" data-user="mkostyrko" data-slug-hash="xxwKKdx" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="easy_centered_layout_example">
  <span>See the Pen <a href="https://codepen.io/mkostyrko/pen/xxwKKdx">
  easy_centered_layout_example</a> by Mikołaj Kostyrko (<a href="https://codepen.io/mkostyrko">@mkostyrko</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>