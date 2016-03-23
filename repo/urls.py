from django.conf.urls import url

from . import views

app_name = 'repo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^component_list', views.componentList, name='componentList'),
    url(r'^components/(?P<component_id>[0-9]+)/$', views.componentDetail, name='componentDetail'),
    url(r'^devices/(?P<device_id>[0-9]+)/$', views.deviceDetail, name='deviceDetail'),
    url(r'^edit_component/(?P<component_id>[0-9]+)/$', views.editComponent, name='editComponent'),
    url(r'^edit_device/(?P<device_id>[0-9]+)/$', views.editDevice, name='editDevice'),
    url(r'^device_list/', views.deviceList, name='deviceList'),
    url(r'^add_test/', views.addTest, name='addTest'),
    url(r'^create_test', views.createTest, name='createTest'),
    url(r'^sort_components', views.sortComponents, name='sortComponents'),
    url(r'^sort_devices', views.sortDevices, name='sortDevices'),
    url(r'^login_page', views.loginIndex, name='loginIndex'),
    url(r'^login', views.authenticateLogin, name='authenticateLogin'),
    url(r'^my_tests', views.myTests, name='myTests'),
    url(r'^logout', views.logMeOut, name='logout'),
    url(r'^save_component/(?P<component_id>[0-9]+)/$', views.saveComponent, name='saveComponent'),
    url(r'^save_device/(?P<device_id>[0-9]+)/$', views.saveDevice, name='saveDevice'),
]
