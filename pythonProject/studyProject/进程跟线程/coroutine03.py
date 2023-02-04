# 常把gevent，跟猴子补丁连用(monkey.patch_all())
import time

import gevent
from gevent import monkey

monkey.patch_all()  # 打补丁，猴子补丁


def a():  # 任务A
    for i in range(5):
        print(f"A{i}")
        time.sleep(0.1)


def b():  # 任务B
    for i in range(5):
        print(f"B{i}")
        time.sleep(0.1)


def c():  # 任务C
    for i in range(5):
        print(f"C{i}")
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
    print("over")