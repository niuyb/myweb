#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/26 11:53
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
import json
import random

from django.http import JsonResponse, HttpResponse, FileResponse, StreamingHttpResponse
from myweb import settings
from myweb.settings import STATICFILES_DIRS
from public.Time import ms_time
from public.config import RESULT, TOOLS_TYPE, FILE_TYPE
import pandas as pd
from public.utils import engine

pd.set_option('display.max_rows', 1000)  # 展示所有行
pd.set_option('display.max_columns', 1000)  # 展示所有列
pd.set_option('display.width', 1000)



def get_color(tools_color_list):
    list_len = len(tools_color_list)
    index=random.randint(0, list_len-1)
    color = tools_color_list[index]
    del tools_color_list[index]
    return tools_color_list,color




def page_tools_api(request):
    # 一共5条工具信息
    # {"id":"1","tools": "/static/img/tools/python.jpg", "title": "个人网站建立","content": "与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼,与怪兽一起嘶吼2", "upload_date": "2020-10-11&17:00","download_times": "20","install_tools":"安装包", "type": "编程工具", "target": "#"},

    page = int(request.GET.get("page",1))
    page_index = page * 5 - 5

    result = RESULT
    conn_myweb = engine(settings.DATABASES['default'])
    tools_sql = """ select id,name,content,upload_date,download_times,file_type,tools_type,target,img_url from tools_page order by upload_date desc limit %s,5 """ %page_index
    total_sql = """ select count(id) as count_num from tools_page """
    tools_df = pd.read_sql_query(tools_sql, conn_myweb)
    total_df = pd.read_sql_query(total_sql, conn_myweb)
    total = total_df['count_num'].iloc[0]
    result["total"] = str(total)
    result["data"] = []

    for row in tools_df.itertuples():
        tools_id = str(getattr(row, 'id'))
        img_url = getattr(row, 'img_url')
        name = getattr(row, 'name')
        content = getattr(row, 'content')
        upload_date = str(getattr(row, 'upload_date'))
        download_times = str(getattr(row, 'download_times'))
        file_type = getattr(row, 'file_type')
        tools_type = getattr(row, 'tools_type')
        target = getattr(row, 'target')
        dict_per = {
            "id": tools_id,
            "img_url": img_url,
            "name": name,
            "content": content,
            "upload_date": ms_time(int(upload_date)),
            "download_times": download_times,
            "file_type": FILE_TYPE.get(file_type, "其他"),
            "tools_type": TOOLS_TYPE.get(tools_type, "其他"),
            "target": target
        }
        result["data"].append(dict_per)
    return JsonResponse(result)


def tools_top_api(request):
    # top 9
    # 添加top数目的时候tools_color_list添加新颜色

    result = RESULT
    tools_color_list = ["#e53935", "#424242", "#4caf50", "#607d8b", "#d32f2f", "#2196f3", "#f4511e", "#757575","#673ab7"]

    conn_myweb = engine(settings.DATABASES['default'])
    top_sql = """ select id,name,remarks,download_times from tools_page order by download_times desc limit 0,9 """
    total_sql = """ select sum(download_times) as count_num from tools_page """

    total_df = pd.read_sql_query(total_sql, conn_myweb)
    total = int(total_df['count_num'].iloc[0])
    top_df = pd.read_sql_query(top_sql, conn_myweb)
    result["data"]=[]

    for row in top_df.itertuples():
        tools_id = str(getattr(row, 'id'))
        name = str(getattr(row, 'name'))
        remarks = str(getattr(row, 'remarks'))
        download_times = int(getattr(row, 'download_times'))

        percent = int(download_times/total*100)
        tools_color_list, color = get_color(tools_color_list)

        result["data"].append({
                "id":tools_id,
                "name": name,
                "description": remarks,
                "color": color,
                "percent": percent,
            })

    #    排序  mysql 排序

    return JsonResponse(result)


def detail_api(request):

    result = RESULT

    result["data"]={
        "title":"钉钉",
        "version":"123123.12.0.8",
        "content":"1111版本号版本号版本号版本号版本号版本号版本号版本版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号号",
        "method":"2222版本号版本号版本号版本号版本号版本号版本号版本版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号版本号号",
        "update":"2020-10-21 17:00",
        "img":"/static/img/tools/python.jpg",
    }

    return  JsonResponse(result)



def download_api(request):
    # D:\file\myweb\myweb\static\file\test_file.exe
    # result = RESULT
    # print(STATICFILES_DIRS,type(STATICFILES_DIRS))
    static_url = STATICFILES_DIRS[0]
    print(static_url+"\\file\\"+"test_file.exe")
    file = open(static_url+"\\file\\"+"test_file.exe", 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="test_file.exe"'
    return response


