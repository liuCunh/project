class Cat:
    # 属性 拥有什么
    face = 'pretty'
    body = 'loveliness'
    voice = 'miaomiaomiao~'
    # 方法 能做什么
    def run(self):
        print('跑的很快')
    def climb(self):
        print('会上树')
obje = Cat()
Cat.face = 'beautiful'
print('Cat.face:', Cat.face)
print('obje.face:', obje.face)
print('这只猫会：', end="")
obje.climb()