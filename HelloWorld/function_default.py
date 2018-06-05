
# 函数默认参数值必须是一个常量，默认参数值必须位于没有默认参数值的参数后面
def say(message, times=1):
    print(message * times)

say('hello')
say('world', 5)
