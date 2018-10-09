import paho.mqtt.client as mqtt
from . import views

MQTT_Topic = "coordinates/#"
#globlist_id=[]
#globlist_x=[]
globlist=[]
globlist2=[]
globlist3=[]
globlist4=[]
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
    mystation = topicSplit[1]
    #[id,x,y,z]=data.decode("utf-8").split(',')
    data=data.decode("utf-8").split(',')
    global globlist2, globlist3, globlist,globlist4
    if topic == "coordinates/" + mystation + "/XYZ":

        #globlist_id.append(id)
        #globlist_x.append(x)
        globlist.append(data)
        #globlist[mystation].append(data[1:4])
        #globlist.append(dictionary)

    elif topic == "coordinates/" + mystation + "/repeatability":
        globlist2.append(data)
    elif topic == "coordinates/" + mystation + "/geodetic":
        globlist3.append(data)

    dictionary = {}
    dictionary[mystation]=(data[1:4])
    globlist4.append(dictionary)


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

