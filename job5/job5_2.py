# 2. 练习会先提供一个李靖类，用以记录人物角色的战斗力。需要你创建一个子类哪吒类，提供属性和参数的修改。
# 要求： 在哪吒的初始化方法中，默认添加`['混天绫', '乾坤圈']` 两个装备,以及初始化战斗力为50.

class Lijing:  # 李靖
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name='李靖', weapons=[], power=10):
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power  # 总战力=武器战力之和


# your code here
# 请你完成子类的定制（包括初始化方法和count_fight函数）
class Nezha(Lijing):  # 哪吒
    def __init__(self, name='哪吒', weapons=['混天绫', '乾坤圈'], power=50):
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power


# 通过两个实例，完成子类和父类的对比（可自行验证）
lijing = Lijing('李靖')
nezha = Nezha('哪吒')
print(lijing.weapons)
print(nezha.weapons)
lijing.count_fight('七宝玲珑塔', 50)  # 七宝玲珑塔 战力 50
print(lijing.weapons)
print(lijing.power)
nezha.count_fight('火尖枪', 40)  #
print(nezha.weapons)
print(nezha.power)
