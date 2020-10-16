Docker
======

I disse oppgavene skal vi bygge image basert på en Dockerfile, 
kjøre en container, utføre noen kommandoer mot containeren, og rydde opp etter oss.

Videre skal vi gjøre noen endringer i Dockerfile, og sjekke at vi oppnår ønsket resultat.

For å kunne gjøre dette fra lokal klient må vi først installere Docker. 
Instruksjoner for oppsett finnes i [OPPSETT.md](OPPSETT.md).


Oppgave 1
------

1.1 Bygg et image med tag 1.0.0 basert på [denne Dockerfilen](javascripteksempel/Dockerfile).

`Hint: docker build -t`

1.2 Kjør en detached container med navn webapp basert på imaget du har bygget

1.3 Sjekk at containeren kjører

1.4 Sjekk logger og stats fra containeren
