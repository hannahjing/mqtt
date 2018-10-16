import paho.mqtt.client as mqtt
from . import views

MQTT_Topic = "coordinates/#"
#globlist_id=[]
#globlist_x=[]

globdict2={}
globdict3={}
globdict={}
key=[]
value=[]

list_to_float = []
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    mqttc.subscribe(MQTT_Topic, 0)


def on_message(mosq, obj, msg):
    data_parse(msg.topic, msg.payload)
    return msg.payload

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


def data_parse(topic,data):
    topicSplit = topic.split('/')
    mystation = topicSplit[1]
    #[id,x,y,z]=data.decode("utf-8").split(',')
    newdata=data.decode("utf-8").split(',')
    global globdict2, globdict3,globdict,key,value,list_to_float
    if topic == "coordinates/" + mystation + "/XYZ":
        globdict[mystation]=newdata[1:4]
    elif topic == "coordinates/" + mystation + "/repeatability":
        globdict2[mystation]=newdata[1:4]
    elif topic == "coordinates/" + mystation + "/geodetic":
        globdict3[mystation]=newdata[1:4]
        key = list(globdict3.keys())
        value = list(globdict3.values())

# Define MQTT broker server
broker_address="203.101.225.212"
broker_port = 1883

#TCP_IP = '127.0.0.1'
#TCP_PORT = 10011

# Establish MQTT connection
mqttc = mqtt.Client() #create new instance
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect(broker_address, broker_port, 60)

