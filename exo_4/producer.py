from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
message = json.dumps({'data': {'size':50, 'nb_rooms':1, 'garden':1}})
message_encoded = message.encode()
producer.send('prediction_florine_kieraga', message_encoded)
producer.flush()