#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from upload import views

app_name="upload"

urlpatterns = [

    # test
    re_path(r'^upload$', views.upload_page, name='upload$'),

    re_path(r'^test$', views.upload_test, name='upload_test'),

]