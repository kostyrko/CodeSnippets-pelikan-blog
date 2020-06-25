Title: CSS - neumorphism
Author: mkostyrko
Date: 2020-04-07 11:00
Updated:
Category: css
Tags: css, neumorphism, style, ux 
Slug: css-neumorphism
related_posts: html-dostepnosc

Neoumorphism jest sposobem stylizacji elementów stron nawiązujący swoją estetyką znaną z środowiska różnego rodzaju smartfonów, choć w duże mierze przymina mi głównie te z nadgryzionym jabłkiem. Poprzez grę cieni ten styl stara się wywołać efekt estetycznej trójwymiarowości gdzie poszczególne elementy są wypukłe lub wklęsłe a ich kształty są obłe lub też zaokrąglone. Neoumorphism wywodzi się z skeuromorfizmu (gr. skeúos "naczynie, przedmiot" + morphé "postać, kształt") stylistyki, ktra miałą nawiązać do istniejących w świecie realnym przedmiotów.

Polecam [generator tego stylu](https://neumorphism.io/#55b9f3) do zapoznania się z tym w jaki sposób można uzyskać wyżej opisany efekt

Zwróć uwagę, że również ja ten styl zastosowałem na tej stronie. Używając poniższej deklaracji wystylizowałem pasek wyszukiwania

    background: #f5f5f5;
    box-shadow: inset 4px 4px 4px #d0d0d0, inset -4px -4px 4px #ffffff;

---

O ile styl neomorfistyczny może wydawać się miły dla oka, należy pamiętać, że nie jest on najbardziej przystępny w odbiorze dla osób z zaburzeniami wzroku - zatem należy pamiętać o stosowaniu odpowiedniego kontrastu, który znajduje się w zgodzie z wytycznymi związanymi z dostępnością/accessibility.
Więcej na temat [neumorphismu i dostępności](https://axesslab.com/neumorphism/) 


---

Źródła:

https://uxplanet.org/the-ground-breaking-possibilities-with-neumorphism-9ed9e64c2513

https://uxdesign.cc/neumorphism-in-user-interfaces-b47cef3bf3a6

https://pl.wikipedia.org/wiki/Skeumorfizm

https://css-tricks.com/neumorphism-and-css/