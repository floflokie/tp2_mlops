from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np

consumer = KafkaConsumer('kieraga', bootstrap_servers='51.38.185.58:9092')
producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
for message in consumer:
    converted_message = message.value.decode()
    message_load = json.loads(converted_message)
    data = np.array(message_load['data'])
    data_sum = np.sum(data)
    data_sum_str = str(data_sum)
    producer.send('processed', data_sum_str.encode())