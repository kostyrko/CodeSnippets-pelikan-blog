Title: React i GitHub Pages
Author: mkostyrko
Date: 2020-11-04 10:00
Updated:
Category: reactjs
Tags: react, hooks, props
Slug: react-routing
related_posts: react-wprowadzenie, react-komponenty, react-listy, react-zdarzenia, react-stany, react-warunkowe-renderowanie

![react](https://res.cloudinary.com/practicaldev/image/fetch/s--klrLsGeS--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://completejavascript.com/wp-content/uploads/2018/08/tao-va-deploy-ung-dung-react-len-github-pages-create-react-app-completejavascript.com_.png)

**Wymagania wstępne:** git, GitHub, Create React App, Node.js, NPM


Poniżej wypunktuje jak w prosty sposób można opublikować na GitHub-Pages swoją aplikację reactową stworzoną przy pomocy narzędzia Create React App 

**!** W pierwszej kolejności warto ustawić środowisko Routera aby dopasowało się do hostującego środowiska (PUBLIC_URL zostanie podstawione przez ścieżkę absolutną folderu)
[process.env.PUBLIC_URL można również wykorzystać w kontekście odwołania się do ścieżki pliku znajdującego się w folderze po za src]

        <BrowserRouter basename={process.env.PUBLIC_URL}>


        // może się to przedstawiać w następujący sposób - App.js

        [...]
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
        [...]


1) W pliku (package.json) pod **name** (jedna z pierwszych linijek) należy podać adres home/strony domowej

        "name": "nazwa_projektu",
        "homepage": "http://{nazwa_użytkownika}.github.io/{nazwa_repo}",


        // u mnie w jednym z projektów przedstawia się to w sposób następujący
        {
        "name": "donate-to-charity",
        "homepage": "https://kostyrko.github.io/donate-to-charity",
        "version": "0.1.0",
        "private": true,
        "dependencies": {
            "@testing-library/jest-dom": "^4.2.4",
            [...]


2) Dodanie w pliku package.json do scripts należy dodać ->

        "predeploy": "npm run build",
        "deploy": "gh-pages -d build"


        // u mnie w jednym z projektów przedstawia się to w sposób następujący
        [...]
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject",
            "postinstall": "node ./scripts/enable-css-sourcemaps.js",
            "predeploy": "npm run build",
            "deploy": "gh-pages -d build"
        },
        [...]

3) należy zainstalować narzędzie gh-pages 

        npm install gh-pages --save-dev


        // w package.json powinna pojawić się informacja o tej zależności
        [...]
                    "devDependencies": {
                "gh-pages": "^3.1.0"
            }
        }

4) Gdy powyżesz warunki zostaną spełnione wystarczy wywołać skrypt (`npm run deploy`), który wypuszuje zawartość builda na gałąź gh-pages (ustawi ją też jako domyślną, z której gh-pages mają być tworzone), zmianę należy nastepnie wypushować na remota


        npm run deploy
        git add .
        git commit -m "first deploy"
        git push origin master





---

Źródła:

[How to deploy React App to GitHub Pages](https://dev.to/yuribenjamin/how-to-deploy-react-app-in-github-pages-2a1f)


[React Router with relative path deployment](https://stackoverflow.com/questions/57572259/react-router-with-relative-path-deployment)

[Create React App - Using Public Folder](https://create-react-app.dev/docs/using-the-public-folder/)
