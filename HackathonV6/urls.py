from django.conf.urls import patterns, include, url

from django.contrib import admin
from hacku.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackathonV6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('hacku.urls')),
)
