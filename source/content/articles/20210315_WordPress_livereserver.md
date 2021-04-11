Title: Wordpress: serwowanie strony na żywo
Author: mkostyrko
Date: 2021-03-15 14:00
Updated:
Category: wordpress
Tags: wordpress, php, local, flywheel, live server
Slug: wordpress-live-server
related_posts: 

![live-server](https://ritwickdey.gallerycdn.vsassets.io/extensions/ritwickdey/liveserver/5.6.1/1555497731217/Microsoft.VisualStudio.Services.Icons.Default)

W trakcie tworzenia strony/motywu w Wordpressie aby wykorzystać podgląd zmian na żywo można skorzystać np. z Webpacka, skonfigurowanego pod to zadanie, ale prostszym sposobem jest wykorzystanie wtyczki Live server z VSC marketplace + wtyczki o tej samej nazwie z np. chrome webstore.

Wykorzystanie obu jest dość proste:

1) serwujemy php np. przy pomocy narzędzia Flywheel (w wersji pro istniej możliwość serwowania w wersji live)

2) Wybieramy plik php do serwowania przez wtyczkę [Live Server](https://github.com/ritwickdey/vscode-live-server) (Ctrl+Shift+P -> Live Server: Open with Live Server)

3) Wykorzystując wtyczkę [Live Server Web Extension](https://chrome.google.com/webstore/detail/live-server-web-extension/fiegdmejfepffgpnejdinekhfieaogmj) w chromę/firefox wpisujemy hosta podstawowego (w pierwszym inpucie np. ten serwowany przez Flywheel) oraz tego z wtyczki Live Server VSC (np. 127.0.0.1:5501 ) w górnej części okna zaznaczamy opcję Live Reload i teraz możemy na żywo obserwować zmiany jak zachodzą na naszym podstawowym serwerze (tym hostowanym przez Flywheel np. localhost:10008)


---

Źródła:

[Live Server Web Extension](https://chrome.google.com/webstore/detail/live-server-web-extension/fiegdmejfepffgpnejdinekhfieaogmj/related)

[Visual Studio Code – PHP — Live Server — Automatyczne odświeżanie strony WWW](https://www.youtube.com/watch?v=0yJxdszD09o)

Webpack:

[Learn Webpack Pt. 6: Cache Busting and Plugins](https://www.youtube.com/watch?v=qXRGKiHmtF8&list=RDCMUCrqAGUPPMOdo0jfQ6grikZw&start_radio=1&t=709s)