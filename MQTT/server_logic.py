import paho.mqtt.client as mqtt

# MQTT broker info
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_SENSOR = "iot/waterSensor"
TOPIC_STATUS = "iot/rainStatus"

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(TOPIC_SENSOR)

# Callback when message received
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        sensor_value = int(payload)
        print(f"Received sensor value: {sensor_value}")
        if sensor_value > 200:
            status = "1"  # Raining
        else:
            status = "0"  # Clear
        print(f"Publishing status: {status}")
        client.publish(TOPIC_STATUS, status)
    except Exception as e:
        print(f"Error: {e}")

# Setup client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect and start loop
client.connect(BROKER, PORT, 60)
client.loop_forever()
