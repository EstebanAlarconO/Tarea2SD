FROM bitnami/python:3.8.13

RUN pip install flask
RUN pip install kafka-python
ENV FLASK_APP=api_producer.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .
CMD ["flask", "run"]