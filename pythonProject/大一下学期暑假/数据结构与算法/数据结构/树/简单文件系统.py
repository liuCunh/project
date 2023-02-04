class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 文件类型dir or file
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node('/')  # 创建一个根目录
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):

        # 判断输入
        if name[-1] != '/':
            name += '/'

        # 返回上一级
        if name == '../':
            self.now = self.now.parent
            return

        # 进入下一个目录
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError('invalid dir')


test = FileSystemTree()
test.mkdir('var/')
test.mkdir('bin/')
test.mkdir('usr/')

test.cd('bin/')
test.mkdir('python/')
print(test.ls())



