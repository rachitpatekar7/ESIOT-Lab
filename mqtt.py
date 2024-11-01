import os
import time
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt

MQTT_SERVER="broker.hivemq.com"
#MQTT_SERVER="mqtt.eclipse.org"
#MQTT_SERVER="test.mosquitto.org"
# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5
next_reading = time.time() 

client = mqtt.Client()

# Connect to server MQTT port and 60 seconds keepalive interval
client.connect(MQTT_SERVER, 1883, 60)

client.loop_start()

try:
    while True:
        humidity,temperature = dht.read_retry(dht.DHT22, 23)
        temperature = round(temperature, 2)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        # Sending  temperature data to broker
        client.publish('mit/temperature', temperature, 1)
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
