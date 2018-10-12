from . import mqtt

#connect to broker
#mqttc.subscribe("coordinates/+/XYZ") #subscribe

mqtt.mqttc.loop_start()

