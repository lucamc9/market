from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from accounts.views import RegisterView, LoginView, activate_user_view, AccountTypeView
from profiles.views import SearchSMEView, HomePageView, HomeActivateView
from businessplan.views import InfoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='base_home'),
    url(r'^activation/$', HomeActivateView.as_view(), name='base_home_activation'),
    url(r'^account/$', AccountTypeView.as_view(), name='account_type'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^info/(?P<slug>[\w-]+)/$', InfoView.as_view(), name='info'),
    url(r'^profile/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    url(r'^businessplan/', include(('businessplan.urls', 'businessplan'), namespace='businessplan')),
    url(r'^diagnostics/', include(('diagnostics.urls', 'diagnostics'), namespace='diagnostics')),
    url(r'^dataroom/', include(('dataroom.urls', 'dataroom'), namespace='accordion')),
    url(r'^diligenceroom/', include(('diligence.urls', 'diligence'), namespace='diligence')),
    url(r'^kpi/', include(('kpi.urls', 'kpi'), namespace='kpi')),
    url(r'^search-companies/', SearchSMEView.as_view(), name='search-companies')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


