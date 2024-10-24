# exo 2
from kafka import KafkaConsumer
import json
import numpy as np

consumer = KafkaConsumer('kieraga', bootstrap_servers='51.38.185.58:9092')
for message in consumer:
    converted_message = message.value.decode()
    message_load = json.loads(converted_message)
    data = np.array(message_load['data'])
    data_sum = np.sum(data)
    print(data_sum)