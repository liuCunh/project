# 持久化保存：文件

# 用户注册
def register():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input('确认密码：')

    if password == repassword:
        path = r"D:\bookSystem\users.txt"
        with open(path, 'a') as wstream:
            wstream.write(f'{username} {password}\n')
        print('用户注册成功！')
    else:
        print('密码不一致！')

# 用户登录
def login():
    username = input('输入用户名：')
    password = input('输入密码：')

    if username and password:
        path = r"D:\bookSystem\users.txt"
        with open(path) as rstream:
            while True:
                user = rstream.readline()
                if not user:
                    print('用户名或者密码输入有误！')
                    break

                input_user = f'{username} {password}\n'
                if input_user == user:
                    print('用户登录成功！')
                    break


def show_books():
    print('--------图书-------')
    with open(r'd:/bookSystem/books.txt', 'r', encoding='utf8') as rstream:
        books = rstream.readlines()
        for book in books:
            print(f'<<{book[0:-1]}>>', end=",")

# register()
# login()
show_books()