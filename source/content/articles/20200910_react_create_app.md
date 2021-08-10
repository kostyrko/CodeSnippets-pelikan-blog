Title: React: create APP
Author: mkostyrko
Date: 2020-09-10 10:00
Updated:
Category: reactjs
Tags: react, hooks, props
Slug: react-cra
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://create-react-app.dev/img/logo.svg)

Przy pomocy Create React APP oraz jednej komendy tworzymy repopozytorium z szkielet aplikacji, instalacją zależności oraz **inicjalizujemy git**


    npx create-react-app <nazwa-aplikacji/projektu>


Jeśli chcemy wypushować do GitHuba to odwiedzamy własne konto tworzymy nowe repo nadajemy mu nazwę (licencję, readme i inne informacje pomijamy) następnie kopiujemy link do wypuszowania (wypchnięcia na zdalne repo)

  git remote add origin https://github.com/kostyrko/<nazwa-repopozytorium>

Sprawdzam wersję repo

    git remote -v

A następnie wypycham na zdalne repozytorium

    git push -u origin master

Aplikacja będzie dostępna na localhost:8000 po wpisaniu komendy 

    npm start

Uruchomienie się serwera jest zdefiniowane w pliku package.json -> wystarczy w terminalu wpisać `npm start`


    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject"
      }


`npm build` - przygotowuje projekt/pliki do umieszczenia na serwerze

---

### Parę przydatnych narzędzi

Instalacja **Sass** (bezpośrednio wczytanie do pliku App.js) // css plik tworzy się dopiero przy buildzie 

    npm install node-sass --save


Instalacja **React-router**

    npm install react-router-dom


---

Źródła:

[Create React App](https://create-react-app.dev/)

