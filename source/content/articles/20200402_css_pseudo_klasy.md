Title: CSS:pseudo-klasy
Author: mkostyrko
Date: 2020-04-02 10:00
Updated:
Category: css
Tags: css, pseudo-klasy
Slug: css-pseudo-klasy
related_posts: css-pseudo-elementy

Pseudo klasy pozwalają na wprowadzenie interaktywnego zachowania się strony przy pomocy CSS, przy pomocy tej deklaracji w zależności od zdefiniowanej sytuacji/stanu dany obiekt może przyjąć inny wygląd. Istotne jest to że deklaracja pseudoklasy poprzedzona jest dwukropkiem `:`

Przykładowy schemat zastosowania

    selektor:pseudoklasa {
      właściwość: wartość;
    }

W przypadku **linków **istniejącą pseudoklasy

`a:visited` - link, który został już użyty
`a:link` - zmienia wygląd odsyłacza

**Pseudoklasy akcji**

`:hover` - obiekt nad którym znajduje się kursor myszy
`:focused` - obiekt na którym jest focus (właściwość przypisana dla klawiatury)
`:active` - obiekt link/używany

Przykładowe zastosowanie

    button:hover {
      color: blue;
    }

**Pseudoklasa dotycząca przycisku**

`button:disabled` - zablokowanie przycisku

**Pseudoklasa dotycząca checkboxa**

`input[type="checkbox"]:checked` - zaznaczenie checkboxa

Ta pseudo klasa często może być wykorzystana również w celu dodanie jakiegoś rodzaju funkcjonalności do strony - np. poprzez ustawienie deklaracji `display` oraz nadanie jej odpowiedniej wartości w momencie gdy `checked = true`. Należy pamiętać wówczas o dwóch ważnych warunkach. 1) checkbox musi znajdować się na poziomie wyżej niż obiekt, na który planujemy mieć wpływ 2) zależność należy oznaczyć znakiem "poprzedzony" -> `~`

CSS

    #theme-checkbox:checked ~article {
      background-color: var(--gray-darker);
    }

Pseudoklasy strukturalne

`:first-child` - wskazanie pierwszego dziecka

`:last-child` - wskazanie ostatniego dziecka

`:nth-child()` - wskazanie wybranego dziecka - w nawias wpisuje się liczbę przypisaną dla danego dziecka

`:nth-of-type()` - n-te element określonego typu

`:nth-last-of-type()` - n-ty element określonego typu licząc od ostatniego dziecka

`:nth-last-child()` - każdy element który jest n-tym dzieckiem licząc od ostatniego dziecka

`:only-child` - każdy element który jest jedynym dzieckiem swojego rodzica

`:first-of-type` - pierwszy określonego typu

`:last-of-type` - ostatni element określonego typu

`:only-of-type` - jedyny element określonego typu / lub ten który nie posiada rodzeństwa określonego typu



Przykładowe zastosowanie

Jedyne dziecko

    p:only-child {
      color:red;
    }

    p:nth-last-child(2) {
      color:red;
    }

    /* ostatni element listy li */

    li:nth-last-of-type(2) {
      background: red;
    }

Źródło i polecane linki:

https://the-awwwesomes.gitbooks.io/html-css-step-by-step/content/pl/appendix/clean-code/index.html

http://www.kurshtml.edu.pl/css/co_to_sa_pseudoklasy,pseudoklasy.html

https://css-tricks.com/pseudo-class-selectors/

https://www.w3schools.com/css/css_pseudo_classes.asp

https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes