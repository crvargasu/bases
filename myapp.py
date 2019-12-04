from flask import Flask, render_template, request, abort, json
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import os

USER_KEYS = ['name', 'last_name', 'occupation', 'follows', 'age']

# El cliente se levanta en la URL de la wiki
URL = "mongodb://grupo90:grupo90@gray.ing.puc.cl/grupo90"
client = MongoClient(URL)

# Iniciamos la aplicación de flask
app = Flask(__name__)


#INCOMPLETO
@app.route("/messages/id", methods=["GET"])
def id():
    #SE RESCATA EL PARAMETRO
    id = request.args.get("id", default = 1, type = int)
    return f"<h1>{id}</h1>"

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