from django.conf.urls import url
from .views import (
    DiligenceRoomCreateView,
    DiligenceRoomDetailView,
    DiligenceRoomUpdateView
)

urlpatterns = [
    url(r'^$', DiligenceRoomCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/update/$', DiligenceRoomUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/$', DiligenceRoomDetailView.as_view(), name='detail'),
]