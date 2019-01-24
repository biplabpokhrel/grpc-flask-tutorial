# grpc-flask-tutorial
This repo contain a tutorial guide to use flask and grpc side by side by side,, and also showing how you can share the codes among the different apps in docker container

## How to run the app
You have to install docker and docker-compose to run this app, if you already have installed then you just have to run following commands 

``` docker-compose build ``` and wait docker to build everything once done

``` docker-compose up -d ``` to run docker in background

``` docker-compose ps ``` Will show you the running instance of docker ( Everything should be up and running )

```           Name                        Command              State            Ports          
--------------------------------------------------------------------------------------------
grpc-flask-tutorial_db_1     /docker-entrypoint.sh mysqld   Up      0.0.0.0:5016->3306/tcp  
grpc-flask-tutorial_grpc_1   python ./app.py                Up      0.0.0.0:50051->50051/tcp
grpc-flask-tutorial_web_1    python application/app.py      Up      0.0.0.0:3001->3001/tcp  

```
## How to test rest-api
Just curl your localhost with port 3001

### POST request
 ```curl -d '[{"name":"ABC", "birth":"2019-01-24", "gender": "MALE"}]' -H "Content-Type: application/json" -X POST http://localhost:3001/users```

### GET request
 ```curl localhost:3001/user/1```
 ```curl localhost:3001/users```

## How to test grpc-api
If you have client setup outside the docker then you call the grpc function using localhost:50051 and it should give you the data. But here we will test is little differently ( Not recommended in productions ), I am doing this because I already have small written client script.

You have to go inside the running grpc docker instance

``` docker exec -it grpc-flask-tutorial_grpc_1 sh ```

You will see new bash shell, Now we have to lunch python terminal so just type

```python ```

You will see python terminal, now you need to import client file and the get_user and get_users function

``` from client import get_user, get_users ```

Once imported then, just call function

```get_user(1)``` you will see result , if you have data or not found error

```get_users()``` it will give you all data


