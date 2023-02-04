import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 非递归， 一次插入一个元素
    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 找到的左孩子不为空，树不允许插入
                    p = p.lchild  # 将找到的左孩子作为新node，从新寻找
                else:  # 找到一个为空的左孩子，树允许插入
                    p.lchild = BiTreeNode(val)  # 赋予插入元素拥有树的属性，将元素插入树中
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:  # 找到的左孩子不为空，树不允许插入
                    p = p.rchild  # 将找到的左孩子作为新node，从新寻找
                else:
                    p.rchild = BiTreeNode(val)  # 赋予插入元素拥有树的属性
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    # 后续遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    # 删除情况一：删除叶子节点
    def __remove_node_1(self, node):  # node想要删除的节点
        # 情况1：node时叶子节点
        if not node.parent:  # 树的父节点为空：根节点
            self.root = None
        elif node == node.parent.lchild:  # node 是父节点的左孩子
            node.parent.lchild = None  # 断开父节点跟node节点的关系
        else:  # node 是父节点的右孩子
            node.parent.rchild = None

    # 删除情况2：删除节点只拥有一个子节点
    # 2.1: node的子节点为左孩子
    def __remove_node_21(self, node):
        if not node.parent:  # 为node为根节点
            self.root = node.lchild  # 将左孩子作为根节点
            node.lchild.parent = None  # 左孩子父节点置为空
        elif node == node.parent.lchild:  # node为父节点的左孩子
            node.parent.lchild = node.lchild  # node父节点的左孩子指向node节点的左孩子
            node.lchild.parent = node.parent  # node左孩子的父节点指向node的父节点
        else:  # node == node.parent.rchild  node为父节点的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # 2.2: node的子节点为右孩子
    def __remove_node_22(self, node):
        if not node.parent:  # node节点为根节点
            self.root = node.rchild
        elif node == node.parent.lchild:  # node为父节点的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # node == node.parent.rchild
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    # 删除节点
    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)  # 找到val值所在节点
            if not node:  # 不存在该节点
                return False

            # 该节点存在
            if not node.lchild and not node.rchild:  # 节点的左右孩子都不存在：删除叶子节点(删除情况一)
                self.__remove_node_1(node)
            elif not node.rchild:  # 节点的右孩子不存在(只存在一个左孩子): 删除情况2.1(node的子节点为左孩子)
                self.__remove_node_21(node)
            elif not node.lchild:  # 节点的左孩子不存在(只有一个右孩子): 删除情况2.2(node的子节点为右孩子)
                self.__remove_node_22(node)
            else:  # node节点拥有两个子节点
                # 将右子树的最小节点(给节点最多有一个右孩子)删除，并替换为当前节点
                min_node = node.rchild

                # 寻找右子树中最小节点
                while min_node.lchild:  # 最小节点的左孩子不为空(节点左孩子为空就是最小节点)
                    min_node = min_node.lchild
                node.data = min_node.data  # 将最小节点跟被删除的节点进行值的交换

                # 删除min_node
                if min_node.rchild:  # 最小节点的右孩子存在：删除条件2.2
                    self.__remove_node_22(min_node)
                else:  # 最小节点为叶子节点：删除条件1
                    self.__remove_node_1(min_node)


# li = list(range(0, 500, 2))
# random.shuffle(li)

# tree = BST(li)
# print(tree.query_no_rec(4))
# tree.pre_order(tree.root)
# print()
# tree.in_order(tree.root)
# print()
# tree.post_order(tree.root)

# tree = BST([1,4,2,5,3,8,6,9,7])
# tree.in_order(tree.root)
# print()
# tree.delete(4)
# tree.delete(1)
# tree.delete(8)
# tree.delete(9)
# tree.in_order(tree.root)


# import random
#
# li = list(range(100000))
# random.shuffle(li)
# tree = BST(li)
# tree.in_order(tree.root)
