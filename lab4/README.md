# ST263: Tópicos Especiales en Telemática
Students: Pascual Gómez, pgomezl@eafit.edu.co

Professor: Edwin Montoya, emontoya@eafit.edu.co

## Lab 4: Monolith Application with Load Balancer and Distributed Data
For this laboratory, we deployed a webserver using nginx, docker, let's encrypt, wordpress, mysql and nfs.

Nginx is being used as a reverse proxy and load balancer, let's encrypt as certificate authority, mysql as a distributed database, nfs as a distributed filesystem, wordspress as cms and docker to run containers of all of them in each machine.

The application receives http and https petitions.

## Run and use
Access to web server on domain http://www.lab4.pgomezl.tk or IP address: 34.67.235.40

To connect via ssh to the VM run this command inside the directory where the ssh key "lab3.pem" is located.
```bash
ssh -i "lab3.pem" paskugomez@34.67.235.40
```
When asked for a passphrase, type
```bash
lab3
```
You should be prompted  with a message saying:
```bash
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1017-gcp x86_64)
```
There you are already inside the VM Instance ready to navegate and check every service and container running.

### VM IPs

Load Balancer:  34.67.235.40  
CMS1:           104.197.202.176  
CMS2:           34.173.235.193  
Database:       34.71.168.6  
NFS:            34.135.7.208

## Deployment
This project was deployed on a VM instance in Google Cloud using Ubuntu as OS, docker to deploy containers with nginx, wordpress and mysql images running on them.

## Evidence
### Running VMs
![Captura de Pantalla 2022-10-23 a la(s) 11 10 29 p m](https://user-images.githubusercontent.com/97640805/197447052-b8e97a84-e5e5-47a4-8ba3-b002c503a898.png)
### DNS Zone
![Captura de Pantalla 2022-10-23 a la(s) 11 12 27 p m](https://user-images.githubusercontent.com/97640805/197447218-38815074-891c-4253-a7e4-fbe30da6652d.png)
### SSL Certificate  
![Captura de Pantalla 2022-10-23 a la(s) 10 38 54 p m](https://user-images.githubusercontent.com/97640805/197446408-40cfbafb-0195-40bc-a3ec-c330930e99c8.png)
### Website
![Captura de Pantalla 2022-10-23 a la(s) 11 05 37 p m](https://user-images.githubusercontent.com/97640805/197446629-a7bfd539-0009-4312-bd3c-16e5e7c0a1a5.png)

## Resources
|Name|Info|Link|
|------|-----------|----|
|nginx|Web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.|[Nginx](https://nginx.org/en/docs/)|
|docker|Set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.|[Docker](https://www.docker.com/)|
|letsencrypt|A nonprofit certificate authority providing TLS certificates.|[Let's Encrypt](https://letsencrypt.org/)|

#### version README.md -> 1.0 (2022-september)

