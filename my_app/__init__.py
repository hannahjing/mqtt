from . import mqtt,latency

#connect to broker
#mqttc.subscribe("coordinates/+/XYZ") #subscribe

mqtt.mqttc.loop_start()
latency.mqttc.loop_start()

