#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/20 20:04
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





from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect





#
def tools_page(request):
    return render(request, "tools/tools_page.html")


# def upload_test(request):
#     return JsonResponse({"id":101})