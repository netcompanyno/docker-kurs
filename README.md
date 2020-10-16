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

1.4 Sjekk logger og stats fra containeren
```shell script
Løsningsforslag oppgave 1
$ docker logs webapp
$ docker container stats webapp
```

### Oppgave 2

2.1 Åpne et shell mot containeren, og sjekk at JavaScript- og HTML-filene ligger der de skal

```shell script
Løsningsforslag oppgave 2
$ docker exec -it webapp sh

# ls 
```

2.2 Stopp og slett containeren, la imaget fra oppgave 1 ligge

```shell script
Løsningsforslag oppgave 2
$ docker stop webapp
$ docker rm webapp
```

### Oppgave 3
3.1 Kjør container med en portåpning mot port 3000
```shell script
Løsningsforslag oppgave 3
$ docker run -d --name webapp -p 3000:3000 javascripteksempel:1.0.1
```

3.2 Sjekk at du kan åpne webapplikasjonen fra nettleser
```shell script
Løsningsforslag oppgave 3
$ curl localhost:3000
```
eller åpne http://localhost:3000/ i en nettleser.

### Oppgave 4
4.1 Som man kan se hvis man åpner webappen i en nettleser, mangler applikasjonen i [eksempelet](/javascripteksempel) 
en fil for å fungere som ønsket.  
Utvid Dockerfilen med en kommando som kopierer innholdet fra public-mappen inn i containeren.

3.2 Bygg nytt image med tag 1.0.1
```shell script
Løsningsforslag oppgave 3
$ docker build -t javascripteksempel:1.0.1 javascripteksempel/
```

3.2 Kjør en container basert på det nye imaget du har bygget
```shell script
Løsningsforslag oppgave 3
$ docker run -d --name webapp javascripteksempel:1.0.1
```

Dockerfile fra oppgave 3
```Dockerfile
FROM node:alpine

WORKDIR /app

COPY app.js package.json package-lock.json index.html ./

COPY ./public ./public

RUN npm install

USER node

EXPOSE 3000

CMD ["npm", "start"]
```
