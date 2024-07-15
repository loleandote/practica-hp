from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def obtener_temperaturas(ciudad=None):
    """Conecta a la base de datos MySQL y consulta la tabla temperatura_media_diaria filtrando por ciudad si se proporciona."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='aplicacionkafka'
        )
        if conexion.is_connected():
            cursor = conexion.cursor(dictionary=True)
            if ciudad:
                query = "SELECT * FROM temperatura_media_diaria WHERE ciudad = %s"
                cursor.execute(query, (ciudad,))
            else:
                cursor.execute("SELECT * FROM temperatura_media_diaria")
            resultados = cursor.fetchall()
            return resultados
    except Error as e:
        print("Error al conectar a MySQL", e)
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

@app.route('/temperaturas/', defaults={'ciudad': None})
@app.route('/temperaturas/<ciudad>')
def hello(ciudad):
    datos = obtener_temperaturas(ciudad)
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)