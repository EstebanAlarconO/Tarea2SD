import json
from flask import Flask, render_template
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)

#producer = KafkaProducer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    consumer = KafkaConsumer()
    return

    
