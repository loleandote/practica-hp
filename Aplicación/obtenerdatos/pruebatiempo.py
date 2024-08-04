import requests
from confluent_kafka import Producer
from datetime import datetime, timedelta
import json

# Configuración inicial de Kafka
config_kafka = {
    'bootstrap.servers': 'localhost:9092'  # Ajusta esto según tu configuración de Kafka
}
producer = Producer(**config_kafka)
topic = 'temperatura_media_diaria'

# Función para enviar mensajes a Kafka
def enviar_a_kafka(mensaje):
    producer.produce(topic, json.dumps(mensaje).encode('utf-8'))
    producer.flush()

# Configuración inicial
API_KEY = "2GR64M3PFFRJEETLCJFVP8SAN"
ciudad = "Madrid"
fecha_final = datetime.now()
fecha_inicio = fecha_final - timedelta(days=3*365)  # Aproximación, no considera años bisiestos

# Formatear las fechas para la solicitud
fecha_inicio_str = fecha_inicio.strftime('%Y-%m-%d')
fecha_final_str = fecha_final.strftime('%Y-%m-%d')

# URL para la API de Visual Crossing Weather
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=2GR64M3PFFRJEETLCJFVP8SAN&taskId=e252bf44bdb6fa8bb1c3300284f39f5a&zip=false'
# Realizar la solicitud a la API
respuesta = requests.get(url)
datos = respuesta.json()

# Extraer y mostrar la temperatura media diaria
for dia in datos['days']:
    fecha = dia['datetime']
    temperatura_media = dia['temp']
    print(fecha)
    mensaje = {'schema': {'type': 'struct', 'fields': [{'type': 'string', 'optional': False, 'field': 'ciudad'}, {'type': 'string', 'optional': False, 'field': 'fecha'}, {'type': 'float', 'optional': False, 'field': 'temperatura'}], 'optional': False, 'name': 'temperaturas'}, 'payload': {'ciudad': ciudad, 'fecha': fecha, 'temperatura': float(temperatura_media)}}
    print(mensaje)
    enviar_a_kafka(mensaje)