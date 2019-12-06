from flask import Flask, render_template, request, abort, json
import pandas as pd
import os
from pymongo import MongoClient


uri = "mongodb://grupo64:grupo64@gray.ing.puc.cl/grupo64"
# La uri 'estándar' es "mongodb://user:password@ip/database"
client = MongoClient(uri)
db = client.get_database()

#qfilter = db.mensaje.find({'metadata.sender':'Proyecto_Agua'}) #Borrar si no funciona



# Iniciamos la aplicación de flask
app = Flask(__name__)


@app.route("/messages/<int:Id>", methods=["GET"])
def id_(Id):
    if not isinstance(Id, str):
        Id = float(Id)
    resultado = db.mensaje.find({"id": Id})
    for x in resultado:
        del x['_id']
        mensaje = x
    return json.jsonify(mensaje)

#COMPLETO
@app.route("/messages/<project_search>", methods=["GET"])
def project_search(project_search):
    # SE RESCATA EL PARAMETRO
    sender = db.mensaje.find({'metadata.sender':'Proyecto_Agua'})
    receiver = db.mensaje.find({'metadata.receiver':'Proyecto_Agua'})
    resultados = dict()
    c = 0
    for x in sender:
        del x['_id']
        resultados[c] = x
        c+=1
    for x in receiver:
        del x['_id']
        resultados[c] = x
        c+=1
    return json.jsonify(resultados)


#INCOMPLETO
@app.route("/messages/content-search", methods=["GET"])
def content_search():
    # SE RESCATA EL PARAMETRO
    contenido = request.get_json() # request.json no esta obteniendo los datos :(
    for x in contenido["required"]:
        consulta += f' {x}'
    consulta = consulta.strip()
    consulta = f'"{consulta}'
    for x in contenido["desired"]:
        consulta += f" {x}"
    for x in contenido['forbbiden']:
        consulta += f' -{x}'
    consulta = f'{consulta}"'
    #db.mensaje.createIndex({"mensaje":"text"})
    resultado = db.mensaje.find({"$text": {"$search": consulta}})
    c = 0
    dic = dict()
    for x in resultado:
        dic[c] = x
    return json.jsonify(dic)

@app.route("/messages", methods=["POST"])
def messages():
    # SE RESCATA PARAMETROS
    _json = request.json
	#_mensaje = request.json['mensaje']
	#_database = _json['database'] #diccionario
    #_id = _json["id"]

	# validate the received values
	#if _id and _mensaje and _database and request.method == 'POST':
    #        id = db.mensaje.insert({'id': _id, 'mensaje': _mensaje, 'database': _database})
    return json.jsonify(_json)

@app.route("/messages/<int:Id>", methods=["POST"])
def delete(Id):
    if not isinstance(Id, str):
        Id = float(Id)
    db.mensaje.deleteOne({"id": Id})
    return f"<h1>mensaje con id: {id} eliminado</h1>"


if __name__ == "__main__":
    app.run()
