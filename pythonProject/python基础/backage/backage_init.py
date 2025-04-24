
"""
__init__.py 文件，当导入包的时候，默认调用__init__.py文件
作用：
    1、当导入包的时候，把一些初始化的函数，变量，定义在__init__方法中
    2、此文件中函数，变量的访问，只需要通过包名，函数
    3、通过__all__=[模块]


"""
# import user
# # from user.modules import User
# user.creat_app()
# user.printa()
# from 模块 import *  表示可以使用模块里的所有内容，如果没有定义__all__= [模块]表示所有模块，如果加上，那么就只有列表中的模块才能fangw
# from 包 import *  必须结合__all__来访问
from user import *
m = modules.User("admine", "123455")
m.show()

# print(test.MAX)
