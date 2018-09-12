
import re

regex = re.compile(r'^[0-9]+\s+\S+\s+0x\w+\s+0x\w+\s+\+\s+[0-9]+$')
line = '0   libsystem_kernel.dylib          0x0000000180b1fde8 0x180b1f000 + 3560';
isMatch = regex.match(line)
pattern = re.compile(r'0x\w+')
addrList = pattern.findall(line)
print(isMatch.group())
print(addrList)
