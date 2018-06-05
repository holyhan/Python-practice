while True:
    s = input('Enter something : ')
    if s == 'quit':     # 如果输入内容为'quit'字符，则跳出
        break
    print('Length of the string is', len(s))    # len()函数用于获取字符串长度
print('Done')
