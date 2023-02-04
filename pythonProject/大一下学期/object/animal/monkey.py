class Monkey:
    # 属性
    id = '22107'
    name = '猴子'
    # 方法
    def effect(self):
        # 方法体
        print('用来观赏')
    def effect1(self):
        # 方法体
        print("吃猴脑")
# 创建对象
objeMonkey = Monkey()
# 调用属性
print(f'编号{objeMonkey.id}')
print(f'姓名{objeMonkey.name}')
# 调用方法
objeMonkey.effect()
objeMonkey.effect1()
