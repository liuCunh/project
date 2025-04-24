# 计数器
def generate_count():
    container = [0]

    def add_one():  # 内部函数就是一个计数器
        container[0] += 1
        print(f'当前时第{container[0]}次访问')

    return add_one


def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():
        inner_func1()
        print('-----> inner_func2')

        return 'hello'

    return inner_func2


f = func()


