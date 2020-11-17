#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from movies import views

app_name="movies"

urlpatterns = [

    # test
    re_path(r'^page$', views.movies_page, name='movies_page'),
    # infos_api
    re_path(r'^infos_api$', views.infos_api, name='infos_api'),



    # test
    re_path(r'^test$', views.test, name='movies_test'),

]