from 二叉搜索树 import BiTreeNode, BST


class VALNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # 平衡b数


class VALTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    # 左旋
    def rotate_left(self, p, c):
        s2 = c.lchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 右旋
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 左旋-右旋
    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更换bf
        if g.bf > 0:  # 情况一：替换的s3
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:  # 情况二：替换的s2
            p.bf = 0
            c.bf = 1
        else:  # 情况三：不存在节点替换的是g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf < 0:  # 处于s2位置
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:  # 处于s3位置
            p.bf = 0
            c.bf = -1
        else:  # 直接替换g
            p.bf = 0
            c.bf = 0
        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = VALNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 找到的左孩子不为空，树不允许插入
                    p = p.lchild  # 将找到的左孩子作为新node，从新寻找
                else:  # 找到一个为空的左孩子，树允许插入
                    p.lchild = VALNode(val)  # 赋予插入元素拥有树的属性，将元素插入树中
                    p.lchild.parent = p
                    node = p.lchild
                    break
            elif val > p.data:
                if p.rchild:  # 找到的左孩子不为空，树不允许插入
                    p = p.rchild  # 将找到的左孩子作为新node，从新寻找
                else:
                    p.rchild = VALNode(val)  # 赋予插入元素拥有树的属性
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val==p.data
                return

        # 更新平衡数bf
        while node.parent:  # node为插入的节点

            # 判断插入操作是左边还是右边
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉
                # 不平衡因素从p的 左子树传递而来。路径上平衡因子都 -1

                # 用node.parent的平衡常数确定旋转方向
                if node.parent.bf < 0:  # 原来的node.parent=-1，更新后变成了-2

                    # 用node.bf 进一步确认旋转方向
                    # 旋转子树，看哪边更沉
                    g = node.parent.parent  # 讲旋转后的子树和根连接的连接点，为了连接旋转之后的子树
                    x = node.parent  # 旋转前子树的根
                    if node.bf > 0:  # c的右边更沉
                        n = self.rotate_left_right(node.parent, node)  # 旋转后子树的根节点
                    else:
                        n = self.rotate_right(node.parent, node)  # 旋转后子树的根节点

                    # 记得将g和n连接起来
                elif node.parent.bf > 0:  # 原来的node.parent.bf=1, 更新后变成了0
                    node.parent.bf = 0  # 当节点的平衡数变成了0，说明树就已经平衡了
                    break
                else:  # 原来的node.parent.bf=0，更新后变成了1
                    # 被破坏后的路径经过旋转后变得平衡，node向上移动继续查看被破坏的路径是否平衡

                    node.parent.bf = 1
                    node = node.parent  # 继续向上找，直到找到一个节点的平衡数变成0
                    continue

            else:  # node.parent.rchild==node  传递是从右子树来的，右子树更沉了
                # 不平衡因素从p的右子树传递而来。路径上平衡因子都 +1
                if node.parent.bf > 0:  # node.parent.bf=1, 更新后变成了2

                    # 旋转调整
                    # 判断旋转方向
                    g = node.parent.parent  # 连接旋转后的子树
                    x = node.parent  # 旋转前子树的根
                    if node.bf < 0:  # c的左边更沉
                        n = self.rotate_right_left(node.parent, node)  # 旋转后树的根
                    else:  # c的右边更沉
                        n = self.rotate_left(node.parent, node)  # 旋转后树的根A
                elif node.parent.bf < 0:  # node.parent.bf=-1, 更新后变成了0
                    node.parent.bf = 0
                    break
                else:  # node.parent.bf=0, 更新后变成了1
                    node.parent.bf = 1
                    node = node.parent  # 继续向上寻找，直到找到一个节点的平衡数变为0
                    continue

            # 在树结构中，一旦涉及到根节点都要考虑根是否为空
            # 连接旋转后的子树
            n.parent = g
            if g:  # 是否为根节点

                # 确定旋转之前的根位于左孩子还是右孩子上面
                if x == g.lchild:
                    g.lchild = n  # 将旋转后的子树连接到树的根上面
                else:
                    g.rchild = n  # 将旋转后的子树连接到树的根上面
                break
            else:
                self.root = n
                break


tree = VALTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
