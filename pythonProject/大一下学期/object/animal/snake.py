class Snake:
    # 定义属性
    id = '22103'
    name = '蛇'
    # 定义方法
    def effect(self):
        # 定义方法体
        print('可以入药')
    def effect1(self):
        # 定义方法体
        print('咬人')
# 创建对象
objesnake = Snake()
# 调用属性
print(f'编号{objesnake.id}')
print(f'姓名{objesnake.name}')
# 调用方法
objesnake.effect()
objesnake.effect1()
