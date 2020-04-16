Title: CSS - place-items (umieść element)
Author: mkostyrko
Date: 2020-03-31 08:00
Updated:
Category: css
Tags: css, place-items, grid, flexbox, start, center, place-items
Slug: css-place-items
related_posts: css-flexbox

Deklaracja **`place-items`** (podobnie jak `align-items`) odnosi się do pozycjonowania dzieci elementu, których układ jest zależny od układu **Flexbox** lub **Grid**.

Deklaracja **`place-items`** jest połączeniem `align-items` oraz `justify-items` i przyjmuje podwójne wartości w odpowiadające kolejno za `align-items` o następnie za `justify-items`. Wymaga wcześniejszej deklaracji `floatbox` lub `grid `

Przykładowe zastosowanie

    .item {
      display: flex;
      place-items: start center;
    }

i odpowiada to:

    .item {
      display: grid;
      align-items: start;
      justify-items: center;
    }

W momencie kidy jedna wartość jest wskazana, wówczas przyjęta jest ona jako wspólna dla obu właściwości

Przykładowe zastosowanie

    .item {
      display: flex;
      place-items: start;
    }

i odpowiada to:

    .item {
      display: flex;
      align-items: start;
      justify-items: start;
    }

Przyjmuje wartości `auto`, normal, strech, start end, center, left, right, flex-start, flex-end, self-start, self-end, first-baseline, last-baseline


Źródło i polecane linki:

https://css-tricks.com/almanac/properties/p/place-items/

https://css-tricks.com/almanac/properties/a/align-items/

