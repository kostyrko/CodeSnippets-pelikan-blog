Title: React: komponenty i właściwości (props) + destrukturyzacja
Author: mkostyrko
Date: 2020-07-21 10:00
Updated:
Category: reactjs
Tags: komponenty, props, react, components, destrukturyzacja, fragmenty
Slug: react-komponenty
related_posts: 

![react-props](https://cms-assets.tutsplus.com/uploads/users/1795/posts/29541/image/Stateful-vs-Stateless-Component-Tutorial-Component-with-prop.jpg){: max-height="300px"}

Aplikacje/strony tworzone przy pomocy *Reacta* składają się z komponentów. Komponenty tworzą strukturę aplikacji i są interaktywny - mogą przyjmować dane i na ich podstawie zwracać zmienione komponenty (tworzona są przy pomocy [klas](#komponent-klasy) lub [funkcji](#komponent-funkcja))


Komponenty są elementami strony, które się powtarzają i stanowią spójną całość, warto podzielić dany komponent na mniejsze części (również komponenty) jeśli ten składa się z większej ilości elementów (5-10).

Istotne jest to, że każdy z tworzonych komponentów może zwracać tylko jeden element - oznacza to, że wszystkie elementy danego komponentu (w tym np. inne komponenty, na które się składa dany komponent) powinny być opakowane w `<div>` lub tzw. [fragmenty](#fragmenty)

---
### Tworzenie komponentu - podstawy

Komponent jest tworzony przy pomocy funkcji lub klasy - w nazewnictwie stosujemy **wielką literę** na początku

**Funkcja**{#komponent-funkcja} tworząca komponent (wcześniej jedynie mogły wyświetlać strukturę JSX bez udziału logiki - to zmieniło się za sprawą [React Hooks](https://kostyrko.github.io/zfrontu/react-hooks.html) - od React v. 16.8)

Przykład komponentu funkcyjnego



    function HelloWookie() {
      return (
        <div>
          <h1>I am Wookie!</h1>;
        </div>
      )
    }


oraz przy pomocy ES6


    const HelloWookie = () => {
      return (
        <div>
          <h1>I am Wookie!</h1>;
        </div>
      )
    }


**Klasa**{#komponent-klasy} tworząca komponent (bardziej skomplikowana struktura, trudniejszy w kod w testowaniu) wymaga zaimportowania **{Component}** i dziedziczenia z klasy **Components**


    import React, {Component} from "react";

    class HelloDroid extends Component {
      render() {
        return <h1>BB-8!</h1>;
      }
    }

---

### Fragmenty{#fragmenty}

Fragmenty pozwalają na zgrupowanie wielu elementów bez konieczności dodawania dodatkowego węzła DOM (np. div) - fragment można stworzyć w sposób skrótowy `<> </>` oraz jako <React.Fragment> </React.Fragment>



    class HelloDroid extends Component {
      render() {
        return (
          <>
            <h1>I am a Wookie!</h1>;
          </>
        )
      }
    }

---

### Renderowanie komponentów

Bez znaczenia czy komponent powstał przy pomocy klasy czy funkcji jest on renderowany w podobny sposób -> nazwa renderowanego komponentów zamknięta jest jest pomiędzy trójkątnymi nawiasami i posiada znak zamknięcia w postaci ukośnika


    ReactDOM.render(
      <HelloDroid/>,
      document.getElementById("app")
    );

#### Praktyka

Częstą praktyką jest korzystanie pliku głównego np. app.js, w ramach którego tworzony jest komponent główny skupiający w sobie podstawowe komponenty (patrz również poniżej [zagnieżdżanie](#zagnieżdżanie)), który następnie jest renderowany (wymaga to wcześniejszego zaimportowania komponentów z innych plików) - zamiast skupiania w metodzie renderującej należącej do ReacDOM, przy pomocy fragmentów wszystkich komponentów


    import React, from "react";
    import ReactDOM from "react-dom";

    import {HoverEventFunc, HoverEventClass} from './HoverEvent'


    const App = () => (
      <>
        <HoverEventFunc/>
        <HoverEventClass/>
      </>
    )


    ReactDOM.render(<App/>, document.getElementById("app"));

---

### Właściwości -> properties (obiekt props)

Właściwości są tym co dodaje dynamiki komponentom - jest tym czym właściwość/argument jest dla funkcji. Aby przekazać props do komponentu należy wykorzystać jego nazwę następnie wykorzystać znak równość oraz podać jego treść. Większa ilość propsów nie jest rozdzielona żadnym znakiem po za spacją.
Argumenty do *propsu* można przekazywać pod różną postacią -> string zamknięty jest w cudzysłowie np. `name='Mike'`, natomiast wartości liczbowe w nawiasach klamrowych np. `number={5}` (więcej na ten temat poniżej [propsy-cd](#propsy-cd)).


Z perspektywy komponentu funkcyjnego może to wyglądać w następujący sposób

    
    function Droid=(props) => {
      return <h1>I am {props.name}</h1>
    }

    ReactDOM.render(
      <Droid name="C3-PO" />,
      document.getElementById('app')
    );

albo z perspektywy komponentu klasowego (warto zwrócić uwagę na pojawienie się słowa kluczowego **this**)


    class Droid extends Component {
      render() {
        return <h1>I am {this.props.name}</h1>
      }
    }


    ReactDOM.render(
      <Droid name="C3-PO" />,
      document.getElementById('app')
    );


React pobiera atrybuty przekazane do komponentu i implementuje je do **obiektu** **props**

np. 

    
    <Droid name="C3-PO" /> => 

    Obiekt props wygląda następująco:
    {
      name: "C3-PO"
    }

albo 

    const droids = ["C3-PO", "R2-D2"];

    <DroidList droids={droids} />

    Obiekt props wygląda następująco:
    {
      droids = ["C3-PO", "R2-D2"]
    }

---
### Destrukturyzacja (obiektów) props

Ze względu na to, że **props** jest obiektem, możemy dokonać na nim destrukturyzacji na różne sposoby tak aby nie odwoływać się cały czas do obiektu **props**

#### Klasy

W przypadku **klas** należy dokonać destrukturyzacji **przed return**em

    class Droids extends Component {
      render() {
        const { droid } = this.props;
        return (
          <ul>
            {droid.map((elem) => (
              <li key={elem.name}>
                {elem.name}</a>
              </li>
            ))}
            </ul>
        );
      }
    }


#### Funkcje

destrukturyzacji dwóch obiektów w przypadku **komponentów funkcyjnych**


    const Droids = (props) => {
      const {droid1, droid2} = props;
      return <h1>{droid1} {droid2}</h1>
    }

    ReactDOM.render(
      <Droids droid1="C3-PO" droid2="R2-D2"/>,
      document.getElementById("app")
    );


destrukturyzacji przekazując arg. do Komponentu


    const Droids = ({droid1, droid2}) => {
      return <h1>{droid1} {droid2}</h1>
    }

    ReactDOM.render(
      <Droids droid1="C3-PO" droid2="R2-D2"/>,
      document.getElementById("app")
    );


Wykorzystując tablicę (w przypadku prostego zwrócenia elementu słowo kluczowe **return** nie jest wymagane podobnie jak nawiasy klamrowe - wynika to funkcji strzałkowej (ang. arrow function))


    const Droids = ({droids}) => (
      <h1>{droids[0]} {droids[1]}</h1>
    )

    const droids = ["C3-PO", "R2-D2"];

    ReactDOM.render(
      <Droids droids={droids}/>,
      document.getElementById("app")
    );


---

### Props cd. {#propsy-cd}

Jako props można przekazać różnego rodzaju dane - liczby, wartości logiczne, łańcuchy szablonowe, zmienne, tablice, funkcje jednak te wówczas winny znaleźć się w **nawiasach klamrowych**. 

    const firstDroid = 'C3-PO'

    ReactDOM.render(
      <Droid name={firstDroid} />,
      document.getElementById('app')
    );


Przy większej ilości właściwości odwołujemy się do ich klucza i nie są oddzielane żadnymi znakami


    const protocol = 'protocol droid'

    ReactDOM.render(
      <Droid 
      name={firstDroid}
      class={protocol} />,
      document.getElementById('app')
    );


W przypadku łańcucha szablonowego zmienna znajduje swoje miejsce w wywołaniu komponentu (przekazania właściwości/propsu)


    const Greeting = (props) => {
      return (
        <div>
          <h2>Welcome!</h2>
          {props.message}
        </div>
        )
    }

    const name = "C3-PO"

    <Greeting message={`Hi, ${user}.`} />


Właściwości pozwalają nam również na przekazanie funkcji, które mogą być wywołane wewnątrz komponentu


    const Greeting = (props) => {
        props.func("Elo")         // wywołanie przkazanej funkcji z podaną właściwością
        return <h2>Hello -> Elo!</h2>
      }

    const simpleFunc = (greeting) => {
      console.log(`Hello -> ${greeting}`)
    }

    <Greeting func={simpleFunc} />

---

### Zagnieżdżanie komponentów{#zagnieżdżanie}

Komponenty mogą składać się z innych mniejszych komponentów (interaktywnych i powtarzalnych w swojej funkcjonalności bloków kodu), oznacza to, że w ramach większego komponentu zagnieżdżane są mniejsze z których się składa

W ramach Greeting zagnieżdżony jest Droid.

    class Droid extends Component {
      render() {
        return <h1>Hi, {this.props.name}</h1>;
      }
    }

    class Greeting extends Component {
      render() {
        return <Droid name="C3-Po"/>;
      }
    }

    ReactDOM.render(
      <Greeting />,
      document.getElementById('app')
    );  


...ale takich elementów mogło by być również więcej

    class Droid extends Component {
      render() {
        return <h1>Hi, {this.props.name}</h1>;
      }
    }

    class Greeting extends Component {
      render() {
        return (
          <div>
            <Droid name="C3-PO" />
            ...
            ...
          </div>
        )
      }
    }

    ReactDOM.render(
      <Greeting />,
      document.getElementById('app')
    );    



---

Źródła:

[komponenty - React docs](https://pl.reactjs.org/docs/components-and-props.html)

[destrukturyzacja - kursjs.pl](http://kursjs.pl/kurs/es6/destructuring.php)

[Przypisanie destrukturyzujące - MDN](https://developer.mozilla.org/pl/docs/Web/JavaScript/Referencje/Operatory/Destructuring_assignment)

[Dobre praktyki w React cz. 1⌨️ hello roman #121](https://www.youtube.com/watch?v=POBekn2ZL9Y)

[Wprowadzenie do hooków](https://pl.reactjs.org/docs/hooks-intro.html)