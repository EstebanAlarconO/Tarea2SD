import json
from flask import Flask, render_template
from kafka import KafkaConsumer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()

@app.route('/')
def index():
    consumer = KafkaConsumer('test')
    for message in consumer:
        print (message)
    return render_template('index.html')


    
