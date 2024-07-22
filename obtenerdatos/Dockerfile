FROM python:3.10
RUN pip install requests
RUN pip install yfinance
RUN pip install confluent-kafka
RUN pip install DateTime

RUN mkdir /home/obtenerdatos
COPY . /home/obtenerdatos

CMD ["python", "/home/obtenerdatos/pruebayahoo.py"]