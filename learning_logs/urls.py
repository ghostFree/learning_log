from django.conf.urls import re_path
from django.urls import path
from . import views



urlpatterns = [
#    re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
#    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^topics/$', views.topics, name='topics')
]

app_name = 'learning_logs'