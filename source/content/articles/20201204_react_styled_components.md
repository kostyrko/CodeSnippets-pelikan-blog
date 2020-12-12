Title: React: Styled Components oraz Radium
Author: mkostyrko
Date: 2020-12-04 10:00
Updated:
Category: react
Tags: react, css, radium, styled components, styled-components, css modules
Slug: react-radium-styled-components
related_posts: react-css-modules

![react-styled-components](https://www.styled-components.com/atom.png)



### Styled components

Biblioteka styled components po wyrenderowaniu nadaje własne nazwy klas, a informację przechowuje w **head** dokumentu, nie jest to zatem styl inlinowy.

**Instalacja**

      npm i --save styled-components

**1** - Import np. w App.js

    import styled from 'styled-components'

**2** - Użytkowanie odwołanie się do metod obiektu `styled` np. div, h1 etc. -> `styled.div` istotne jest to, że styl wpisuje się pomiędzy -> **``**

      const StyledDiv = styled.div`
              backgroundColor: 'yellow';
              '@media (min-width: 500px)': {
                backgroundColor: 'pink'
              }
            `

      return (
        <StyledDiv>

          [...]

        </StyledDiv>
      )

**3** - Możliwość definiowania stylu po za komponentem i wówczas deklaracje styli będą przypominały te znane bezpośrednio z CSS/SCSS a nie Reacta

    const StyledButton = styled.button`
            background-color: yellow;
            &:hover: {
              background-color: blue
            }
          `

    const App = () => {
      [...]
      render (
        <StyledButton onClick={this.handleClick}>
          Zatwierdź
        </StyledButton>
      )
    }


**4** - Dynamiczne style w zależności od tego czy warunek zawarty w deklaracji jest spełniony (true/false)

    const StyledButton = styled.button`
                      background-color: ${props=>props.alt ? 'red' : 'green'};
                      &:hover: {
                        background-color: blue
                      }
                    `

    const App = () => {
          [...]
          render (
            <StyledButton alt={this.state.droid} onClick={this.handleClick}>
              Zatwierdź
            </StyledButton>
          )
        }

---
![radium](https://sahilthakur7blog.files.wordpress.com/2018/01/og-image.jpg?w=648)

### Radium - pseudoselektory

Biblioteka, która umożliwia pseudoklas przy stylowaniu bezpośrednio w komponencie

**Instalacja**

        npm i --save radium

Użytkowanie:

**1** - import Radium

        import Radium from 'radium'

**2** - opakowanie eksportu w komponent wyższego rzędu `Radium(component)`

        export default from Radium(App)

**3** - Możliwość stosowania pseudoklas przedstawionych jako String

    const style = {
      backgroundColor: 'red',
      'hover:' {
        backgroundColor: 'blue',
      }
    }

**4** - Odwołanie się do zastosowanej stylistyki w dalszej części komponentu np. w celu nadawania dynamicznych styli

    style.backgroundColor = 'purple'
    style['hover:'] {
      backgroundColor: 'yellow'
    }

---


### Radium - media queries

**1** - import StyleRoot

      import Radium, {StyleRoot} from 'radium'

**2** - opakowanie zwracanego komponentu w komponentu StyleRoot

    return (
      <StyleRoot>
        <div className="App>

          [...]

        </div>
      </StyleRoot>
    )

**3** - definiowanie Media Query

    const style = {
      '@media (min-width: 500px)': {
        backgroundColor: 'pink'
      }
    }



---


Źródła:

[Hello Roman -> styled components](https://www.youtube.com/playlist?list=PL19053wDcT0-JONXrzsngyTS4CJI8V_QE)

[nafrontendzie.pl -> Styled Components - najlepszy sposób na style w ReactJS?](https://www.nafrontendzie.pl/styled-components-sposob-style-reactjs)

[nafrontendzie.pl -> CSS Modules - kolejny sposób na style w React](https://www.nafrontendzie.pl/css-modules-kolejny-sposob-style-react)

[Dimitry Nozhenko - 9 Ways To Implement CSS in React JS](https://medium.com/@dmitrynozhenko/9-ways-to-implement-css-in-react-js-ccea4d543aa3)
