Title: Git - cofanie commita w VSC
Author: mkostyrko
Date: 2020-06-24 12:00
Updated:
Category: git
Tags: git, cofanie commita, github, git-hub, commit, github, system kontroli wersji
Slug: git-vsc-cofanie
related_posts: git-gitignore, git-wprowadzenie

![git-logo](https://buddy.works/guides/thumbnails/cover-first-steps-git.png#center){: height="300px"}

Na co dzień korzystam z zestawu VSC + GitHub

Bywa tak, że chcę usunąć ostatni dodany przez nas commit lub cofnąć daną gałąź do określonego commita usuwając wszystkie, które po nim nastąpiły.

Aby cofnąć daną gałąź o jeden commit wystarczy wpisać

    git reset --hard HEAD~1

a jeśli zależy nam na konkretnym commicie to wówczas

    git reset --hard <adres commita>

Zachodzi wówczas sytuacja, w której repozytorium znajdujące się na GitHubie jest "do przodu" względem tego, które znajduje się u mnie na dysku lokalnym - sygnalizuje to min. ikona w lewym dolnym rogu jeśli teraz dokonam synchronizacji (Synchronise Changes)

![synchronizacja zmian](https://i.stack.imgur.com/P5VKm.png)

vsc zrobi `pull` a następnie `push` - repo wróci do stanu sprzed cofnięcia commita. Stąd zamiast tego muszę zrobić tzw twardy (lub przy użyciu siły push) korzystając z komendy:

    git push origin HEAD --force

dzięki niej repozytorium zostanie sprowadzone ("wyzerowane") do tego stanu jaki mam u siebie na dysku lokalnym

Warto pamiętać o tym, że można dodać własne komendy do narzędzia (Synchronise Changes) przy pomocy `.gitconfig`

---
Źródła:

https://stackoverflow.com/questions/1338728/delete-commits-from-a-branch-in-git

https://stackoverflow.com/questions/36878344/what-does-git-sync-do-in-vscode

https://evilmartians.com/chronicles/git-push---force-and-how-to-deal-with-it