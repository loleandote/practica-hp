from flask import Flask, jsonify, request
from pymongo import MongoClient
import json


app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['datos_energia']
collection = db['nombre_de_tu_coleccion']

@app.route('/temperaturas/<pais>')
def hello(pais):
    documentos = collection.find()
    # Convertir los documentos a una lista de diccionarios
    lista_documentos = [doc for doc in documentos]
    # Convertir la lista de diccionarios a JSON
    return jsonify(lista_documentos)

if __name__ == '__main__':
    app.run(debug=True)