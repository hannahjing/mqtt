#!/usr/bin/python


import paho.mqtt.client as mqtt

mytime = 0
latency = {}
id=[]
latency_time=[]
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mosq, obj, msg):
    global s
    # print(msg.topic,msg.payload)
    data_parse(msg.topic, msg.payload)


#    s.send(msg.payload)

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


def data_parse(topic, data):
    topicSplit = topic.split('/')
    mystation = topicSplit[4]
    # [id,x,y,z]=data.decode("utf-8").split(',')
    newdata = data.decode("utf-8").split(',')
    newdata = list(map(lambda x: float(x), newdata))
    global mytime, latency, newtime, id,latency_time
    for i in mystation:
        station_name = mystation[0:4]
    if topic == "auscors/GA/CORS/RTCMv3/" + mystation + "/OBS/timestamped":
        # globlist_id.append(id)
        # globlist_x.append(x)
        # globlist.append(data)
        newtime = newdata[0]
        latency[station_name] = newtime - mytime
        mytime = newtime
        id = list(latency.keys())
        latency_time = list(latency.values())
# Define MQTT broker server
broker_address = "203.101.226.126"
broker_port = 1883

# Establish MQTT connection
mqttc = mqtt.Client()  # create new instance
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect(broker_address, broker_port, 60)  # connect to broker
mqttc.subscribe("auscors/GA/CORS/RTCMv3/+/OBS/#")  # subscribe
