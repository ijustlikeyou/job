# 2. 打印斐波那契数列
def print_1(n):
    print('打印方法1:')
    count = 1
    next = 1
    for i in range(1, n + 1):
        if i < 3:
            print(1)
        else:
            index = next
            next = count + next
            count = index
            print(next)


def print_2(n):
    print('打印方法2:')
    def recursion(index):
        if index < 2:
            return 1
        else:
            return recursion(index - 1) + recursion(index - 2)

    [print(recursion(i)) for i in range(n)]


def print_3(n):
    print('打印方法3:')
    arrayList = [1, 1]
    for i in range(n):
        if i < 2:
            print(1)
        else:
            arrayList.append(arrayList[i - 1] + arrayList[i - 2])
            print(arrayList[i])

# 根据测试使用方法2递归的方式打印，性能是最低，1和3虽然所用方式不同，但原理都类似，经测试性能较好，性能排序应该是132
n = int(input('请输入要打印的斐波那契数列:'))
print_1(n)
print_2(n)
print_3(n)