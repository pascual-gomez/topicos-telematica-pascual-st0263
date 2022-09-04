# ST263: Tópicos Especiales en Telemática
Students: Pascual Gómez, pgomezl@eafit.edu.co - Sebastián Granda Gallego, sgrandag@eafit.edu.co
Professor: Edwin Montoya, emontoya@eafit.edu.co

## Lab 2: Message-oriented Middleware
Deploy a MOM in order to strengthen the knowledge developed in the class session.

This MOM serves as a communicator among two temperature sensors that measure the temperature for a group of plants. If the temperature in any of the sensors is above 18, the air conditioner must be turned on, and if the temperature is below 15, air conditioner must be turned off. All of this in order to keep the temperature in the room among the boundaries [15-18].

## Run and use
Start machines 'rabbitmq', 'rbmq-prod', 'rbmq-prod-2' and 'rbmq-cons' on Pascual's AWS Academy.

On 'rabbitmq' run the commands:
```bash
#start rabbitmq docker container
docker start rabbit-server

#check container is running
docker ps
```

On 'rbmq-prod' and 'rbmq-prod-2' run the command:
```bash
#start producers application
python3 /etc/prod_app/prod.py 
```
Messages on console should appear as:
```bash
[x] Sent: 2 17.129862010412676
```
Where 2 is the sensonr number and 17.129862010412676 the temperature measured.

On 'rbmq-cons' run the command:
```bash
#start producers application
python3 /etc/cons_app/cons.py 
```
Messages on console should appear as:
```bash
13.909974713640878 is received by sensor 2
temperature is too low. If on, air conditioner will be turned off.
```

## Project Structure
 ```bash
.
├── cons_app                                         
│   └── cons.py                     # Consumer Application                                
├── prod_app                        
│   └── prod.py                     # Producer Application         
└── README.md  
```

## Deployment
This project was deployed on EC2 machines in AWS Academy using Ubuntu as OS, docker to deploy a container with a RabbitMQ image and Python as the programming language for the producers and consumer's applications.

## Resources
|Name|Info|Link|
|------|-----------|----|
|docker|Open platform for developing, shipping, and running applications|[Docker](https://www.docker.com)|
|pika|Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.|[Pika](https://pypi.org/project/pika/)|

## References

#### version README.md -> 1.0 (2022-september)
