from time import time
import json
from flask import Flask, render_template, request
from kafka import KafkaConsumer
from aiokafka import AIOKafkaConsumer
import asyncio

app = Flask(__name__)
#topic_list = []

async def consume():
    consumer = AIOKafkaConsumer(
        'test',
        bootstrap_servers='kafka:9092')
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
            return json.loads(msg.value)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blocked')
def blocked():
    message=asyncio.run(consume())
    #fecha = json.dumps(date.timetuple(date.today())).encode('utf-8')
    #message['time_consumer'] = fecha
    '''consumer = KafkaConsumer('test', bootstrap_servers=['kafka:9092'], consumer_timeout_ms=300000, enable_auto_commit=True)
    for message in consumer:  
        message = message.value  '''
    return render_template('blocked.html', valor=time()-message['time_login'])
    
if __name__== "__main__":
    app.run(debug = True)
    
