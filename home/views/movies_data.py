#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/12 13:35
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


def home_movies_api(request):
    # 一共8条数据
    # 标题不能超过10个字符
    # content 内容不能超过50个字符
    result={"data":[],"code":1,"msg":""}

    result["data"]=[
      {"movies": "/static/img/home/godzilla.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼1", "target": "#","class_name":"solu_dl_0"},
      {"movies": "/static/img/home/waterfall_img3.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼2", "target": "#","class_name":"solu_dl_1"},
      {"movies": "/static/img/home/waterfall_img1.jpg", "title": "与怪兽一起嘶吼与怪兽", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼3", "target": "#","class_name":"solu_dl_2"},
      {"movies": "/static/img/home/waterfall_img2.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼4", "target": "#","class_name":"solu_dl_3"},
      {"movies": "/static/img/home/waterfall_img5.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼5", "target": "#","class_name":"solu_dl_3"},
      {"movies": "/static/img/home/waterfall_img4.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼6", "target": "#","class_name":"solu_dl_2"},
      {"movies": "/static/img/home/waterfall_img3.jpg", "title": "哥斯拉", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼7", "target": "#","class_name":"solu_dl_1"},
      {"movies": "/static/img/home/godzilla.jpg", "title": "我的世界", "content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼8", "target": "#","class_name":"solu_dl_0"},
    ]

    return JsonResponse(result,safe=False)