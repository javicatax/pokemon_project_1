# pokemon_project_1

Pokemon challenge django-docker Django+SQLite3 with Docker

Welcome to Django+SQLite with Docker I'm attempting to create Django based web backend with SQLite3 database using Docker.

To run the project, you need to have Docker and Docker Compose installed.

Once Docker and Docker Compose is installed, run the following command:

$ cd pokemon_project_1 $ docker-compose up To start the containers in demon mode, use the following command instead:

$ docker-compose up -d Project Architecture There are two Docker containers linked with each other in this project:

web (for django files) db (for sqlite3 database) When you run docker-compose up, it builds these containers from Dockerfile, links them, installs the dependancies and starts the django apps. Pages Once the containers are running, you just have to get the docker IP (localhost or if you're running docker in boot2docker for mac or inside a VM then VM/boot2docker's IP, please keep in mind it has to be NATed/Bridged properly for this to function)

Then go to browser and type in the IP and port 8000:

:8000 Some pages for the site are:

:8000/admin :8000/api/pokemon_detail/<id_pokemon> :8000/api/pokemons (more to come)

Pokemons IDS available (id_pokemon):
12
