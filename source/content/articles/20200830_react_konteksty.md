Title: React: kontekst
Author: mkostyrko
Date: 2020-08-30 10:00
Updated:
Category: reactjs
Tags: react, hooks, props, props-drilling, kompozycja
Slug: react-kontekst
related_posts: react-kompozycja, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://codesource.io/wp-content/uploads/2019/12/Getting-Started-with-React-Context-API-950x500.png)

### Context API

Kontekst/*Context API* pozwala komponentowi na pozyskanie danych z **kontekstu** a **nie** przez **props** poprzez tworzenie *globalnych* danych dostępnych dla całości drzewa komponentu [innymi słowy uniknięcia sytuacji, w której przekazujemy informację do wielowarstwowo-zagnieżdżonego komponentu przez wiele pośredniczących komponentów (tzn. przez każdy poziom struktury)].
Na jakiego typu danych może nam zależeć aby były dostępne globalnie? Np. preferencje językowe, stylistyczne (np. kolorystyka) lub informacja o zalogowaniu się użytkownika.

Context API ma również swoje limity - z dokumentacji Reacta możemy dowiedzieć się, że utrudnia on "wielokrotne używanie komponentów zależnych" (zalecane rozwiązanie jest poprzez skorzystanie z możliwości kompozycji i props.children)

![react context api](https://www.carlrippon.com/static/0d1f722d0fe4c2bc4c3d71595dbe67dd/799d3/prop-drilling-v-context.png)

### Praca z kontekstem

W pierwszej kolejności należy stworzyć obiekt kontekstowy w który przekazujemy zdefiniowany kontekst/dane do przekazania 
    
    const MyContext = React.createContext(defaultValue);

Komponent *providera* przetrzymuje wartość jaką "konsumencki" komponent będzie wykorzystywał

    <MyContext.Provider value={/* jakaś wartość */}>

Wskazanie *konsumenta* odbywa się poprzez opakowanie go w kompontent wyżeszgo tympanus

    <MyContext.Consumer>


Następnie w komponencie odbierającym/konsumenckim w odpowiedni sposób należy przypisać do niego kontekst wykorzystując właściwość `contextType` (komponent klasowy) lub `consumer` (komponent funkcyjny). Przypisanie odbywa się po za blokiem klasy komponentu oraz odwołując się do właściwości *consumer* komponentu funkcyjnego.

W przypadku komponentów funkcyjnych można również skorzystać z hooka `useContext` i tą opcję uważam za najprostszą

([źródło poniższych przykładów](https://reactjs.org/docs/context.html))

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
### Przykład zastosowania Context API - jednostronne

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

    // komponent będący konsumentem
    function ThemedButton() {
      const theme = useContext(ThemeContext);
      return (
        <button style={{ background: theme.background, color: theme.foreground }}>
          I am styled by theme context!
        </button>
      );
    }


---

### Dynamiczny kontekst

Aby kontekst edytować, podobnie jak w przypadku dziedziczenia oraz przekazywania właściwości przy pomocy drylowania również i tutaj należy stworzyć funkcję/metodę, która pozwoli na jego edycję a następnie należy ją przekazać lub rozpakować (w zależności od wybranego podejścia zastosowania) w komponencie będącym providerem/dostawcą.

Przykładowo 

    // theme-context.js (plik przechowujący kontekst)

      const themes = {
        light: {
          foreground: '#000000',
          background: '#eeeeee',
        },
        dark: {
          foreground: '#ffffff',
          background: '#222222',
        },
      };

    export const ThemeContext = React.createContext({
      theme: themes.dark,  
      toggleTheme: () => {},})

    =================================

    // theme-toggler-button.js (tu wykorzystywany jest kontekst)
      <ThemeContext.Consumer>
      {({theme, toggleTheme}) => (        
        <button
          onClick={toggleTheme}
          style={{backgroundColor: theme.background}}>
          Toggle Theme
        </button>
      )}
    </ThemeContext.Consumer>


    =================
    // app.js (aplikacja)

    import {ThemeContext, themes} from './theme-context';
    import ThemeTogglerButton from './theme-toggler-button';

    class App extends React.Component {
      constructor(props) {
        super(props);

        this.toggleTheme = () => {
          this.setState(state => ({
            theme:
              state.theme === themes.dark
                ? themes.light
                : themes.dark,
          }));
        };

        // State also contains the updater function so it will    // be passed down into the context provider    this.state = {
          theme: themes.light,
          toggleTheme: this.toggleTheme,    };
      }

      render() {
        // The entire state is passed to the provider    return (
          <ThemeContext.Provider value={this.state}>        <Content />
          </ThemeContext.Provider>
        );
      }
    }

    function Content() {
      return (
        <div>
          <ThemeTogglerButton />
        </div>
      );
    }

    ReactDOM.render(<App />, document.root);

=================================

Inny przykład - wykorzystyjący hook useContext ([źródło przykładu](https://stackoverflow.com/questions/41030361/how-to-update-react-context-from-inside-a-child-component))


    // context.js
    const LanguageContext = React.createContext({
      language: "en",
      setLanguage: () => {}
    });


    //LanguageSwitcher.js Context Consumer
    const LanguageSwitcher = () => {
      const { language, setLanguage } = useContext(LanguageContext);
      return (
        <button onClick={() => setLanguage("jp")}>
          Switch Language (Current: {language})
        </button>
      );
    };

    // App.js
    const App = () => {
      const [language, setLanguage] = useState("en");
      const value = { language, setLanguage };

      return (
        <LanguageContext.Provider value={value}>
          <h2>Current Language: {language}</h2>
          <p>Click button to change to jp</p>
          <div>
            {/* Can be nested */}
            <LanguageSwitcher />
          </div>
        </LanguageContext.Provider>
      );
    };


Ten sam przykład klasowo ->


    // context.js
    const LanguageContext = React.createContext({
      language: "en",
      setLanguage: () => {}
    });

    // konsumer LanguageSwitcher.js

    class LanguageSwitcher extends Component {
      render() {
        return (
          <LanguageContext.Consumer>
            {({ language, setLanguage }) => (
              <button onClick={() => setLanguage("jp")}>
                Switch Language (Current: {language})
              </button>
            )}
          </LanguageContext.Consumer>
        );
      }
    }

    // App.js (provider)

    class App extends Component {
      setLanguage = language => {
        this.setState({ language });
      };

      state = {
        language: "en",
        setLanguage: this.setLanguage
      };

      render() {
        return (
          <LanguageContext.Provider value={this.state}>
            <h2>Current Language: {this.state.language}</h2>
            <p>Click button to change to jp</p>
            <div>
              {/* Can be nested */}
              <LanguageSwitcher />
            </div>
          </LanguageContext.Provider>
        );
      }
    }



---

Źródła:

[pl.reactjs.org - Kontekst](https://pl.reactjs.org/docs/context.html)

[Playing with the Context API in React 16.3](https://www.carlrippon.com/playing-with-the-context-api-in-react-16-3/)

[Getting Started with React Context API](https://codesource.io/getting-started-with-react-context-api/)

[React Context API: updating Context from a nested component (in functional components with Hooks and class components)](https://ramonak.io/posts/react-context-api-update-from-nested-component)

[Context API - React.js dla początkujących](https://www.youtube.com/watch?v=SpG3NUMiPwA)