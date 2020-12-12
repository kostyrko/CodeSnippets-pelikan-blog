daTitle: React: modułowy CSS (CSS Modules)
Author: mkostyrko
Date: 2020-12-05 10:00
Updated:
Category: react
Tags: react, css, radium, styled components, styled-components, css modules
Slug: react-css-modules
related_posts: react-radium-styled-components

---

![css-modules](https://raw.githubusercontent.com/css-modules/logos/master/css-modules-logo.png)


Kolejnym sposobem na indywidualne stylowanie komponentów lub jego elementów w React są [CSS Modules](https://github.com/css-modules/css-modules), który oparty jest na rozgraniczeniu warstwy CSS do osobnego pliku, następnie zaimportowania go do pliku zawierającego komponent i wykorzystywania tego importu (obiektu) w oparciu o przypisane do niego style, traktowane jako moduły.

W takim ujęciu style CSS są zintegrowane z komponentami,  jednak ich logika przechowywana jest w osobnych plikach.


### Instalacja i Konfiguracja środowiska

**react-scripts < 2.0** - package.json

**1** - `npm run eject`

**2** - pojawi się folder **config** -> pliki **webpack.config.dev.js/webpack.config.prod.js** -> dodanie 2 lini kodu

    {
      test: /\.css$/,
      use: [
        require.resolve('style-loader),
        {
          loader: require.resolve('style-loader),
          options: {
            importLoaders: 1,
            modules: true, // ! dodana linia
            localIdentName: '[name]__[local]__[hash:base64:5]' // ! dodana linia
          },
        },
      {
    [...]

**3** - `npm start`

Dla **react-scripts > 2.0** powyższa konfiguracja nie jest potrzebna, różnica polega jednak na tym że nazwa pliku przechowującego deklaracje css powinna zawierać słowo `module` np. `App.module.css`, oznacza to również i import jest innych tzn. powinien i powinien zawierać słowo `module` np. `import classes from './App.module.css';`

### Użytkowanie

Style można przechowywać w plikach typu CSS o tej samej nazwie co komponent, wygenerowana klasa będzie miała unikalną nazwę, stąd nawet jeśli dla wielu komponentów będziemy mieli klasę np. Button w końcowym wyniku będzie ona przetworzona na inną unikalną.

App.css / lub App.module.css (pisanie klasy z wykorzystaniem dużej litery)


    .Button {
      background-color: yellow;
    }

    .Button:hover: {
      background-color: blue;
    }

    .Button.Red {
      background-color: red;
    }

    .Button.Red:hover {
      background-color: pink;
    }

    .App button { // każdy button w komponencie App
      color: white;
    }

    @media (min-width: 500px): {
      .Button {
        width: 450px;
      }
    }

App.js (nazwa **classes** nie jest narzucona może się tu znaleźć dowolny wyraz służący jako identyfikator)

    import classes from './App.css';
    // import classes from './App.module.css'; dla react-scripts > 2.0 gdzie plik z css powinien być -> App.module.css

    class App extends Component {
      [...]
      render() {
        <Button className={classes.Button} onClick={this.handleClick}>
              Zatwierdź
        </Button>
      }
    }

Dynamiczne stylowanie klasą z wykorzystaniem `.join(' ')`

    import classes from './App.css';
    // import classes from './App.module.css';


    class App extends Component {
      [...]
      render() {
        let btnClass = [classes.Button]

        if ([...] // warunek
          btnClass.push(classes.Red) // => button.Button.Red/<button class="Button Red"></button>
        }

        return (
          <Button className={btnClass.join(' ')} onClick={this.handleClick}>
              Zatwierdź
          </Button>
        )
      }
    }


---


Źródła:

[nafrontendzie.pl -> CSS Modules - kolejny sposób na style w React](https://www.nafrontendzie.pl/css-modules-kolejny-sposob-style-react)


