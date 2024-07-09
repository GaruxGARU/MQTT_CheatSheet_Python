import paho.mqtt.client as mqtt
import time

# MQTT broker details
broker = 'your_broker_address'
port = 1883
topic = 'your/topic'
username = 'your_username'
password = 'your_password'


# Define the on_connect callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

# Define the on_disconnect callback function
def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")
    if rc != 0:
        print("Unexpected disconnection.")        

# Define the on_publish callback function
def on_publish(client, userdata, mid):
    print("Message Published")

# Define the on_message callback function
def on_message(client, userdata, message):
    #---------------------------------------------program start here----------------------------------------
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")




    
    #---------------------------------------------program here---------------------------------------------------------


# Create an MQTT client instance
client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message

# Set username and password
client.username_pw_set(username, password)

# Connect to the broker
client.connect(broker, port)
client.loop_start()

# Keep the program running to receive messages
try:
    while True:
        time.sleep(1)  # You can adjust the sleep time as needed
except KeyboardInterrupt:
    print("Interrupted, exiting...")
    client.loop_stop()
    client.disconnect()
