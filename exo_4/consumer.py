from kafka import KafkaConsumer
from model_utils import load_model, make_prediction
import json

model = load_model()
consumer = KafkaConsumer('prediction_florine_kieraga', bootstrap_servers='51.38.185.58:9092', group_id='prediction_group')
for message in consumer:
    converted_message = message.value.decode()
    message_load = json.loads(converted_message)
    data = message_load['data']
    prediction = make_prediction(size=data['size'], nb_rooms=data['nb_rooms'], garden=data['garden'], model=model)
    print("Prédiction : ", prediction)