# 协程：微线程。 进程》线程》协程
# 协程得底层时生成器
"""
耗时操作：网络请求，网络下载(爬虫)，网络上传， IO：文件得读写

"""
import time


def task1():
    for i in range(3):
        print(f"A{i}")
        yield
        time.sleep(1)


def task2():
    for i in range(3):
        print(f"B{i}")
        yield
        time.sleep(2)

if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break

