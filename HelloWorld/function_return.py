# return语句如果没有搭配任何一个值，则返回None，代表空。
# 每一个没有使用return的函数块，在函数末尾都隐含一句 return None.
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))
