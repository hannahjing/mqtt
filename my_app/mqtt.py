

import paho.mqtt.client as mqtt
from my_project import settings

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    global s
    print(msg.payload)
#    s.send(msg.payload)

#def on_publish(mqttc, obj, mid):
#    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


# Define MQTT broker server
broker_address="203.101.225.212"
broker_port = 1883

#TCP_IP = '127.0.0.1'
#TCP_PORT = 10011

# Establish MQTT connection
mqttc = mqtt.Client() #create new instance
mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect(broker_address, broker_port, 60) #connect to broker
xyz = mqttc.subscribe("coordinates/+/XYZ") #subscribe
#mqttc.loop_forever()


