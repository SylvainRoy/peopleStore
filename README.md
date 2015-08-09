This is a very basic key value store with a REST interface.
Implemented with Flask.

It does support the following commands:
 * curl 127.0.0.1:5000/people/
 * curl 127.0.0.1:5000/people/0
 * curl -X POST 127.0.0.1:5000/people/ --data '{"aa":"tutu"}'
 * curl -X PUT 127.0.0.1:5000/people/0 --data '{"bb":"titi"}'
 * curl -X DELETE 127.0.0.1:5000/people/0