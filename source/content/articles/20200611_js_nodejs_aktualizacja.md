Title: Node.js aktualizacja (Ubuntu)
Author: mkostyrko
Date: 2020-06-11 11:00
Updated:
Category: nodejs
Tags: node.js, node, nvm, aktualizacja, linux, ubuntu, bash, curl, npm
Slug: js-nodejs-aktualizacja
related_posts:

![node](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/1024px-Node.js_logo.svg.png#center){:height="50%" width="50%"}

Moja pierwsza instalacja node.js na Ubuntu odbyła się poprzez pobranie paczki i instalację zawartości paczki [Linux Binaries](https://nodejs.org/en/download/) 
    node -v
    >> v10.19.0
    
#### Moduł N z NMP

Moduł [**n**](https://www.npmjs.com/package/n) służy do interaktywnego zarządzani wersjami *Node.js*

Kroki podjęte do instalacji najnowszej wersji *Node.js*

Czyszczenie pamięci cache

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

Instalacja NVM (uwaga v0.35.3 jest aktualną wersją, która ulegnie zmianie) - pobranie skryptu install_nvm.sh przy pomocy `culr` (klonuje repozytorium nvm do ~/.nvm) lub bezpośrednio z [repo na GitHubie](https://github.com/nvm-sh/nvm/blob/master/install.sh)

    curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.35.3/install.sh -o install_nvm.sh

Uruchomienie skryptu przy pomocy komendy `bash`


Pobranie, kompilacja i instalacja najnowszej wersji *Node.js*

    nvm install node

Zwrócenie listy dostępnych wersji 

    nvm ls-remote

Instalacja konkretnej wersji

    nvm install 6.14.4

---

Źródła:

https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages

https://github.com/nodesource/distributions/blob/master/README.md

https://askubuntu.com/questions/426750/how-can-i-update-my-nodejs-to-the-latest-version

https://github.com/nvm-sh/nvm

https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04