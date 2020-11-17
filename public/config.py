#!/usr/bin/env python
# encoding: utf-8


# 数据请求格式
# 1成功
# 0无
#-1异常
RESULT = {"data": [], "code": 1, "msg": ""}

# 正则匹配规则
RE_EMAIL = r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$"
RE_PHONE = r'^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$'

# tools   install_tools
FILE_TYPE={
    "1":"安装包",
    "2":"免安装",
    "3":"压缩包",
}

# tools  type
TOOLS_TYPE={
    "1":"编程工具",
    "2":"办公工具",
    "3":"娱乐",
    "4":"游戏",
    "5":"便利软件"
}