Title: Ubuntu zwalnianie i przenoszczenie pamięci
Author: mkostyrko
Date: 2020-10-14 10:00
Updated:
Category: ubuntu
Tags: ubuntu, linux
Slug: ubuntu-czyszczenie
related_posts: ubuntu-skroty-klawiszowe

![ubuntu 20](https://upload.wikimedia.org/wikipedia/commons/2/21/Desktop_Ubuntu_20.04.png)

W tym artykule znajdzie się opis podstawowych kroków, które można wykonać w celu zwolnienia miejsca pracę systemu (Ubuntu)

Podstawowym narzędziem, z którego korzystam jest **Disk Usage Analyzer**, które wizualizuje rozkład oraz zużycie miejsca na poszczególne foldery/aplikacje. U mnie w tym momencie najwięcej miejsca zajmuje anaconda3 - 4,6gb (tj 10% miejsca jakie mam przeznaczone pod Ubuntu w całości oraz ponad 1/4 jaką mam przeznaczoną na folder home). Zwykle sporo miejsca pozwala zaoszczędzić odchudzenie folderu *snap* (tu przechowywane instalacje aplikacji snapowych/ubuntu) oraz *cache* (podręczna pamięć).

Można również sprawdzić sprawdzić stan zapełnienia dysku przy pomocy komendy (report free disk space)

    df
    df -h // human-readable
    df -l // only local filesystems


## Podręczna pamięć Ubuntu vs folder Home

Sprawdza jak duży jest folder apt-cache


    du -sh /var/cache/apt/archives


Czyści apt-cache


    sudo apt-get clean

---

### .catche (folder Home/Użytkownika)

Znajdź pliki starsze niż 90 dni


    find ~/.cache/ -depth -type f -atime +90


Znajdź i i skasuj starsze niż 90 dni


    find ~/.cache/ -type f -atime +90 -delete

---

### Usunięcie nieużywanych paczek/zależności

    sudo apt-get autoremove

---

## Instalacja Bleachbit

    sudo bleachbit

Bleachbit jest programem, który został stworzony w celu (skanowania) zwalniania miejsca na dysku

---
## Pozbycie się niużywanychy snapów

W celu pozbycia się archiwalnych snapów (programów, które były aktualizowane -> przechowywane w folderze `/var/lib/snapd/snaps/`) i zachowania jedynie aktualnej można wykorzystać poniższy skrypt (link do źródła poniżej), który należy wkleić do pliku (np o nazwie `remove-old-snaps`) i zapisać w folderze **home**


        #!/bin/bash
        # Removes old revisions of snaps
        # CLOSE ALL SNAPS BEFORE RUNNING THIS
        set -eu

        LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
            while read snapname revision; do
                snap remove "$snapname" --revision="$revision"
            done

Następnie należy nadać możliwość egzekucji skryptu poniższą komendą


    chmod +x remove-old-snaps


A w ostatniej kolejności wywołać jego wykonanie


    sudo ./remove-old-snaps


Myśląc na przyszłość można również zdefiniować ilość przechowywanych snapów (2-20) korzystając z poniższej komendy


        sudo snap set system refresh.retain=2

---

![gparted](https://i.stack.imgur.com/nYWt3.png)

## Relokacja pamięci przy dual-boocie

Może się okazać, że powyższe kroki pomimo tego,  że zostały wykonane z sukcesem dalej nie gwarantują nam dostatecznej ilości miejsca na dysku, w przypadku dual-boota można dokonać relokacji części pamięci z Windowsa - w tym celu niezbędne jest posiadanie Ubuntu w wersji Live np na DVD i USB i skorzystać z programu **gparted**

1) w pierwszej kolejności należy w Windowsie zwolnić miejsce -> "my computer" -> "manage" -> "Storage" -> "disk Management" -> NTFS -> Shrink Volume (stworzenie partycji która nie ma alokacji)

2) Włączenie Ubuntu wersji Live -> Gparted -> Wybranie dysku z instalacją Ubuntu -> "resize/move" -> Rozciągnięcie partycji Ubuntu o wolne miejsce -> Uruchomienie zmian (warto wcześniej zrobić backup danych, u mnie poszło gładko i bez problemów)



---

Źródło:

[Is it okay to delete the ~/.cache folder?](https://askubuntu.com/questions/102046/is-it-okay-to-delete-the-cache-folder)

[How To Remove Old Snap Versions To Free Up Disk Space](https://www.linuxuprising.com/2019/04/how-to-remove-old-snap-versions-to-free.html)

[Add more disk space for linux from windows in a dual bootable machine](https://askubuntu.com/questions/871825/add-more-disk-space-for-linux-from-windows-in-a-dual-bootable-machine/871858)

[re-allocate partition space from windows to linux](https://askubuntu.com/questions/852395/re-allocate-partition-space-from-windows-to-linux)

[ubuntu-manuals](http://manpages.ubuntu.com/manpages/trusty/man1/df.1posix.html)