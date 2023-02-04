class BiTree:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTree('A')
b = BiTree('B')
c = BiTree('C')
d = BiTree('D')
e = BiTree('E')
f = BiTree('F')
g = BiTree('G')

root = e
e.lchild = a 
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f


print(root.lchild.rchild.data)