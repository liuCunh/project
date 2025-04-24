"""
生产者和消费者，两个线程之间得通信
"""
import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put(f"生产者产生得数据{num}")
        print(f"生产者产生得数据{num}")
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"消费者获取到：{item}")
        time.sleep(4)

    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print("Over")