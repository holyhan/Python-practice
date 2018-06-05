# y = 30
#
#
# def func():
#     # 这里修改函数外部y的值是无效的，因为函数块内部会作为局部变量声明
#     y = 20
#     print('y is', y)
#
#
#
# func()
# print(y)

x = 50


def func():
    # global语句用以声明x是一个全局变量
    global x


    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
