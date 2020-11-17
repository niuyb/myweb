#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from picture import views
from picture.views import picture_data, picture

app_name="picture"

urlpatterns = [

    # picture分页
    path(r'',views.picture, name='picture'),
    # picture_api
    re_path(r'^img/i_api$', picture_data.picture_api, name='picture_api'),





    # test
    re_path(r'^per$', views.picture_per, name='picture_base'),
    # test
    re_path(r'^pexels$', views.picture_base, name='picture_base'),

    re_path(r'^test$', views.picture_test, name='picture_t'),

]