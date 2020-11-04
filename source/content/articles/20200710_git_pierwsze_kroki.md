Title: Git - pierwsze kroki
Author: mkostyrko
Date: 2020-07-10 10:00
Updated:
Category: git
Tags: git, branch, gałąź, github, git-hub, commit, github, system kontroli wersji, dev, git init
Slug: git-pierwsze-kroki
related_posts: git-gitignore, git-wprowadzenie, git-vsc-cofanie, git-galezie

![git-branch](https://i.morioh.com/2019/11/11/1f265e2d4c43.jpg)

### Git lokalnie

0. Instalacja GITa

1. Stworzenie folderu na dysku

2. Wewnątrz folderu zainicjowanie projektu GIT wpisując w linię komend

        git init

Istnieje parę możliwości rozegrania kolejnych kroków

3. Można najpierw sprawdzić czy w danym repozytorium posiadamy pliki, które nie są zapisane (untracked)

        git status

4. Następnie dodać pliki do przestrzeni roboczej (stage)

        git add .

5. Można cofnąć plik z przestrzeni roboczej używając komendy

        git reset HEAD >>Nazwa-Pliku-Do-Cofnięcia<<

6. Następnie można wykonać commita (zapisanie zmian) -> m (od message)

        git commit -m "First commit"

---

### Git + GitHub


7. Stworzenie "gołego" repo na GitHubie (bez README, licencji etc.) -> Skopiowanie jego URL


8. Wskazanie lokalnie ścieżki do tzw "remot'a" (zdalen repo)


        git remote add origin >>URL<<


9. Można zweryfikować połączenie z remotem poprzez użycie komendy (zwrotną informacją powinien być link do origin)


        git remote -v


10. Wypchnięcie zmian do origina/remota odwołując się do maina (wcześniej master)


        git push origin main


---
Źródła:

[Start a new git repository](https://kbroman.org/github_tutorial/pages/init.html)

[Adding an existing project to GitHub using the command line](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)


