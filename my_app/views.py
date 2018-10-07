from django.shortcuts import render
# Create your views here.
from . import mqtt
from django.http import HttpResponse


def index(request):
    return render(request, 'my_app/index.html')


def location(request):
    return HttpResponse(mqtt.mqttc.loop_start())


def geo(request):
    return render(request, 'my_app/geo.html')


def repeatablity(request):
    return render(request, 'my_app/repeatability.html')



