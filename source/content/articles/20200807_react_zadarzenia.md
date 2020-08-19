Title: React: zdarzenia - podstawy
Author: mkostyrko
Date: 2020-08-07 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-zdarzenia
related_posts: react-wprowadzenie, react-komponenty, react-listy

![react](https://i0.wp.com/css-tricks.com/wp-content/uploads/2018/08/react-events.png){: max-height="300px"}

Zdarzenia w React obsługiwane są  w podobny sposób jak w HTML -> oznacza to, że inlinowo wpisywane są "nasłuchiwacze" (używając **camelCase**) do którego przekazywany jest atrybut w nawiasach klamrowych -> przekazywanie funkcji jako props

    <button onClick={buttonClick}>Button</button>

Metoda, do której się odwołujemy poprzez atrybut może znaleźć swoje miejsca w ramach stworzonego komponentu lub jego rodzica (istotnej jest aby była osiągalna/możliwa do wywołania).

Pozytywnie na wydajność wpływa umieszczanie funkcji po za komponentem - gdy renderowany jest komponent wielokrotnie to funkcja nie musi być tworzona na nowo.

---

### Zdarzenia w komponentach klasowych 

W przypadku komponentów klasowych istotne jest pamiętanie o odwołaniu się do słowa kluczowego **this**


      class Droid extends Component {
        helloDroid() {
          console.log("Hi R2D2!");
        }
        render(){
          return (
            <>
            <h2>Greet Droid by clicking below!</h2>
            <button onClick={this.handleClick}>
            Start!
            </button>
            </>
          );
        }
      }


Słowo kluczowe **this** jest zależne od kontekstu, w przypadku gdy dany element powinien mieć dostęp do całości komponentu (np w celu skorzystania z *props*) stosuje się **funkcję strzałkową** [jej zastosowania wymaga użycia **dodatkowej wtyczki** *@babel/plugin-proposal-class-properties* (w klasie ES6 nie ma możliwości zastosowania funkcji strzałkowej)].

#### Konfiguracja wtyczki Babel: plugin-proposal-class-properties{#plugin-proposal-class-properties}

**Konfiguracja @babel/plugin-proposal-class-properties** w .babelrc 

    {
      "presets": ["@babel/preset-env", "@babel/preset-react"],
      "plugins": [
        ["@babel/plugin-proposal-class-properties", { "loose": true }]
      ]
    }


W funkcji strzałkowej **this** nie ulega zmianie i odwołuje się do elementu najwyższego rzędu


Porównanie zachowania się **this** - `greetDroid` (funkcja strzałkowa) zadziała podczas gdy `helloDroid` nie będzie w stanie odwołać się do **props**


    import React, {Component} from "react";
    import ReactDOM from "react-dom";


    class Droid extends Component {
      helloDroid() {
        console.log(`Hi ${this.props.droidName}`);
      }
      greetDroid= () => {
        console.log(`Hi ${this.props.droidName}`);
      }
      render(){
        return (
          <>
          <h2>Greet Droid by clicking below!</h2>
          <button onClick={this.helloDroid}>
          Funkcja
          </button>
          <button onClick={this.greetDroid}>
          Funkcja strzałkowa
          </button>
          </>
        );
      }
    }


    ReactDOM.render(
      <Droid droidName='C3PO'/>,
      document.getElementById("app")
    );   

---

### Zdarzenia w komponentach funkcyjnych

Zdarzenia w komponentach funkcyjnych wyglądają podobnie do tych stosowanych w komponentach klasowych


    import React from "react";
    import ReactDOM from "react-dom";

    const Droid = ({droidName}) => {
      const greetDroid = () => {
        console.log(`Hi ${droidName}`);
      }
      return (
        <>
          <h2>Greet Droid by clicking below!</h2>
          <button onClick={greetDroid}>
            Start!
          </button>
        </>
      );
    }

    ReactDOM.render(
      <Droid droidName='C3PO'/>,
      document.getElementById("app")
    );

### Nazwy najczęściej stosowanych wydarzeń

| Nazwa zdarzenia | Opis | 
|---|---|
| **onClick** | kliknięcie |
|**onDoubleClick**|podwójne kliknięcie|
|**onMouseEnter**| najazd myszką |
|**onMouseLeave**| opuszczenie myszki |
|**onKeyDown**| wciśnięcie klawisza (strzałka w dół) |
|**onKeyPress**| wciśnięcie klawisza (dowolnego) |
|**onKeyUp**| wciśnięcie klawisza (strzałka w górę)|
|**onSubmit**| po wysłaniu formularza|
|**onChange**| detekcja zmiany|
|**onFocus**| skupienie|
|**onBlur**| zmiana skupienia|
|**onLoad**| gdy się załaduje|


---

### Zatrzymanie domyślnej akcji

Zatrzymanie domyślnej akcji stosuje się poprzez odwołanie się do eventu


    const Link = () => {
      function clickLink(e){
        e.preventDefault();
      }

      return (
        <>
          <a href="#" onClick={clickLink}>Link</a>
        </>
      );
    }


---

Źródła:

[Interakcja z komponentami React.js](https://typeofweb.com/interakcja-komponentami-react-js/)

[SyntheticEvent](https://pl.reactjs.org/docs/events.html)


