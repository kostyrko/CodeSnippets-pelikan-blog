Title: Pelican blog - GitHub pages
Author: mkostyrko
Date: 2020-03-24 22:00
Updated:
Category: pelican-blog
Tags: python, gh-pages, pelican, github, github pages, blog
Slug: pelican-blog-ghpages
related_posts: pelican-blog-instalacja

Krótka instrukcja hostowania bloga przy pomocy GitHub-Pages

* Instalowanie gh-pages dla Pelicana

    `pip install pelican ghp-import Markdown`

* Sklonowanie pustego repozytorium / Repo wcześniej stworzone na stronie github.com

    `git clone https://GitHub.com/username/username.github.io`

* Stworzenie nowej gałęzi `content` gdzie przechowywane będą surowe/źródłowe pliki - Git Hub pages będzie czerpało z głównej gałęzi `master`

    `git checkout -b content`

    (Alternatywnie można korzystać z dwóch repozytoriów - gdzie na jednym są przechowywane pliki źródłowe a na kolejnym jest hostowana strona)

* Tworzenie treści - stron statycznych gotowej do publikacji. W terminali wpisz (gdzie wyjściowym folderem jest source a output miejsce zapisania plików do wgrania do repozytorium na githubie) - praca na gałęzi `content`:

        pelican content -o output -s publishconf.py

        np.

    (gdzie -s oznacza settings/ustawienia a -o miejsce w którym mają się zapisać pliki)

    np.

        pelican content -o ../../zfrontu/site -s publishconf.py

* Tworzenie plików do wgrania do repozytorium (gdzie output - miejsce zapisu plików może być np. '.' jeśli w danym folderze) ale tego do gałęzi `master`

        ghp-import -m "Generate Pelican site" --no-jekyll -b master output

    tłumacząc

        ghp-import -m "wiadomość" --no-jekyll -b [nazwa_gałęzi] [folder_zapisu_danych]

* Wypchnięcie do repozytorium

        git push origin master

    (alternatywnie można zautomatyzować ten proces `make publish` [więcej na ten temat tutaj](http://docs.getpelican.com/en/3.6.3/publish.html))

* Dodawanie nowej treści do gałęzi `content`

        git add content

        git commit -m 'treść wiadomości

        git push origin content


### Źródło: {#zrodla}

https://opensource.com/article/19/5/run-your-blog-github-pages-python