#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/10/12 15:35
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


def log_time(func):  # 此函数的作用时接受被修饰的函数的引用test，然后被内部函数使用
    def make_decorater():
        print('现在开始装饰')
        func()
        print('现在结束装饰')

    return make_decorater  # log_time()被调用后，运行此函数返回make_decorater()函数的引用make_decorater


@log_time  # 此行代码等同于，test=log_time(test)=make_decorater
def test():
    print('我是被装饰的函数')


# test()  # test()=make_decorater()



"""
---------------------------------------------------------------------------------------------------------
"""


def log_time(func):
    def make_decorater(*args, **kwargs):  # 接受调用语句的实参，在下面传递给被装饰函数（原函数）
        print('现在开始装饰')
        test_func = func(*args, **kwargs)  # 如果在这里return，则下面的代码无法执行，所以引用并在下面返回
        print('现在结束装饰')
        return test_func  # 因为被装饰函数里有return，所以需要给调用语句（test（2））一个返回，又因为test_func = func(*args,**kwargs)已经调用了被装饰函数，这里就不用带（）调用了，区别在于运行顺序的不同。

    return make_decorater


@log_time
def test(num):
    print('我是被装饰的函数')
    return num + 1


# a = test(2)  # test(2)=make_decorater(2)
# print(a)


"""
---------------------------------------------------------------------------------------------------------
"""



def get_parameter(*args, **kwargs):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
    def log_time(func):
        def make_decorater(num):
            print(args, kwargs)
            print('现在开始装饰')
            func(num)
            print('现在结束装饰')

            return func(num)

        return make_decorater

    return log_time


@get_parameter('index.html/')
def test(num):
    print('我是被装饰的函数',num)
    # return num+1


test(2)
# test()=make_decorater()


