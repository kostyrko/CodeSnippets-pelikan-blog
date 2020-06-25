Title: HTML -> zasady dostępności (ang. Accessibility)
Author: mkostyrko
Date: 2020-06-23 11:00
Updated:
Category: html
Tags: 
Slug: html-dostepnosc
related_posts: 


  ![accessibility](https://miro.medium.com/max/1400/1*kxPPtGoUuY2EX41DbQMLOw.jpeg#center){: height="300px"}

Kwestia *dostępności* (ang. accessibility) jest związana z takim tworzeniem stron internetowych (w tym w dużej mierze odpowiedniej struktury HTML) aby osoby posiadające różnego rodzaju zaburzenia (np. widzenia) lub problemami z motoryką ciała w możliwie jak najprostszy sposób mogły z nich korzystać.

Do osób wykluczonych zaliczyć można:

* osoby niepełnosprawne sensorycznie

* osoby niepełnosprawne manualnie

* osoby niepełnosprawne intelektualnie

* seniorów

* obcokrajowców

* osoby niezamożne

Podstawowym dokumentem jest [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/), w którym określono wymogi jakie należy spełnić projektując możliwie szeroko dostępne strony internetowe.

---

Podstawowe i najważniejsze zasady:

Stosowanie **semantycznego HTML** oraz przypisywania tagom odpowiednich im atrybutów informujących użytkownika o treści w nich zawartych w dodatkowy sposób.

Należy również pamiętać o kwestii wizualnej - stosowanie odpowiedniego kontrastu (osoby niedowidzące) oraz o znacznym ograniczeniu animacji (zaburzenia neurologiczne - epilepsja).

Treść strony internetowej oraz jej układ również ma znaczenie - powinna być przekazana w możliwie najprostszy sposób.

---

#### Skrót ogólnych zasad

#### Obraz

Jeśli obraz jest istotnym elementem tekstu powinien zostać dodany przy pomocy taga `img` i posiadać atrybut `alt` (tekst będący alternatywą dla obrazu - powinien opisywać to co się na nim znajduje). Obrazy będące jedynie ozdobnikami należy załączać przy pomocy CSS i `background`. 

::: Warto pamiętać, że animacje oraz jaskrawe kolory mogą użytkowników rozproszyć lub wywołać padaczkę. :::

#### Dźwięk i wideo

Nagrania różnego typu (sam dźwięk jak i wideo) powinny posiadać transkrypcje.

Elementy strony sterujące odtwarzaniem dźwięku oraz obrazu winny być widoczne i łatwo dostępne, również przy pomocy klawiatury jak i czytnika.

### Nawigacja i poruszanie się po stronie

Istotne jest to aby elementy posiadały opcję **focusu**, a przechodzenie pomiędzy kolejnymi elementami strony było dostępne z poziomu **klawiatury**. 

::: `Taindex` pozwala na nadanie wyższego priorytetu dostępności przy pomocy klawisza TAB. :::

Sama nawigacja powinna być skonstruowana według jednej zasady.

Odnośniki powinny być jasno oznaczone i zrozumiałe/wytłumaczone.

Strona powinna posiadać możliwość powiększenia (np. przy pomocy przeglądarki) w sposób responsywny.

### Konstrukcja strony

Strona winna posiadać odpowiedni `title` oraz oznaczenie języka `lang`, powinno stosować się nagłówki `h1-h6` mając na uwadzę znaczenie treści, którą reprezentują. Treść powinna być porządkowana przy pomocy `list` (klamra semantyczna). Tabele powinny posiadać wszystkie elementy (np. nagłówek) i służyć jedynie do prezentowania treści oraz danych. Formularze powinny posiadać podpisy `label`.


#### Barwy

Bardzo ważne jest stosowanie odpowiedniego kontrastu pomiędzy wykorzystanymi barwami tak aby miały odpowiedni kontarast

patrz na narzędzie -> [Contrast Checker](https://webaim.org/resources/contrastchecker/)

#### Treść

`visibility: hidden` oraz `display: none` nie powinny być stosowane do ukrywania dużej ilości tekstu (są ignorowane przez czytniki)

`<b>` - wyróżniamy tekst na stronie

`<i>`- wyróżnienie słowa w treści tekstu

`<strong>` - wzmocnienie znaczenia na stronie (całe zdanie)

`<em>`- wyróżnienie słowa w treści w tekście (część zdania)

`<ins>` - oznacza tekst dodany (insertion) zawierające atrybuty `cite` (metadane zmian) i `datatime`

    <ins cite="github.io..." datetime="2222-02-02"> Zaktualizowano 2020-06-26 </ins>

`<del>` - usunięcie - te same zasady co dla `<ins>`

    <del cite="github.io..." datetime="2222-02-02"> Zaktualizowano 2020-06-26 </del>

`<s>` - strike-through/przekreślenie - oznaczenie już niekatulanej informacji

`u` - underline/podkreślenie - imiona lub specjalnie wstawione w tekst błędy językowe

---
### Atrybuty WAI-ARIA -> Accessible Rich Internet Applications.

Standard mający na uwadzę dostępność i użyteczność stron internetowych dla tzw wykluczonych cyfrowo

Poprzez przypisanie ról do poszczególnych elementów HTML współpracuje z czytnikami stron -> te dzielą się na 4 kategorie **abstract**, **widget** (wszystko to co odpowiada za interaktywność strony), **landmark roles** (regiony dokumentu) i **document structure roles** (struktura dokumentu)

Stany kontrolowane są przy pomocy JS - jednak istnieją atrybuty, które w przypadku niezaładowania JS działają w zbliżony i określony sposób np `aria-hidden=""`

| atrybut | znaczenie |
|---|---|
| `<div role="banner">` | przypisanie znaczenia np. banneru/dialogu/prezentacji/navigacji |
| `aria-hidden="true"`| ukrycie elementu | 
| `aria-haspopup="true"` | posiada okno wyskakujące | 
| `aria-haspopup="true"` | posiada okno wyskakujące | 

---

Czytaj więcej tutaj [Things I learned by pretending to be blind for a week](https://silktide.com/blog/things-i-learned-by-pretending-to-be-blind-for-a-week/)

---
Źródła:

[WAVE (Web Accessibility Evaluation Tool)](http://wave.webaim.org/)

[Imitacja czytnika stron - wtyczka Chrome](https://chrome.google.com/webstore/detail/chromevox/kgejglhpjiefppelpmljglcjbhoiplfn?utm_source=chrome-app-launcher-info-dialog)

https://developer.mozilla.org/en-
US/docs/Web/Accessibility/ARIA

https://developer.mozilla.org/pl/docs/Web/Dost%C4%99pno%C5%9B%C4%87

http://users.uj.edu.pl/~konior/tech_www/disabled/dostepnosc1.html#_Toc319571640

http://www.pad.widzialni.org/narzedziownia

http://dostepnestrony.pl