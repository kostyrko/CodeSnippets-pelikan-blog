Title: Ubuntu - zamiana bobra na gronostaja
Author: mkostyrko
Date: 2020-03-26 21:00
Updated: 
Category: ubuntu
Tags: linux, ubuntu, aktualizacja, ciemny motyw, ubuntu 19.10
Slug: linux-aktualizacja
related_posts:

Do tej pory pracowałem na Bionicznym Bobrze (Ubuntu 18.04) ale gdy system zaproponował mi aktualizację na Eonicznego Gronostaja (19.10) postanowiłem z niej skorzystać. Zmiana nie obyła się bez małego zgrzytu. 

### Zawieszający się ekran ładowania Ubuntu 19.10 po aktualizacji

Ekran ładowania (tzw. splash screen) się zawiesił, musiałem wyłączyć komputer ręcznie a następnie w momencie pojawienia się Gruba wybrałęm literę 'e' - pozwalającą na edycję ustawień opcji włączania systemu. Za pierwszym razem system od razu się uruchomił bez mojej konieczności zmiany ustawień. W trakcie kolejnego włączani powtórzył się ten sam problem. Tym razem postąpiłem zgodnie z opisanymi [w tym miejscu krokami](https://nezhar.com/blog/fix-ubuntu-19.10-stuck-on-splash-screen/) - opcję

    quiet splash_

zmieniłem na

    nonsplash

system uruchomił się bez większych problemów.

Po uruchomieniu się systemu nie przechodziłem kolejnych opisanych kroków tylko zaktualizowałem gruba

    sudo update-grub

### Ubuntu 19.10 zmiana motywu na ciemny

Bóbr przyzwyczaił mnie do miłego dla oka ciemnego motywu oprogramowania. Fioletowy terminal z zielonymi i jasnymi literami również przypadł mi do gustu (na szczęście zmiana z podstawowego jasnego na ciemny motyw jest prosta) niestety Gronostaj już ciemnego motywu aplikacji nie posiada w trybie podstawowym i trzeba go dodać.

W pierwszej kolejności należy zainstalować program Gnome Tweaks
Instalowanie programu do zarządzania wyglądem/skórką Ubuntu

    sudo apt install gnome-tweak-tool


W zakładce 

**Appearance -> Themes -> Aplications -> Adwait** - skórka podstawowa można zmienić np. na **Yaru-dark** 

(z tej obecnie korzystam - zrobiło się nieco ciemniej niż za kadencji Bobra, ale pewnie szybko się przyzwyczaję)

Jednak aby powrócić do ciemnych ustawień aplikacji należy zmienić opcję Shell, ta jednak jest nieaktywna

**Shell -> ! - nieaktywny**

Na szczęście rozwiązanie trudne nie jest i postępując zgodnie z opisanymi [w tym miejscu](https://www.linuxuprising.com/2019/10/how-to-get-dark-gnome-shell-menus-and.html) krokami można dodać nową/starą skórkę - (motywem Gronostaja jest fioletowy i trzeba przyznać, że widoczność tego koloru na ciemnym tle jest słabsza od bobrowego pomarańczowego)

* Instalujemy skórkę Yaru 

        sudo apt install git meson sassc libglib2.0-dev libxml2-utils

        git clone https://github.com/ubuntu/yaru

        cd yaru

        git checkout 2c22b5178f321f62f8d914e27b4739eecb7e3b6b

        meson build

        cd build

        sudo ninja install
        

(zwróć uwagę, że wybieramy konkretną wersję, która posiada czarną skórkę)

* Instalujemy rozszerzenie GNOME Shell User themes

    sudo apt install gnome-tweaks gnome-shell-extensions

* Restartujemy GNOME Shell  `ALT + F2` następnie wpisujemy `r` i wybieramy `ENTER`

* W (GNOME) Tweaks wybieramy zakładkę **Extensions** i włączamy **User themes** 

* wyłączamy i włączamy program

* Przechodzimy do zakładki **Appearance** i możemy w **Shell** wybrać **Yaru-dark**

### Dodatkowe opcje w nowej wersji Ubuntu (które do tej pory zauważyłem)

* W momencie wybierania linka, który otwiera przeglądarkę pojawiła się nowa opcja **configure trusted domains**

