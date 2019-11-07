class A0:
    name = 'A0'


class A2(A0):
    num = 2


class A1:
    num = 1


class A3:
    name = 'A3'


class A4(A1, A2, A3):
    pass


ins = A4()
print(ins.name)  #
print(ins.num)  #

if __name__=='__main__' or True:
    print(321)