from time import time
import json
from flask import Flask, render_template, request
from kafka import KafkaConsumer
from aiokafka import AIOKafkaConsumer
import asyncio

app = Flask(__name__)
message = ''
usuarios = {}

def is_blocked(msg):
    
    if msg['user'] not in usuarios:
        usuarios[msg['user']] = [msg['time_login'], 5, 0]
    else:
        if (usuarios[msg['user']][0] - msg['time_login'] <= 1) and (usuarios[msg['user']][1]-1 == 0):
            usuarios[msg['user']] = [msg['time_login'],0,1]
        else:
            usuarios[msg['user']] = [usuarios[msg['user']][0],usuarios[msg['user']][1]-1,0]
                    
    return

def get_blocked():
    users_blocked = []

    for keys in usuarios:
        if usuarios[keys][2] == 1:
            users_blocked.append(keys)

    return users_blocked       

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
            is_blocked(son.loads(msg.value))
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blocked')
def blocked():
    users_blocked = get_blocked()
    #message=asyncio.run(consume())
    #fecha = json.dumps(date.timetuple(date.today())).encode('utf-8')
    #message['time_consumer'] = fecha
    '''consumer = KafkaConsumer('test', bootstrap_servers=['kafka:9092'], consumer_timeout_ms=300000, enable_auto_commit=True)
    for message in consumer:  
        message = message.value  '''
    return render_template('blocked.html', valor=time(), values= users_blocked)
    
if __name__== "__main__":
    message = asyncio.run(consume())
    app.run(debug = True)
    
