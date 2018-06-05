# coding: utf-8


# 字体变粗装饰器
def makebold(fn):
    # 装饰器将返回新的函数
    def wrapper():
        # 在之前或者之后插入新代码
        return "<b>" + fn() + "</b>"
    return wrapper


# 斜体装饰器
def makeitalic(fn):
    # 装饰器将返回新的函数
    def wrapper():
        # 在之前或者之后插入新代码
        return "<i>" + fn() + "</i>"
    return wrapper


@makebold
@makeitalic
def say():
    return "hello"


print(say())

