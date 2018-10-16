from django.conf.urls import url
from my_app import views


#Template tagging
app_name = 'my_app'

urlpatterns = [
    url(r'^geo/$', views.geo, name='geo'),
    url(r'^location/$', views.location, name='location'),
    url(r'^repeatability/$', views.repeatablity, name='repeatability'),
    url(r'^test/$', views.test, name='test'),
    url(r'^performance/$', views.performance, name='performance'),
]