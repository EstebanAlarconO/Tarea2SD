from time import time
import json
from flask import Flask, render_template, request
from kafka import KafkaConsumer
from aiokafka import AIOKafkaConsumer
import asyncio

app = Flask(__name__)
message = ''
usuarios = {}
users_blocked = []

def is_blocked(msg):
    
    if msg['user'] in users_blocked:
        return
    elif msg['user'] not in usuarios:
        usuarios[msg['user']] = [msg['time_login'], 5, 0]
    else:
        if (msg['time_login'] - usuarios[msg['user']][0] <= 60) and (usuarios[msg['user']][1]-1 == 0):
            usuarios[msg['user']] = [msg['time_login'],0,1]
            get_blocked(msg['user'])
        else:
            if (msg['time_login'] - usuarios[msg['user']][0] <= 60):
                usuarios[msg['user']] = [usuarios[msg['user']][0],usuarios[msg['user']][1]-1,0]
            else:
                usuarios[msg['user']] = [msg['time_login'], 5, 0]
                    
    return

def get_blocked(usuario):

    users_blocked.append(usuario)

def view_blocked():
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
            is_blocked(json.loads(msg.value))
            return json.loads(msg.value)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

@app.route('/')
def index():
    message = asyncio.run(consume())
    return render_template('index.html')

@app.route('/blocked')
def blocked():
    users_blocked = view_blocked()
    #message=asyncio.run(consume())
    '''consumer = KafkaConsumer('test', bootstrap_servers=['kafka:9092'], consumer_timeout_ms=300000, enable_auto_commit=True)
    for message in consumer:  
        message = message.value  '''
    return render_template('blocked.html', valor=time(), values= users_blocked, usuarios = usuarios)
    
if __name__== "__main__":
    app.run(debug = True)
    
