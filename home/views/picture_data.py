#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/10 13:37
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


def home_picture_api(request):
    # 一共25条图片信息
    # 图片宽度为224  高度不限   按照原图片比例 向上取整之后赋值height即可
    # 标题不填写

    result=[
      # {"picture": "{%  static 'img/home/waterfall_img4.jpg' %}", "title": "picture-4", "height": 224, "target": "#"},

      {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
      {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},
      {"picture": "/static/img/home/waterfall_img1.jpg", "title": "", "height": 336, "target": "#"},
      {"picture": "/static/img/home/waterfall_img2.jpg", "title": "", "height": 317, "target": "#"},
      {"picture": "/static/img/home/waterfall_img5.jpg", "title": "", "height": 373, "target": "#"},
      {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
      {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},

      # {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
      # {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},
      # {"picture": "/static/img/home/waterfall_img1.jpg", "title": "", "height": 336, "target": "#"},
      # {"picture": "/static/img/home/waterfall_img2.jpg", "title": "", "height": 317, "target": "#"},
      {"picture": "/static/img/home/waterfall_img5.jpg", "title": "", "height": 373, "target": "#"},
      {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
      {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},

      {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
      {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},
      {"picture": "/static/img/home/waterfall_img3.jpg", "title": "", "height": 336, "target": "#"},

      {"picture": "/static/img/home/banner_tree.jpg", "title": "", "height":140, "target": "#"},
      {"picture": "/static/img/home/banner_light.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_tree.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_light.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_tree.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_light.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_tree.jpg", "title": "", "height": 140, "target": "#"},
      {"picture": "/static/img/home/banner_light.jpg", "title": "", "height": 140, "target": "#"},

      {"picture": "/static/img/home/waterfall_img1.jpg", "title": "", "height": 336, "target": "#"},
      {"picture": "/static/img/home/waterfall_img2.jpg", "title": "", "height": 317, "target": "#"},
      {"picture": "/static/img/home/waterfall_img5.jpg", "title": "", "height": 373, "target": "#"},
      {"picture": "/static/img/home/waterfall_img4.jpg", "title": "", "height": 224, "target": "#"},
    ]

    return JsonResponse(result,safe=False)








