from django.conf.urls import url
from .views import (
    DiagnosticsDetailView,
    DiagnosticsCreateView,
)

urlpatterns = [
    url(r'^$', DiagnosticsCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', DiagnosticsDetailView.as_view(), name='detail'),
]