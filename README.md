# Docker Compose

Vi skal i denne oppgaven sette sammen en enkel applikasjon bestående av en backend skrevet i Python, en frontend 
med JavaScript/HTML og en cache med Redis. I applikasjonen er det et klikkbart bilde, og en tekst under som viser hvor
mange ganger man har klikket på det. Frontenden sender beskjed til backend om et nytt klikk, og henter deretter det nye
totale antallet klikk. Backend er igjen integrert med Redis som holder styr på antall klikk. 

Vi skal bruke docker-compose for å kjøre disse komponentene og få dem til å snakke sammen.

Back- og frontendkomponentene er definert i henholdsvis `click-backend` og `click-frontend`, med hver sin Dockerfile.
I filen `docker-compose.yml` ligger det services for de tre komponentene vi skal bruke i løsningen.


## Oppgave 1
Først må vi få backenden til å kjøre, ved å legge til litt i filen `click-backend/Dockerfile`.

Prøv å bygge _click-backend_ med `docker build`- da vil det komme en feilmelding.
* Legg inn det som mangler og se at du får bygget imaget.

I Flask kjører serveren by default på localhost/127.0.0.1. Dette fungerer fint så lenge man kjører applikasjonen lokalt, 
men når man kjører den med Docker skal man kalle den fra utsiden av containeren. localhost er ikke tilgjengelig for
nettverkskall utenfra, så man må sette opp en annen adresse. 

* Sett en miljøvariabel `FLASK_RUN_HOST` med verdi `0.0.0.0`

## Oppgave 2
Vi skal nå starte komponentene ved hjelp av `docker-compose`. Dette gjøres ved å stå i rotmappa og kjøre kommandoen
`docker-compose up`. Det man derimot vil se er at de imagene som compose-filen inneholder ikke eksisterer.

* Bygg hver av de to komponentene med `docker build`. Pass på at navngivningen stemmer overens med _image_ i `docker-compose.yml`.
Kjør til slutt `docker-compose up` og se at begge komponentene starter opp.
(Vi har fortsatt ikke kommet helt dit at applikasjonen er tilgjengelig) 

Løsningsforslag:
```
$ docker build -t click-backend click-backend/
$ docker build -t click-frontend click-frontend/
$ docker-compose up
```

## Oppgave 3
Foreløpig skjer det jo ikke så veldig mye interessant når vi starter komponentene. Dette er fordi vi ikke har bundet 
portene i containerne til porter på maskinen.

* Legg inn portmapping for _click-frontend_ og _click-backend_ i `docker-compose.yml`. 
Se i Dockerfilene hvilke porter som er benyttet, og map disse til de samme portene.

Hvis du nå kjører `docker-compose up` skal du kunne gå til `localhost:3000` og se en nettside som kommer opp. 
I outputen fra `docker-compose` kan man se at requester kommer inn til backend, men feiler videre mot Redis.
Hvis du får opp nettsiden, men det ikke dukker opp noe tekst under bildet (og du ser en feil i konsollen i nettleseren),
er det et tegn på at frontenden og backenden ikke klarer å snakke sammen.

## Oppgave 4
Nå har vi fått til å kjøre applikasjonen vår, men har fortsatt ikke satt opp Redis.
* Legg inn en service for Redis i `docker-compose.yml` - bruk imaget `redis:alpine`. 
Pass på at servicen har samme navn som hosten spesifisert i tilkoblingen i `app.py`.

Når du så starter komponentene med `docker-compose up` skal klikktelleren fungere!

#### Litt tilleggsinfo
Merk at man her ikke trenger å publisere noen porter for Redis. 
Dette er fordi Docker-containere by default kan snakke sammen på portene som er exposed i containerne, 
basert på navnet til servicen.
Om man skulle kjørt backenden direkte på maskinen, hadde man måttet publisere en port mappet til den eksponerte i 
Redis-containeren, og bruke _localhost_ i stedet for _redis_ i tilkoblingen fra `app.py`.
(Grunnen til at man bruker _localhost_ i `ìndex.html` er at dette er kode som kjører i nettleseren på maskinen, 
og ikke fra selve Docker-containeren)

## Oppgave 5
Vi har nå en fungerende applikasjon som teller klikk, som vil peristere antall klikk hvis man stopper applikasjonen og 
starter den igjen. Dette er fordi containeren beholdes mellom kjøringene. 

Hvis man derimot stopper applikasjonen og kjører (bytt eventuelt ut `redis` hvis containeren din heter noe annet)
```
$ docker rm redis
```
og så starter igjen, vil tellingen være nullstilt. 
Vi skal nå sette opp et volum som gjør at data lagres også hvis containeren slettes.

* Legg inn konfigurasjon for _volumes_ for _redis_ i `docker-compose.yml`. Det skal mappes til pathen `/data` i containeren.
Du kan velge selv om du vil bruke et volume som du definerer nederst i filen, eller et bind mount som binder til en mappe på maskinen din.

## Oppgave 6
Sånn systemet vårt er satt opp til nå må vi manuelt bruke `docker build` for å bygge imagene før vi kan kjøre dem med 
`docker-compose`.
Hvis for eksempel noen andre skulle klonet repoet og startet applikasjonen, 
er dette litt upraktisk fordi det medfører flere manuelle steg.
For å unngå dette kan man legge til et parameter i `docker-compose.yml`, `build`, 
hvor man spesifiserer pathen på samme måte som man gjør til `docker build`.

* Legg til build-parameter for _click-backend_ og _click-frontend_.

Etter dette kan du slette alle images (med `docker rmi`) og kjøre `docker-compose up` igjen, og se at imagene bygges automatisk.


**NB!** 
Hvis du har sett nøye på outputen har du kanskje sett noen linjer som dette:
> WARNING: Image for service frontend was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

Dette vil si at imagene kun bygges hvis de ikke eksisterer allerede, så om man f.eks. gjør endringer i koden må man bruke
en av kommandoene over for å tvinge gjennom et nytt bygg.


#### Dette var siste oppgave, sjekk ut branch _docker-compose-oppgaver-fasit_ for løsningsforslag!
