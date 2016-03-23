from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^component_list', hello.views.componentList, name='componentList'),
    url(r'^components/(?P<component_id>[0-9]+)/$', hello.views.componentDetail, name='componentDetail'),
    url(r'^edit_component/(?P<component_id>[0-9]+)/$', hello.views.editComponent, name='editComponent'),
    url(r'^sort_components', hello.views.sortComponents, name='sortComponents'),
    url(r'^save_component/(?P<component_id>[0-9]+)/$', hello.views.saveComponent, name='saveComponent'),
               
    url(r'^devices/(?P<device_id>[0-9]+)/$', hello.views.deviceDetail, name='deviceDetail'),
    url(r'^edit_device/(?P<device_id>[0-9]+)/$', hello.views.editDevice, name='editDevice'),
    url(r'^device_list/', hello.views.deviceList, name='deviceList'),
    url(r'^sort_devices', hello.views.sortDevices, name='sortDevices'),
    url(r'^save_device/(?P<device_id>[0-9]+)/$', hello.views.saveDevice, name='saveDevice'),
    
    url(r'^add_test/', hello.views.addTest, name='addTest'),
    url(r'^create_test', hello.views.createTest, name='createTest'),
    url(r'^my_tests', hello.views.myTests, name='myTests'),
    
    url(r'^login_page', hello.views.loginIndex, name='loginIndex'),
    url(r'^login', hello.views.authenticateLogin, name='authenticateLogin'),
    url(r'^signup', hello.views.authenticateSignUp, name='authenticateSignUp'),
    url(r'^logout', hello.views.logMeOut, name='logout'),
]