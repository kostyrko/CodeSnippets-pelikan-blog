Title: CSS - max(), min(), clamp()
Author: mkostyrko
Date: 2020-05-24 10:00
Updated:
Category: css
Tags: css, max, min, clamp, funkcje
Slug: css-max-min-clamp
related_posts: 

`min()` - jest funkcją CSS i pozwala na oznaczenie najmniejszej wartości w przypadku szerokości obiektu i przyjmuje jedno lub więcej wyrażeń rozgraniczonych przecinkami jako parametry (istnieje możliwość mieszania jednostek np. px, vw,  %) - najmniejszy z dwóch podanych parametrów w danym momencie jest obowiązujący.

    .second-level {
      width: min(50vw, 400px);
    }
    

Przykładowo powyższy zapis zakłada, że dany element o klasie `second-level` będzie miał szerokość 400px do momentu, w którym połowa szerokości ekranu (50vw, innymi słowy gdy ekran jest węższy od 800px) nie będzie mniejsza niż 400px i wówczas przyjmie wartość 50vw.
Ubierając to w inne słowa, dany element będzie zajmował połowę szerokości ekranu jeśli ten będzie mniejszy niż 800px, a w przypadku szerszych ekranów jego szerokość będzie maksymalnie wynosiła 400px.

Innymi słowy min() oznacza podanie maksymalnej wartości jaką może mieć dany element

---

`max()` - jest funkcją podobną do min() jednak odnosi się do maksymalnej wartości danego elementu - również przyjmuje jedną lub więcej wyrażeń jako parametr. Za wartość, ustawiającą szerokość przyjmuje największą wartość z podanych parametrów

  .second-level {
      width: max(50vw, 400px);
  }

Powyższe wyrażenie zakłada, że dany element o klasie `second-level` będzie miał szerokość 400px do momentu, w którym połowa ekranu nie będzie większa niż 800 px i wówczas przyjmie wartość połowy szerokości ekranu (50vw). Dla ekranu węższego niż 400px zajmie 100% rodzica.

Innymi słowy max() oznacza podanie minimalnej (największej w danym momencie) wartości jaką może mieć dany element

Inny przykład oznacza maksymalną wielkość fontu na stronie, który będzie zależny od jego rozmiaru np.

  p {
    font-size: max(4vw, 2em, 2rem)
  }

---

`clamp()` - pozwala na zdefiniowanie przedziału, w ramach, które powinien zamknąć się dany element. Przyjmuje trzy wartości - minimalną, preferowaną oraz maksymalną -> clamp(MIN, VAL, MAX). Tym samym istnieje możliwość ustawienia wielkości elementu, który zmieniać się będzie razem z wielkością ekranu ale nie będzie mniejsza niż dana wartość ani większa od innej podanej.

  p {
    font-size: max(1rem, 2.5vw, 2rem)
  }



---

Źrdóła: 

https://developer.mozilla.org/en-US/docs/Web/CSS/min

https://developer.mozilla.org/en-US/docs/Web/CSS/max

https://css-tricks.com/snippets/css/fluid-typography/