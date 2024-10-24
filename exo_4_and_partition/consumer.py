from kafka import KafkaConsumer, TopicPartition

from model_utils import load_model, make_prediction
import json

model = load_model()
topic_partition = TopicPartition('prediction_florine_kieraga', 0)
consumer = KafkaConsumer(bootstrap_servers='51.38.185.58:9092', group_id='grp1')
consumer.assign([topic_partition])
for message in consumer:
    converted_message = message.value.decode()
    message_load = json.loads(converted_message)
    data = message_load['data']
    prediction = make_prediction(size=data['size'], nb_rooms=data['nb_rooms'], garden=data['garden'], model=model)
    print("Prédiction : ", prediction)