import time
import numpy as np
from paho.mqtt import client as mqtt_client
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMGXX(i2c)

broker = "farmer.cloudmqtt.com"
port = 16736
topic = "ees/irbruh"
username = 'elmyzmin'
password = 'POq5B4tgE72j'

delay = 0.005


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        time.sleep(delay)
        data = read_sensor()
        client.publish(topic, data)


def read_sensor():
    data = amg.pixels
    return np.array(data).tobytes()


client = connect_mqtt()
client.loop_start()
publish(client)
