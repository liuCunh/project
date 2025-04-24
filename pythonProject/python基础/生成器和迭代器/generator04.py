# 进程 > 线程 > 协程

def task1(n):
    for i in range(n):
        print(f'正在搬低{i}块砖')
        yield


def task2(n):
    for i in range(n):
        print(f'正在听{i}首歌')
        yield


# 交替实现方法
g1 = task1(10)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break

"""
生成器：generator

定义生成器方式：
    1、通过列推导式
        g = (x+1 for x in range(6))
    2、函数yield
        def fun():
            ...
            yield
        g = fun()
    
    产生元素：
        1、next(generator)  --> 每次调用都会产生一个新的元素，如果元素产生完毕，再次调用就会报错StopIteration
        2、生成器自带方法：
            g__next__()
            g.send(value)  最初必须g.send(None)
        
    应用：协程
            
"""