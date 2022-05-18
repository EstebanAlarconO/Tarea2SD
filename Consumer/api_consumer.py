import json
from time import sleep
from flask import Flask, render_template, request
from kafka import KafkaConsumer


app = Flask(__name__)
#topic_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blocked')
def blocked():
    consumer = KafkaConsumer('test', bootstrap_servers=['kafka:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer:  
        message = message.value  
        return render_template('blocked.html', valor=message)
    
if __name__== "__main__":
    app.run(debug = True)
    
