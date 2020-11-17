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


def home_content_api(request):
    # 4条滚图信息


    result={"data":[],"code":1,"msg":""}

    result["data"]=[
      {"contents": "/static/img/home/banner_sea.jpg","target": "#",},
      {"contents": "/static/img/home/banner_leaf.jpg","target": "#",},
      {"contents": "/static/img/home/banner_tree.jpg","target": "#",},
      {"contents": "/static/img/home/banner_light.jpg","target": "#",},
    ]

    return JsonResponse(result,safe=False)