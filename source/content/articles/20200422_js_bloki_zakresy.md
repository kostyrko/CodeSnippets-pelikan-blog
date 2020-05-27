Title: JavaScript - bloki i zakres
Author: mkostyrko
Date: 2020-04-22 10:00
Updated:
Category: javascript
Tags: javascript, blocks, scopes, zakres, blok
Slug: js-blok-zakres
related_posts: js-funkcja

Instrukcja blokowa (ang. blocks) - blok służy do grupowania wyrażeń i jest kodem zamkniętym w nawiasach klamrowych. Przykładem bloku kodu jest funkcja lub instrukcja if.

Zmienna znajduje się w zasięgu funkcji jeśli zamknięta jest w tym samym bloku kodu jak i wówczas gdy znajduje się po za nim.

### Zakres/scope

*Zakres (scope)* jest kontekstem, w którym dana zmienna jest zadeklarowana.
*Zakres blokowy* odnosi się do zmiennej, która jest dostępna w ramach bloku.
*Zmienne o globalnym* zakresie zadeklarowane są po za blokiem.

        const droid = "R2D2"

        const droidSeeker = () => {
                return droid; // R2D2
        }

        console.log(droidSeeker()) // = R2D2

Gdy zmienna jest deklarowana wewnątrz bloku, wówczas jest osiągalna jedynie tam i jest zwana lokalną zmienną. Zmienna zadeklarowana globalnie jest dostępna w trakcie całości wykonywania się programu (zużycie pamięci + możliwość zmiany), w przypadku zmiennej lokalnej tak nie jest.

Zmiana zmiennej w funkcji

        let droid = "R2D2";

        const droidSeeker = () => {
        droid = "C3PO"; // Take note of this line of code
        console.log(droid);
        };

        logNum(); // > C3PO
        console.log(num); // > C3PO

Deklarowanie zmiennej w ramach bloku pozwala na tworzeni czystszego kodu, łatwiejszego w utrzymaniu (dana zmienna jest odpowiedzialna za wybrany fragment kodu), pozwala na tworzeni kodu w sposób modułowy.

        const droidSeeker = () => {
        const smallDroid = true;
        let droid = 'C3PO'; 
        if (smallDroid) {
        let droid = 'R2D2';
        console.log(droid); // R2D2
        }
        console.log(droid); // C3PO
        };

        console.log(droid); // ReferenceError

*Global namespace* - odnosi się do przestrzeni, w której przechowywane są nazwy zmiennych o globalnym zasięgu.

<!-- Domknięcia/Closures -->

---

Źródła:

https://developer.mozilla.org/pl/docs/Web/JavaScript/Guide/Control_flow_and_error_handli

http://blog.nebula.us/13-javascript-closures-czyli-zrozumiec-i-wykorzystac-domkniecia