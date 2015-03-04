# Hello Word web app in Python
Python hello-world based on the app.py from the (Docker Compose tutorial)[https://docs.docker.com/compose/#installation-and-set-up].
Includes both a version that needs a Redis DB and one that doesn't.

## How to use
```
# Hello world without Redis DB
docker run -d -p 80:80 cargonauts/helloworld-python python /srv/helloworld.py

# Hello world with Redis DB
docker run -d -p 80:80 cargonauts/helloworld-python python /srv/helloworld-db.py
```
