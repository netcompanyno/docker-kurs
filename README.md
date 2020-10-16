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