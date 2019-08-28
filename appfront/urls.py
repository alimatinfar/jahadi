from django.conf.urls import url
from . import views


app_name = 'appfront'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cooperation/$', views.cooperation, name='cooperation'),

]