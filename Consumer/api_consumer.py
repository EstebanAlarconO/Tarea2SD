import json
from time import sleep
from flask import Flask, render_template
from kafka import KafkaConsumer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()

@app.route('/blocked', methods=['GET'])
def index():

    consumer = KafkaConsumer('test', bootstrap_servers=['kafka:9092'])
    for message in consumer:
        print (message)
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug = True)
    
