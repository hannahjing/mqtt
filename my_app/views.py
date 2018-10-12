from django.shortcuts import render
from . import mqtt,models,mqtt_server
import json
# Create your views here.


def index(request):
    location_data=json.dumps(mqtt.globdict,separators=(',', ':'))
    return render(request, 'my_app/index.html',{"my_data": location_data})


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

