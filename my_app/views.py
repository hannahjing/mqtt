from django.shortcuts import render
# Create your views here.
from . import mqtt
from django.http import HttpResponse


def index(request):
    return render(request, 'my_app/index.html')


def location(request):

    dict_xyz = {'xyz': mqtt.xyz}
    return render(request,'my_app/location.html', dict_xyz)


def geo(request):
    dict_geo ={'geo':mqtt.geo}
    return render(request, 'my_app/geo.html', dict_geo)


def repeatablity(request):
    dict_repeat={'repeat':mqtt.repeat}
    return render(request, 'my_app/repeatability.html', dict_repeat)


