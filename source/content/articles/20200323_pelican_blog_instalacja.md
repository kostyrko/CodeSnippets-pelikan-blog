Title: Pelican blog - instalacja
Author: mkostyrko
Date: 2020-03-23 9:00
Updated: 2020-03-24 10:00
Category: pelican-blog
Tags: python, markdown, pelican, blog
Slug: pelican-blog-instalacja

Gdy szukałem platformy do tworzenia bloga, wybór w pierwszej kolejności padł na Jakyll (Ruby on Rails), rozważałem również Hugo (Go), ostatecznie padło jednak na Pelicana bo ten "stoi" na Pythonie, choć jest dużo mniej popularny od wcześniej wspomnianych generatorów stron statycznych. W przyszłości planuję również wypróbować [Lektora](https://www.getlektor.com/), który również wywodzi się z Pythona

W trakcie tworzenia bloga przy pomocy Pelicana korzystałem z informacji zawartych [na tym blogu](matthewdevaney.com) posiłkując się informacjami zawartymi w dokumentacji Pelicana oraz Flexa (wybranego przeze mnie motywu) - patrz [źródła](#zrodla)) jak i [repozytoriów na githubie](https://github.com/alexandrevicenzi/Flex/wiki/Flex-users) wykorzystujących ten sam motyw. 

### Instalacja

    pip install pelican
    pip install markdown

### Uruchomienie

    pelican-quickstart

przygotowanie struktury folderów 

    blog
      └── output
      └── source

### Wypełnienie podstawowych informacji

    Where do you want to create your new web site? [.] .
    # wskazanie folderu w którym ma być zapisana strona
    What will be the title of this web site? ...z frontu
    # nazwa
    Who will be the author of this web site? kostyrko
    # autor 
    What will be the default language of this web site? [English] pl
    # język
    Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
    # wskazanie adresu strony
    Do you want to enable article pagination? (Y/n) Y
    # ograniczona ilość postów/artykułów na stronie - paginacja
    What is your time zone? [Europe/Paris] Europe/Warsaw
    # strefa czasowa
    Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y

Powyżej zawarte informacje będą zawarte w pliku pelicanconf.py i można je zmienić
Uzyskany efekt:

    blog
      ├──  output
      └── source
          ├── content (folder)
          ├── output (folder)
          ├── pelicanconf.py
          └── publishconf.py

w pliku pelicanconf.py definiujemy miejsce w którym będzie generować się statyczna strona

    OUTPUT_PATH = '../output'

Tworzymy zawartość strony komendą:

    pelican content

Tworzymy server lokalny pozwalający na przeglądanie strony (:8000)

    pelican --listen

Przeglądamy osiągnięty efekt:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)





---


### Przydatne liki i źródła: {#zrodla}


[mBuild A Blog With Pelican And Python - Pt. 1 Installation & Theme](https://matthewdevaney.com/posts/2019/03/04/build-a-blog-with-pelican-and-python-pt-1-installation-theme/)

[Build A Blog With Pelican And Python - Pt. 2 Creating Content](https://matthewdevaney.com/posts/2019/03/07/build-a-blog-with-pelican-and-python-pt-2-creating-content/)

[How to Create Your First Static Site with Pelican and Jinja2](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html)

[Ustawienia dla Pelican blog - pelicanconf.py](https://docs.getpelican.com/en/stable/settings.html)

[Dokumentacja Pelican blog](http://docs.getpelican.com/en/latest/)

[Flex](https://github.com/alexandrevicenzi/Flex)

Inne generatory stron statycznych korzystające z Pythona:

[Lektor](https://www.getlektor.com/) - posiada wbudowany CMS (Content Management System)

Motywy warte uwagi:
[Pure](https://github.com/PurePelicanTheme/pure)
