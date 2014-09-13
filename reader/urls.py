__author__ = 'arya'
from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns('',
    url(r'^$', views.upload_file, name='index'),
    url(r'^results/', views.results, name='results'),
)
