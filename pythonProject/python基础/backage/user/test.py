# 用户发表文章
# 创建用户对象

# 发表文章， 文章对象
from modules import User
from article.modules import Article
# from modules import User  # 当前同级目录下的User类
# from .modules import User
from calculate import add

# user = User("admin", "123456")

article = Article("个人总结", "刘春")
article.show()
# user.publish_article(Article)

list1 = [1, 2, 3, 4, 5]
add(*list1)

MAX = 1000