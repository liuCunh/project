class Bird:
    # 属性
    id = '22104'
    name = '小鸟'
    # 创建方法
    def effect(self):
        # 方法体
        print('散播种子')
    def effect1(self):
        # 方法体
        print('吃肉')
# 创建对象
objeBird=Bird()
# 调用属性
print(objeBird.id)
print(objeBird.name)
# 调用方法
objeBird.effect()
objeBird.effect1()
