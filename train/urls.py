#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

from django.conf.urls import url
from train import views

urlpatterns = [
    url(r'^video/$',views.TrainVideo, name='TrainVideo'),
]