import random

import numpy as np

# data1 =np.array(["8", "7.5", "8", "0123","1","2","9"])
# arr1 = np.array(data1)
# print(arr1, arr1.dtype)
# test=np.empty((8,4))
#
# print(test[[1,4,5,6]])
# data = np.random.randn(8, 2)
# print(data1=="8")
# print(test)
# for i in range(8):
#     test[i]=i
# print(test)

# test =np.array([1.11,-2.2,12.32,34.,345.,223.,4.,-3.11])
# print(np.sqrt(test))
# ttt =np.arange(8)
# print(ttt)
# np.sqrt(test,test)
# print(test)

# print(np.arange(20))
# print(data[data1=="8"])

#
# for i in range(8):
#     test[i]=i
# print(test)

# sss=np.array([[123,123,123],[2,2]])
# print(sss)
# arr=np.random.randn(100)
# print(arr)
# arr.sort()
# print(arr)

np.random.seed(1)

# 首先创建array
A = np.random.randn(5)
# print(A)
# # 然后直接调用 np.sqrt
# B = np.sqrt(A)
# print("A", A)
# print("B", B)
# 首先当地修改A
b=np.random.randn(5)
np.sqrt(A, out=b)
print("A", b)

lty='洛神天之依'
print(rf'\n我的名字是{lty}')
# np.sqrt(B, B)
# print("B", B)

ttt=[1,2,4,5,4,6]

def test(i):
    return i**2
pf=list(map(test,ttt))
print(pf)