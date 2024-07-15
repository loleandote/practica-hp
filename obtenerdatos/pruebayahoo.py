import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
from confluent_kafka import Producer
import json

# Configuración inicial de Kafka
config_kafka = {
    'bootstrap.servers': 'localhost:9092'  # Ajusta esto según tu configuración de Kafka
}
producer = Producer(**config_kafka)
topic = 'cotizaciones_bolsa'

def enviar_a_kafka(mensaje):
    producer.produce(topic, json.dumps(mensaje).encode('utf-8'))
    producer.flush()

   

# Uso de la clase
indice = '^IBEX'
fecha_actual = datetime.now()
fecha_hace_cinco_anos = fecha_actual - relativedelta(years=5)
datos = yf.download(indice, start=fecha_hace_cinco_anos.strftime('%Y-%m-%d'), end=fecha_actual.strftime('%Y-%m-%d'))

for fecha, fila in datos.iterrows():
    mensaje = {'schema': {'type': 'struct', 'fields': [{'type': 'string', 'optional': 'false', 'field': 'indice'},{'type': 'string', 'optional': False, 'field': 'fecha'}, {'type': 'float', 'optional': False, 'field': 'cierre'}], 'optional': False, 'name': 'cotizacion'}, 'payload': {'indice': indice, 'fecha': fecha.strftime('%Y-%m-%d %H:%M:%S'), 'cierre': float(fila['Close'])}}
    #mensaje = {'fecha': fecha.strftime('%Y-%m-%d'), 'cierre': float(fila['Close'])}
    print(mensaje)
    enviar_a_kafka(mensaje)