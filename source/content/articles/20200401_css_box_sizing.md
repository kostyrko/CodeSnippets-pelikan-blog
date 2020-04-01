Title: CSS: box-sizing
Author: mkostyrko
Date: 2020-04-01 10:00
Updated:
Category: css
Tags: css
Slug: css-box-sizing
related_posts: css-place-items, css-float


Box-sizing

Możliwe wartości do zastosowania przy tej właściwości

border-box - wielkość *kontenera* (div) jest dokładnie taka jak wskazano - definiuje wielkość kontenera po jego granicy

content-box- podstawowe, zachowanie się *kontenera* (div) od obszaru, w którym znajduje się jego zwartość /wskazana wartość wielkość pudełka odnosi się do jego zawartości, - oznaczo to że margines jak oraz padding będą naddane ponad wskazaną wielkość

padding-box - wielkość *kontenera* jest zależna od *paddingu*, granica jest nadana

Przykładowe zastosowanie

    div {
      box-sizing: border-box;
      width: 100%;
      border: solid #5B6DCD 10px;
      padding: 5px;
    }

Kliknij tutaj:
[**Interaktywna aplikacja do sprawdzania wielkości boxa**](https://codepen.io/carolineartz/full/ogVXZj/)

![box-sizing](https://codropspz-tympanus.netdna-ssl.com/codrops/wp-content/uploads/2014/09/box-areas1.png)

Źródło i polecane linki:

https://www.w3schools.com/css/css3_box-sizing.asp

https://www.youtube.com/watch?v=WlGQdgy-M6w

https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing

https://css-tricks.com/box-sizing/

https://tympanus.net/codrops/css_reference/box-sizing/