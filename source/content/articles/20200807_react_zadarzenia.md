Title: React: zdarzenia - podstawy
Author: mkostyrko
Date: 2020-08-07 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-zdarzenia
related_posts: react-wprowadzenie, react-komponenty, react-listy

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}

Zdarzenia w React obsługiwane są  w podobny sposób jak w HTML -> oznacza to, że inlinowo wpisywane są nasłuchiwacze (używając **camelCase**) do którego przekazywany jest atrybut w nawiasach klamrowych -> przekazywanie funkcji jako props

    <button onClick={buttonClick}>Button</button>

Metoda, do której się odwołujemy poprzez atrybut powinna znaleźć swoje miejsca w ramach stworzonego komponentu lub jego rodzica (tak aby była osiągalna/możliwa do wywołania) - uwaga ta dotyczy komponentów klasowych oraz funkcyjnych

Wydajniejszym rozwiązaniem jest jednak tworzenie funkcji po za komponenetem, ale w ramach fuunkcji/klasy- wtedy gdy renderowany jest komponent wielokrotnie to funkcja nie musi być tworzona na nowo (koszt wydajnościowy)

### Zdarzenia w komponentach klasowych 

W przypadku komponentów klasowych istotne jest pamiętanie o odwołaniu się do słowa kluczowego **this**, które jest dynamiczne i będzie zależne od interakcji - stąd aby odwołanie odbywało się do całości klasy/komponentu najlepiej zastosować funkcję strzałkową (wiecej na ten temat poniżej)


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

**Konfiguracja @babel/plugin-proposal-class-properties** w .babelrc

    {
      "presets": ["@babel/preset-env", "@babel/preset-react"],
      "plugins": [
        ["@babel/plugin-proposal-class-properties", { "loose": true }]
      ]
    }


Wykorzystując funkcję strzałkową


Funkcja strzałkowa ma **this** ze scopa zewnętrznego/**this** nie ulega zmianie


      class Droid extends Component {
        greetDroid= () => {
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

### Zdarzenia w komponentach funkcyjnych

    const Droid = (props) => {
      const greetDroid = () => {
        console.log("Hi R2D2!");
        console.log(props.someProp);
      }
      return (
        <>
          <h2>Greet Droid by clicking below!</h2>
          <button onClick={handleClick}>
            Start!
          </button>
        </>
      );
    }

### Nazwy najczęściej stosowanych wydarzeń

**onClick**
**onDoubleClick**
**onMouseEnter**
**onMouseLeave**

**onKeyDown**
**onKeyPress**
**onKeyUp**

**onSubmit**
**onChange**

**onFocus**
**onBlur**
**onLoad**

### Zatrzymanie domyślnej akcji

Zatrzymanie domyślnej akcji stosuje się poprzez odwołanie się do eventu


    <a href="#" onClick={clickLink}>Link</a>

    function clickLink(e){
      e.preventDefault();
    }




---

Źródła:

[Interakcja z komponentami React.js](https://typeofweb.com/interakcja-komponentami-react-js/)


