# ST263: Tópicos Especiales en Telemática
Student: Pascual Gómez, pgomezl@eafit.edu.co  
Professor: Edwin Montoya, emontoya@eafit.edu.co

## Lab 1: Socket Web Server
Simple concurrent web server made with sockets in Go using the net pacakge (https://pkg.go.dev/net).

This server accepts GET HttpRequests by default on the port 80. It then processes the request and replies with a HttpResponse containing the asked resource.

## Run
Install Go 1.16 or a higher version.

You can run the project with
```bash
#run by default on port 80
go run main.go

#run on a different port (e.g. 8080)
go run main.go -port 8080

```

## Use
After running the project, it is available in localhost through the chosen port to request any file on the static folder.

Open a browser and type
```bash
#request index.html on port 80.
localhost/index.html

#request test.txt on port 8080.
localhost:8080/test.txt
```

## Project Structure
 ```bash
.
├── static                          # Files                  
│   ├── test.txt                    # TXT                 
│   ├── index.html                  # HTML
│   ├── lab1.pdf                    # PDF
│   └── favicon.ico                 # ICON
├── main.go                         # Web Server
├── go.mod                          # Go Module
└── README.md  
```

## Deployment
This web server was deployed on a EC2 machine in AWS Academy. 

Its IP address is 3.224.154.71 but since it is an Academy license, the machine is not always running and the server is not always available.

Contact Pascual to run the EC2 machine.

## Resources
|Name|Info|Link|
|------|-----------|----|
|net|Package net provides a portable interface for network I/O, including TCP/IP, UDP, domain name resolution, and Unix domain sockets.|[Net](https://pkg.go.dev/net)|
|regexp|Package regexp implements regular expression search.|[Regexp](https://pkg.go.dev/regexp)|

## References
https://github.com/rsharifnasab/go-socket-http-server

#### version README.md -> 1.0 (2022-august)
