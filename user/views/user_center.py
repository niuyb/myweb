#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/14 17:19
# 工具：PyCharm
# Python版本：3.7.0

# python 2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python 3
# import sys
# import importlib
# importlib.reload(sys)
from django.shortcuts import render




def user_center_home(request):
    return render(request, 'user/user_center_home.html')

def user_center_test(request):
    return render(request, 'user/temp.html')