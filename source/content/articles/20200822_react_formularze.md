Title: React: formularze
Author: mkostyrko
Date: 2020-08-25 10:00
Updated:
Category: reactjs
Tags: react, formularze
Slug: react-formularze
related_posts: react-wprowadzenie, react-komponenty, react-listy

![react](https://vegibit.com/wp-content/uploads/2019/03/A-Simple-Reactjs-Form-Example.png){: max-height="300px"}

W kontekście Reacta można stosować dwa rodzaje formularzy - tzw. *kontorolowane* i *niekontorlowane*

Formularze *niekontorlowane* to są te, których logika nie jest sterowana przy pomocy JS/Reacta innymi słowy, których dane nie są przechwytywane przez stworzone komponenty aplikacji -> przeciwieństwem tego podejścia są **formularze kontrolowane**


### Stany ponad wszystko -> stan jako “wyłączne źródło prawdy”

Różnego rodzaju elementy formularzy takie jak `<input>` `<textarea>` `<select>` w HTML posiadają własny stan, który jest aktualizowany na podstawie informacji wpisywanych przez użytkownika w **recatowych formularzach kontrolowanych** ten stan jest przechwytywany i skorelowany ze stanem danego komponentu np. poprzez metodę setState lub inną przypisaną do zmiany stanu komponentu w przypadku komponentów funkcyjnych (stan może być zapisany jako obiekt i zbierać informację z wielu formularzy lub każdy z nich może mieć osobny stan).


Prosty przykład gdzie 1 funkcja obsługuje jeden element formularza


    class NameForm extends React.Component {
      constructor(props) {
        super(props);
        this.state = {value: ''};
      }

      handleChange = (event) => {    
        this.setState({value: event.target.value});
        console.log(this.state.value) // wartość stanu jest stale aktualizowana
      }

      render() {
        return (
          <form> 
            <input type="text" value={this.state.value} onChange={this.handleChange}/>
          </form>
        );
      }
    }


Przykład gdzie jedna funkcja obsługuje wiele elementów formularza


    class NameForm extends React.Component {
      constructor(props) {
        super(props);
        this.state = {
          name: '',
          surname: '';
          };
      }

      // funkcja wykorzystująca event i przypisująca dane do konkretnego elementu stanu o tej samej nazwie gdzie name === jak element, do którego wartość ma być przypisana
      handleChange = (event) => {    
        this.setState({
          [e.target.name]: event.target.value
        });
      }

      // funkcja zajmująca się przesłaniem danych
      handleSubmit(event) {
        alert('Podano następujące imię: ' + this.state.value);
        event.preventDefault();
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
            <input type="text" name='name' value={this.state.name} onChange={this.handleChange}/>
            <input type="text" name='surname' value={this.state.surname} onChange={this.handleChange}/>
            <input type="submit" value="Send"/>
          <form>
          
        );
      }
    }


W przypadku komponentów funkcyjnych możemy daną funkcję odpowiedzialną za zmianę stanu komponentu wpisać inlinowo


    const Form = () => {
      const [name, setName] = useState("");

    return (
      <form>
        <input type="text" value={name} onChange={e => setName(e.target.value)}/>
      </form>
      );
    };


W przypadku stworzenia jednego stanu dla wielu elementów formularza należy pamiętać o tym, że będzie musiał być on w całości przywołany - można do tego wkorzystać operatora rozpraszającego (destrukturyzacji)

const Form = () => {
      const [form, setForm] = useState({
        name: '',
        surname: ''
      });

    const handleChange = (e) => {
      const {name, value} = e.target; // destrukturyzacja obiektu e.target na imię i wartość
      setForm(prevState => { // wykorzystanie poprzedniego stanu do jego modyfikacji
        return {    // zwrócenie obiektu
          ...prevState,
          [name]: value // wprowadzenie nowej wartości
          }
      });
    };

    return (
      <form>
        <input type="text" name='name' value={form.name} onChange={handleChange}/>
        <input type="text" name='surname' value={form.surname} onChange={handleChange}/>
      </form>
      );
    };


Custom hook dla formularza

Przykładowe użycie wygląda w następujący sposóbu
W komponencie wykorzystującym custom hook przy pomocy destrukturyzacji należy go zaimportować, użyć a następnie wyspredować lub wypisać


    // useInput.js
    import {useState} from "react";
    export default (valueOnStart) => {
      const [value, setValue] = useState(valueOnStart);
      
      return [
        value, // zwraca nazwę stanu i jest odpowiednikiem [name]: value 
        {   // tablica
          value,  // stan pola
          onChange: e => { // gdy wykryje zmianę aktualizuje stan
            setValue(e.target.value);
          }
        }
      ]
    };

    import React from "react";
    import useInput from "./hooks/useInput";

    const Form = () => {
      const [name, connectName] = useInput("");
      const [age, connectSurname] = useInput("");
      return (
        <form>
          <input type="text" {...connectName}/>  / destrukturyzacja zwracanego obiektu przez custom hooka, który jest tablicą {value, onChange: e=>{setValue(e.target.value)}}
          <input type="number" {...connectSurname}/>
        </form>
        );
    };



---

Więcej informacji na temat forms:

[formularze - React docs](https://pl.reactjs.org/docs/forms.html)

[A Simple React.js Form Example](https://vegibit.com/a-simple-react-js-form-example/)

[React form validation library built under 5kB](https://medium.com/@bruce1049/form-validation-with-hook-in-3kb-c5414edf7d64)

[GitHub: react-hook-form](https://github.com/react-hook-form/react-hook-form)

[YT- The BEST Way To Create Forms In React - React Hook Form Tutorial - How To Create Forms In React](https://www.youtube.com/watch?v=bU_eq8qyjic)
