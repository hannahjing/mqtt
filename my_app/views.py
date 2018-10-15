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
    dict_test ={'timestamp': mqtt_server.timestamp}
    return render(request, 'my_app/test.html', dict_test)

