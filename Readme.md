# FantaliBOT

A discord bot for me and my friends

## Install

There are two type of install:
 - **manual**
 - **dockerize**

### Manual install 

Prerequisite:
 - python3.9
 - pip3
 - A mariadb database

You have to create a config.ini under ./config and complete the fields with your discord TOKEN and your database infos.
`config/config.sample.ini` can serve as example.
You have to install the dependencies with `pip install -r requirements.txt`

### Dockerize install

Prerequisite:
 - docker
 - docker-compose

You just have to `cp config/config.sample.ini config/config.ini` and change the value of the discord token.
Be aware if you change any fields about the database you have to change it in docker-compose.yaml too!
Then just launch `docker-compose up -d`

PS: It's normal if the bot restart copple of times if db is not fully started. Wait 30 seconds.
