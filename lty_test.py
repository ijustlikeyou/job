from random import choice
import re

def compute(func, x, y):
    return func(x,y)

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divid(x,y):
    return x/y

functoins = [add, minus, multiply, divid]
operation = choice(functoins)
x,y = 6,2

print(compute(operation, x, y))

m = re.match('foo', 'foo string')
print(m.group())

m = re.findall('[1-9][0-9]{4,}', '这是我的QQ号781504542,第二个qq号：10054422288')
print(m) if m is not None else print('None')

t=1
print(t) if t==2 else print(False)