# 猫
class Cat:
    type = '猫'

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print(f'{self.nickname}喜欢吃{food}')

    def catch_mouse(self, color, weight):
        print(f'{self.nickname}抓了一只{weight}kg的老鼠，{color}的大老鼠！')

    def sleep(self, hour):
        if hour < 5:
            print(f'乖乖，继续睡觉吧！')
        else:
            print(f'赶快起床，出去抓老鼠')

    def show(self):
        print('猫的详细信息')
        print(self.nickname, self.age, self.color)


cat1 = Cat('花花', 2, '灰色')
cat1.catch_mouse('黑色', 2)
cat1.sleep(8)

cat1.eat('小金鱼')
cat1.show()