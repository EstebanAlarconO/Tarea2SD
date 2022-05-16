import json
from flask import Flask, render_template
from kafka import KafkaProducer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
    return

    
