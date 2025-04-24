"""
导入方法：
    1. import 模块名
        模块名.方法
    2. from 模块名 import 变量。函数。类
        在代码中直接使用变量，函数，类
    3. from 模块名 import *
        导入模块中的所有内容
        但是想限制获取的内容，可以在模块中使用__all__ = [能够访问的内容]
    4. 无论是import还是from，都会将模块内容进行加载
        如果不希望其进行调用，就会用大__name__
        __name__在自身的模块中为__main__，而在其他模块中通过引入(导入)的方式被调用就为模块名
    5. from的导入方法时基于项目文件下的，包跟项目文件的距离超过1层将无法导入

"""

list1 = [11, 2, 3, 4, 5, 7, 33]

# # 导入模块
# import calculat
#
# # 使用模块中的函数  模块名.Module  模块名.函数  模块名.类  模块名.变量
# print(calculat.add(*list1))
#
# # 使用模块变量
# print(calculat.number)
#
# # 使用模块中的类
# cal = calculat.Calculat(10)
# cal.test()
#
# # 调用模块中的类方法
# calculat.Calculat.test1()

# from calculat import add, number, Calculat
from studyProject.backage.calculate import *

result = add(*list1)
print(result)

sum = result + number
print(sum)

c = Calculat(100)
c.test()
Calculat.test1()