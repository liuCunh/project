"""
避免死锁：
解决：
1. 重构代码
2. 添加acquire参数，timeout

"""

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()
class MyThread(Thread):
    def run(self):  # start()时默认找run方法
        if lockA.acquire():  # 如果获取到锁，返回True
            print(self.name+"获取了a锁")
            time.sleep(0.1)
            if lockB.acquire(timeout=4):
                print(self.name + "获取了b锁,原来还有a锁")
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()时默认找run方法
        if lockB.acquire():  # 如果获取到锁，返回True
            print(self.name+"获取了B锁")
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + "获取了A锁,原来还有B锁")
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()