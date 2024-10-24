from kafka import KafkaAdminClient
from kafka.admin import NewPartitions

admin_client = KafkaAdminClient(bootstrap_servers='51.38.185.58:9092')
topic_partitions = {}
topic = 'prediction_florine_kieraga'
new_partitions = NewPartitions(total_count=2)
topic_partitions[topic] = new_partitions
admin_client.create_partitions(topic_partitions)