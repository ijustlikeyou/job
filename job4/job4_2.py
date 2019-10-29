# 2.打乱数据集
# 同时打乱 x,y，保证数据和标签的对应关系
import random
from typing import List, Any

x = ['快递太慢了！', '不好吃', '特别难吃', '要齁死我了', '很划算', '下次还来', '味道很不错！', '香']
y = ['差评', '差评', '差评', '差评', '好评', '好评', '好评', '好评']


def shuffle(x, y):
    # 对两个集合进行随机打乱
    def randomlist(l):
        newList = list()
        for i in range(len(l)):
            randomData = random.choice(l)
            newList.append(randomData)
            l.remove(randomData)
        return newList

    return randomlist(x), randomlist(y)


x, y = shuffle(x, y)

# print result for certify
for i, j in zip(x, y):
    print(i, ':', j)
