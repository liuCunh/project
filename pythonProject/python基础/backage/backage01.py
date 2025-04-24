"""
# 文件夹
# 一个包中可以放多个模块
项目》包》模块》类》函数》变量
"""

# 使用包中的模块中的user类

# from user import modules
#
# u = modules.User("Admin", "123456")
# u.show()

# from user.modules import User
# u = User("Admin", "123456")
# u.show()
#
# from article.modules import Article
#
# a = Article("个人总结", "刘春")
# a.show()

from user.modules import *
from user.modules import version
# print(version)
# u = User("admin", "12345")


"""
article
    --modules.py
    --__init__.py
    __...
user
    --modules.py
    --__init__.py
    --...
package01.py
from 包 import 模块
from 包.模块 import 函数
from 包.模块 import *

"""

