from flask import Flask, render_template, request, abort, json
import pandas as pd
import matplotlib.pyplot as plt
import os
from pymongo import MongoClient


uri = "mongodb://grupo64:grupo64@gray.ing.puc.cl/grupo64"
# La uri 'estándar' es "mongodb://user:password@ip/database"
client = MongoClient(uri)
db = client.get_database()


"""
qfilter = db.mensaje.find()


for i in qfilter:
    print(i.id)
"""

filt = db.mensaje.find({"id": 2})

for i in filt:
    print(i["mensaje"])





# Iniciamos la aplicación de flask
app = Flask(__name__)


#COMPLETO
@app.route("/messages/id", methods=["GET"])
def id():
    #SE RESCATA EL PARAMETRO
    id = request.args.get("id", default = 1, type = int)
    filt = db.mensaje.find({"id": id})
    for i in filt:
        msj = i["mensaje"]
        data = i["metadata"]
    respuesta = f"Mensaje: {msj}, Data: {data}"
    return f"<h1>{respuesta}</h1>"

#INCOMPLETO
@app.route("/messages/project-search", methods=["GET"])
def project_search():
    # SE RESCATA EL PARAMETRO
    proyecto = request.args.get("proyecto", default = " ", type = str)
    return f"<h1>{proyecto}</h1>"


#INCOMPLETO
@app.route("/messages/content-search", methods=["GET"])
def content_search():
    # SE RESCATA EL PARAMETRO
    contenido = request.args.get("contenido", default = " ", type = str)
    return f"<h1>{contenido}</h1>"


if __name__ == "__main__":
    app.run()

