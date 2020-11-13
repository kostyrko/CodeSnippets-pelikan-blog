Title: Redux: Duck + Redux-thunk
Author: mkostyrko
Date: 2020-11-08 10:00
Updated:
Category: redux
Tags: react, redux, Redux DevTools Extension, useDispatch, useSelector
Slug: redux-thunk
related_posts: react-wprowadzenie

![redux-react](https://miro.medium.com/max/700/1*uHumlKU6fado6sOF2eHVwg.jpeg)

### Istotne pojęcia

**Thunk** jest innym słowem na funkcję, która jest zwrócona przez inną funkcję.

        function wrapper_function() {
                // >> to jest "thunk" ponieważ odracza wykonanie kodu na później:
                return function thunk() {   // >> anonimowa lub nazwana
                console.log('do stuff now');
                };
        }

W Reduxie **akcje/actions** są jedynie obiektami, z kolei **reduktory/reducers** są "czyste" (nie zmieniają nic co znajduje się po za ich własnym zakresem).

Zatem aby akcja w reduxie miała być funkcyjna powinna wewnątrz wywoływać funkcję -> innymi słowy **thunk**

**Redux-thunk** jest kodem/oprogramowaniem pośredniczącym (biblioteką) - sprawdza każdą przekazywaną akcję, przechodzącą przez aplikację i jeśli ta jest funkcją, wówczas ją wywołuje. Redux przekaże do Redux-thunk dwa argumenty: `dispatch` oraz `getState` (pozyskanie stanu)


---

**Ducks** - nazwa pochodzi od ostatniej sylaby Redux  i jest propozycją konwencji strukturyzowania plików związanych ze stanem komponentów oraz Reduxem. Duck ma tworzyć pakiet reduktorowy Reduxa i zawierać takie pliki jak => {actionTypes, actions, reducer} [więcej na ten temat [Ducks: Redux Reducer Bundles](https://github.com/erikras/ducks-modular-redux)]

![duck](https://raw.githubusercontent.com/erikras/ducks-modular-redux/master/duck.jpg)

----

----

**1.** Faza projektu (App.js) - brak rozbudowanej struktury

        import './App.css';

        import {createStore, combineReducers, bindActionCreators} from 'redux'


        // ---------- Zmienne przechowujące stan wyjściowy ----------

        // wyjściowy state

        const initialDroids = {
                droidsName: 'Favorite',
                list: [
                'R2D2', 'C3PO', 'BB8'
                ]
        }

        const initialDroidClasses = {
                listName: 'working droids',
                list : [
                "Protocol droid", "Astromech droid", "Power droid", "Utility droid"
                ]
        }


        // ---------------------------- Reduktory (stan) -----------------------

        // reduktory (reducers)

        function droids(state=initialDroids, action) {
            switch (action.type) { // >> sprawdza typ akcji
                case 'RESET_DROIDS': // >> nazwa wywołania akcji (np. window.store.dispatch({type: 'RESET'}) przy założeniu że -> window.store = store) -> zwraca pustą tablicę
                    return {
                        ...state, // >> kopiowanie atrybutów, które nie mają zostać zmienione
                        list: []
                    }
                    case 'ADD_DROID': // >>nazwy akcji nie mogą się pokrywać
                        return {
                            ...state,
                            list: [...state.list, action.item]
                            // (np. window.store.dispatch({type: 'ADD', droid: 'D-O'}) przy założeniu że -> window.store = store) - spowoduje dodanie nowego droida
                        }
                    default:
                        return state
                    }
        }

        function droidClasses(state=initialDroidClasses, action) {
                switch (action.type) {
                case 'RESET_DROID_CLASS':
                    return {
                        ...state,
                        list: []
                    }
                case 'ADD_DROID_CLASS':
                    return {
                        ...state,
                        list: [...state.list, action.item]
                    }
                default:
                        return state
                }
        }

        // >> łącznie reduktorów w obiekt mapujący akcje reduktorów
        const allReducers = combineReducers({droids, droidClasses}) //  obiekt mapujący akcje stora na reducer

        // ---------------------------- Store -----------------------

        // >>store + REDUX_DEVTOOLS_EXTENSION

        const store = createStore(allReducers, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())


        // ---------------------------- Kreator akcji -----------------------

        // >> kreator akcji - funkcja, która opakowuje obiekt przekazywany do dispatch'a
        const addDroid = item => ({type: 'ADD_DROID', item})
        const reset = () => ({type: 'RESET_DROIDS'})

        // >> wywołanie kreatora akcji
        store.dispatch(addDroid('ME-8D9'))

        // >> łączenie kreatorów akcji - obiekt w którym przekazywane są różne funkcje + obiekt dispatch
        const droidActions = bindActionCreators({add: addDroid, reset}, store.dispatch)

        // >> odwołanie się do metody łączącej w sobie akcje (dispatch już jest wpisany)
        droidActions.add('DN-LD')
        droidActions.reset()



        // ---------------------------- window.store -----------------------

        window.store = store // przypisuje wyżej stworzenie store do obiektu window.store pozwala na wpisanie w konsolę window.store.getState() (zwraca wtedy state)



        function App() {
                return (
                    <div className="App">
                            [...]
                    </div>
                );
        }

        export default App;

---

**2.** Faza projektu i jego struktura (istotne pliki/te które są edytowane oraz które zostaną/ły dodane są zilustrowane poniżej). 
W tej fazie logika projektu zostaje rozłożona pomiędzy poszczególnymi plikami. Główna logika odpowiedzialna za pracę ze stanem przy pomocy Reduxa znajduje się w folderach `duck`
Pliki index.js skupiają w sobie logikę z poszczególnych plików i eksportują ją według przyjętego wzoru, zapewniając czytelność kodu.


        {public}
        |
        |_ [...]
        {src}
            |
            |
            |---App.js
            |--- reducers.js
            |---[...]
            |
            |_{app}
                |
                |_ {droids}
                |    |
                |    |_ {duck}
                |       |
                |       | --- actions.js
                |       | --- index.js
                |       | --- reducers.js
                |       | --- types.js
                |_ {droidClasses}
                |    |
                |    |_ {duck}
                |       |
                |       | --- actions.js
                |       | --- index.js
                |       | --- reducers.js
                |       | --- types.js
            [...]

**Przykładowa zawartość >>ducks<<**

        //types.js
        const ADD_DROID = 'ADD_DROID'
        const RESET_DROIDS = 'RESET_DROIDS'

        export default {
            ADD_DROID,
            RESET_DROIDS
        }


        //reducers.js
        import types from './types'

        const INITIAL_STATE = {
        droidsName: "Favorite",
        list: ["R2D2", "C3PO", "BB8"],
        };

        const droidsReducer = (state = INITIAL_STATE, action) => {
        switch (action.type) {
            case types.RESET_DROIDS:
            return {
                ...state,
                list: [],
            };
            case types.ADD_DROID:
                return {
                ...state,
                list: [...state.list, action.item],
                };
            default:
                return state;
        }
        };

        export default droidsReducer

        // action.js

        import types from './types'

        const add = item => ({
            type: types.ADD_DROID, item
        })

        const reset = item => ({
            type: types.RESET_DROIDS, item
        })

        export default {
            add,
            reset
        } 

        //index.js - integruje oraz eksportuje logikę z duck
        import droidsReducer from './reducers'
        export {default as droidTypes} from './types'
        export {default as droidActions} from './actions'
        export default droidsReducer


W pliku **>>reducers.js<<** łączone są reduktory i eksportowane jako jeden obiekt

        import { combineReducers } from "redux";

        import droidsReducer from './app/droids/duck'
        import droidsClassReducer from './app/droidClasses/duck'

        const rootReducer = combineReducers({
            droids: droidsReducer,
            classes: droidsClassReducer
        })

        export default rootReducer


Do pliku **>>App.js<<** należy zaimportować połączone reduktory (rootReducer)

        import {createStore } from 'redux'
        import rootReducer from './reducers'
        import {droidActions} from './app/droids/duck'

        const store = createStore(rootReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())
        window.store = store 

        store.dispatch(droidActions.add('D-O'))

        [...]

wszystkie zmiany jakie zaszły na tym etapie projektu można znaleźć w tym miejscu: [2_redux-thunk-> distribution of logic](https://github.com/kostyrko/JS-sandbox/commit/d73069b2b79e8b28e3f965d3ec6ac555ca3e2f65)

---

**3.** Faza projektu oparta jest na podłączeniu Reduxa do Reacta oraz zastosowaniu Redux-Thunk

W tym celu należy zainstalować react-redux oraz redux-thunk

     npm i react-redux redux-thunk

Pliki, które uległy zmianie lub zostąły dodane:

        {public}
                |
                |_ [...]
                {src}
                    |
                    |---index.js // <Provider> - tu jest podpięta logika Reduxa
                    |---App.js // store zostaje usunięty
                    |---store.js // plik przechowujący konfigurację stora
                    |---[...]
                    |
                    |_{app}
                        |
                        |_ {droids}
                        |    |
                        |    |_ {components}
                        |    |    |
                        |    |    | --- DroidsContainer.js // "smart" component połączony z Redux
                        |    |    | --- DroidsForm.js // input - dodawanie droida to stanu  / zastoswanie akcji
                        |    |
                        |    |_ {duck}
                        |         |
                        |         |_operations.js // !! pobieranie wysyłanie danych z API
                        |         [...]

                        |_ {droidClasses}
                        |    |
                        |    |_ {duck}
                        |       |
                        |       [...]
                        |
                        |_{jsServer}
                        |     |
                        |     |_db.json (baza danych w formacie json -> Json Server)
                      [...]


**>>index.js<<** - tu zostaje przeniesiony store i App.js jest opakowany w <Provider> tak aby cała aplikacja miała dostęp do Reduxa

        [...]
        import {Provider} from 'react-redux'
        import store from './store'

        ReactDOM.render(
        <Provider store={store}>
            <App />
        </Provider>,
        document.getElementById('root')
        );

**>>DroidsContainer.js<<**


        import {connect} from 'react-redux'
        import {getAllDroids} from '../duck/operations'

        const DroidsContainer = ({droids,getAllDroids}) => {

            useEffect(() => {
                console.log(getAllDroids());
                console.log("ComponentDidMount");
            },[])


            return (
                <ul>
                    {droids.list.map((droid,i)=> 
                        <li key={i}>{droid}</li>
                        )}
                </ul>
            );
        }
        // przyjmuje stan i zwraca obiekt z zawartością stanu znajdującą się pod kluczem droids
        const mapStateToProps = state => ({
            droids : state.droids
        })

        // funkcja wywołująca funkcję dispatch z parametrem funkcji, która ma być wykonana
        const mapDispatchToProps = dispatch => ({
            getAllDroids : ()=> dispatch(getAllDroids())
        })


        // funkcja connect
        // 1. argument - mapowanie elementów ze stora, które mają być przyjęte w komponencie jako propsy
        // 2. obiekt przyjmujący dane z API
        export default connect(mapStateToProps, mapDispatchToProps)(DroidsContainer);



**>>DroidsForm.js<<**

        import React from 'react';
        import {connect} from 'react-redux'
        import actions from '../duck/actions'

        const DroidsForm = (props) => {

            const droidInput = React.createRef()

            const addDroid = event => {
                event.preventDefault()
                // podanie stora na którym ma się dokonać operacja dodania
                // add jest kluczem w obiekcie zwróconym przez mapDispatchToProps
                props.add(droidInput.current.value)
                console.log('form', droidInput.current.value)
                droidInput.current.value = ''
            }

            return (
                <form onSubmit={addDroid}>
                    <input ref={droidInput}/>
                    <button type="submit">Add droid</button>
                </form>
            );
        }

        // przygotowanie obiektu, który zawiera funkcje jakie należy wywołać na storze
        const mapDispatchToProps = dispatch => ({
            add: droid => dispatch(actions.add(droid))
        })

        // null ponieważ state nie jest sczytywany
        export default connect(null, mapDispatchToProps)(DroidsForm);


**>>operations.js<<**

        // akcje generują state
        import actions from "./actions";

        const fetchDroids = async () => {
            const response = await fetch('http://localhost:3001/droidsTypes', { method: 'GET' })
            const json = await response.json()
            console.log('json');
            return json
        };

        // thunk - zwraca funkcję asynchroniczną i przekaże w niej dispatcha powodując zmianę statu
        // export const getAllDroids = () => {

        export const getAllDroids = () =>
        async (dispatch) => {
            const droids = await fetchDroids()
            console.log(droids);
            droids['list'].map(droid => dispatch(actions.add(droid)))
        }

**>>store.js<<** - redux-thunk => applyMiddleware(thunk)
więcej na temat composeEnhancers patrz tutaj: [Redux DevTools Extension - 1.2 Advanced store setup](https://github.com/zalmoxisus/redux-devtools-extension#usage)

        import {createStore, applyMiddleware, compose } from 'redux'
        import rootReducer from './reducers'
        import thunk from 'redux-thunk'

        const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

        const store = createStore(rootReducer, composeEnhancers(applyMiddleware(thunk)))


        export default store



wszystkie zmiany jakie zaszły na tym etapie projektu można znaleźć w tym miejscu: [2_redux-thunk-> Connect to React + Thunk](https://github.com/kostyrko/JS-sandbox/commit/2ccfcedbb19f1e4acdce5543fff4139e8bc10e08)


**4.** faza zastosowanie hooków `useDispatch/useSelector` (wszystkie operacje zachodzą na pliku **DroidsContainer.js**)

co zostało zastąpione? -> **connect, mapStateToProps, mapDispatchToProps**

        // DroidsContainer.js
        import React, {useEffect} from 'react';

        import {useSelector, useDispatch} from 'react-redux'
        import {getAllDroids} from '../duck/operations'

        const DroidsContainer = (props) => {

            // deklarowania dispatch i użycie hooka
            const dispatch = useDispatch()
            useEffect(() => {
                dispatch(getAllDroids())

                // dla przypomnienie - co się tam dzieje?
                // dispatch({type: 'ADD_DROID', item: 'D-O'})
            }, [])


            // pobranie wycinka statu przy pomocy -> useSelector
            const droids = useSelector((state) => state.droids);

            return (
                <ul>
                    {droids.list.map((droid,i)=> 
                        <li key={i}>{droid}</li>
                        )}
                </ul>
            );
        }

        export default DroidsContainer;


---

**Źródła**:

Podstawowe:

[Podstawy Redux - Artur Chmaro](https://www.youtube.com/watch?v=qIaLloDosxs&list=PLOzzvlJKwOdWIKw_f1-3l15bODB1CcUPh)

[Actions must be plain objects. Use custom middleware for async actions. #146](https://github.com/reduxjs/redux-thunk/issues/146)

Dodatkowe:

[What is Redux Ducks?](https://medium.com/@matthew.holman/what-is-redux-ducks-46bcb1ad04b7)

[React Lesson 13. Part 1: Asynchronous actions](https://soshace.com/react-lesson-13/)

[Handling Asynchronous Actions with Redux Thunk](https://medium.com/swlh/handling-asynchronous-actions-with-redux-thunk-86b8d8e0b83e)

[Understanding Redux Middleware And Writing Custom Ones](https://designingforscale.com/understanding-redux-middleware-and-writing-custom-ones/)

[What the heck is a 'thunk'?](https://daveceddia.com/what-is-a-thunk/)

[GH - Redux Thunk (Thunk middleware for Redux.)](https://github.com/reduxjs/redux-thunk)


