Title: React: Haki (hooks) na Reacta 
Author: mkostyrko
Date: 2020-08-08 10:00
Updated:
Category: reactjs
Tags: react, formularze, hooks
Slug: react-hooks
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany

![react](https://i.morioh.com/2934a8d84c.png){: max-height="300px"}

### Haki/Przyczepienia (hooks)

*Hooki* mogą być używane jedynie w komponentach funkcyjnych i pozwalają na przechowanie stanu pomiędzy kolejnymi wywołaniami funkcji zawartych w komponentach! Podstawowe dwa z nich pozwalają na wprowadzenie stanów (**useState**) podczas gdy inny pozwala na zarządzanie automatycznym zachowaniem się danego komponentu (**useEffect**) - kompensując brak funkcji znanych z komponentów klasowych jak *componentDidMount()*, *componentDidUpdate()* oraz *componentWillUnmount()*. 
Jednym z szybko zauważalnych efektów korzystania z komponentów funkcyjnych + *hooków* jest uproszczenie kodu.
*Hooki* nie mogą znaleźć się w pętlach, funkcjach, ifach etc. i powinny być zadeklarowane w określonej kolejności (najlepiej jak najwcześniej)

Hooki zaimportować z biblioteki React podobnie jak Component w przypadku komponentów klasowych.


    import React, {useState} from 'react';

---

### Definiowanie stanu -> useState()

**useState()** - zwraca tablicę elementów (parę) - przy pomocy destrukturyzacji można "wyciągnąć" poszczególne elementy do zmiennych (co jest przyjętą praktyką). Istotną konwencją, o której warto w tym kontekście pamiętać jest to, że pierwsza zmienna przechowuje stan natomiast kolejna powinna odwoływać się do funkcji, która ma wpływ na zmianę stanu. Nazwa 2. elementu powinna powielać nazwę tej, która przechowuje stan ale poprzedza ją słowem 'set'. **useState** przyjmuje argument określający początkową właściwość stanu

    const[stanu, funkcjaZmieniającaStan] = useState(początkowyStan)
    const [state, setstate] = useState(initialState);
    ====== przykładowo =====
    const [counter, setCounter] = useState(0)
    

Aby użyć analogii można stwierdzić, że **useState()** w funkcyjnym komponencie "zastępuje" z komponentu klasowego **konstruktor stanu** oraz **setState()** (setState() => setWybranaNazwaFunkcjiModyfikatora() np. setCounter())

Przykład


    const Counter = () => {
      const[counter, SetCounter] = useState(0)
      const increment = () => (setCounter(prevCounter=> prevCounter +1)
      return <button onClick={increment}>{counter}</button>
    }

---

### Obsługa efektów ubocznych useEffect()

**useEffect()** ma mieć wpływ na kod z poza zakresu wywoływanej funkcji lub inaczej rzecz ujmując odpowiada za wykonywanie efektów ubocznych w komponentach funkcyjnych. Hook **useEffect()** pozwala na ustawienie zależności wywoływania się konkretnej zawartej w nim funkcji oraz na zwolnienie jej zasobów - jednak nie w każdej sytuacji jest to wymagane.


    //wywoła się podczas każdorazowego renderowania komponentu

    useEffect(() => {
      console.log('Komponent zamontowany')
    })


Podstawowy schemat prezentuje się następująco. Warto zwrócić uwagę na tablicę kończącą wyrażenie (input) w to miejsce można wpisać zależności, których zmiana spowoduje wywołanie się funkcji - brak elementów oznacza, że funkcja powinna wywołać się tylko raz, podczas pierwszego renderowania elementu

    useEffect(() => {
        effect
        return () => {
          cleanup
        };
      }, [input]);


Przykład 1

    // uruchamia się tylko raz ponieważ w arg. brak info o tym by się uruchamiał ponownie
    // co 1 sekundę dodaj kropkę do stringa zawartego w stanie >>message<<
    useEffect(() => {
    const intervalId = setInterval(() => {
      setMessage((prev)=> prev+'.'); 
      }, 1000); 
      return () => { // czyszczenie interwału/pamięci
        clearInterval(intervalId)
      };
    }, []);


Przykład 2

    // uruchamia się za każdym razem jak counter ulegnie zmianie
    useEffect(() => {
      document.title = `Clicked:${counter}`
    },[counter]) // kiedy wywołać? - jak counter ulegnie zmianie



Przykład komponentu funkcyjnego korzystającego z **hooków**


import React, {useState, useEffect} from "react";
import ReactDOM from "react-dom";

const ShowInfo = ({info}) => {
  return <h1>{info}</h1>
}

    const PropsToState = ({text}) => {
      const [message, setMessage] = useState(text)
      const [click, setClick] = useState(0)

      useEffect(() => {
        const intervalId = setInterval(() => {
          setMessage((prev)=> prev+'.');
        }, 1000);
        return () => {
          clearInterval(intervalId)
        };
      }, []);

      useEffect(() => {
        document.title = `Clicked:${click}`
      },[click])

      const clicked = () => (setClick(prev=>prev+1))

      return (
        <>
          <ShowInfo info={message}/>
          <h2>Clicked {click} times</h2>
          <button onClick={clicked}>Clicke Me</button>
        </>
      )
    }

    ReactDOM.render(
      <PropsToState text='Wielokropek'/>,
      document.getElementById("app")
    );


---

Źródła:

[React Hooks — wprowadzenie i motywacja](https://typeofweb.com/react-hooks-wprowadzenie-i-motywacja/)

[React Hooks: useState, czyli stan w komponentach funkcyjnych](https://typeofweb.com/react-hooks-usestate-czyli-stan-w-komponentach-funkcyjnych/)

[Clean Up Async Requests in `useEffect` Hooks](https://dev.to/pallymore/clean-up-async-requests-in-useeffect-hooks-90h)

[[PL]React Hooks: Wstęp + useState](https://medium.com/@m.kwiecien916/pl-react-hooks-wst%C4%99p-i-usestate-44784199da22)

[Obsługa stanu z useState - React Hooks w 5 minut #1](https://www.youtube.com/watch?v=5SgtFIiIsKk)

[Czym są React Hooks?](http://www.algosmart.pl/czym-sa-react-hooks)
