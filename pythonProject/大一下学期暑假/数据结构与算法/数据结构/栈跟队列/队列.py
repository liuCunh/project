class Queue:
    def __init__(self, size=100):
        self.size = size
        self.queue = [0 for _ in range(size)]
        self.rare = 0  # 队尾指针
        self.front = 0  # 队首指针

    def is_empty(self):
        return self.rare == self.front

    def is_filled(self):
        return (self.rare + 1) % self.size == self.front  # 当rare=最后一个数，front=第一个数时，必须取余

    def push(self, element):
        if not self.is_filled():
            self.rare = (self.rare + 1) % self.size  # 队尾指针后拨一位，取余操作使得指针可以拨向零点
            self.queue[self.rare] = element  # 替换元素
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")


q = Queue(10)
for i in range(9):
    q.push(i)
print(q.queue)
print(q.front, q.rare)







