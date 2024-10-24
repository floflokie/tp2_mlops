# exo 2
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
message = json.dumps({'data': [[1, 2], [3, 4]]})
message_encoded = message.encode()
producer.send('kieraga', message_encoded)
producer.flush()