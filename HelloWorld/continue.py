while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue            # continue语句可以同样用于for循环
    print('Input is of sufficient length')
