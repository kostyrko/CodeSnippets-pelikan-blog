Title: Git - aktualizacja sforkowanego repo
Author: mkostyrko
Date: 2020-07-11 10:00
Updated:
Category: git
Tags: git, branch, gałąź, github, git-hub, commit, github, system kontroli wersji, dev, git init
Slug: git-aktualizacja-forka
related_posts: git-gitignore, git-wprowadzenie, git-vsc-cofanie, git-galezie

![git-branch](https://i.morioh.com/2019/11/11/1f265e2d4c43.jpg)


### Aktualizacja sklonowanego repozytorium


Sprawdzenie remotów

        git remote -v

Dodanie kolejnego remota, z którego będą pobierane dane (tzw. upstream)

        git remote add upstream <link do remota>

Pobieranie info z dodanego/upstream remota

        git fetch upstream

Zmian (lub upewnienie się że jest się na gałęzi master lub tej gałęzi na której zależy nam aby była aktualna)

        git checkout master

        np. git checkout dev

Łączenie mastera (main) lub gałęzi z zawartością tego co znajduje się w repo z upstream

    git merge upstream/master

    np. git merge upstream/dev


Zaakceptowanie konfliktów na korzyść zmian zewnętrznych

        git checkout --theirs .
        git add .

Zaakceptowanie konfliktów na korzyść zmian wewnętrznych

        git checkout --ours .
        git add .


Wypushowanie zmian na remota


        git push origin master

        np. git push origin dev


Usunięcie konkretnego remota

        git remote rm <nazwa remota np. upstream>

---
Źródła:

[Start a new git repository](https://kbroman.org/github_tutorial/pages/init.html)

[Adding an existing project to GitHub using the command line](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)

[StackOverflow - How do I update a GitHub forked repository?](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository)
