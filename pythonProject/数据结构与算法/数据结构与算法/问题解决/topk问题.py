import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper


# 现有n个数，设计算法得到前k大的数
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j+1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            break
        li[i] = tmp


@cal_time
def topk(li, k):
    heap = li[0:k]

    # 对heap进行建堆操作
    for i in range((k-2)//2, -1, -1):
        # i标识当前堆的堆根
        sift(heap, i, k-1)

    # 对堆进行比较操作，将排序好的小根堆的根与k后面的数进行比较
    for i in range(k, len(li)-1):
        # i表示k后面的数
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)

    # 出堆，将堆排好序后输出
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap


import random
li = [i for i in range(100)]
random.shuffle(li)
print(topk(li, 10))



