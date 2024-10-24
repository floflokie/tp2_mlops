from kafka import KafkaConsumer

consumer = KafkaConsumer('processed_florine_kieraga', bootstrap_servers='51.38.185.58:9092')
for message in consumer:
    print (message.value)