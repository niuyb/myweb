#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from home import views

app_name="home"

urlpatterns = [
    # 主页
    path(r'', views.home, name='home_page'),


    # img_api
    re_path(r'^img/i_api$', views.home_picture_api, name='home_picture_api'),
    # movies_api
    re_path(r'^movies/m_api$', views.home_movies_api, name='home_movies_api'),
    # life_api
    re_path(r'^life/l_api$', views.home_life_api, name='home_life_api'),
    # tools_api
    re_path(r'^tools/t_api$', views.home_tools_api, name='home_tools_api'),
    # content_api
    re_path(r'^content/c_api$', views.home_content_api, name='home_content_api'),


    # test
    re_path(r'^test$', views.post_input, name='test'),
    re_path(r'^show$', views.post_show, name='show'),

    #htmltest
    re_path(r'^mytest$', views.mytest, name='mytest'),

]