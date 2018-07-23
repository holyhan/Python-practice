import re

f = open('whodata.txt', 'r')
for eachLine in f:
    print(re.split(r'\s\s+', eachLine))

f.close()


# 版本3
import os

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.strip()))
