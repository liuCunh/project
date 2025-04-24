class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print(f"发表{self.name}文章的作者是：{self.author}")


class Tag:
    def __init__(self, name):
        self.name = name
