"""
面向对象：
程序  现实中
对象  --》具体的事物

现实中的事物 --》 封装成电脑程序
世间万物皆对象

面向对象：
    类
    对象
    属性
    方法
"""

# 所有类名要求首字母大写，多个单词使用驼峰式命名
# ValuesError, TypeError, ...
"""
class 类名[(父类)]:
    属性： 特征
    
    方法： 动作
"""


class Phone(object):
    # 属性
    brand = 'HUAWEI'

    # 方法
    pass


# 使用类创建对象
lc = Phone()
print(lc)
print(lc.brand)
lc.brand = "IPhone"
print(lc.brand)

print(f'------------------')

lm = Phone()
print(lm)
print(lm.brand)
lm.brand = 'OPPO'
print(lm.brand)

print(f'------------------')

xiaowei = Phone()
print(xiaowei.brand)
