import json
from flask import Flask, render_template
from kafka import KafkaProducer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()

@app.route('/')
def index():
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
    producer.send('test', b'Hello, World!')
    producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
    return render_template('index.html')
    
'''
@app.route('/login', methods = ['POST'])
def login():
    

    return
'''


    
