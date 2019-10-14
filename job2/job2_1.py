# 1. 实现一周的记账功能
a = list()
b = list()
c = dict()
count = 0
for i in range(1,8):
    a.append(float(input("请输入第"+str(i)+"天的收入:")))
    b.append(float(input("请输入第"+str(i)+"天的支出:")))
    c[i-1] = a[i-1]-b[i-1]
    count += a[i-1]-b[i-1]
for i in range(1,8):
    print("第"+str(i)+"天收入:"+str(a[i-1])+"支出:"+str(b[i-1])+"当天剩余:"+str(c[i-1]))
print("最终剩余:"+str(count))



