import json
from time import sleep, localtime
from flask import Flask, render_template, request
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)
topic_list = []

#producer = KafkaProducer()
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x: json.dumps(x).encode('ascii'))
        producer.send('test', {'user':user, 'hora_login': localtime()})
        producer.flush()
        #producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
    return render_template('index.html')
    

if __name__== "__main__":
    app.run(debug = True)
    
