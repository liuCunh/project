# 自定义进程
from multiprocessing import Process
from time import sleep


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()

        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            sleep(1)
            print('进程名字：', n, "------》自定义进程", self.name)
            n += 1


if __name__ == '__main__':
    p = MyProcess('小米')
    p.start()
    p1 = MyProcess("小红")
    p1.start()