from django.shortcuts import render
from . import mqtt,models,mqtt_server,latency
import json
from builtins import filter
# Create your views here.


def index(request):
    location_key=mqtt.key
    location_value=mqtt.value
    lat_id=latency.id
    lat_time=latency.latency_time
    lat=latency.latency
    return render(request, 'my_app/index.html',{'myvalue':json.dumps(location_value),'mykey':json.dumps(location_key),
                                                'latency':lat,'id':json.dumps(lat_id),'time':json.dumps(lat_time)})
    #'time':json.dumps((lat_time))})


def location(request):
    #dict_xyz={'id':mqtt.globlist_id,'x':mqtt.globlist_x}
        #,'y':mqtt.globlist_y,'z':mqtt.globlist_z}
    dict_xyz={'xyz':mqtt.globdict}
    return render(request, 'my_app/location.html',dict_xyz)


def geo(request):
    dict_geo ={'geo':mqtt.globdict3}
    return render(request, 'my_app/geo.html', dict_geo)


def repeatablity(request):
    dict_repeat={'repeat':mqtt.globdict2}
    return render(request, 'my_app/repeatability.html', dict_repeat)


def test(request):
    lat_id = latency.id
    lat_time = latency.latency_time
    lat = latency.latency
    return render(request, 'my_app/test.html', {'id':json.dumps(lat_id),'time':json.dumps(lat_time),'latency':lat})


def performance(request):
    S1=mqtt_server.MITProject_2018_S1
    S2=mqtt_server.MITProject_2018_S2
    S3=mqtt_server.MITProject_2018_S3
    S4=mqtt_server.MITProject_2018_S4
    RA=mqtt_server.raspberrypi
    return render(request, 'my_app/performance.html', {'s1':S1,'s2':S2,'s3':S3,'s4':S4,'ra':RA})
