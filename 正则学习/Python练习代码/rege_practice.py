import re

text = re.search(r'\b\w{6}\b', 'My phone number is 421-2343-121')
print(text.group())

m = re.search('^The', 'The end.')
if m is not None:
    print('1: ', m.group())

m = re.search('^The', 'end. The')
if m is not None:
    print('2: ', m.group())

# r代表raw，标识不加转义处理的原始字符串
m = re.search(r'\bthe', 'bite the dog')
if m is not None:
    print('3: ', m.group())

m = re.search(r'\bthe', 'bitethe dog')
if m is not None:
    print('4: ', m.group())

m = re.search(r'\Bthe', 'bitethe dog')
if m is not None:
    print('5: ', m.group())


s = 'This and that.'
m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(m)


m = re.findall(r'(th\w+)', s, re.I)
print(m)


it = re.finditer(r'(th\w+)', s, re.I)
n = next(it)
print(n.groups())
print(n.group(1))

n = next(it)
print(n.groups())
print(n.group(1))

print([n.group(1) for n in re.finditer(r'(th\w+)', s, re.I)])

# sub()和subn()的区别，sub()只是替换匹配的内容，而subn()不仅替换匹配
# 的内容，还返回总共匹配了几组内容
n = re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X,\n')
print('sub()输出:', n)

n = re.subn('X', 'Mr.Smith', 'attn: X\n\nDear X,\n')
print('subn()输出:', n)

# 下列内容将美式日期表示法MM/DD/YY{,YY}转换成其他国家常用的格式DD/MM/YY{,YY}
n = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
print('日期转换1：', n)

n = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')
print('日期转换2：', n)


# split()方法练习
DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))
