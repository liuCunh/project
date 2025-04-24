# myself
# def login_my(username, password):
#     user = {'username': '潘周丹', 'password': '123456'}
#     if username == user['username'] and password == user['password']:
#         return True
#     return False
#
#
# def add_shopping(goodsName):
#     goods = [goodsName]
#     return goods


islogin = False


def add_shoppingcart(goodsName):
    global islogin

    if islogin:
        if goodsName:
            print(f'成功将{goodsName}加入购物车！')
        else:
            print('没有选中任何商品！')
    else:
        answer = input('用户没有登录！重新登录用户y/n：')
        if answer == 'y':
            username = input('用户名：')
            password = input("密码：")
            islogin = login(username, password)
            print(f'islogin={islogin}')

        else:
            print('很遗憾，不能添加任何商品')


def login(username, password):
    if username == '潘周丹' and password == '123456':
        return True
    else:
        print('用户名或者密码错误！')
        return False


islogin = login('潘周', '123456')

add_shoppingcart('阿玛尼唇釉')

