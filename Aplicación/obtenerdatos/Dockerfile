FROM python:3.10
RUN pip install requests
RUN pip install yfinance
RUN pip install confluent-kafka
RUN pip install DateTime

RUN mkdir /home/obtenerdatos
COPY  pruebayahoo.py pruebayahoo.py

CMD ["python", "pruebayahoo.py"]