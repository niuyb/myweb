#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ksar4
@file: operate_sql.py
@time: 2020/7/3 11:14
'''
"""
# 默认时区为0：00，改为东八区
# time_zone="+8:00"
"""



"""
torndb 只使用于 python2X 由于 Python3x语法不同使用时需要对torndb源码进行更改
主要是修改链接方式由MySQLdb 改为pymysql
语法的更改

需要修改五处

1、导入模块
import  pymysql
try:
    import pymysql.connections
    import pymysql.converters
    import pymysql.cursors
    #import MySQLdb.constants
    #import MySQLdb.converters
    #import MySQLdb.cursors


2、链接方式的更改
def reconnect(self):
    # Closes the existing database connection and re-opens it.
    self.close()
    self._db = pymysql.connect(**self._db_args)# self._db = MySQLdb.connect(**self._db_args)
    self._db.autocommit(True)



3、修改连接参数
#if MySQLdb is not None:
if pymysql is not None:
    # Fix the access conversions to properly recognize unicode/binary
    FIELD_TYPE = pymysql.connections.FIELD_TYPE # FIELD_TYPE = MySQLdb.constants.FIELD_TYPE
    FLAG = pymysql.constants.FLAG#FLAG = MySQLdb.constants.FLAG
    CONVERSIONS = copy.copy(pymysql.converters.conversions)#CONVERSIONS = copy.copy(MySQLdb.converters.conversions)

    field_types = [FIELD_TYPE.BLOB, FIELD_TYPE.STRING, FIELD_TYPE.VAR_STRING]
    if 'VARCHAR' in vars(FIELD_TYPE):
        field_types.append(FIELD_TYPE.VARCHAR)

    for field_type in field_types:
        CONVERSIONS[field_type] = [(FLAG.BINARY,str)].append(CONVERSIONS[field_type])
        #CONVERSIONS[field_type] = [(FLAG.BINARY, str)] + CONVERSIONS[field_type]

    # Alias some common MySQL exceptions
    IntegrityError = pymysql.IntegrityError#IntegrityError = MySQLdb.IntegrityError
    OperationalError = pymysql.OperationalError#OperationalError = MySQLdb.OperationalError



4、更改链接超时时间   use_unicoded去掉
def __init__(self, host, database, user=None, password=None,
             max_idle_time=7 * 3600, connect_timeout=10,
             time_zone="+0:00", charset = "utf8", sql_mode="TRADITIONAL"):



5、修改查询方法中的迭代方法（将izip改为zip_longest）
def query(self, query, *parameters, **kwparameters):
    #Returns a row list for the given query and parameters.
    cursor = self._cursor()
    try:
        self._execute(cursor, query, parameters, kwparameters)
        column_names = [d[0] for d in cursor.description]
        return [Row(itertools.zip_longest(column_names, row))for row in cursor]
        #return [Row(itertools.izip(column_names, row)) for row in cursor]
    finally:
        cursor.close()
"""



import torndb

from myweb.config import LOCAL_DB_NAME, LOCAL_DB_USER, LOCAL_DB_PASSWORD, LOCAL_DB_HOST, LOCAL_DB_PORT

# LOCAL_DB = torndb.Connection("127.0.0.1:3306", "sinodata_rpa", user="root", password="root",time_zone="+8:00")

# ALIYUN_DB = ""

class  Operate_DB():

    def __init__(self,host,port,user,password,db_name):
        self.Connection(host,port,user,password,db_name)

    def Connection(self,host,port,user,password,db_name):

        url = host+":"+str(port)
        self.db = torndb.Connection(url,db_name, user=user, password=password,time_zone="+8:00")
        # return self.db


    def select(self,sql):
        try:
            return self.db.query(sql)
        except  Exception as e:
            return e

    def insert(self,sql):
        try:
            result =  self.db.execute(sql)
            if result == 0:
                return "success"
            else:
                return "fail"
        except Exception as e:
            return e

    def delete(self,sql):
        try:
            result =  self.db.execute(sql)
            if result == 0:
                return "success"
            else:
                return "fail"
        except Exception as e:
            return e

    def update(self,sql):
        try:
            result =  self.db.execute(sql)
            if result == 0:
                return "success"
            else:
                return "fail"
        except Exception as e:
            return e

    def work(self,sql):
        try:
            result =  self.db.execute(sql)
            if result == 0:
                return "success"
            else:
                return "fail"
        except Exception as e:
            return e











if __name__ == "__main__":
    # pass
    a = Operate_DB(LOCAL_DB_HOST,LOCAL_DB_PORT,LOCAL_DB_USER,LOCAL_DB_PASSWORD,LOCAL_DB_NAME)

    # db=a.Connection(LOCAL_DB_HOST,LOCAL_DB_PORT,LOCAL_DB_USER,LOCAL_DB_PASSWORD,LOCAL_DB_NAME)

    # test_select
    sql ="select * from student where Sid='01'"
    print(a.select(sql))
    #
    # # test_insert
    # sql_insert = """insert into student (Sid,Sname,Sage,Ssex) values(101,'王明',"1990-01-01 00:00:00",'男')"""
    # b = a.insert(sql_insert)
    # print(b)
    #
    # # test_update
    # sql_insert = """update student set Sname="mike.zhao" where Sid='101'"""
    # b = a.insert(sql_insert)
    # print(b)
    #
    # # test_delete
    # sql_insert = """delete from student where Sid='101'"""
    # b = a.insert(sql_insert)
    # print(b)












