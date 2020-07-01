Title: Git - tworzenie gałęzi (branch) i angaż (commit)
Author: mkostyrko
Date: 2020-07-01 10:00
Updated:
Category: git
Tags: git, branch, gałąź, github, git-hub, commit, github, system kontroli wersji, dev
Slug: git-galezie
related_posts: git-gitignore, git-wprowadzenie, git-vsc-cofanie

![git-branch](https://i.stack.imgur.com/F00b8.png){: height="300px"}

System kontroli wersji jakim jest GIT (nie jest to akronim, a znaczenie tego słowa w kontekście IT jest dyskusyjne - ja trzymam się tej wersji, że jest ono połączone z brytyjskim slangiem oznaczającym bękarta - [patrz wikipedia](https://en.wikipedia.org/wiki/Git_(slang))) pozwala na różne ścieżki rozwoju przygotowywanego "produktu" i najbardziej ogólnie można ująć tą kwestię stwierdzając, że może być ona liniowa (rozwój odbywa się na jedynej gałęzi (Master/**Main**)) jak i nieliniowa (oparta na równoległych gałęziach pobocznych tzw. niewolniczych(slave) lub też **secondary)**. To właśnie ta druga historia rozwoju jest przedmiotem tego wpisu

---

### Metadane

Pokaż wszystkie gałęzie

    git branch -a

Wynik pokazuje te lokalne oraz remotes (-a -> all, jeśli mają być jedynie remotes to wówczas flaga -r)


Jeśli chcemy zobaczyć dokonane commity należy wpisać

    git show-branch


W wyniku tego widzimy wiadomości powiązane z commitami oraz w jakich gałęziach się one znalazły

---
### Trawersowanie

Jeśli chcemy przełączyć się na wybraną gałąź należy wpisać

    git checkout <nazwa gałęzi>


Przykładowo


    git checkout master

---
### Tworzenie


Jeśli checmy stworzyć nową gałąź i się na nią również przełączyć to należy wpisać

    git checkout -b <nazwa głęzi>

np.

    git checkout -b issue_1.7

Jeśli chcemy stworzyć gałąź z konkretnej gałęzi wówczas należy ją wskazać po nazwie nowej gałęzi

    git checkout -b <nazwa nowej gałęzi> <nazwa gałęzi, której ma wychodzić>

Przykładowo

    git checkout -b issue_1.7 dev

Następnie

        git push origin < nazwa nowej gałęzi >

---
### Usuwanie

Usuwanie gałęzi

    git push origin --delete <nazwa gałęzi>

Przykładowo

    git push origin --delete issue_1.5

lub jeśli jedynie lokalnie (wcześniej należy przełączyć się na inną gałąź)

    git branch -d <nazwa gałęzi>

    lub

    git branch -D <nazwa gałęzi> // jeśli zachodzą pojawiają się ostrzeżenia ale jesteśmy pewnie swojej decyzji

    >> Deleted branch issue_1.5 (was 9ef25f3).

---
### Angażowanie

Faza przejściowa => stage oraz komitowanie

-m -> --message/wiadomość
-a -> --all wszystkie (pliki trafiają na stage/etap przejściowy )

więcej wyjaśnieni skrótów można znaleźć w [explainshell](https://explainshell.com/explain/1/git-commit)

    git commit -a -m 'treść wiadomości'

alternatywnie można skorzystać z komendy

    git add -A

Spowoduje, że pliki, które do tej pory były edytowane (zawierają zmiany) trafią do stadium przejściowego (ich zmiana jest zauważona i odnotowana lokalnie) i wymagają wypchnięcia do remote repo jeśli mają być widoczne dla innych. Można tego dokonać poprzez...

        git commit -m "treść wiadomości"

---

### Wizualizacja gałęzi

Wizualizacja repo przy pomocy git-grafu


        git log --all --decorate --oneline --graph


![DOG](https://i.stack.imgur.com/ElVkf.jpg)

---
Źródła:

[Git-Branch](http://blog.pjuskiewicz.com/2019/01/26/git-branch/)

[Easily rename your Git default branch from master to main](https://www.hanselman.com/blog/EasilyRenameYourGitDefaultBranchFromMasterToMain.aspx)


https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs

https://stackoverflow.com/questions/4470523/create-a-branch-in-git-from-another-branch