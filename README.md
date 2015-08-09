This is a very basic key value store with a REST interface.
Implemented with Flask.

It does support the following commands:
 * curl 127.0.0.1:5000/people/
 * curl 127.0.0.1:5000/people/0
 * curl -X POST 127.0.0.1:5000/people/ --data '{"name":"Jean Dupont"}'
 * curl -X PUT 127.0.0.1:5000/people/0 --data '{"name":"Gerard Martin"}'
 * curl -X DELETE 127.0.0.1:5000/people/0

To build the docker:
 * sudo docker build -t sroy/peoplestore

To run it:
 * sudo docker run -d -p 5000:80 sroy/peoplestore
