#!/usr/bin>/python3

import flask
import app_tasques
import tasca
import json

app = flask.Flask(__name__)
core_app = app_tasques.App_tasques()

@app.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    resutat = core_app.esborra_tasca(id)
    return "", 204

@app.route("/tasks", methods=["POST", "GET", "PUT"])
def tasks():
    if flask.request.method == "POST":
        info_body = flask.request.get.data()
        tasca_nova = json.loads(info_body)
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"])
        resultat = core_app.afegueix_tasca(objecte_tasca)
        return "", 201
    elif flask.request.method == "PUT":
        info_body = flask.request.get.data()
        tasca_nova = json.loads(info_body)
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"], tasca_nova["done"], tasca_nova["id"])
        resultat = core_app.modifica_tasca(objecte_tasca)
        return "", 204
    elif flask.request.method == "GET":
        llista_jsons = []
        llista_tasques = core_app.llegir_tasques()
        for t in llista_tasques:
            tasca_json = str (t)
            tasca_diccionaty = json.loads(tasca_json)
            llista_jsons.append(tasca_diccionaty)
        return flask.jsonify(llista_jsons), 200
    
app.run(host="0.0.0.0")

# curl -d'{title: "Barrer el cuarto de las ratas"}' -H "Content-type: application/json" 192.168.3.120:5000/tasks