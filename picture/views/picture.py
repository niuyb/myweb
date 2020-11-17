#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/13 11:56
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





def picture(request):
    return render(request, "picture/picture.html")


def picture_base(request):
    return render(request, "picture/picture_b.html")

def picture_per(request):
    return render(request, "picture/picture_per.html")

def picture_test(request):
    return render(request, "picture/picture_test.html")