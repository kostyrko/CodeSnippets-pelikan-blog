Title: React: kompozycja
Author: mkostyrko
Date: 2020-08-30 10:00
Updated:
Category: reactjs
Tags: react, hooks, props, props-drilling, kompozycja
Slug: react-kompozycja
related_posts: react-kontekst, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react-kompozycja](https://res.cloudinary.com/practicaldev/image/fetch/s--uhp38MJ0--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/1cjigsdjmgz5j8lohlch.png)


`props.children` pozwala nam na tworzenie komponentów otwartych na uzupełniania nowym kodem, wystarczy wykorzystać {props.children} w ramach komponentu aby wskazać, w którym miejscu istnieje możliwość uzupełnienia/wstawienia kodu

Komponent otwarty na ew. rozszerzenia o nową treść

    function TestComposition(props) {
      let {children} = props;
      return (<div>
          <h1>Test Kompozycji</h1>
          {children}
          <h2>Konice testu kompozycji</h2>
        </div>
        )
    }


    function App() {
      return (
        <TestComposition>
          <h3>Element będący zagnieżdżoną treścią</h3>
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Culpa, eum!</p>
        </TestComposition>
      )
    }


    ReactDOM.render(
      <App/>,
      document.getElementById("app")
    );



W efekcie tego powstanie

    <div>

      <h1>Test Kompozycji</h1>

      <h3>Element będący zagnieżdżoną treścią</h3>

      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Culpa, eum!</p>

      <h2>Konice testu kompozycji</h2>

    </div>


`props.children` może wyrenderować inny komponent przyjęty w propsie.

Powyższy przykład, może wyglądać również w poniższy sposób


    function TestComposition(props) {
      let {children} = props;
      return (<div>
          <h1>Test Kompozycji</h1>
          {children}
          <h2>Konice testu kompozycji</h2>
        </div>
        )
    }

    function ChildComponent() {
      return (
        <h3>Element będący zagnieżdżonym dzieckiem</h3>
      )
    }

    function App() {
      return (
        <TestComposition children={<ChildComponent/>}/>
      )
    }


    ReactDOM.render(
      <App/>,
      document.getElementById("app")
    );

---

A co jeśli zależy nam na tym aby dany komponent był w stanie przyjąć wiele innych komponentów lub inaczej rzecz ujmując mieć możliwość wypełnienia wielu luk. W tym przypadku należy zastosować odrębne nazewnictwo dla każdego fragmentu/luki, który ma być uzupełniony a następnie przekazać go w odpowiedni sposób w props.


    function TestComposition(props) {
      let {child1, child2} = props;
      return (<div>
          <h1>Test Kompozycji</h1>
          {child1}
          {child2}
          <h2>Konice testu kompozycji</h2>
        </div>
        )
    }

    function ChildComponent({text}) {
      return (
        <h3>Element będący zagnieżdżonym {text}</h3>
      )
    }

    function App() {
      return (
        <TestComposition child1={<ChildComponent text='dzieckiem-1'/>} child2={<ChildComponent text='dzieckiem-2'/>}/>
      )
    }


    ReactDOM.render(
      <App/>,
      document.getElementById("app")
    );

W efekcie tego powstanie


    <div>
      <h1>Test Kompozycji</h1>

      <h3>Element będący zagnieżdżonym dzieckiem-1</h3>

      <h3>Element będący zagnieżdżonym dzieckiem-2</h3>

      <h2>Konice testu kompozycji</h2>

    </div>



### Ominięcie prop-drilling wykorzystując kompozycję oraz props.children

Przekazywanie propsów do elementu liściowego z pominięciem pośredników (lub tzw. prop-drilling -> gdzie dane w postaci propsów są przekazywane przez komponenty które, z nich faktycznie nie korzystają) może odbyć się poprzez wykorzystanie props.children. Wymaga to jednak *otwartości* poprzednich komponentów na możliwość (włączenia) wywołania w nich dzeci.



    function TestComposition({children,i}) {
      
      return (
        <div className='testComposition' key={i}>
          <h2>Beginning o parent component</h2>
          {children}
          <h2>End of parent component</h2>
          <p>--------------------</p>
        </div>
        )
    }

    function ChildComponent({children}) {
      return (
        <div className='childComponent'>
          <h3>Beginning o child component</h3>
          {children}
          <h3>End of child component</h3>
        </div>
      )
    }

    function GrandChild({text}) {
      return (
        <h3 className='grandChild'>{text}</h3>
      )
    }

    function App({grandChildren}) {
      return (
        grandChildren.map((elem,i)=>
          <TestComposition id={i}>
            <ChildComponent>
              <GrandChild text={elem}/>
            </ChildComponent>
          </TestComposition>  
        )
      )
    }


    ReactDOM.render(
      <App grandChildren = {['Grand Child 1', 'Grand Child 2', 'Grand Child 3']}/>,
      document.getElementById("app")
    );

W wyniku tego powstanie:


    <div id="app">

      <div id="app"><div class="testComposition">
        <h2>Beginning o parent component</h2>
        <div class="childComponent">
          <h3>Beginning o child component</h3>
            <h3 class="grandChild">Grand Child 1</h3>
          <h3>End of child component</h3>
        </div>
        <h2>End of parent component</h2>
        <p>--------------------</p>
      </div>

      <div class="testComposition">
        <h2>Beginning o parent component</h2>
        <div class="childComponent">
          <h3>Beginning o child component</h3>
            <h3 class="grandChild">Grand Child 2</h3>
          <h3>End of child component</h3>
        </div>
        <h2>End of parent component</h2>
        <p>--------------------</p>
      </div>


      <div class="testComposition">
        <h2>Beginning o parent component</h2>
        <div class="childComponent">
          <h3>Beginning o child component</h3>
            <h3 class="grandChild">Grand Child 3</h3>
          <h3>End of child component</h3>
        </div>
        <h2>End of parent component</h2>
        <p>--------------------</p>
      </div>

    </div>



---

Źródła:

[Kompozycja vs dziedziczenie - Wzorce w React #3](https://www.youtube.com/watch?v=9n9Er-NIJ_c)

[Thinking in React: Component Composition](https://dev.to/bouhm/thinking-in-react-component-composition-fp5)

[How To Avoid Prop Drilling in React Using Component Composition](https://medium.com/javascript-in-plain-english/how-to-avoid-prop-drilling-in-react-using-component-composition-c42adfcdde1b)