
class A:

    def __init__(self):
        self.a = 1

aa = A()

a = 1

def func():
    # aa.a = 2
    # print(aa.a)
    global a
    a = 2
    print(a)

func()
# print(aa.a)
print(a)

# 值类型使用copy进入闭包，对象类型使用引用进入闭包


# 参数不能使用可变类型对象，默认值要用None
def generate_new_list_with(my_list=None, element=None):
    if my_list is None:
        my_list = []
    else:
        my_list.append(element)
    return my_list

print(generate_new_list_with([], element=1))
print(generate_new_list_with(element=2))
print(generate_new_list_with([], element=11))
print(generate_new_list_with(element=3))
