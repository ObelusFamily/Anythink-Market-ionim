# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup
* Install docker 
    * According to your OS follow the instructions at https://docs.docker.com/get-started/#download-and-install-docker
* Clone repo (you probably already did it since you can read this)
* Run from repo ```docker-compose up -d```
* Check the backend is up
    * Open http://localhost:3000/api/ping in your local browser it should return Pong! (as a json output)
* check the frontend is up
    * open http://localhost:3001/register in your local browser 
    * create a new user
    
