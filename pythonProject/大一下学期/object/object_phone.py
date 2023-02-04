class Phone:
    # 属性
    color = 'red'
    size = 8.0
    price = 1500
    # 过程
    def call(self, num):
        print(f'给{num}打电话')
    def playGame(self):
        print('玩游戏')
    def photo(self):
        print('5000w高清像素')
# 创建对象
iPhone1 = Phone()
print('手机颜色是：', iPhone1.color)
print(f'手机的尺寸是{iPhone1.size}')
print(f'手机的价格是{iPhone1.price}')
for i in range(3):
    print('他可以', end="")
    if i == 0:
        iPhone1.call(110)
    if i == 1:
        iPhone1.playGame()
    if i == 2:
        iPhone1.photo()
iPhone2 = Phone()


