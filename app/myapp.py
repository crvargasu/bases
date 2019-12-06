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
"""
filt = db.mensaje.find()

mensajes = []
nom = "Proyecto_Agua"
resp = ""
n = 1
for i in filt:
    #print(i)
    if i["metadata"]["sender"] == nom:
        mensajes.append(i["mensaje"])
    if i["metadata"]["receiver"] == nom:
        mensajes.append(i["mensaje"])
for i in mensajes:
    resp += f"{n}: {i} "
    n += 1
print(resp)

"""



# Iniciamos la aplicación de flask
app = Flask(__name__)


@app.route("/messages/<int:Id>", methods=["GET"])
def id_(Id):
    mensaje = ''
    if not isinstance(Id, str):
        Id = float(Id)
    resultado = db.mensaje.find({"id": Id})
    for x in resultado:
        mensaje = x
    return f"<h1>{mensaje}</h1>"

#COMPLETO
@app.route("/messages/<project_search>", methods=["GET"])
def project_search(project_search):
    # SE RESCATA EL PARAMETRO

    sender = db.mensaje.find({'metadata.sender':'Proyecto_Agua'})
    receiver = db.mensaje.find({'metadata.receiver':'Proyecto_Agua'})
    resultados = []
    for x in sender:
        resultados.append(x)
    for x in receiver:
        resultados.append(x)

    return f"<h3>{resultados}</h3>"


#INCOMPLETO
@app.route("/messages/content-search", methods=["GET"])
def content_search():
    # SE RESCATA EL PARAMETRO
    contenido = request.args.get("contenido", default = " ", type = str)
    return f"<h1>{contenido}</h1>"


if __name__ == "__main__":
    app.run()
