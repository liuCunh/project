import time


islogin = False


# 定义登录函数
def login():
    print('--------登录界面-------')
    username = input('username:')
    password = input('password:')
    if username == 'admin' and password == '123456':
        print('--------》登录成功！')
        return True
    else:
        return False


# 定义一个装饰器：进行付款验证
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        # 验证用户是否登录
        print('---------付款界面---------')
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('支付失败，你未登录，请登录！')
            islogin = login()

    return wrapper


@login_required
def pay(money):
    print(f'支付金额：{money}')
    print('付款中。。。')
    time.sleep(2)
    print('付款完成')


pay(10000)
pay(8000)