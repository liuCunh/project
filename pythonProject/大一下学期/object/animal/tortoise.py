class Tortoise:
    # 属性
    id = '22105'
    name = '乌龟'
    # 方法
    def effect(self):
        # 方法体
        print("供奉")
    def effect1(self):
        print('拿来吃')
# 创建对象
objeTortoise = Tortoise()
# 调用属性
print(f'编号{objeTortoise.id}')
print(f'姓名{objeTortoise.name}')
# 调用方法
objeTortoise.effect()
objeTortoise.effect1()
