#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: urls.py
@time: 2020/7/3 10:39
'''
from django.conf.urls import url
from django.urls import re_path, path

from tools import views

app_name="tools"

urlpatterns = [

    #  tools页面
    re_path(r'^page$', views.tools_page, name='tools_page'),
    #  tools工具信息接口
    re_path(r'^page_api$', views.page_tools_api, name='page_tools_api'),
    #  tools页面排行接口
    re_path(r'^top_api$', views.tools_top_api, name='top_api'),
    #  tools detail
    re_path(r'^detail_api$', views.detail_api, name='detail_api'),
    #  tools down_load
    re_path(r'^download_api$', views.download_api, name='download_api'),

]