Title: VSC i Ubuntu - dodawanie fontu JetBrains Mono  i Fira Code
Author: mkostyrko
Date: 2020-03-29 22:00
Updated:
Category: VSC
Tags: vsc, visual studio code, visual studio, JetBrains Mono, Fira Code, font
Slug: vsc-dodawanie-fontu
related_posts: vsc-edytowanie-barw-motywu


Początkowo w *Visual Studio Code* korzystałem z fontu *Monospace*, który ze względu na domyślny odstęp pomiędzy literami oraz sam kształt fontu jest przystępny do nauki, z czasem jednak postanowiłem przejść na inny i przyjemniejszych dla oka **Fira Code **

Instalacja na Ubuntu jest bardzo prosta, wystarczy w terminal wpisać komendę 

    `sudo apt install fonts-firacode`

Następnie należy zdefiniować użycie nowego fontu (wymaga ponownego włączenie VSC!) w `settings.json`

    "editor.fontFamily": "Fira Code",
    // "editor.fontFamily": "Fira Code Retina", // 2. opcjonalna wersja fontu Fira Code
    "editor.fontLigatures": true,

Po jakimś czesie przeszedłem na **JetBrains Mono** aby z niego korzystać musiałem postąpić w następujący sposób

Pobrać (paczkę z fontem z oficjalnej strony )[https://www.jetbrains.com/lp/mono/]

Wypakowałem paczkę w odpowiednim miejscu (`~/.local/share/fonts)` przy użyciu komendy

    unzip JetBrainsMono-1.0.3.zip -d ~/.local/share/fonts && fc-cache -fv
    unzip <nazwa_katalogu.zip> -d ~/.local/share/fonts && fc-cache -fv

Następnie w pliku `settings.json` dokonałem odpowiednią zmienną

    "editor.fontSize": 18,
    "editor.fontFamily": "JetBrains Mono",
    "editor.fontLigatures": true,
    // "editor.letterSpacing": -0.05, // edytuje odległość pomiędzy literami

Źródło: 

https://www.guyrutenberg.com/2020/01/29/
install-jetbrains-mono-in-debian-ubuntu/

https://www.jetbrains.com/lp/mono/

https://github.com/JetBrains/JetBrainsMono

https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions

https://github.com/tonsky/FiraCode/wiki/Linux-instructions#installing-with-a-package-manager

https://freebiesupply.com/blog/top-monospace-fonts-for-developers/