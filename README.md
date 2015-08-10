This is a very basic key value store with a REST interface.
It is implemented with Python, Flask and Redis.

It does support the following commands:
 * curl 127.0.0.1:8080/people/
 * curl 127.0.0.1:8080/people/0
 * curl -X POST 127.0.0.1:8080/people/ --data '{"name":"Jean Dupont"}'
 * curl -X PUT 127.0.0.1:8080/people/0 --data '{"name":"Gerard Martin"}'
 * curl -X DELETE 127.0.0.1:8080/people/0

The objective of the whole thing was to play with docker.
To manually get the whole thing running:
 * sudo docker build -t sroy/peoplestore .
 * sudo docker run -d redis
 * sudo docker run -d -p 8080:8080 --name peoplestore --link redis:redis sroy/peoplestore
