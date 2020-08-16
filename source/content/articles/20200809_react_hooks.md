Title: React: Haki (hooks) na Reacta 
Author: mkostyrko
Date: 2020-08-08 10:00
Updated:
Category: reactjs
Tags: react, formularze, hooks
Slug: react-hooks
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany

![react](https://teamquest.pl/img/static/blog/reactjs.jpeg){: max-height="300px"}

## Haki/Przyczepienia (hooks)

*Hooki* pozwalają na tworzenie stanów oraz cykli życia w komponentach funkcyjnych
Muszą być zadeklarowane w określonej kolejności, na górze (nie mogą znaleźć się w pętlach, ifach etc.). Mogą być używane jedynie w komponentach funkcyjnych!

Każdy *hook* zaczyna się od **use** np **useState** **useEffect**

Hooki importowane są na początku podobnie jak Component w przypadku klas.

    import React, {useState} from 'react';

**useState** - zwraca tablicę elementów (parę) - i przy pomocy destrukturyzacji można sie wyciągnąć do zmiennych

    const [counter, setCounter] = useState(0)
    const[zmiana do odczytu stanu, funkcja do zapisu stanu] = useState(0)
    

setState() z klasowego podejścia zmieniony jest na **setWybranaNazwaFunkcjiModyfikatora()** np. setCounter()

slajd 15/20
const App = () => {
  const[counter, SetCounter] = useState(0)
  const increment = () => (setCounter(prevCounter)=> prevCounter +1)
  return <h1 onClick={increment}>{counter}</h1>
}

**Istotna konwencja** zapisu nazw parami np. num, setNum

---

**useEffect** wykonywanie efektów ubocznych w komponentach funkcyjnych
Zmiana tytułu jest efektem (zmiana zewnętrzne stanu po za komponentami)

// uruchamia się przy każdej aktualizacji/renderowaniu (analogia w klasach componentDidMount/componentDidUpdate)
useEffect(() => {
  console.log('Komponent zamondowany')
})


// uruchamia się tylko raz ponieważ w arg. brak info o tym by się uruchamiało
useEffect(() => {
  console.log('Komponent zamondowany')
  const interval = setInterval(() => {
    setCounter(prevState [............])
  },1000)
},[]) // info o aktualizacji/powody do aktualizacji - jeśli puste to tylko 1 raz się uruchomi

// uruchamia się za każdym razem jak counter ulegnie zmianie
useEffect(() => {
  document.title = `Clicked:${counter}`
},[counter]) // kiedy nasłuchiwać na zmianę? - jak counter ulegnie zmianie

// uruchamia się za każdym razem jak counter ulegnie zmianie
useEffect(() => {
  document.title = `Clicked:${counter}`
},[counter]) // kiedy nasłuchiwać na zmianę? - jak counter ulegnie zmianie



useEffect(() => {
  const Interval = setInterval(
    [......]
  )
  return () => { // czyszczenie interwału/pamięci
    clearInterval(interval)  // wywoła się kiedy komponent zniknie
  }
},[counter]) // kiedy nasłuchiwać na zmianę? - jak counter ulegnie zmianie

---

Źródła:

[React Hooks — wprowadzenie i motywacja](https://typeofweb.com/react-hooks-wprowadzenie-i-motywacja/)

[React Hooks: useState, czyli stan w komponentach funkcyjnych](https://typeofweb.com/react-hooks-usestate-czyli-stan-w-komponentach-funkcyjnych/)


