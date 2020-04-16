Title: CSS - reset i normalizer
Author: mkostyrko
Date: 2020-04-05 11:00
Updated:
Category: css
Tags: css, normalizer, reset, Toggle Debug CSS
Slug: css-reset-normalizer
related_posts: css-neumorphism, css-box-sizing

### Reset

Każda z przeglądarek ma swoje domyślne style, celem `reset`u jest ich wyzbycie się i doprowadzenie do sytuacji, w której zadeklarowane style własne spowodują, możliwie jak najbliższe sobie zachowanie w różnego typu wyszukiwarkach internetowych. Normalizer zaczyna się od gwiazdki `*` wyznaczając, że deklaracja odnosi się do wszystkich elementów. Tu często również wskazuje się na rozmiar box-sizingu.

    * {
      margin: 0;
	    padding: 0;
      box-sizing: border-box
    }

Reset można również pobrać już gotowy i podlinkować go w html

do tego celu można np. pobrać go [z tego repo](https://gist.github.com/karbassi/5256094)

---

### Normalizer

Jest opisywany jako alternatywa dla `reset`u faktycznie jednak, nie ma on na celu "wyzerowania" podstawowych styli a nadania nowych lub też **nadpisania** jednych innymi, takimi które ułatwią tworzenie deklaracji dla strony. Przykładowo domyślna wielkość fontu to 16px co nie ułatwia pracy korzystając z wartością rem ('root' em - element) i dlatego być może warto zadeklarować na początku jego wielkość na 10px. Normalizer jest również swoistego rodzaju **komentarzem** do dalej pojawiających się deklaracji. Normalizer zadeklarowałbym jako element należący do html. Przykłąd:

  html {
    font-size: 10px;
  }



również można podlinkować do html w postaci np. linku znajdującego się [tutaj](https://cdnjs.com/libraries/normalize)

---

### Bonus - sposób oraz narzędzia na "wrysowanie" granic poszczególnych elementów

Wtyczki (Chrome/Chromium):

* Layout Debugger

* Toggle Debug CSS

* Outliner CSS

Dodać do style.css

    * {
      outline: 1px solid red;
    }



Źródło:

https://meyerweb.com/eric/tools/css/reset/

https://stackoverflow.com/questions/6928492/what-can-i-use-to-outline-html-elements-with-visible-padding-margin-and-border/24151270#24151270

https://css-tricks.com/modern-normalize/

http://nicolasgallagher.com/about-normalize-css/

https://github.com/sindresorhus/modern-normalize

https://medium.com/@elad/normalize-css-or-css-reset-9d75175c5d1e