from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

DB = {}
DB["0"] = {"id":0, "name":"Jean"}

@app.route('/')
def welcome_view():
    return render_template('./index.html'), 200

@app.route('/people/', methods=['POST', 'GET'])
def people():
    global DB
    if request.method == 'POST':
        id = str(int(sorted(DB.keys())[-1])+1)
        return people_update(id)
    else:
        json = app.json_encoder(indent=2).encode(DB)
        return json, 200

@app.route('/people/<id>', methods=['GET'])
def people_read(id):
    global DB
    json = app.json_encoder(indent=2).encode(DB[id])
    return json, 200

@app.route('/people/<id>', methods=['PUT',])
def people_update(id):
    global DB
    data = request.get_data()
    p = app.json_decoder().decode(data)
    p['id'] = id
    DB[id] = p
    json = app.json_encoder(indent=2).encode(DB[id])
    return json, 200

@app.route('/people/<id>', methods=['DELETE',])
def people_delete(id):
    global DB
    del(DB[id])
    json = app.json_encoder(indent=2).encode({"status": "ok"})
    return json, 200


if __name__ == '__main__':
    app.run(debug=True)
