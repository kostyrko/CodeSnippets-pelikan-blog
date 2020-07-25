Title: React: komponenty i właściwości (props)
Author: mkostyrko
Date: 2020-07-21 10:00
Updated:
Category: reactjs
Tags: komponenty, props, react, components
Slug: react-komponenty
related_posts: 

![react-props](https://cms-assets.tutsplus.com/uploads/users/1795/posts/29541/image/Stateful-vs-Stateless-Component-Tutorial-Component-with-prop.jpg){: max-height="300px"}

Komponent to struktura będący częścią aplikacji składająca się elementów. Komponent jest interaktywny - może przyjmować dane i zwracać inne komponenty lub elementy. Komponent może składać się z innych komponentów (zagnieżdżanie) jak i elementów.

Z elementów warto stworzyć komponenty gdy te: się powtarzają i stanowią spójną całość, jeśli komponent jest duży (5-10 elmentów) wówczas należy go podzielić na mniejsze komponenty 

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


albo


    const HelloWookie = () => {
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


albo

    class HelloDroid extends Component {
      render() {
        return (
          <div>
            <h1>I am a Wookie!</h1>;
          </div>
        )
      }
    }



#### Renderowanie

Bez znaczenia czy komponent powstał przy pomocy klasy czy funkcji jest on renderowany w podobny sposób


    ReactDOM.render(
      <HelloDroid />,
      document.getElementById("app")
    );


---

### Zagnieżdżanie

W ramach Greeting zagnieżdżony jest Droid.

    class Droid extends Component {
      render() {
        return <h1>Hi, {this.props.name}</h1>;
      }
    }

    class Greeting extends Component {
      render() {
        return <Hi name="C3-Po" />;
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

### Właściwości -> properties (obiekt props)

Właściwości są tym co dodaje dynamiki komponentom - jest tym czym właściwość/argument jest dla funkcji.


Z perspektywy funkcji może to wyglądać w następujący sposób

    
    function Droid=(props) => {
      return <h1>I am {props.name}</h1>
    }

    ReactDOM.render(
      <Droid name="C3-PO" />,
      document.getElementById('app')
    );

albo z perspektywy klasy (warto zwrócić uwagę na pojawienie się słowa kluczowego **this**)


    class Droid extends Component {
      render() {
        return <h1>I am {this.props.name}</h1>
      }
    }


    ReactDOM.render(
      <Droid name="C3-PO" />,
      document.getElementById('app')
    );


React pobiera atrybuty przekazane do komponentu i implementuje je do obiektu **props**

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
### Destrukturyzacja

Ze względu na to, że **props** jest obiektem, możemy dokonać na nim destrukturyzacji na różne sposoby


destrukturyzacji dwóch obiektów


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


Wykorzystując tablicę


    const Droids = ({droids}) => {
      return <h1>{droids[0],droids[1]}</h1>
    }

    <Droids props={droids} />

---

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

Źródła:

[komponenty - React docs](https://pl.reactjs.org/docs/components-and-props.html)

