# 进程通信
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载：", image)
        sleep(1)
        q.put(image)


def getfile(q):
    # while True:
    #     try:
    #         file = q.get(timeout=5)
    #         print(file, '保存成功')
    #     except:
    #         print('全部保存完毕')
    #         break
    while q.qsize():
        file = q.get()
        print(file, '保存成功！')


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('over')