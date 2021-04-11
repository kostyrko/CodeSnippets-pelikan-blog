Title: React: warunkowe renderowanie
Author: mkostyrko
Date: 2020-08-26 10:00
Updated:
Category: reactjs
Tags: react, formularze, hooks
Slug: react-warunkowe-renderowanie
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany

![react](https://daqxzxzy8xq3u.cloudfront.net/wp-content/uploads/2019/06/29192442/react-conditional-types.jpg)


Warunkowe renderowanie pozwala na zmianie zachowania się komponentu w zależności od informacji zawartych w stanie komponentu lub w propsie. Jest parę prostych zasad, o których warto pamiętać w tym kontekście.


W zależności od złożoności sytuacji, w której chcemy wykorzystać warunkowe renderowanie możemy:
  
  1) wykorzystać operator trójargumentowy w formie in-linowej walidacji
  2) zapisać element do zmiennej i ją modyfikować a następnie przekazywać ją do JSX 
  3) zmieniać treść komponentu, który jest zwracany

### 1) Inline - operator trójargumentowy + null

Ta opcja sprawdza się najlepiej w przypadku pojedynczych zmiennych lub gdy treść danego elementu jest krótka lub jeśli zwracamy dany element lub w jego miejsce nic nie jest zwracane jeśli walidacji przechodzi negatywnie.


**:::** Istotne jest to aby pamiętać, że jeśli chcemy korzystać z warunków w ramach JSX musi być to wówczas przy pomocy operatora trójargumentowego **:::**

    // jeśli droids !== false nie renderuj tego elementu
    [...]
    return (
        {droids=== false ? <h2> Wybierze klasę droidów do wyświetlenia</h2> : null}
      )
    [...]


Warunków może być więcej - wówczas można zastosować and **&&** lub or **||**


    [...]
    return (
        {droids=== false || droids.length < 1  ? <h2> Wybierze klasę droidów do wyświetlenia</h2> : null}
      )
    [...]

### 2) Zmiana zmiennej

W zmiennej przechowywany jest element, na którego treść wpływa stan lub props


    [...]
    let menu
    if(droids === false) {
      info = <h2> Wybierze klasę droidów do wyświetlenia</h2>
    } else {
      info = <h2>Korzystając z powyższego menu możesz wyświetlić równiez inne klasy droidów</h2>
    }

    return (
      <>
        {info}
        [....]
      </>
    )


### 3) Zmiana treści zwracanego komponentu

Treść zwracanego komponentu jest zależna od stanu lub propsu

Przykład (element funkcyjny)


    [...]

      // zapisywanie elementu do zmiennej
      const menu = (<select 
        value={select} onChange={e => setSelect(e.target.value)}>
          <option value="">Wybierz klasę droidów</option>
          {droids.map((option,i)=><option key={i} value={option}>{option}</option>)}
        </select>)

      // warunek (droids zawiera wybór i na początek jest ustawiony jak false)
      if(droids === false) {
          return (
            menu
          )
        }

      // w momencie gdy dojdzie do wyboru danej klasy droidów to wówczas wyświetl menu + ich listę
      return (
        <>
        {menu}
        <ul>
          {droids.map(({id, droid, specs})=> <li key={id}>
          <h3>{name}</h3>
          <time>{specs}</time>
          </li>)}
        </ul>
        </>
      );



---

Źródła:

[4 React conditional rendering methods with props and state](https://linguinecode.com/post/4-techniques-conditional-render-react-props-state)
