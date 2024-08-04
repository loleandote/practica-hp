from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def obtener_cotizaciones(indice=None):
	"""Conecta a la base de datos MySQL y consulta la tabla cotizaciones_bolsa filtrando por índice si se proporciona."""
	try:
		conexion = mysql.connector.connect(
			host='localhost',
			user='root',
			password='1234',
			database='aplicacionkafka'
		)
		if conexion.is_connected():
			cursor = conexion.cursor(dictionary=True)
			if indice:
				print("indice", indice  )
				query = "SELECT * FROM cotizaciones_bolsa WHERE indice = %s"
				cursor.execute(query, (indice,))
			else:
				cursor.execute("SELECT * FROM cotizaciones_bolsa")
			resultados = cursor.fetchall()
			return resultados
	except Error as e:
		print("Error al conectar a MySQL", e)
	finally:
		if conexion.is_connected():
			cursor.close()
			conexion.close()

@app.route('/cotizaciones/', defaults={'indice': None})
@app.route('/cotizaciones/<indice>')
def hello(indice):
	datos = obtener_cotizaciones(indice)
	return jsonify(datos)

if __name__ == '__main__':
	app.run(debug=True)