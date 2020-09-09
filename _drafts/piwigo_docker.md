---
date: '2020-09-08 15:00 -0700'
layout: post
title: Setup Piwigo with Docker
---

Photo gallery hosting

## Complicating Things

The basic components [required](https://piwigo.org/doc/doku.php):
* Web Server
  * With Php
* MariaDB install
* Piwigo install
* Some place to store the photos, web logs, database files.

I could just load up a basic Linux image and script the initial install, and copy over the existing image directory, then import the existing database dump. But why make things simple when you can Dockerize.

So for this I'd need:
* Piwigo Docker image (presumably with Nginx or Apache?)
* MariaDB Docker
* Docker Volume to store the files across restarts
* Docker compose to weave it all together
* Some plan for how to import the data to the volume and the db

### Options

* https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host
but I don't think we want a bind mount, we want a proper volume as part to the compose
https://docs.docker.com/storage/volumes/

Where to get the Docker images:
* https://fleet.linuxserver.io/image?name=linuxserver/mariadb
* https://hub.docker.com/r/linuxserver/piwigo
* https://github.com/mathieuruellan/docker-piwigo <- uses apache
* https://github.com/moritzheiber/piwigo-docker <- runs php as a service

Nginx or Apache2?
* Nginx seems rare https://piwigo.org/forum/viewtopic.php?pid=162898
*

The problem with installing piwigo inside a docker is that it needs to update the container every time there's an upgrade? Or can the install be done writing to a docker volume of a webserver container, and then work more normally?
