from abc import ABCMeta, abstractmethod
from time import sleep


class Windows(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):  # 模板方法
        self.start()
        while True:
            try:
                self.repaint()
                sleep(2)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindows(Windows):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行')

    def stop(self):
        print('窗口结束运行')

    def repaint(self):
        print(self.msg)


MyWindows('hahah...').run()
