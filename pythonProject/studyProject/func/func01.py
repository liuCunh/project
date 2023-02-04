"""
 定义一个登录函数，参数是：username，password
 函数体：
 判断实参是否正确，如果争取着登录成功，否者打印登录失败
"""


def is_user(username, password):
    if username == 'username' and password == "password":
        print('登录成功')
    else:
        print('登录失败！')


is_user('username', 'password')
