#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'


from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^article/list/$',views.article_list, name='article_list'),
]