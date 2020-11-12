Title: React: routing
Author: mkostyrko
Date: 2020-09-14 10:00
Updated:
Category: reactjs
Tags: react, hooks, props
Slug: react-routing
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://www.educative.io/api/page/4807683539468288/image/download/5379198832082944)

Routing - "ścieżkowanie", rozpoznawanie na podstawie ścieżki zasobów jaki serwer może zwrócić, inaczej to określając jest procesem rozpoznawania zasobów serwera

React Router jest tzw **high order component** i dostarcza nam szereg innych komponentów, które można wykorzystać w trakcie tworzenia nawigacji tworzonej aplikacji

        HashRouter lub BrowserRouter - główny komponent "opakowujący" nawigację
        Route, - komponent "wywołujący" inny komponent jeśli warunek podanego linku zostaje spełniony (powiązuje scieżkę z komponentem)
        Link, - link
        Switch, - komponent "opakowujący" linki w nawigacji
        NavLink, - Komponent linku nawigacji

Component HashRouter (lub BrowserRouter) posiada dzieci Route, które posiadają propsy path, gdzie można zdefiniować ścieżkę do którego dany komponent może się odwoływać, posiada również props component w który należy przekazać komponent do wyrenderowania.
Jego zadaniem jest wyrenderowanie jedynie tych komponentów, które w danym momencie są wskazane, a nie wszystkie możliwe. Natomiast renderowanie jest zależne od ścieżki.

#### HashRouter

**HashRouter** - wszystkie ścieżki poprzedzane są # (wie,że korzystać z aliasów # a nie brać z miejsca zapisania całej strony) ww.wp.pl/#/kalkulator. HashRouter jest wykorzystywany do celów deweloperskich (BrowserRouter jest podstawowy do prod. skończonych)

W ramach komponentu Route można użyć słowa kluczowego exact (a dokładnie exact={true})
tak aby sprawdzał dokładnie podaną ścieżkę np. rozróżnić od /about /about-us
bez exact sprawdza czy ścieżka posiada taki sam element = -1

        <Component exact path="/calculator" component={calculator}>

#### Switch

Komponent **Switch** wyświetla pierwszy możliwy komponent, który spełnia warunek lub jakiekolwiek jeśli warunek nie został podany (w ten sposób zwykle zamieszcza się informację o błędzie 404). Komponent odpowiedzialny za 404 powinien być dodany jako ostatnie dziecko.

        <HashRouter>
            // komponent zawsze wyświetlany ponieważ nie posiada warunku (pod postacią propsu path)
            <Clock/>
            <Switch>
                <Route exact path='/' component={Main}>
                // jeśli ścieżka jest poprawna kolejny komponent się nie wyświetla
                // w przeciwnym razie <Switch> szuka kolejnego, który może się wyświetlić
                <Reoute component={NotFound}>
            <Switch/>
        <HashRouter/>

#### Link

Komponent Linki w React Routerze - ma domyślnie event.preventDefault() jego zastosowanie jest podobne do `<a>` - odnośnik do cześci przeglądanej strony lub odsyłacz do innej

    <Link to='./'>Home<Link/>

#### Placeholder i cd linku

Routning "placeholder" -> :userId (zmienna) - zawsze po dwukropku (React tworzy z tego klucz w obiekcie przypisywany do params props.match.userId)
<Route path='/user/:userId' component={UserInfo}/>

        // component UserInfo ma dostęp do userId

        <li>
            <Link to={"/hello/jan"}>Say Hello</Link>
        </li>

        // umożliwia dodanie informacji, która będzie przekazana jako props
        <Route exact path='/hello/:name' component={HelloYou}/>

        const CheckAge = (props) => {
        const {age} = props.match.params
        return (
            <div>
            <h1>Your age is {age}
            , you are: { age >= 18 ? 'an adult':'a child'}</h1>
            </div>
        );
        }

#### active (stylowanie aktywnego komponentu)

Styl aktywny dla komponentów NavLink -> `activeStyle={activeStyle} ` klasa **active** jest przypisywany do komponentu gdy zostanie spełniony warunek (exact)

    // zastosowanie
    <NavLink activeStyle={activeStyle}></NavLink>

---

### Instalacja + ract-scroll

Instalacja instalacja wtyczki React-Router

    npm i react-router-dom --save

Popularną biblioteką stosowaną w kontekście wewnętrznej nawigacji jest react-scroll (patrz przykład 2 na zastosowanie) - pozwala min. na gładkie przejścia pomiędzy częściami strony

    npm install react-scroll

---

**Przykład zastosowania 1**

        // App.js
        [...]
        const App = () => {
        return (
            <BrowserRouter basename={process.env.PUBLIC_URL}>
            {/* <BrowserRouter> */}
                <NavWithRouter/>
                <Switch>
                <Route exact path='/uslugi' component={ServicesPage}/>
                <Route exact path='/projekty' component={PortfolioPage}/>
                <Route exact path='/kalkulator' component={CalculatorPage}/>
                <Route exact path='/onas' component={AboutPage}/>
                <Route exact path='/kontakt' component={ContactPage}/>
                <Route component={process.env.PUBLIC_URL ? undefined:NotFoundPage}/>
                </Switch>
                <Footer/>
            </BrowserRouter>
        );
        }

        //Fragment Nav.js - zastosowanie NavLink
        [...]
        return (
            <nav className={location.pathname==='/' || location.pathname==='/flacky-meble/' ? "home": 'main-nav'}>
            <div className="container">
                <div className="logo-container">
                <h1 className="logo">
                    <NavLink exact to='/'> <span className="name-1">FLACKY</span>
                    <span className="name-2"> COMBINATION MEBLE</span>
                    <p className="logo-desc"> <span>MEBLE na MIARĘ</span> Twoich potrzeb</p>
                    </NavLink>
                </h1>
                </div>
                [...]

---

**Przykład zastosowanie 2**

        // App.js
        [...]
        import * as ROUTES from "./constants/routers";
        [...]
            return (
                <BrowserRouter basename={process.env.PUBLIC_URL}>
                <UserContext.Provider value={{ email: content.email }}>
                    <Switch>
                    <Route exact path={ROUTES.LANDING} component={HomePage} />
                    {content.email ? <Route exact path={ROUTES.DONATE} component={DonatePage} /> : null}
                    <Route exact path={ROUTES.LOG_IN} component={LogInPage} />
                    <Route exact path={ROUTES.SIGN_UP} component={SignUpPage} />
                    <Route exact path={ROUTES.LOG_OUT} component={LogOutPage} />
                    <Route exact path="" component={NotFoundPage} />
                    </Switch>
                </UserContext.Provider>
                </BrowserRouter>
            );
        }

        // NavMain.js
        import { Link } from "react-scroll";
        import { NavLink } from "react-router-dom";

        const NavMain = () => {
        return (
            <nav className="nav-main">
            <NavLink className="nav-link" exact to="/">
                Start
            </NavLink>

            <Link
                className="nav-link"
                activeClass="active"
                to="about-project"
                spy={true}
                smooth={true}
                offset={0}
                duration={500}
            >
                O co chodzi?
            </Link>

            <Link
                className="nav-link"
                activeClass="active"
                to="about-us"
                spy={true}
                smooth={true}
                offset={0}
                duration={500}
            >
            [...]

---

Źródła:

[React-router w wersji 4 czyli wszystko od nowa...](https://www.nafrontendzie.pl/react-router-wersji-4-wszystko-nowa)

[React Router Tutorial: Adding Navigation to your React App](https://www.educative.io/blog/react-router-tutorial)
