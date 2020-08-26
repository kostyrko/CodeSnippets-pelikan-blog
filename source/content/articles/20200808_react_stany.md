Title: React: (zjednoczne) Stany React'a
Author: mkostyrko
Date: 2020-08-08 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-stany
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia

![react](https://ihatetomatoes.net/wp-content/uploads/2017/08/03-state-vs-props.png){: max-height="300px"}

## Stateful components (komponenty ze stanami)

Stan (ang. state) jest miejscem przechowywania aktualnego stanu (wewnętrznego) komponentu Reacta - jest wykorzystywany gdy komponent wymaga aktualizacji (np. licznik, godzina, ukrywanie/pokazywanie części komponentu) -> dla przypomnienia: Props/Informacje przekazywane do komponentu nie ulegają zmianie w ramach niego (props przekazuje informacje z góry na dół - od rodzica do dziecka).

State - przechowuje inf. o własnym stanie komponentu - może być modyfikowany (analogia - zmienne wewnątrz funkcji). Początkowo ze stanów można było korzystać jedynie w kontekście komponentów klasowych, jednak wraz z prowadzeniem tzw. funkcji **hooks** również można z nich korzystać w kontekście komponentów funkcyjnych (patrz. [React: Haki (hooks) na Reacta ](https://kostyrko.github.io/zfrontu/react-hooks.html))

---

## Komponenty klasowe

### Tworzenie stanu

W przypadku komponentów klasowych należy odwołać się do funkcji konstruktora oraz konstruktora rodzica. **State** jest słowem kluczowym i powinien być obiektem.

    constructor(props) {
      super(props)
    }


    constructor(props) {
      super(props)
      this.state = {
        name: ''
      }
    }

    =======
    import React, {Component} from "react";
    import ReactDOM from "react-dom";

    class Droid extends Component {
      constructor(props) {
        super(props)
        this.state = {
          name: 'R2D2!'
        }
      }

      // funkcja strzałkowa!
      helloDroid=()=> {
        console.log(this.state.name);
      }

      render(){
        return (
          <>
          <h2>Greet Droid by clicking below!</h2>
          <button onClick={this.helloDroid}>
          Start!
          </button>
          </>
        );
      }
    }


    ReactDOM.render(
      <Droid/>,
      document.getElementById("app")
    );


### Automatyczny Inicjalizator stanu
W prostszy sposób (skrócony) można zainicjalizować state przy pomocy wtyczki *@babel/plugin-proposal-class-properties* (więcej na ten temat znajdziesz tutaj: [konfiguracja wtyczki Babel: plugin-proposal-class-properties](https://kostyrko.github.io/zfrontu/react-zdarzenia.html#plugin-proposal-class-properties))

Wówczas nie musimy odwoływać się do funkcji konstruktora a wystarczy jedynie zadeklarować obiekt przechowujący stan używając słowa kluczowego **state**

    state = {
      name: ''
    }


Przykład


    import React, {Component} from "react";
    import ReactDOM from "react-dom";

    class Clock extends Component {
      render(){
        return <h2>{this.props.time.toLocaleTimeString()}</h2>;
        }
    }

    class App extends Component {
      state = {
        time: new Date()
      }
      render() {
        return (
        <>
          <h1>(zegar nie ulega zmianie)</h1>
          <Clock time={this.state.time} />
        </>
        );
      }
    }


    ReactDOM.render(
      <App/>,
      document.getElementById("app")
    );

---
### Modyfikacja stanu .setState()

Do modyfikacji stanu odbywa się poprzez odwołanie się do metody **.setState()** zwracającej obiekt - przyjmuje obiekt jak i funkcję modyfikującą poprzedni stan, zwracającą obiekt



Schemat 1 - nadpisanie stanu nową wartością


    this.setState({
      key: value
    });


Schemat 2 - modyfikacja poprzedniego stanu


    this.setState(prevState=> {
      return {
        key: prevState.value + 1;
    }});


Przykład 1


    import React, {Component} from "react";
    import ReactDOM from "react-dom";


    class Counter extends Component {
      constructor(props) {
        super(props)
        this.state = {
          counter: 0
        }
      }

      countClick = () => {
        this.setState(prevState=> {
        return {
          counter: prevState.counter + 1
        }});
        console.log(this.state.counter);
      }

      render(){
        return (
          <>
          <button onClick={this.countClick}>
          Click here
          </button>
          </>
        );
      }
    }


    ReactDOM.render(
      <Counter/>,
      document.getElementById("app")
    );


Przykład 2

    import React, {Component} from "react";
    import ReactDOM from "react-dom";


    class App extends Component {
      
      state = {
        droids: ["C3PO", "BB8"]
      }

      addUser = () => {
        const droids = [...this.state.droids];
        droids.push(this.props.droid);
        this.setState({
          droids
        });
      }


      render() {
        return (
        <>
          <h2 onClick={this.addUser}>{this.state.droids.join(",")}</h2>
        </>
        );
      }
    }


    ReactDOM.render(
      <App droid='R2D2'/>,
      document.getElementById("app")
    );



Alternatywny zapis modyfikacji stanu w powyższym przykładzie mógłby przedstawiać się w następujący (skrócony sposób)


    this.setState((prevState) => ({
      users: [...prevState.users, "Marek"]
    }));


---
### Inicjowanie stanu poprzez props

**Props** nie ulega modyfikacji w ramach komponentu stąd aby dane przekazane przez props mogły by zostać zmodyfikowane muszą znaleźć się stanie - aby tego dokonać należy odnieść się do props w ramach deklaracji state


    class Counter extends Component {
      state = {
        counter: this.props.counter,
      };
      }
      render(){
        return <h1>Twoje kliknięcia: {this.state.counter}</h1>
      }
    }
    <Counter counter={3} />

---

### Renderowanie
-
State powinien się aktualizować, react jednak sam renderuje komponenty/sam decyduje kiedy jest to najoptymalniejsze



    class ColorBox extends Component {
      state = {
        color: '#000'
      }
      
      newColor = () => {
        const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        this.setState(()=> (
          // setState musi zwrócić obiekt
          {color: randomColor}
        ))
      }

      render(){
        //redneruje styl za każdym razem stąd musi być definiowany w tym miejscu
        const style = {
          backgroundColor: this.state.color,
          width: '200px',
          height: '200px'
        }
        return <div style={style} onMouseEnter={this.newColor}></div>
      }
    }

    ReactDOM.render(
      <ColorBox/>,
      document.getElementById("app")
    )

---
### Cykle życia komponentu

Każdy komponent posiada własny i zdefiniowany cykl życia ( zamontowanie(stworzenie),aktualizacja, odmontowanie (zniszczenie)), do którego przypisane są odpowiednie metody przy pomocy, których można kontrolować zachowanie się danego komponentu


| Nazwa metody | Opis | 
|---|---|
| **constructor()** | inicjalizacja state |
| **componentDidMount()** | uruchamia się po zamontowaniu komponentu |
|**componentDidUpdate()**|uruchamia się po aktualizacji komponentu|
|**componentWillUnmount()**|uruchamia się przed odmontowaniem komponentu - w tym miejscu zwalnia się zasoby|


Przykład zastosowania [w tym przypadku componentWillUnmount() nigdy nie zostanie wywołany ponieważ pomimo tego,  że shouldComponentUpdate() zablokuje aktualizację komponentu to setInterval() będzie dalej w tle pracował]


    import React, {Component} from "react";
    import ReactDOM from "react-dom";


    class FinalCountDown extends Component {
      state = {
        seconds: 5
      }

      componentDidMount(){
        this.intervalId = setInterval(() => {
          this.setState( (prevState) => {
            return {
              seconds: prevState.seconds - 1
            }
          });
        }, 1000);
      }

      componentDidUpdate(){
        console.log('componentDidUpdate');
      }

      shouldComponentUpdate(){
        console.log('shouldComponentUpdate');
        if (this.state.seconds > 0) {return true}
        else {return false};
      }

      componentWillUnmount(){
        console.log('componentWillUnmount');
        clearInterval(this.intervalId);
      }

      render(){
        return <h1>Pozostało {this.state.seconds} sekund.</h1>;
        }
      }


    ReactDOM.render(
      <FinalCountDown/>,
      document.getElementById("app")
    );



---

Źródła:

[Stan komponentów React.js](https://typeofweb.com/state-react-js/)

[Understanding React `setState`](https://css-tricks.com/understanding-react-setstate/)


