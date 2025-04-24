# 线程
"""
创建线程， 使用线程

"""
import threading

# 进程： Process
# 线程： thread
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print(f"正在下载:{image}")
        sleep(q)
        print(f"{image}下载成功")


def listenMusic():
    musics = ['老鼠爱大米', '打完款面', '烤面筋', '土耳其冰淇淋']
    for music in musics:
        sleep(0.5)
        print(f'正在听“{music}”')


if __name__ == '__main__':

    # 创建一个线程对象
    t = threading.Thread(target=download, name="xiaoming", args=(1,))
    t.start()

    t1 = threading.Thread(target=listenMusic, name="吴亦凡")
    t1.start()

    # n = 1
    # while True:
    #     sleep(1.5)
    #     print(n)
    #     n += 1
