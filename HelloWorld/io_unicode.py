# encoding=utf-8
import io


f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"上海自来水来自海上")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
