from django.conf.urls import url
from .views import (
    BusinessPlanDetailView,
    BusinessPlanCreateView,
    BusinessPlanUpdateView,
)

urlpatterns = [
    url(r'^$', BusinessPlanCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/update/$', BusinessPlanUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/$', BusinessPlanDetailView.as_view(), name='detail'),
]