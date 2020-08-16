Title: React: (zjednoczne) Stany React'a
Author: mkostyrko
Date: 2020-08-08 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-stany
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}

## Stateful components (komponenty ze stanami)

Stan (ang. state) jest miejscem przechowywania aktualnego stanu (wewnętrznego) komponentu Reacta - jest wykorzystywany gdy komponent wymaga aktualizacji (np. licznik, godzina, ukrywanie/pokazywanie części komponentu) -> Props/Informacje przekazywane do komponentu nie ulegają zmianie w ramach niego (props przekazuje informacje z góry na dół - od rodzica do dziecka).

State - przechowuje inf. o własnym stanie kompontentu
- może być modyfikowany (analogia - zmienne wewnątrz funkcji)

---

## Komponenty klasowe

### Tworzenie stanu

W przypadku komonentów klasowych należy odwołać się do funkcji konstruktora oraz konstruktora rodzica. **State** jest słowem kluczowym i powinien być obiektem.

    constructor(props) {
      super(props)
    }


    constructor(props) {
      super(props)
      this.state = {
        name: ''
      }
    }


### Automatyczny Inicjalizator stanu
Wymaga wykorzystani wtyczki @babel/plugin-proposal-class-properties

Nie wymaga odwołania do funkcji konstruktora


    state = {
      name: ''
    }

### Modyfikacja stanu
Do modyfikacji stanu należy używać metody .setState() nigdy w sposób bezpośredni
  
Schemat


    this.setState({
      key: value
    });


Przykładowe zastosowanie

  [...]
  state = {
    counter: 0,
  }
  handleClick = () => {}
    this.setState(prevState=> {
    return {
      counter:prevState.counter + 1;
    }});
  }
  
  [...]

// zmodyfikować poniższe _>

  class Clock extends Component {
    render(){
      return <strong>{this.props.time.toLocaleTimeString()}</strong>;
      }
  }

  class App extends Component {
    state = {
      time: new Date()
    }
    render() {
      return (
      <>
        <h1>Czas na świecie</h1>
        <Clock time={this.state.time} />
      </>
      );
    }
  }

Modyfikacja statu przekazanego jako **props** odbywa się poprzez klonowanie w state a następnie zmianę, tzn dalej pracujemy na state  -> stąd można np. wykorzystać spread do sklonowania tablicy, obiektu.

    // users tj props stąd
    const users = [...this.state.users];
    users.push("Mike");
    this.setState({
      users
    });


Alternatywny zapis


    this.setState((prevState) => ({
      users: [...prevState.users, "Marek"]
    }));


Stan jest czymś lokalnym, stąd jeden element będzie miał inny stan od innego.


<!-- Przykład 


    class Counter extends Component {
      state = {
        counter: this.props.counter,
      };
      }
      render(){
        return <h1>Twoje kliknięcia: {this.state.counter}</h1>
      }
    }
    <Counter counter={3} /> -->



### Asynchroniczność
State powinien się aktualizować, react jednak sam renderuje komponenty/sam decyduje kiedy jest to najoptymalniejsze -> stąd należy wykorzystywać funkcje po sobie następujące



    class MagicBox extends Component {
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
        return (
          <>
            <h1>r2d2</h1>
            <div style={style} onMouseEnter={this.newColor}></div>
          </>
        )
      }
    }

    export default MagicBox

---
Żywotność



---

Przykładowe zastosowanie

<!-- React/1_Zadania/Dzien_1/3_Metody_cyklu_zycia -->
Zadanie 4
Stwórz komponent Clock, który przechowuje w state aktualną datę.



---

Źródła:

[Stan komponentów React.js](https://typeofweb.com/state-react-js/)


