#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/16 14:19
# 工具：PyCharm
# Python版本：3.7.0
""""""


"""
myuser.has_perm('myapp.fix_car')
has_perm()方法的参数，即permission的codename，但传递参数时需要加上model 所属app的前缀，
格式为<app label>.<permission codename>。
"""




"""
user.get_all_permissions()
方法列出用户的所有权限，返回值是permission name的list

user.get_group_permissions()
方法列出用户所属group的权限，返回值是permission name的list
"""




