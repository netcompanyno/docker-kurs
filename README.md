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
Kjør til slutt `docker-compose up` og se at alle tre komponentene starter opp. 
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
Som man kan se fra webappen og fra loggene får ikke backenden kontakt med Redis selv om Redis kjører.
Det er fordi det mangler en mapping mellom portene her.

* Legg inn en portmapping for _redis_ i `docker-compose.yml`.
(Hint: du kan se hvilken port som er eksponert i containeren med  `docker ps` etter å ha startet den opp, 
og hvilken port man prøver å koble til i kildekoden til backendkomponenten)
