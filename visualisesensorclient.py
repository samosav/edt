import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from paho.mqtt import client as mqtt_client

broker = "farmer.cloudmqtt.com"
port = 16736
topic = "ees/ir"
username = 'elmyzmin'
password = 'POq5B4tgE72j'

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

def subscribe(client, ax, cbar_ax):
    def on_message(client, userdata, msg):
        if msg.topic == topic:
            data = np.frombuffer(msg.payload, dtype=float).reshape((8, 8))
            update_plot(data)
    client.subscribe(topic)
    client.on_message = on_message


grid_kws = {'width_ratios': (0.8, 0.05), 'wspace': 0.2}
fig, (ax, cbar_ax) = plt.subplots(1, 2, gridspec_kw=grid_kws)


def update_plot(data):
    sns.heatmap(ax=ax, data=data, cmap="jet", cbar_ax=cbar_ax)
    plt.draw()
    plt.pause(0.001)

client = connect_mqtt()
subscribe(client, ax, cbar_ax)
client.loop_forever()
