from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()

import repo.views

urlpatterns = [
               url(r'^$', repo.views.index, name='index'),
               url(r'^component_list', repo.views.componentList, name='componentList'),
               url(r'^components/(?P<component_id>[0-9]+)/$', repo.views.componentDetail, name='componentDetail'),
               url(r'^devices/(?P<device_id>[0-9]+)/$', repo.views.deviceDetail, name='deviceDetail'),
               url(r'^edit_component/(?P<component_id>[0-9]+)/$', repo.views.editComponent, name='editComponent'),
               url(r'^edit_device/(?P<device_id>[0-9]+)/$', repo.views.editDevice, name='editDevice'),
               url(r'^device_list/', repo.views.deviceList, name='deviceList'),
               url(r'^add_test/', repo.views.addTest, name='addTest'),
               url(r'^create_test', repo.views.createTest, name='createTest'),
               url(r'^sort_components', repo.views.sortComponents, name='sortComponents'),
               url(r'^sort_devices', repo.views.sortDevices, name='sortDevices'),
               url(r'^login_page', repo.views.loginIndex, name='loginIndex'),
               url(r'^login', repo.views.authenticateLogin, name='authenticateLogin'),
               url(r'^my_tests', repo.views.myTests, name='myTests'),
               url(r'^logout', repo.views.logMeOut, name='logout'),
               url(r'^save_component/(?P<component_id>[0-9]+)/$', repo.views.saveComponent, name='saveComponent'),
               url(r'^save_device/(?P<device_id>[0-9]+)/$', repo.views.saveDevice, name='saveDevice'),
               ]