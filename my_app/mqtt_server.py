import paho.mqtt.client as mqtt

MQTT_Topic = "auscors/GA/CORS/RTCMv3/+/OBS/#"
#globlist_id=[]
#globlist_x=[]
timestamp = []

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    mqttc.subscribe(MQTT_Topic, 0)


def on_message(mosq, obj, msg):
    #global s

    #print(msg.payload)
    #views.getdata(msg.payload)
    #store_Sensor_Data_to_DB.sensor_Data_Handler(msg.topic, msg.payload)
    #views.sensor_Data_Handler(msg.topic, msg.payload)
    #s = msg.payload
    #list = []
    data_parse(msg.topic, msg.payload)
    return msg.payload

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


def data_parse(topic,data):
    topicSplit = topic.split('/')
    mystation = topicSplit[4]
    data=data.decode("utf-8").split(',')
    dictionary=[]
    global timestamp
    if topic =="auscors/GA/CORS/RTCMv3/"+mystation+"/OBS/timestamped":
        dictionary[mystation]=data
        timestamp.append(data)
# Define MQTT broker server
broker_address="203.101.226.126"
broker_port = 1883

#TCP_IP = '127.0.0.1'
#TCP_PORT = 10011

# Establish MQTT connection
mqttc = mqtt.Client() #create new instance
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect(broker_address, broker_port, 60)

