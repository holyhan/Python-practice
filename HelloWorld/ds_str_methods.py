# 这是一个字符串对象
name = 'Swaroop'


if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')


if 'a' in name:
    print('Yes, it contains the string "a"')

# str.find(value)函数用来查找value所在的位置，比如下面返回1，找不到返回-1
if name.find('war') != -1:
    print('Yes, it contains the string "war"')


delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
