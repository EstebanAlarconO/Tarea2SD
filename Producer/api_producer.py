import json
from time import sleep, ctime, time
from flask import Flask, render_template, request
from kafka import KafkaProducer
from aiokafka import AIOKafkaProducer
import asyncio

app = Flask(__name__)
topic_list = []


async def send_one(message):
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("test", message)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
#producer = KafkaProducer()
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        message={'user': user, 'time_login': time()}
        message = json.dumps(message).encode('utf-8')
        asyncio.run(send_one(message))
        '''producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x: json.dumps(x).encode('UTF-8'))
        producer.send('test', {'user':user, 'hora_login': localtime()})'''
        #producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
    return render_template('index.html')
    

if __name__== "__main__":
    app.run(debug = True)
    
