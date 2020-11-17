#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/12 15:48
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

from django.http import JsonResponse


def home_tools_api(request):
    # 一共6条工具信息
    # title  标题不能超过18个字符
    # content 内容不能超过60个字符
    result={"data":[],"code":1,"msg":""}

    result["data"]=[
      {"tools": "/static/img/home/tools_img.jpg",       "title": "个人网站建立个人网站建立个人网站我的", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪与怪嘶吼,与嘶吼,与怪兽一起怪兽一起怪兽一起怪兽", "target": "#"},
      {"tools": "/static/img/home/tools_img.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼2", "target": "#"},
      {"tools": "/static/img/home/tools_img.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼3", "target": "#"},
      {"tools": "/static/img/home/tools_img.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼4", "target": "#"},
      {"tools": "/static/img/home/tools_img.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼5", "target": "#"},
      {"tools": "/static/img/home/tools_img.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼6", "target": "#"},
    ]

    return JsonResponse(result,safe=False)