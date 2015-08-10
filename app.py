#!/usr/bin/env python

import os, urllib, urllib2
from redis import Redis

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# The following assume the presence of REDIS_PORT (like you would get it with --link in docker)
# e.g. REDIS_PORT='tcp://172.17.0.12:6379'
redis_ip_port = urllib2.urlparse.urlsplit(os.environ['REDIS_PORT'])[1]
(ip, port) = urllib.splitport(redis_ip_port)
redis = Redis(host=ip, port=int(port))


@app.route('/')
def welcome_view():
    return render_template('./index.html'), 200

@app.route('/people/', methods=['POST', 'GET'])
def people():
    global redis
    if request.method == 'POST':
        id = redis.incr("key")
        return people_update(id)
    else:
        print {k:redis.get(k) for k in redis.keys() if k != "key"}
        all = {k:app.json_decoder().decode(redis.get(k)) for k in redis.keys() if k != "key"}
        json = app.json_encoder().encode(all)
        return json, 200

@app.route('/people/<id>', methods=['GET'])
def people_read(id):
    global redis
    json = app.json_encoder().encode(redis.get(id))
    return json, 200

@app.route('/people/<id>', methods=['PUT',])
def people_update(id):
    global redis
    data = request.get_data()
    p = app.json_decoder().decode(data)
    p['id'] = id
    json = app.json_encoder().encode(p)
    redis.set(id, json)
    return json, 200

@app.route('/people/<id>', methods=['DELETE',])
def people_delete(id):
    global redis
    redis.delete(id)
    json = app.json_encoder().encode({"status": "ok"})
    return json, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
