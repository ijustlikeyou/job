from test2 import test1 as lty
import test2

print(test2)
sta =list()
sta.append("123")
sta.append(342)
sta.append(432)
str1=''
c=','
for s in sta:
    str1+=str(s)+c
print(str1[:-1])