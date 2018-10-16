from . import mqtt,latency,mqtt_server

#connect to broker
#mqttc.subscribe("coordinates/+/XYZ") #subscribe

mqtt.mqttc.loop_start()
latency.mqttc.loop_start()
mqtt_server.mqttc.loop_start()


