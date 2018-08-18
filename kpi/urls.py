from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',  kpi_home, name='home'),
    url(r'^follower/(?P<slug>[\w-]+)/$', KPIFollowerView.as_view(), name='detail-follower'),
    url(r'^business/(?P<slug>[\w-]+)/$', KPIBusinessView.as_view(), name='detail-business'),
    url(r'^follower/(?P<slug>[\w-]+)/api/data/$', get_data_follower, name='api-f-data'),
    url(r'^business/(?P<slug>[\w-]+)/api/data/$', get_data_business, name='api-b-data'),
    # url(r'^data', get_data, name='bussness_data'),
    # url(r'^prueba', prueba, name='prueba'),
]