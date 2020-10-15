Title: Node.js aktualizacja (Ubuntu) oraz Node Version Manager!
Author: mkostyrko
Date: 2020-06-11 11:00
Updated:
Category: nodejs
Tags: node.js, node, nvm, aktualizacja, linux, ubuntu, bash, curl, npm, node version manager
Slug: js-nodejs-aktualizacja
related_posts:

![node](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/1024px-Node.js_logo.svg.png#center){:height="50%" width="50%"}

Moja pierwsza instalacja node.js na Ubuntu odbyła się poprzez pobranie paczki i instalację zawartości paczki [Linux Binaries](https://nodejs.org/en/download/) 
    node -v
    >> v10.19.0
    
#### Moduł N z NMP

Moduł [**n**](https://www.npmjs.com/package/n) służy do interaktywnego zarządzani wersjami *Node.js*

Kroki podjęte do instalacji najnowszej wersji *Node.js*

Czyszczenie pamięci cache (aby nie korzystać z sudo - innymi słowy by instalowane paczki nie miały dostępu do roota, należy korzystać z NVM - więcej na ten temat poniżej)

    sudo npm cache clean -f

Instalacja przy pomocy nmp modułu n (-g -> globalnie)

    sudo npm install -g n

Instalacja najnowszej wersji (w domyśle *Node.js*) oraz usunięcie poprzedniej

    sudo n latest

#### NVM - Node Version Manager

Zalecane jest instalacja oraz zarządzanie wersją(w tym przypadku również wieloma wersjami) przy pomocy NVM (Node Version Manager)

Pobranie paczek dla Ubuntu, które pozwolą na budowę paczek źródłowych (NVM będzie je wykorzystywał w trakcie instalacji)

    sudo apt-get update
    sudo apt-get install build-essential libssl-dev

Instalacja NVM - pobranie skryptu install_nvm.sh przy pomocy `culr` (klonuje repozytorium nvm do ~/.nvm) lub bezpośrednio z [repo na GitHubie](https://github.com/nvm-sh/nvm/blob/master/install.sh)

    curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

[być może będzie wymagane `. ~/nvm/nvm.sh` - wskazanie na interpretację skryptu w danym procesie]

Pobranie, kompilacja i instalacja najnowszej wersji *Node.js*

    nvm install node

Zwrócenie listy dostępnych wersji

    nvm ls-remote

Instalacja konkretnej wersji

    nvm install 6.14.4

lub ostatniej stablinej

    nvm install stable


Aby node działał właśnie poprzez NVM pozbyłem się wcześniej zainstalowanego noda

    sudo apt-get purge --auto-remove nodejs

Znalezienie lokalizacji node.js

    which node

Wykasowanie folderu z nodem

    sudo rm -rf /usr/local/bin/node

Wskazanie nvm na używanie konkretnej wersji noda

    nvm use 12.19.0

Komenda `nvm current `powinna zrówić wersję noda

    nvm current

    >>  v12.19.0

---

Źródła:

[Installing Node.js via package manager](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages)

[NodeSource Node.js Binary Distributions](https://github.com/nodesource/distributions/blob/master/README.md)

[How can I update my nodeJS to the latest version?](https://askubuntu.com/questions/426750/how-can-i-update-my-nodejs-to-the-latest-version)

[Node Version Manager](https://github.com/nvm-sh/nvm)


[JSHint is not working](https://stackoverflow.com/questions/30666177/jshint-is-not-working)

[How to Install Node.js via NVM on Ubuntu 14.04 LTS](https://www.liquidweb.com/kb/how-to-install-node-js-via-nvm-node-version-manager-on-ubuntu-14-04-lts/)

[How to remove nodejs from Ubuntu 16.04?](https://askubuntu.com/questions/786015/how-to-remove-nodejs-from-ubuntu-16-04)

[How to delete a non-empty directory in Terminal?](https://askubuntu.com/questions/217893/how-to-delete-a-non-empty-directory-in-terminal)