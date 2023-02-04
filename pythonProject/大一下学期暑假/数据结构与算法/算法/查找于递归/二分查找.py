# 必须在有序数列里面才能进行查找
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1

    while left <= right:  # 候选区有值
        mid = (left + right) // 2

        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

@cal_time
def book_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return book_binary_search(data, target, low, mid - 1)
        else:
            return book_binary_search(data, target, mid + 1, high)


@cal_time
def book(data, target, low, high):
    return book_binary_search(data, target, low, high)


li = list(range(10000000))
# print(book_binary_search(li, 500, 0, len(li) - 1))
print(binary_search(li, 500))
