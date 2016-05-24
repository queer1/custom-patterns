from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^measurements/new/$', views.new_measurements, name='new_measurements'),
]