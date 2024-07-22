import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime, timedelta

def obtener_interes_historico(kw_list, fecha_inicio, fecha_fin, intervalo='1d'):
	pytrend = TrendReq()
	resultados = pd.DataFrame()

	# Convertir intervalo a entero, asumiendo que siempre termina con 'd' para días
	intervalo_dias = int(intervalo[:-1])

	fecha_actual = fecha_inicio
	while fecha_actual <= fecha_fin:
		siguiente_fecha = fecha_actual + timedelta(days=intervalo_dias)
		if siguiente_fecha > fecha_fin:
			siguiente_fecha = fecha_fin

		frame_tiempo = f'{fecha_actual.strftime("%Y-%m-%d")} {siguiente_fecha.strftime("%Y-%m-%d")}'
		pytrend.build_payload(kw_list=kw_list, timeframe=frame_tiempo)
		datos = pytrend.interest_over_time()
		resultados = pd.concat([resultados, datos])

		fecha_actual = siguiente_fecha + timedelta(days=1)

	return resultados

# Ejemplo de uso
kw_list = ['pizza']
fecha_inicio = datetime(2021, 12, 28)
fecha_fin = datetime(2021, 12, 29)
datos = obtener_interes_historico(kw_list, fecha_inicio, fecha_fin)
print(datos)