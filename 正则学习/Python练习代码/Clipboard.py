#!/usr/bin/env python3


import re, pyperclip

# 匹配电话
phoneRegex = re.compile(r'((13[0-9]|14[579]|15[0-3,5-9]|18[0-3,5-9])\d{8})', re.VERBOSE)

# 匹配邮件地址
emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))', re.VERBOSE)

# 从剪切板中获取字符串
text = str(pyperclip.paste())
# 存放匹配到的字符串
matches = []
for phone in phoneRegex.findall(text):
    matches.append(phone[0])
    # print('phone: ', matches)
for email in emailRegex.findall(text):
    # print('email: ', matches)
    matches.append(email[0])

# 将匹配到的字符串复制到剪切板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone or email found.')
