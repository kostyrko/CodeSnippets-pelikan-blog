Title: VSC - edytowanie barw motywu
Author: mkostyrko
Date: 2020-03-29 23:30
Updated:
Category: VSC
Tags: vsc, visual studio code, visual studio, edycja, motyw, theme, brawa
Slug: vsc-edytowanie-barw-motywu
related_posts: vsc-skroty-klawiszowe, vsc-dodawanie-fontu

W ciągu dnia w Visual Studio Code korzystam jasnego motyw *Github Light Theme - Gray*. Uznałem jednak, że główny panel okna jest dla mnie za jasny, a różnica barwna pomiędzy panelem bocznym a głównym jest dla mnie za mała.
Postanowiłem nadpisać wybrane przeze mnie zmienne w pliku przechowującym spersonalizowane ustawienia VSC `settings.json`
Aby go odnaleźć wystarczy otworzyć ustawienia (np. CTRL+,) i wpisać nazwę wspomnianego pliku, a następnie wybrać opcję `Edit in settings.json`

    Command Palet -> Developer: Generate Color Theme From Current Settings

Pomocy narzędzia `Generate Color Theme From Current Settings` wywołałem plik jsonowy ze wszystkimi ustawieniami wykorzystywanego motywu. Do w pliku settings.json odwołałem się do zmiennej `workbench.colorCustomizations` w sposób przedstawiony jak poniżej, gdzie wkleiłem odpowiednie zmienne, które edytowałęm (opatrzone poniżej przeze mnie komentarzami - zostawiłem również te, których nie zmieniałem dla ogólnej orientacji). W ten sposób nadpisałem ustawienia wykorzystywane motywu

    "workbench.colorTheme": "Github Light Theme - Gray",
    "workbench.colorCustomizations": {
        "[Github Light Theme - Gray]": {

            "editor.background": "#ebebeb", // główne okno edytora
            
            "activityBar.background": "#d1d1d1", // boczny pasek z ikonami
            
            "activityBar.border": "#e0e0e0", // granica bocznego paska
            "activityBar.foreground": "#000000", // kolor ikon na bocznym pasku
            "activityBarBadge.background": "#ac3b46", // ikona wskazująca na aktywność na bocznym pasku

            "button.background": "#d73a49",
            "button.foreground": "#f0f0f0",
            "dropdown.background": "#f0f0f0",
            "dropdown.border": "#b2b2b2",
            "dropdown.listBackground": "#f0f0f0",
            
            "editor.foreground": "#000000",
            "editor.lineHighlightBackground": "#f0ecd0", // linia podświetlająca miejsce edycji
            "editor.lineHighlightBorder": "#f0ecd0",
            "editor.selectionBackground": "#fed442", // podświetlenie zaznaczonej linii
            "editorGroup.border": "#f0f0f0",
            "editorGroupHeader.noTabsBackground": "#f0f0f0",
            "editorGroupHeader.tabsBackground": "#f0f0f0",
            "editorGroupHeader.tabsBorder": "#f0f0f0",
            "editorLineNumber.activeForeground": "#000000",
            "editorLineNumber.foreground": "#aaa9a9", // numeracja linii w edytorze

            "editorSuggestWidget.highlightForeground": "#d73a49",
            "editorSuggestWidget.selectedBackground": "#e1e1e1",
    
            "editorWidget.background": "#f0f0f0",
            "editorWidget.border": "#000000",

            "focusBorder": "#f0f0f000",
            "foreground": "#000000",
            "input.background": "#f0f0f0",
            "input.border": "#b2b2b2",
            
            "list.activeSelectionBackground": "#cccccc", // podświetlenie wybranego pliku na bocznym menu
            "list.activeSelectionForeground": "#000000", // kolor fontu wybrengeo przedmiotu w bocznym menu
            "list.focusBackground": "#dfdfdf",
            "list.focusForeground": "#d73a49",
            "list.highlightForeground": "#d73a49",

            "list.hoverBackground": "#c2c2c2", // podświetlenie najechanego myszką przedmiotu w bocznym menu
            "list.hoverForeground": "#fcfcfc", // kolor fontu j.w.
            
            "list.inactiveSelectionBackground": "#d6d6d6", // kolor tła wybranego przedmiotu - obecnie będącego w edycji
            "list.inactiveSelectionForeground": "#d73a49", // kolor fontu j.w.
            
            "notificationCenter.border": "#f0f0f0",
            "notificationCenterHeader.background": "#f0f0f0",
            "notificationToast.border": "#f0f0f0",
            "notifications.background": "#f0f0f0",
            
            "notifications.border": "#f0f0f0",
            "panel.border": "#d73a49",

            "scrollbar.shadow": "#f0f0f0",
            
            "sideBar.background": "#e4e4e4", // tło bocznego menu !!!
            "sideBar.border": "#e0e0e0", // granica bocznego menu
            "sideBar.foreground": "#000000",
            "sideBarSectionHeader.background": "#ebebeb", // kolor paska sekcji

            // dolny pasek
            "statusBar.background": "#e4e4e4", // kolor tła dolnego paska
            "statusBar.border": "#e0e0e0",
            "statusBar.debuggingBackground": "#f0f0f0",
            "statusBar.debuggingForeground": "#000000",
            "statusBar.foreground": "#000000",
            "statusBar.noFolderBackground": "#f0f0f0",
            "statusBar.noFolderForeground": "#000000",

            "tab.activeBackground": "#f0f0f0",
            "tab.activeBorder": "#d73a49",
            "tab.border": "#f0f0f0",
            "tab.inactiveBackground": "#f0f0f0",

            
            "titleBar.activeBackground": "#f0f0f0",
            "titleBar.activeForeground": "#000000",
            "titleBar.border": "#f0f0f0",
            "titleBar.inactiveBackground": "#f0f0f0",
            "titleBar.inactiveForeground": "#000000",
        }
    }

Źródła:

https://stackoverflow.com/questions/35165362/how-to-edit-default-dark-theme-for-visual-studio-code

https://css-tricks.com/creating-a-vs-code-theme/

https://www.youtube.com/watch?v=3Ju74i1MyBg

https://www.youtube.com/watch?v=4hdJwHZNDT4

https://www.youtube.com/watch?v=EZHg7Uv-0-8

