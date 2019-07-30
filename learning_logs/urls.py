from django.conf.urls import re_path
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
#    re_path(r'^$', views.index, name='index'),
    path('', views.index)
]

