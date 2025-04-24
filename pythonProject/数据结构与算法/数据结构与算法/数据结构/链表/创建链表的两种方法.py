class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def creat_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:  # 0  1  2  3 -> node = Node(1) , node.next=0, head=Node(1) -> node=Node(2) node.next=1
        node = Node(element)  # 新节点
        node.next = head  # 将新链表跟链表头连接
        head = node  # 将链表头转移到新节点的item元素上面
    return head


def creat_link_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=",")
        lk = lk.next


li = [1, 2, 3]
lk_head = creat_linklist_head(li)
lk_tail = creat_link_tail(li)
print_linklist(lk_head)
print()
print('tail:')
print_linklist(lk_tail)
