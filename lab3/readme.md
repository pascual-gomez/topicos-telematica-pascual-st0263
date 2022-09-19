# ST263: Tópicos Especiales en Telemática
Students: Pascual Gómez, pgomezl@eafit.edu.co

Professor: Edwin Montoya, emontoya@eafit.edu.co

## Lab 3: Containers - Docker - Wordpress - Domains - SSL
Build, deploy and manage apps using containers (Docker)

For this laboratory, we deployed a webserver using nginx, docker, let's encrypt, wordpress and mysql.

Nginx is being used as a reverse proxy, let's encrypt as certificate authority, mysql as database, wordspress as cms and docker to run containers of all of them.

The application receives http and https petitions.

## Run and use
Access to web server on domain http://www.pgomezl.tk or IP address: 35.202.222.65

## Deployment
This project was deployed on a VM instance in Google Cloud using Ubuntu as OS, docker to deploy containers with nginx, wordpress and mysql images running on them.

## Resources
|Name|Info|Link|
|------|-----------|----|
|nginx|Web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.|[Nginx](https://nginx.org/en/docs/)|
|docker|Set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.|[Docker](https://www.docker.com/)|
|letsencrypt|A nonprofit certificate authority providing TLS certificates.|[Let's Encrypt](https://letsencrypt.org/)|

#### version README.md -> 1.0 (2022-september)
