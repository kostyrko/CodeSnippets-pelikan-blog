Title: .gitignore
Author: mkostyrko
Date: 2020-03-25 22:00
Updated:
Category: git
Tags: gh-pages, git, github, github pages, system kontroli wersji
Slug: git-gitignore
related_posts: git-wprowadzenie

![git-logo](https://buddy.works/guides/thumbnails/cover-first-steps-git.png)


`.gitignore` - plik o takiej dokładnie nazwie (rozszerzenie bez nazwy), które zawiera reguły wykluczające z systemu kontroli wersji - GIT konkretne pliki oraz foldery innymi słowy te, której mają być ignorowane przez git. 
Sam plik powinien znajdować się w folderze źródłowym.

Sposoby na wykluczenie

pliki: 
    
    .gitignore
    .vscode

pliki po rozszerzeniu tzw. dzika karta:

    *.txt

`~` - kończące się na daną frazę

    index.html~

`!` - negacja np. wykazanie pliku, który ma nie być ignorowany

    !nowy_folder/nowy_plik.txt

foldery: 

  `nazwa_folderu/`

`**` - każda ilość folderów

    **/folder

    logs/**/*.log

`#` - komentarz

    # to jest komentarz

---

Źródła:

https://www.pluralsight.com/guides/how-to-use-gitignore-file

https://git-scm.com/docs/gitignore

https://www.atlassian.com/git/tutorials/saving-changes/gitignore

https://www.coderomeos.org/gitignore-file-and-its-usage