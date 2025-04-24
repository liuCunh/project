"""
非阻塞式：进程池的运行依赖于主进程
    全部添加到队列中，立刻返回，并没有等待其他的进程完毕之后才结束
    但是回调函数是在等待任务完成之后才调用的。
"""
# 进程池
import os
import time
from multiprocessing import Pool

# 非阻塞式进程
from random import random


def task(task_name):
    print('开始左任务啦！', task_name)
    start = time.time()

    # 使用sleep
    time.sleep(random() * 2)  # 控制在两秒内
    end = time.time()
    # print(f'完成任务: {task_name}, 用时{end - start}小时，进程id={os.getpid()}')
    return f'完成任务: {task_name}, 用时{end - start}小时，进程id={os.getpid()}'


container = []
# 这里时一个回调方法(回调方法必须传参)
def callback_fun(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)  # 创建5个进程

    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '上学', '购物']
    for i in tasks:
        # 非阻塞式创建 (执行动作，args=可迭代参数, callback=回调方法名)
        pool.apply_async(task, args=(i,), callback=callback_fun)

    pool.close()  # 添加任务结束
    pool.join()  # 阻塞主进程结束

    for c in container:
        print(c)
    print('over')
