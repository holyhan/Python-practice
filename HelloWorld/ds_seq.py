shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或'下标(Subscription)'运算符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])   # 使用负数索引，可以从后向前索引，只是索引从-1开始计数
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])


# Slicing on a list #
print('character 1 to 3 is', name[1:3])
print('character 2 to end is', name[2:])
print('character 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 切片可以有第三个参数，代表步长，不写步长，默认步长为1
print(shoplist[::1])
print(shoplist[::2])
# 如果步长为-1表示倒序返回
print(shoplist[::-1])
