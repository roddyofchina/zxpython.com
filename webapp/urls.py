#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'


from django.conf.urls import url
from webapp import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'login/$', views.login,name='login'),
]




