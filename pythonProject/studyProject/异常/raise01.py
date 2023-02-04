# 异常抛出

# 注册 用户名必须6位
def register():
    username = input('用户名：')
    if len(username) < 6:
        raise Exception('用户名长度必须6位及以上')
    else:
        print(f'输入的用户名: {username}')


try:
    register()
except Exception as err:
    print('注册失败！', end='')
    print(err)
else:
    print('注册成功！')

