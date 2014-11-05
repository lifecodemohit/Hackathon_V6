from django.conf.urls import patterns, url
from hacku import views
from hacku.models import *
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)