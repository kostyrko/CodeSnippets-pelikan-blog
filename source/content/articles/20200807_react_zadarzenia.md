Title: React: zdarzenia - podstawy
Author: mkostyrko
Date: 2020-08-07 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-zdarzenia
related_posts: react-wprowadzenie, react-komponenty, react-listy

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}

Zadarzenia w React obługiwane są  w podobny sposób jak w HTML -> oznacza to, że inlinowo wpisywane są nasłuchiwacze (używając **camelCase**) do którego przekazywany jest atrybut w nawiasach klamrowych

    <button onClick={buttonClick}>Button</button>

Metoda, do której się odwołujemy poprzez atrybut powinna znaleźć swoje miejsca w ramach stworzonego komponentu lub jego rodzica (tak aby była osiągalna/możliwa do wywołania) - uwaga ta dotyczy komponentów klasowych oraz funkcyjnych

### Zdarzenia w komponentach klasowych 

W przypadku komponentów klasowych istotne jest pamiętanie o odwołaniu się do słowa kluczowego **this**, które jest dynamiczne i będzie zależne od interakcji - stąd aby odwołanie odbywało się do całości klasy/komponentu najlepiej zastosować funkcję strzałkową (która wymaga transpilacji np. poprzez użycie wtyczki Babel -> @babel/plugin-proposal-class-properties)

      class ClickTest extends Component {
        handleClick() {
          console.log("Clicked!");
        }
        render(){
          return (
            <>
            <h2>Start clicking!</h2>
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


      class ClickTest extends Component {
        handleClick= () => {
          console.log("Clicked!");
        }
        render(){
          return (
            <>
            <h2>Start clicking!</h2>
            <button onClick={this.handleClick}>
            Start!
            </button>
            </>
          );
        }
      }    

### Zdarzenia w komponentach funkcyjnych

    const ClickTest = (props) => {
      const handleClick = () => {
        console.log("Clicked!");
        console.log(props.someProp);
        console.log(props.someProp);
      }
      return (
        <>
          <h2>Start clicking!</h2>
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


