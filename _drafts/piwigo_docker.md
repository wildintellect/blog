---
date: '2020-09-08 15:00 -0700'
layout: post
title: Setup Piwigo with Docker
---

Photo gallery hosting

## Complicating Things

The basic components required:
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
