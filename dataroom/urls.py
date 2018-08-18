from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    RedirectView,
    DataRoomFormView,
    DataRoomDetailView
)


urlpatterns = [
    url(r'^$', RedirectView.as_view(), name='redirect'),
    url(r'^compliance-form/$', DataRoomFormView.as_view(sub_area='Compliance'), name='compliance'),
    url(r'^legal-form/$', DataRoomFormView.as_view(sub_area='Legal'), name='legal'),
    url(r'^environmental-form/$', DataRoomFormView.as_view(sub_area='Environmental'), name='environmental'),
    url(r'^finance-form/$', DataRoomFormView.as_view(sub_area='Finance'), name='finance'),
    url(r'^company-form/$', DataRoomFormView.as_view(sub_area='Company'), name='company'),
    url(r'^governance-form/$', DataRoomFormView.as_view(sub_area='Governance'), name='governance'),
    url(r'^facilities-form/$', DataRoomFormView.as_view(sub_area='Facilities'), name='facilities'),
    url(r'^technology-form/$', DataRoomFormView.as_view(sub_area='Technology'), name='technology'),
    url(r'^processes-form/$', DataRoomFormView.as_view(sub_area='Processes'), name='processes'),
    url(r'^organisation-form/$', DataRoomFormView.as_view(sub_area='Organisation'), name='organisation'),
    url(r'^staff-form/$', DataRoomFormView.as_view(sub_area='Staff'), name='staff'),
    url(r'^competition-form/$', DataRoomFormView.as_view(sub_area='Competition'), name='competition'),
    url(r'^marketing-form/$', DataRoomFormView.as_view(sub_area='Marketing'), name='marketing'),
    url(r'^procurement-form/$', DataRoomFormView.as_view(sub_area='Procurement'), name='procurement'),
    url(r'^(?P<slug>[\w-]+)/$', DataRoomDetailView.as_view(), name='detail'),
]