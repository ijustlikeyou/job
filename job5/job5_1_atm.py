class ATM:
    # 余额
    balance = 0.0

    # 构造方法
    def __init__(self, balance=0.0):
        self.balance = balance

    # 主菜单
    def show(self):
        print("欢迎使用洛神天之依银行"
              "\n==================="
              "\n1.查询余额"
              "\n2.存款"
              "\n3.取款"
              "\n4.退出")
        try:
            option = int(input("请输入您的选项:"))
            if option > 4 or option < 1:
                raise Exception("输入错误")
            return option
        except Exception:
            print("请输入正确的选项")
            return self.show()

    # 查询余额
    def selectBalance(self):
        print("您的银行账户余额为{}\t".format(self.balance))

    # 存款余额
    def deposit(self):
        try:
            money = float(input("请输入您的存入金额:"))
            if money >= 0:
                self.balance += money
                self.selectBalance()
            else:
                raise Exception("输入错误")
        except Exception:
            print("输入错误返回主菜单")

    # 取款余额
    def withdrawal(self):
        try:
            money = float(input("请输入您的取款金额:"))
            if self.balance - money >= 0:
                self.balance -= money
            else:
                print("您的余额不足！")
            self.selectBalance()
        except Exception:
            print("输入错误返回主菜单")

    # 退出
    def exit(self):
        print("已退出！感谢您的使用")
