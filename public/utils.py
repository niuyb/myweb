#!/usr/bin/env python
# encoding: utf-8
import base64
import hashlib

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


"""pandas查询数据的连接信息"""
def engine(db_info):
    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format(
            db_info['USER'],
            db_info['PASSWORD'],
            db_info['HOST'],
            db_info['NAME'],
            'utf8'
        ), poolclass=NullPool
    )
    conn_engine = engine.connect()  # 创建连接
    return conn_engine


"""获取pymsql链接与游标"""
def get_conn(host,user,passwd,db,port=3306):
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset='utf8')
    # 获得游标
    cur = conn.cursor()
    return conn,cur


"""加密方式 MD5(base64)"""
def Encrypt(string):
    str_64=str(base64.b64encode(string.encode("utf-8")),'utf-8')
    print(str_64)
    # h= hashlib.md5()
    # h.update(str_64.encode(encoding = 'utf-8'))
    # return  h.hexdigest()

"""解密方式 MD5(base64)"""

def Decrypt():
    pass



print(Encrypt("qweqwsadfdsfgds213423423423452fsdfsfeqwe牛于斌"))


