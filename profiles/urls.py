from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sme/create/$', SMEProfileCreateView.as_view(), name='create-sme'),
    url(r'^sme/(?P<slug>[\w-]+)/update/$', SMEProfileUpdateView.as_view(), name='update-sme'),
    url(r'^sme/(?P<slug>[\w-]+)/$', SMEProfileDetailView.as_view(), name='detail-sme'),
    url(r'^staff/create/$', StaffProfileCreateView.as_view(), name='create-staff'),
    url(r'^staff/(?P<slug>[\w-]+)/update/$', StaffProfileUpdateView.as_view(), name='update-staff'),
    url(r'^staff/(?P<slug>[\w-]+)/$', StaffProfileDetailView.as_view(), name='detail-staff'),
]