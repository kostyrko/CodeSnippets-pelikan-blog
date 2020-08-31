Title: React: kontekst
Author: mkostyrko
Date: 2020-08-30 10:00
Updated:
Category: reactjs
Tags: react, hooks, props
Slug: react-kontekst
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://codesource.io/wp-content/uploads/2019/12/Getting-Started-with-React-Context-API-950x500.png)

### Context API

Kontekst/*Context API* pozwala komponentowi na pozyskanie danych z **kontekstu** a **nie** przez **props** poprzez tworzenie *globalnych* danych dostępnych dla całości drzewa komponentu [innymi słowy uniknięcia sytuacji, w której przekazujemy informację do wielowarstwowo-zagnieżdżonego komponentu przez wiele pośredniczących komponentów (tzn. przez każdy poziom struktury)].
Na jakiego typu danych może nam zależeć aby były dostępne globalnie? Np. preferencje językowe, stylistyczne (np. kolorystyka) lub informacja o zalogowaniu się użytkownika.

Context API ma również swoje limity - z dokumentacji Reacta możemy dowiedzieć się, że utrudnia on "wielokrotne używanie komponentów zależnych"

![react context api](https://www.carlrippon.com/static/0d1f722d0fe4c2bc4c3d71595dbe67dd/799d3/prop-drilling-v-context.png)

### Praca z kontekstem

W pierwszej kolejności należy stworzyć obiekt kontekstowy w który przekazujemy zdefiniowany kontekst/dane do przekazania 
    
    const MyContext = React.createContext(defaultValue);

Komponent *providera* przetrzymuje wartość jaką "konsumencki" komponent będzie wykorzystywał

    <MyContext.Provider value={/* jakaś wartość */}>

Następnie w komponencie odbierającym/konsumenckim w odpowiedni sposób należy przypisać do niego kontekst wykorzystując właściwość `contextType` (komponent klasowy) lub `consumer` (komponent funkcyjny). Przypisanie odbywa się po za blokiem klasy komponentu oraz odwołując się do właściwości *consumer* komponentu funkcyjnego.

W przypadku komponentów funkcyjnych można również skorzystać z hooka `useContext`

    ========== Komponent klasowy ===========
    // context.js
    let MyContext = React.createContext(defaultValue);
    export { MyContext }


    // exampleClass.js
    import { MyContext } from './myContext';
    
    class ExampleClass extends React.Component {
        render(){
            let value = this.context;
            // zwraca kontekst    
        }
    }
    ExampleClass.contextType = MyContext;
    // przypisanie MyContext do ExampleClass


    ========== Komponent funkcyjny ===========
    <MyContext.Consumer>
    {value => {
        return (
            // zwraca element zależny od kontekstu
        )
    }}
    </MyContext.Consumer>

    //////////// Przykładowe zastosowanie ////////////

    ....
    return (
      <div>
        <MyContext.Consumer>
          {value => {
              return (
                  // zwraca element zależny od kontekstu
              )
          }}
          </MyContext.Consumer>
      </div>
    )


---
### Przykład zastosowania Context API

Poniższy przykład za [reactjs.org - Hooks API Reference](https://reactjs.org/docs/hooks-reference.html#usecontext)

    const themes = {
      light: {
        foreground: "#000000",
        background: "#eeeeee"
      },
      dark: {
        foreground: "#ffffff",
        background: "#222222"
      }
    };

    const ThemeContext = React.createContext(themes.light);

    function App() {
      return (
        <ThemeContext.Provider value={themes.dark}>
          <Toolbar />
        </ThemeContext.Provider>
      );
    }

    function Toolbar(props) {
      return (
        <div>
          <ThemedButton />
        </div>
      );
    }

    function ThemedButton() {
      const theme = useContext(ThemeContext);
      return (
        <button style={{ background: theme.background, color: theme.foreground }}>
          I am styled by theme context!
        </button>
      );
    }



---

Źródła:

[pl.reactjs.org - Kontekst](https://pl.reactjs.org/docs/context.html)

[Playing with the Context API in React 16.3](https://www.carlrippon.com/playing-with-the-context-api-in-react-16-3/)

[Getting Started with React Context API](https://codesource.io/getting-started-with-react-context-api/)

[React Context API: updating Context from a nested component (in functional components with Hooks and class components)](https://ramonak.io/posts/react-context-api-update-from-nested-component)