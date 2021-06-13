# Python Microservices
Python Microservices Web App  with Angular, Django and Flask.
Container based deployment using docker including MySQL and cloudAMPQ for RabbitMQ.

#### Microservice #1: (Dinosaurs Collections - Administration)
+ Django application (REST API)
+ MySQL
+ RabbitMQ - cloudampq service (Producer)

#### Microservice #2: (Dinosaurs Collection - Main display)
+ Flask application (REST API)
+ MySQL
+ RabbitMQ - cloudampq service (Consumer)
