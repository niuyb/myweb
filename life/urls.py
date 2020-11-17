#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from life import views

app_name="life"

urlpatterns = [

    # test
    re_path(r'', views.life_page, name='life_page'),

    # test
    re_path(r'^copy$', views.life_copy, name='life_copy'),

    # infos_api
    # re_path(r'^infos_api$', views.infos_api, name='infos_api'),

]