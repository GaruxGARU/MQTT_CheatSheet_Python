import paho.mqtt.client as mqtt
import time
# MQTT broker details
broker = 'your_broker_address'
port = 1883
topic = 'your/topic'
username = 'your_username'
password = 'your_password'

# Message to publish
message = 'Hello, MQTT!'

# Define the on_connect callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

# Define the on_disconnect callback function
def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")
    if rc != 0:
        print("Unexpected disconnection.")        

# Define the on_publish callback function
def on_publish(client, userdata, mid):
    print("Message Published")

# Create an MQTT client instance
client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# Set username and password
client.username_pw_set(username, password)

# Connect to the broker
client.connect(broker, port)
client.loop_start()

#------------------------------------------program here----------------------------------------
# Publish the message to the topic
client.publish(topic, message)
time.sleep(0.001)

#------------------------------------------end program here----------------------------------------

# Disconnect from the broker
client.loop_stop()
client.disconnect()
