from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'my_app'

   # def ready(self):
    #    from . import mqtt
     #   mqtt.client.loop_start()