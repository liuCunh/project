import random


def generate_checkcode(n):
    s = '123456789qwertyuiopasdfghjkklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s)-1)
        code += s[ran]
    return code


def login():
    username = input('username:')
    password = input('password:')
    code = generate_checkcode(5)
    print(code)
    code1 = input('code:')
    if code1.lower() == code.lower():
        if username == '潘周丹' and password == '123456':
            print('登录成功！')
        else:
            print('用户名或者密码有误！')
    else:
        print('验证码错误')


login()
login()