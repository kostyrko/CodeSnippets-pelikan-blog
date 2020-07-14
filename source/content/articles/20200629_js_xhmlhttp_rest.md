Title: JavaScript: XMLHttpRequest i REST API
Author: mkostyrko
Date: 2020-06-29 12:00
Updated:
Category: javascript
Tags: javascript, js, ajax, rest, XMLHttpRequest, delete, get, put
Slug: js-xhr-rest
related_posts: js-asynchronicznosc-ajax, js-xhr

!![XMLHttpRequest](https://phpenthusiast.com/theme/assets/images/blog/what_is_rest_api.png?021019a){: max-height="300px"}

**REST -> Representational state transfer (pl. zmiana stanu poprzez reprezentacje)**


### Wysyłanie danych

Tym razem do prezentacji możliwości XMLHttpRequest posłużę się fake API -> [https://reqres.in/](https://reqres.in/) ("A hosted REST-API ready to respond to your AJAX requests"), które pozwala na ćwiczenie funkcjonalności REST API 

Wysyłanie danych wymaga

(1) przygotowanie danych do wysłania 

      const data = {
        firstname = "John";
        lastname  = "Snow";
      };

      const json = JSON.stringify(data);


(2) stworzenie nowego obiektu XMLHttpRequest 

      const xhr = new XMLHttpRequest();

(3) Zdefiniować połączenie za pomocą metody `open()` wykorzystując słowo kluczowe POST 

      const url = https://reqres.in/api/users';
      xhr.open("POST", url, true);

(4) ustalenie metadanych wysyłanej informacji - nagłówek (headera) będącego częścią teksty wysłanego do serwera, który jest informacją o przesyłanych danych 

      setRequestHeader(nagłówek, wartość)
    
Gdzie -> `nagłówek`: określa nazwę nagłówka, `wartość`: określa wartość nagłówka, tu również może pojawić się informacja na temat formatu kodowania

    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

(5) Ustawienie nasłuchiwania z wiadomością nastawioną na tworzenie **201** - Created (Utworzono – wysłany dokument został zapisany na serwerze)

    xhr.onload = function () {
      const users = JSON.parse(xhr.responseText);
      if (xhr.readyState == 4 && xhr.status == "201") {
        console.table(users);
      } else {
        console.error(users);
      }
    }

(6) Wysłanie żądania z przekazanymi danymi

    xhr.send(json);

Całość zapytania może prezentować się w następujący sposób:

    const url = 'https://reqres.in/api/users';

    const data = {};
    data.first_name = "John";
    data.last_name  = "Snow";
    const json = JSON.stringify(data);


    const xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
      const users = JSON.parse(xhr.responseText);
      if (xhr.readyState == 4 && xhr.status == "201") {
        console.table(users);
      } else {
        console.error(users);
      }
    }
    xhr.send(json);

---

### Edytowanie/Uaktualnianie istniejących danych

Edytowanie danych istniejących na serwerze jest zbliżone do procesu wyżej przedstawionego związanego z wysyłaniem danych -> główne różnice zwarte są w definiowaniu połączenia (należy użyć słowo kluczowe PUT oraz zdefiniować pozycję dla której dane powinny zostać zmienione), tym razem status odpowiedzi zwrotnej powinien być równy *200*

Przykładowo 

    xhr.open("PUT", url+'/12', true);

Gdzie url + 12 wyznacza konkretną część danych/obiekt zawartą na serwerze, w tym przypadku użytkownika


Zapytanie może prezentować się w następujący sposób:

    const url = https://reqres.in/api/users';

    const data = {};
    data.firstname = "Jan";
    data.lastname  = "Snieg";
    const json = JSON.stringify(data);


    const xhr = new XMLHttpRequest();
    xhr.open("PUT", url+'/12', true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
      const users = JSON.parse(xhr.responseText);
      if (xhr.readyState == 4 && xhr.status == "200") {
        console.table(users);
      } else {
        console.error(users);
      }
    }
    xhr.send(json);


---
### Usuwanie danych

Usuwanie danych jest jeszcze prostsze, ponieważ wymaga jedynie wskazanie na obiekt do usunięcia oraz  poprawnego zdefiniowania połączenia, tym razem przy pomocy słowa kluczowego DELETE. Usuwanie danych nie wymaga tworzenia nagłówka, jednak tym razem status odpowiedzi powinien być równy *204*

Przykładowo:

    function deleteUser () {
      const usrId = document.querySelector('.delete-by-id').value
      const xhr = new XMLHttpRequest();
      xhr.open("DELETE", url+`/${usrId}`, true);
      xhr.onload = function () {
        if (xhr.readyState == 4 && xhr.status == "204") {
          userInfo.innerText = `User width id: ${usrId} was deleted`
        } else {
          console.error(users);
        }
      }
      xhr.send(null);
    }



Przedstawiony wyżej kod znajduje się również tutaj na [GitHub - Gist](https://gist.github.com/kostyrko/d04ed2eb6aa9b9d9dc87d07e5f6e0c0a)





I małe podsumowanie:

![REST API CHECKLIST](https://usercontent.one/wp/www.kennethlange.com/wp-content/uploads/2020/04/customer_rest_api-624x314.png)

---

Źródła:


Duckett, Jon. Javascript and jquery: Interactive front-end web development. Wiley Publishing, 2014.

[kursjs.pl](http://kursjs.pl/kurs/ajax/xmlhttprequest.php)

[MDN-Using XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)

[The XMLHttpRequest Definitive guide](https://medium.com/@giacintocarlucci/xmlhttprquest-definitive-guide-e3a2fd7a85a4)



