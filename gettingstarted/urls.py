from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^component_list', hello.views.list_all_components, name='componentList'),
    url(r'^components/(?P<component_id>[0-9]+)/$', hello.views.component_details, name='componentDetail'),
    url(r'^edit_component/(?P<component_id>[0-9]+)/$', hello.views.edit_component, name='editComponent'),
    url(r'^sort_components', hello.views.sort_all_components, name='sortComponents'),
    url(r'^save_component/(?P<component_id>[0-9]+)/$', hello.views.save_component, name='saveComponent'),
               
    url(r'^devices/(?P<device_id>[0-9]+)/$', hello.views.deviceDetail, name='deviceDetail'),
    url(r'^edit_device/(?P<device_id>[0-9]+)/$', hello.views.editDevice, name='editDevice'),
    url(r'^device_list/', hello.views.deviceList, name='deviceList'),
    url(r'^sort_devices', hello.views.sortDevices, name='sortDevices'),
    url(r'^save_device/(?P<device_id>[0-9]+)/$', hello.views.saveDevice, name='saveDevice'),
    
    url(r'^add_test', hello.views.addTest, name='addTest'),
    url(r'^create_test', hello.views.createTest, name='createTest'),
    url(r'^my_tests', hello.views.myTests, name='myTests'),
    url(r'^add_component', hello.views.add_component_test, name='add_component'),
    url(r'^add_device', hello.views.add_device_test, name='add_device'),
    url(r'^remove_component/(?P<component_id>[0-9]+)/$', hello.views.delete_component, name='delete_component'),
    url(r'^remove_device/(?P<device_id>[0-9]+)/$', hello.views.delete_device, name='delete_device'),
    
    url(r'^login_page', hello.views.login_page, name='loginIndex'),
    url(r'^signup_page', hello.views.signup_page, name='signup_index'),
    url(r'^login', hello.views.authenticate_login, name='authenticateLogin'),
    url(r'^signup', hello.views.authenticate_signup, name='authenticateSignUp'),
    url(r'^logout', hello.views.logout, name='logout'),
    url(r'^my_account', hello.views.my_account, name='my_account'),
]