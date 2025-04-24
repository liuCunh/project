li = [['张三', '110'], ['李四', '120'], ['王五', '119'], ['test', 1]]
print(f'1.增加用户信息\t2.删除用户\t3.修改手机\t4.查询所有用户\t5.查找用户手机号\t6.推出')
while True:
    usr_in = int(input('请输入：'))
    if usr_in == 1:
        add_name = input("用户姓名：")
        phone = input("电话号码")
        tmp = [add_name, phone]
        li.append(tmp)
        print('添加成功！')
    elif usr_in == 2:
        del_name = input('删除的用户姓名：')
        for ind, users in enumerate(li):
            if del_name == users[0]:
                del li[ind]
                print('删除成功')
    elif usr_in == 3:
        update_usr = input('被修改人姓名：')
        for ind, users in enumerate(li):
            print(users)
            if update_usr == users[0]:
                num = input('电话号码：')
                li[ind][1] = num
                print('修改成功')
    elif usr_in == 4:
        for user in range(len(li)):
            print(f'用户姓名：{li[user][0]}\t用户电话号码：{li[user][1]}')
    elif usr_in == 5:
        find_num = input('查找的用户姓名：')
        for ind, users in enumerate(li):
            if find_num == users[0]:
                print(f'用户姓名：{li[ind][0]}\t用户电话号码：{li[ind][1]}')
    elif usr_in == 6:
        break
    else:
        print('输入错误，重新输入！')
