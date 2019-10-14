# 2. 实现ATM机功能
count = 0
state = True
while state:
    print("欢迎使用洛神天之依银行"
          "\n==================="
          "\n1.查询余额"
          "\n2.存款"
          "\n3.取款"
          "\n4.退出")
    type = float(input("请选择操作项:"))
    if type == 1:
        print("您的余额:" + str(count))
    elif type == 2:
        count += float(input("请您输入存款金额:"))
    elif type == 3:
        a = float(input("请您输入取款金额:"))
        if count - a < 0:
            print("抱歉！您的余额没有这么多钱！")
        else:
            count -= a
    else:
        print("欢迎使用，再见！ヾ(￣▽￣)Bye~Bye~")
        state = False
