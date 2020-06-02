Title: CSS - centrowanie treści
Author: mkostyrko
Date: 2020-04-07 10:00
Updated:
Category: css
Tags: css, centrowanie, wyśrodkowanie
Slug: css-centrowanie-tresci
related_posts: css-flexbox, css-rwd


Istnieje parę sposobów na to w jaki sposób można wycentrować treść, na środku strony w taki sposób aby znajdowała na środku strony.

Można to zrobić łątwo przy pomocy flexboxa, ale gdy nie chcemy zmieniać deklaracji 'rodzeństwa' (rodzica) danego elementu wówczas nie będzie to możliwe.

Bez jakiejkolwiek ingerencji w deklaracje przypisaną do rodzica możemy skorzystać z pomocy marginesów oraz jednostek relatywnych np.

    .centered_text {
    margin-top: -50px; //  powinna być połowa wysokości obiektu 
    margin-left: -100px; // połowa szerokości obiektu
    margin-top: 50vw;
    margin-lef: 50vw;
    }

lub można również wykorzystać pozycjonować przy pomocy absolute

  .centered_text {
    position: absolutne;
    top: 50vh; // ew. 50% jeśli do rodzica
    left: 50vw; // ew. 50% jeśli do rodzica
    transform: translate(-50%, -50%); // zmień pozycję o połowę rozmiaru wysokość i szerokość
  }

W obu przypadkach wymagana jest transformacja pozycjonowanego elementu w taki sposób aby znajdował się on na środku ponieważ powyższymi deklaracjami wskazujemy na lewy górny róg danego elementu - stąd należy od odpowiednio wyrównać aby znalazł się na środku a nie był przesunięty w prawo i w dół o własną wysokość i szerokość.

Być może lepszy rozwiązaniem jest zatem, ustawienie marginesu na auto i jedynie kontrola marginesu od góry:

  .centered_text {
    margin: auto;
    margin-top: 50%;
  }

---

Źródło:

https://www.w3schools.com/css/css_align.asp

https://www.freecodecamp.org/news/how-to-center-things-with-style-in-css-dc87b7542689/