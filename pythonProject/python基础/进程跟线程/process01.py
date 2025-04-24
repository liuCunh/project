# 进程的创建
"""
from multipreocessing import Process

percess = Process(target=函数, name=进程的名字, args=(函数传参值，必须可迭代))
process 对象

process.start() 启动进程并且执行任务
process.run() 执行任务，没有启动进程
terminate() 终止

"""

from multiprocessing import Process
from time import sleep
import os


"""
多进程对于全局变量的访问，在每一个全局变量里面放一个m变量
保证每个进程访问变量互不干扰

"""

m = 1  # 不可变类型
list1 = []  # 可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        print('这是任务-1---------', m, list1)


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        print('这是任务-2---------', m, list1)


if __name__ == '__main__':
    # 子进程
    p = Process(target=task1, name="任务1", args=(1, 'aa '))
    p.start()
    p1 = Process(target=task2, name="任务2", args=(2, 'bb'))
    p1.start()

    while True:
        sleep(1)
        m += 1
        print('-====', m)



# def task1():
#     while True:
#         sleep(1)
#         print('这是任务-1---------', os.getpid(), '------', os.getppid())
#
#
# def task2():
#     while True:
#         sleep(2)
#         print('这是任务-2---------', os.getpid(), '------', os.getppid())
#
#
# if __name__ == '__main__':
#     print(os.getpid())  # 获取当前进程号
#     # 子进程
#     p = Process(target=task1, name="任务1")
#     p.start()
#     print(p.name)
#     p1 = Process(target=task2, name="任务2")
#     print(p1.name)
#     p1.start()
#
#     print('------------')
#     print('************')


# 传参
# def task1(s, name):
#     while True:
#         sleep(s)
#         print('这是任务-1---------', os.getpid(), '------', os.getppid(), name)
#
#
# def task2(s, name):
#     while True:
#         sleep(s)
#         print('这是任务-2---------', os.getpid(), '------', os.getppid(), name)
#
# number = 1
# if __name__ == '__main__':
#     print(os.getpid())  # 获取当前进程号
#     # 子进程
#     p = Process(target=task1, name="任务1", args=(1, 'aa '))
#     p.start()
#     print(p.name)
#     p1 = Process(target=task2, name="任务2", args=(2, 'bb'))
#     print(p1.name)
#     p1.start()
#     while True:
#         number += 1
#         sleep(0.2)
#         if number == 100:
#             p.terminate()
#             p1.terminate()
#             break
#         else:
#             print(f'---------{number}')
#
#     print('------------')
#     print('************')