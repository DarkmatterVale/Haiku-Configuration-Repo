from django.conf.urls import url

from . import views

app_name = 'repo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^component_list', views.componentList, name='componentList'),
    url(r'^components/(?P<component_id>[0-9]+)/$', views.componentDetail, name='compondentDetail'),
    url(r'^device_list', views.deviceList, name='deviceList'),
]
