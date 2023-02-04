import threading
from time import sleep

"""
线程共享全局变量

全局解释器
"""
ticket = 1000
def run1():
    global ticket
    for i in range(100):
        sleep(0.1)
        ticket -= 1
# def run2():
#     global ticket
#     for i in range(100):
#         ticket -= 1

if __name__ == '__main__':
    th1 = threading.Thread(target=run1, name="th1")
    th2 = threading.Thread(target=run1, name="th2")
    th3 = threading.Thread(target=run1, name="th3")
    th4 = threading.Thread(target=run1, name="th4")

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    print(f"ticket={ticket}")