from django.conf.urls import patterns, url
from hacku import views
from hacku.models import *
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addQues$', views.addQues, name='addQues'),
    url(r'^places$', views.cat1, name='cat1'),
    url(r'^handsets$', views.cat2, name='cat2'),
    url(r'^coding$', views.cat3, name='cat3'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^abc$', views.logout_v, name='logout'),
    url(r'^(?P<qComment_id>\d+)/$', views.qdisplay, name='qdisplay'),
)