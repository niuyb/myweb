#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/19 10:52
# 工具：PyCharm
# Python版本：3.7.0

import time


class elevator():
    def __init__(self,len_min,len_max):
        self.len_min = int(len_min)
        self.len_max = int(len_max)
        self.lost_floor=[14,18]

    def run_elevator(self):
        while True:
            time.sleep(1)
            print("------------------------------------")
            try:
                floor = int(input("请输入想到达的楼层"))
            except:
                print("请正确的输入数字楼层")
                continue
            if floor > self.len_max :
                print("最高层数为%s,已选择楼层%s,超出最大层数请重新选择"%(self.len_max,floor))
                continue
            if floor < self.len_min :
                print("最低层数为%s,已选择楼层%s,超出最低层数请重新选择"%(self.len_min,floor))
                continue

            if floor in self.lost_floor:
                print("不存在%s楼层,请重新选择"%floor)
                continue

            print("已到达%s层"%floor)


if __name__ == "__main__":
    e=""
    try:
        e = elevator(-5,40)
    except:
        print("电梯配置失败")
    if e:
        e.run_elevator()
