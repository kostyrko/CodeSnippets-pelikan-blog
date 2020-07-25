Title: React: Klucz do tworzenia wielu elementów listy
Author: mkostyrko
Date: 2020-07-22 10:00
Updated:
Category: reactjs
Tags: listy, klucze, react
Slug: react-listy
related_posts: react-wprowadzenie, react-komponenty, react-formularze

![react](https://daveceddia.com/images/render-a-list.png){: max-height="300px"}


Wiele elementów można tworzyć na różne sposoby. W tym kontekście należy wspomnieć o kluczach (ang key), których przypisanie do poszczególnego elementu pozwala na wskazanie Reactowi, które z elementów są stabilne (nie uległy zmianie) - jeśli React sam znajdzie zmianę (bez stosowania klucza) uzna, że każdy kolejny element również został zmieniony usunie go a następnie ponownie wstawi. Klucze pozwalają na wskazanie,  które z elementów są tymi samymi, niezmienionymi. React poradzi sobie z brakiem kluczy lub gdy będą one losowe - jednak będzie to miało negatywny wpływ na wydajność.


### Tablice
Proste tworzenie elementów (klucz nie jest wymagany wymaga kluczy -> dopiero od dynamicznych elementów - np. zwykła list, która zmianie nie ulega nie będzie tego wymagać)

    const droids = [
      <span>C3-PO</span>,
      <span>R2-D2</span>
    ];


    <>
      {droids}
    </>


### map() i klucz

Elementom tworzonej listy przypisywane są klucze (klucz musi być unikalny w ramach rodzeństwa np. jednej listy... można do tego wykorzystać np. id, pesel etc., ew. może być to indeks z tablicy - chóć gdy tablica ulegnie zmianie może to stanowić problem)

Atrybut klucza (ang. key) przekazywany Reactowi jest użytkowany wewnętrznie stąd nie jest on widoczny po wyrenderowaniu, tak samo nie będzie on widoczny/dostępny we właściwościach (props)


    const droids = ["C3-PO", "R2-D2"];

    const list = (
      <ul>
        {
          droids.map(droid => {
            return <li key={droid}>{droid}</li>
          })
        }
      </ul>
    );


Wersja z indeksem

    const droids = ["C3-PO", "R2-D2"];

    const list = (
      <ul>
        {
          droids.map((droid, index) => {
            return <li key={index}>{droid}</li>
          })
        }
      </ul>
    );

    <ul>
      {list}
    </ul>


Funkcja

Props (właściwość) jest obiektem stąd aby dostać się do tablicy droids należy -> props.droids
Właściwość/props należy przekazać w trakcie wywoływanie komponentu

    props {droids: Array(2)}
    props.doroids (2) ["C3-PO", "R2-D2"]



    const droids = ["C3-PO", "R2-D2"];
    
    function DroidList(props) {
      const droids = props.droids;
      return (
        <ul>
          {droids.map((droid) =>
            <li key={droid}>{droid}</li>
          )}
        </ul>
      );
    }

    ReactDOM.render(
      <DroidList droids={droids} />,
      document.getElementById('root')
    );

---

Źródła:

[listy i klucze - React docs](https://pl.reactjs.org/docs/lists-and-keys.html)

[How to Display a List in React](https://daveceddia.com/display-a-list-in-react/)

