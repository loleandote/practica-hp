1. Ir a la ubicacion de kafka
```
cd c:\kafka
```
2. Ejecutar zookeeper.
```
bin/windows/zookeeper-server-start.bat config/zookeeper-windows.properties
```
3. Ejecutar el servidor
```
bin/windows/kafka-server-start.bat config/server-windows.properties     
```
4. Ejecutar el conector con la base de datos
```
bin/windows/connect-standalone.bat config/connect-standalone.properties config/mysql-sink-connector.properties
```