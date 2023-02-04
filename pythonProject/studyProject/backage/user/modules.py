__all__ = ["User"]  # 只是针对from导入的*起作用
version = "3.9"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print("登录成功")
        else:
            print("登录失败")

    def show(self):
        print(self.username, self.password)

    def publish_article(self, article):
        print(f"{self.username}发表了：{article.name}这篇文章")


if __name__ == "__main__":
    print("-------------user------------")
    pass
