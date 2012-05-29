from django.conf.urls.defaults import patterns, include, url
from fbapp.fb.views import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^fbapp/', include('fbapp.fb.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^facebook/', include('django_facebook.urls')),
		url(r'^accounts/', include('django_facebook.auth_urls')),
)
