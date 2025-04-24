# 阻塞式
import os
import time
from multiprocessing import Pool

"""
阻塞式提点：
    添加一个执行一个任务，如果一个任务不结束另一个任务就进不来
    
进程池：
 pool = Pool(num) 创建进程池对象
 pool.apply() 阻塞式
 pool.apply_async() 非阻塞式
 
 pool.close()
 pool.join() 让主进程让步
"""

# 非阻塞式进程

# from random import random
#
#
# def task(task_name):
#     print('开始左任务啦！', task_name)
#     start = time.time()
#
#     # 使用sleep
#     time.sleep(random() * 2)  # 控制在两秒内
#     end = time.time()
#     print(f'完成任务: {task_name}, 用时{end - start}小时，进程id={os.getpid()}')
#     # return f'完成任务: {task_name}, 用时{end - start}小时，进程id={os.getpid()}'
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '上学', '购物']
#     for i in tasks:
#         # 非阻塞式创建 (执行动作，args=可迭代参数, callback=回调方法名)
#         pool.apply(task, args=(i,))
#
#     pool.close()
#     pool.join()
#     print('over')

# 进程间通信
from multiprocessing import Queue

q = Queue(5)
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())  # 获取队列长度
if not q.full():  # full()判断queue是否是满的，q.empty()判断队列是否为空
    q.put("F", timeout=3)  # put方法中如果queue满了，则只能等待，除非queue有空位，则添加成功
else:
    print('queue满了 ')

# 获取队列值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))