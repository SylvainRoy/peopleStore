This is a very basic key value store with a REST interface.
It is implemented with Python, Flask and Redis.

The objective of the whole thing was to play with docker, puppet, kubernetes and their friends.

It does support the following commands:
 * curl 127.0.0.1:8000/people/
 * curl 127.0.0.1:8000/people/0
 * curl -X POST 127.0.0.1:8000/people/ --data '{"name":"Jean Dupont"}'
 * curl -X PUT 127.0.0.1:8000/people/0 --data '{"name":"Gerard Martin"}'
 * curl -X DELETE 127.0.0.1:8000/people/0
(You'll have to replace the IP by the right one...)

To manually get the whole thing running with docker:
 * sudo docker build -t sroy/peoplestore .
 * sudo docker run -d --name redis redis
 * sudo docker run -d -p 8000:8000 --name peoplestore --link redis:redis sroy/peoplestore
(Then "docker ps" to find the IP to use.)

To do the same thing with docker-compose:
 * docker-compose up

To do the same thing with kubernetes:
 * kubectl create -f ./kubernetes/controler_and_pod.yaml
 * kubectl create -f ./kubernetes/service.yaml
(Then "kubectl get pods" to find the IP to use.)
(Note, to get kubernetes running, you can [run in via dockers](http://kubernetes.io/v1.0/docs/getting-started-guides/docker.html).)

