# 基于链表的哈希表
class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:  # 链表可迭代
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:  # 链表为空时
            self.head = s  # 创建头尾节点
            self.tail = s
        else:  # 满足添加条件
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):  # 让列表具有迭代属性
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+",".join(map(str, self))+">>"


class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)]  # 创建哈希表

    def h(self, k):  # 1、插入下标
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):  # 链表中值存在
            print('Duplicated Insert')  # 重复的插入
        else:  # 链表中值不存在
            self.T[i].append(k)

    def find(self, k):  # 2、是否存在，出去重复
        i = self.h(k)
        return self.T[i].find(k)

    def __repr__(self):
        return ",".join(map(str, ht.T))


# lk = LinkList([1, 2, 3, 4, 5])
# for element in lk:
#     print(element)
# print(lk)
ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(2)
ht.insert(3)
ht.insert(101)
print(ht)
print(ht.find(5))
