# mqtt_client.py
import asyncio
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker_url: str, port: int):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker_url, port)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        print("Received message on topic " + msg.topic + ": " + str(msg.payload))

    async def publish_message(self, topic: str, payload: str) -> None:
        self.client.publish(topic, payload)

    async def subscribe_to_topic(self, topic: str) -> None:
        self.client.subscribe(topic)
