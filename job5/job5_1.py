# 1. 完成ATM的类实现
# 将第二次课程的ATM机器改写成类实现
from job5.job5_1_atm import ATM as atm

lty = atm(0)

state = True

while state:
    option = lty.show()
    if option == 1:
        lty.selectBalance()
    elif option == 2:
        lty.deposit()
    elif option == 3:
        lty.withdrawal()
    else:
        lty.exit()
        state = False
