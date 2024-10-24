from kafka import KafkaProducer
import json


producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
for i in range(10):
    k = 0
    if i % 2 == 0:
        k = 1
    message = json.dumps({'data': {'size':70, 'nb_rooms':1, 'garden':1}})
    message_encoded = message.encode()
    producer.send('prediction_florine_kieraga', message_encoded, partition=k)
    producer.flush()