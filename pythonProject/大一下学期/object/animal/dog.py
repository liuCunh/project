class Dog:
    # 属性--》有什么
    name = '哈士奇'
    character = '夺笋'
    # 方法--》有能力做什么
    def attack(self):
        print('追着咬人！')
    def fear(self):
        print('路过旺旺叫')
objeDog = Dog()
print(f'这条狗的名字叫:{objeDog.name}')
print('他可以在你放学时：', end="")
objeDog.attack()
