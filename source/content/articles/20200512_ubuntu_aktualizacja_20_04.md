Title: Ubuntu - zamiana gronostaja na fossę - przerwana aktualizacja
Author: mkostyrko
Date: 2020-05-12 21:00
Updated: 
Category: ubuntu
Tags: linux, ubuntu, aktualizacja, ciemny motyw, ubuntu 19.10, ubuntu 20.04 
Slug: ubuntu-aktualizacja-fossa
related_posts: ubuntu-skroty-klawiszowe, ubuntu-aktualizacja-gronostaj

Do tej pory pracowałem na Bionicznym Bobrze (Ubuntu 18.04) następnie Eonicznum Gronostaju (19.10) i gdy przyszedł czas na Skupioną Fossę (20.04) postanowiłem skorzystać z możliwości aktualizowania systemu - niestety w trakcie dokonywania się aktualizacji została ona przerwana w nieoczekiwany sposób, w wyniku czego system przestał się uruchamiać.

---

### Przerwana aktualizacja Ubuntu 20.04

W pierwszej kolejności musiałem dostać się do konsoli (z pozycji Grub'a). W tym celu wykorzystałem następującą ścieżkę postępowania:

`Grub `-> `Advance options for Ubuntu` -> `...(recovery mode)` -> `root` -> `Enter`

Następnie zgodnie z sugestią wpisałem w terminal komendę (odpakowującą ale nie skonfigurowane paczki) - instalacja została przerwana na dość późnym etapie

    $ sudo dpkg --configure -a

Po uruchomieniu Ubuntu (20.04) działało ale nie w pełni poprawny sposób (program z aktualizacjami nie funkcjonował w sposób poprawny) stąd wywołałem komendę aktualizującą poszczególne paczki, z których składa się system

    $ sudo apt-get upgrade

---
### Ubuntu 20.04 centralizacja paska "dokującego"

Aby dokonać różnego rodzaju zmian z paskiem dokującym należy zainstalować rozszerzenie `dconf-editor `

np.

    $ sudo apt install dconf-tools

Po uruchomieniu programu należy odznaczyć opcję `extend-height` (ustawić na `false`)


Ten program pozwala również na zmianę wydarzeń generowanych przez kliknięcie na ikonę w pasku dokującym - `click-action`

Przykładowo można ustawić na `minimize-or-previews` - minimalizuje okno po kliknięciu jeśli jest jedynym oknem danego programu lub wywołuje podgląd jeśli jest ich więcej (domyślnie ustawione jest `previews`)

---

Źródła:

https://askubuntu.com/questions/346678/how-do-i-resume-a-release-upgrade

https://askubuntu.com/questions/859630/how-to-start-ubuntu-in-console-mode

https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do

https://linuxconfig.org/how-to-customize-dock-panel-on-ubuntu-18-04-bionic-beaver-linux