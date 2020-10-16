Docker
======

I disse oppgavene skal vi bygge image basert på en Dockerfile, 
kjøre en container, utføre noen kommandoer mot containeren, og rydde opp etter oss.

Videre skal vi gjøre noen endringer i Dockerfile, og sjekke at vi oppnår ønsket resultat.

For å kunne gjøre dette fra lokalt klient må vi først installere Docker. 
Instruksjoner for oppsett finnes [her](OPPSETT.md)


Oppgave 1
------

1.1 Bygg et image med tag 1.0.0 basert på [denne](javascripteksempel/Dockerfile) Dockerfilen

`Hint: docker build -t`
```shell script
Løsningsforslag oppgave 1
$ docker build -t javascripteksempel:1.0.0 javascripteksempel/.
```

1.2 Kjør en detached container med navn webapp basert på imaget du har bygget
```shell script
Løsningsforslag oppgave 1
$ docker run -d --name webapp javascripteksempel:1.0.0
```

1.3 Sjekk at containeren kjører
```shell script
Løsningsforslag oppgave 1
$ docker ps
```

1.4 Sjekk logger og status fra containeren
```shell script
Løsningsforslag oppgave 1
$ docker logs webapp
$ docker container stats webapp
```

### Oppgave 2

2.1 Åpne et shell mot containeren, og sjekk at javascript- og htmlfilene ligger der de skal

2.2 Stopp og slett containeren, la imaget fra oppgave 1 ligge
