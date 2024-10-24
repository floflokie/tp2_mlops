from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
for _ in range(10):
    producer.send('exo1', b'coucou florine')
    print("ici")