from collections import deque
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


# 前序遍历
def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)

# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

# 后续遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


# 层序遍历
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


print('pre_order:', end="")
pre_order(root)
print()
print('in_order:', end="")
in_order(root)
print()
post_order(root)
print()
level_order(root)