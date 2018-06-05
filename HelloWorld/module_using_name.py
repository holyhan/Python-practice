# 每一个Python模块都定义了它的__name__属性。
# 如果它与__main__属性相同，则代表这一模块是由用户独立运行的。
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
