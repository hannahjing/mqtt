from django.shortcuts import render
# Create your views here.
from . import mqtt
from django.http import HttpResponse


def index(request):
    return render(request, 'my_app/index.html')


def location(request):
    #dict_xyz={'id':mqtt.globlist_id,'x':mqtt.globlist_x}
        #,'y':mqtt.globlist_y,'z':mqtt.globlist_z}
    dict_xyz={'xyz':mqtt.globlist}
    return render(request, 'my_app/location.html',dict_xyz)


def geo(request):
    dict_geo ={'geo':mqtt.globlist3}
    return render(request, 'my_app/geo.html', dict_geo)


def repeatablity(request):
    dict_repeat={'repeat':mqtt.globlist2}
    return render(request, 'my_app/repeatability.html', dict_repeat)

def test(request):
    dict_test ={'test':mqtt.globlist4}
    return render(request, 'my_app/test.html', dict_test)


#def parsedata(data):
 #   global a,b,c,d
  #  string=data.decode("utf-8")
   # [a,b,c,d]=string.split(',')
    #print(a)

