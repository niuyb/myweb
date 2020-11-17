#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/12 15:06
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


def home_life_api(request):
    # 一共6条生活信息
    # title  标题不能超过18个字符
    # content 内容不能超过80个字符
    result={"data":[],"code":1,"msg":""}

    result["data"]=[
      {"life": "/static/img/home/godzilla.jpg",       "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼1", "target": "#","date":"2020-10-11"},
      {"life": "/static/img/home/waterfall_img3.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼2", "target": "#","date":"2020-10-12"},
      {"life": "/static/img/home/waterfall_img1.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼3", "target": "#","date":"2020-10-13"},
      {"life": "/static/img/home/waterfall_img2.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼4", "target": "#","date":"2020-10-14"},
      {"life": "/static/img/home/waterfall_img5.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼5", "target": "#","date":"2020-10-15"},
      {"life": "/static/img/home/waterfall_img4.jpg", "title": "个人网站建立", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼6", "target": "#","date":"2020-10-16"},
    ]

    return JsonResponse(result,safe=False)