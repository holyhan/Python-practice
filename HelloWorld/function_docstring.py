def print_max(x, y):
    # 下面的字符串为文档字符串，规则：第一行首字母大写，并以句号结尾；第二行设为空行，第三行为详细文档描述。
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)


    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)
