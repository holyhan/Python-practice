
age = 20
name = 'Swaroop'

# 输出语句中可以直接使用{}来代替{0}和{1}
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing whit that python?'.format(name))
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 由于Python默认在print打印的字符串结尾加换行符，因此如果消除换行符可以这样
print('a', end='')
print('b', end=' ')     # 这里也可以在输出结尾加空格
print('c')

# 转义输出
print('What\'s your name!')
# 末尾加反斜杠，换行输出
print('This is the first sentence. \
This is the second sentence.')

