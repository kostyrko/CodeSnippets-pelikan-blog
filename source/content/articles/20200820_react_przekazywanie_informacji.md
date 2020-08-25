Title: React: przekazywanie danych pomiędzy komponentami
Author: mkostyrko
Date: 2020-08-08 10:00
Updated:
Category: reactjs
Tags: react, formularze, hooks
Slug: react-przekazywanie-danych
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany

![react](https://cdn-media-1.freecodecamp.org/images/1*Rzaf_TyulUee7xEdDs3bRw.png){: max-height="300px"}



### Przekazywanie informacji pomiędzy komponentami

W **React** przekazywanie informacji pomiędzy komponentami odbywa się w dół -> od rodzica do dziecka (przy pomocy propsu), aby móc odwrócić ten proces należy w propsie przekazać referencję do funkcji modyfikującej stan rodzica i następnie wywołać ją w komponencie dziecka przekazując do niej odpowiedni argument - w ten sposób przy pomocy komponentu dziecka oraz jego wynikowych można modyfikować stan rodzica.

W przypadku przekazywania danych pomiędzy dziećmi rodzic staje się mediatorem i to w nim deklarowny jest odraz do niego przekazywany odpowiedni stan, który odgrywa określoną rolę w innym dziecku.


Przykład przekazania informacji w komponencie funkcyjnym


    import React, {useState} from 'react';

    import ShopDroid from './ShopItem'

    const ShopForDroid = () => {
      const [droids, setDroids] = useState([])

      const addDroid = (droid) => {
        setList(prevState=>[...prevState, droid])}

      return (
        <div>
          <ShopDroid name="R2D2" onBuy={addDroid}/>
          <ShopDroid name="C3PO" onBuy={addDroid}/>
          <ShopDroid name="BB8" onBuy={addDroid}/>
          {list.length > 0 &&
            <ul>
              {droids.map((droid,i)=>
              <li key={i}>{droid}</li>)}
            </ul> }
        </div> 
      );
    }

    export default ShopForDroid;



W komponencie wykorzystującym przekazaną przez props funkcję, należy wykonać prostą walidację - sprawadzającą czy przekazana referencja jest funkcją (nie jest to wymagane, ale jest to forma zabezpieczenie (dokumentacji) na wypadek przyszłej pracy z kodem wskazuąca na funkcję)


    import React from 'react';

    const ShopDroid = ({name, onBuy}) => {
      const handleClick = () => {
        if(typeof addDroid === 'function') {
          onBuy(title);
        }
      }
      
      return (
        <div>
          <h1>{name}</h1>
          <button onClick={handleClick}>I choose this droid</button>
        </div>
      );
    }

    export default ShopDroid;
    

----

Przykład przekazania informacji w komponencie klasowym



    import React from 'react';

    class App extends React.Component {
      constructor(props) {
        super(props)
        this.state ={
          droids: []
        }
      }

      addDroid = (droid) ={
        this.setState(prevState=>[...prevState, droid])
      }

      render(){
        <div>
          <PickDroid name="R2D2" onPick={this.addDroid}/>
          <PickDroid name="C3PO" onPick={this.addDroid}/>
          <PickDroid name="BB8" onPick={this.addDroid}/>
          {list.length > 0 &&
            <ul>
              {this.state.droids.map((droid,i)=>
              <li key={i}>{droid}</li>)}
            </ul> }
        </div>
      }
    }


    import React from 'react';

    class PickDroid extends React.Component {
      const handleClick = () => {
        if(typeof addDroid === 'function') {
          this.props.onBuy(title);
        }
      }


      render(){
        <div>
          <h1>{this.props.name}</h1>
          <button onClick={this.handleClick}>I choose this droid</button>
        </div>
      }
    }


---

Źródła:

[Passing Data Between React Components](https://medium.com/@ruthmpardee/passing-data-between-react-components-103ad82ebd17)

[Passing data between different component levels in Reactjs](https://medium.com/@nipunadilhara/passing-data-between-different-components-using-react-c8e27319ee69)
