import threading

n = 0
def task1():
    global n
    for i in range(10000000):
        n += 1

    print(f"task1------n={n}")


def task2():
    global n
    for i in range(10000000):
        n += 1

    print(f"task2------n={n}")

if __name__ == '__main__':
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f"最后打印n：{n}")
