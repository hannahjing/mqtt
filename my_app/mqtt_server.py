#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:25:50 2018

@author: jing
"""

# !/usr/bin/python
raspberrypi = {}
MITProject_2018_S3 = {}
MITProject_2018_S1 = {}
MITProject_2018_S2 = {}
MITProject_2018_S4 = {}
myserver=[]
import sys, time, os
import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mosq, obj, msg):
    global s
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
    # [id,x,y,z]=data.decode("utf-8").split(',')
    newdata = data.decode("utf-8").split(',')
    # newdata= list(map(lambda x:float(x), newdata))

    mytopic = ['/stat/ipaddr/chkTime', '/stat/ipaddr/ip', '/stat/Uptime/chkTime', '/stat/Uptime/Uptime',
               '/CPU_Pct/chkTime', '/CPU_Pct/CPU']
    global MITProject_2018_S1,MITProject_2018_S2,MITProject_2018_S3,MITProject_2018_S4,raspberrypi,myserver
    for i in mytopic:
        if topic == "/QUT/MITProjects_2018/Servers/MITProject_2018_S1" + i:
            i = i.replace('/', ' ')
            MITProject_2018_S1[i] = newdata
        elif topic == "/QUT/MITProjects_2018/Servers/MITProject_2018_S2" + i:
            i = i.replace('/', ' ')
            MITProject_2018_S2[i] = newdata
        elif topic == "/QUT/MITProjects_2018/Servers/MITProject_2018_S3" + i:
            i = i.replace('/', ' ')
            MITProject_2018_S3[i] = newdata

        elif topic == "/QUT/MITProjects_2018/Servers/MITProject_2018_S4" + i:
            i = i.replace('/', ' ')
            MITProject_2018_S4[i] = newdata
        elif topic == "/QUT/MITProjects_2018/Servers/raspberrypi" + i:
            i = i.replace('/', ' ')
            raspberrypi[i] = newdata


# Define MQTT broker server

broker_address = "203.101.225.212"
broker_port = 1883

# Establish MQTT connection
mqttc = mqtt.Client()  # create new instance
mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect(broker_address, broker_port, 60)  # connect to broker
# mqttc.subscribe("auscors/GA/CORS/RTCMv3/STR24") #subscribe
mqttc.subscribe("/QUT/MITProjects_2018/Servers/#")  # subscribe
# mqttc.subscribe("auscors/GA/CORS/RTCMv3/+/BDS/#") #subscribe
