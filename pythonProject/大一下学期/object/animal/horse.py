class Horse:
    # 属性
    id = '22101'
    name = '马儿'
    # 方法
    def run(self):
        print('跑得快')
    def competion(self):
        print('能够用来举行赛马比赛')
objeHouse=Horse()
print(objeHouse.id)
print(objeHouse.name)
objeHouse.run()
objeHouse.competion()
