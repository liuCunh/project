class Donkey:
    # 属性
    id = '22102'
    name = '驴子'
    def effect(self):
        print('可以用来拉货')
    def effect1(self):
        print('可以拿来做阿胶')
objeDonkey = Donkey()
print(f'编号{objeDonkey.id}')
print(f'姓名{objeDonkey.name}')
objeDonkey.effect()
objeDonkey.effect1()
