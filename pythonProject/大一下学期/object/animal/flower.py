class Flower:
    outside = 'pretty'
    smell = 'balmiest'
    def effect(self):
        print('它可以入药')
    def effect1(self):
        print('作为观赏性植物')
objectFlower = Flower()
print(f'这个花是非常的{objectFlower.outside}')
print('这个花的作用是：', end='')
objectFlower.effect()
