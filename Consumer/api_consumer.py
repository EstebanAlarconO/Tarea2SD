import json
from flask import Flask, render_template
from kafka import KafkaConsumer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()

@app.route('/')
def index():
    return render_template('index.html')


    
