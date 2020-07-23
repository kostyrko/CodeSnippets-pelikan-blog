Title: React: komponenty i właściwości (props)
Author: mkostyrko
Date: 2020-07-23 10:00
Updated:
Category: reactjs
Tags: komponenty, props, react, components
Slug: react-komponenty
related_posts: 

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}

Komponent to struktura będący częścią aplikacji składająca się elementów. Komponent jest interaktywny - może przyjmować dane i zwracać inne komponenty lub elementy. Komponent może składać się z innych komponentów jak i elementów.

### Tworzenie komponentu

Komponent jest tworzony przy pomocy funkcji lub klasy - w nazewnictwie stosujemy **wielką literę** na początku

**Funkcja** tworząca komponent (wcześniej jedynie mogły wyświetlać strukturę JSX bez udziału logiki - to zmieniło się za sprawą React Hooks)


    function HelloWookie() {
      return (
        <div>
          <h1>I am Wookie!</h1>;

        </div>
      )
    }


**Klasa** tworząca komponent (bardziej skomplikowana struktura, trudniejszy w kod w testowaniu)
Wymaga zaimportowania **{Component}** i dziedziczenia od klasy **Components**

    import React, {Component} from "react";

    class HelloDroid extends Component {
      render() {
        return <h1>BB-8!</h1>;
      }
    }


### Renderowanie

Bez znaczenia czy komponent powstał przy pomocy klasy czy funkcji jest on renderowany w podobny sposób


    ReactDOM.render(
      <HelloDroid />,
      document.getElementById("app")
    );

### Właściwości -> properties (pros)

Właściwości są tym co dodaje dynamiki komponentom - jest tym czym właściwość/argument jest dla funkcji




---

Źródła:

[Podstawowe informacje](https://pl.reactjs.org/docs/getting-started.html)


YT: 

[Wprowadzenie do biblioteki React.js](https://www.youtube.com/watch?v=DN73tm89cgU)

[React JS - kurs w 60 minut](https://www.youtube.com/watch?v=Qz7swLxNS0Y)

