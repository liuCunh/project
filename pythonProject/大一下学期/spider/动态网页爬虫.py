# 爬取英雄联盟皮肤

import requests
import prettytable as pt

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'  # everything
url2 = "https://game.gtimg.cn/images/lol/act/img/js/hero/"  # 单个英雄


def getHerolist():  # 得到英雄列表
    json = requests.get(url).json()
    hero_list = json["hero"]  # 英雄编号
    # list1 = []  # 英雄列表
    tb = pt.PrettyTable()  # 创建表格

    # 定义字段名
    tb.field_names = [
        '英雄ID',
        '英雄名字',
    ]

    # 加入列表元素
    for hero in hero_list:
        hero_ID = hero['heroId']
        hero_Name = hero['name']
        tb.add_row([
            hero_ID,
            hero_Name,
        ])

        # list1.append(hero['heroId'] + ":" + hero['name'])  # 加入英雄列表
    print(tb)

    # 换行输出英雄列表
    # for l in list1:
    #     print(l)


def downLoadById(heroid):  # 下载图片
    url3 = url2 + str(heroid) + ".js"  # 英雄的url
    json = requests.get(url3).json()
    list = json["skins"]  # 皮肤
    list1 = []  # 皮肤列表

    # 筛选图片姓名跟地址
    for l in list:
        if l['mainImg'] not in "":  # 查看主要图片是否为空
            list1.append(l['name'] + "," + l['mainImg'])  # 加入皮肤列表

    # 筛选主要皮肤
    for l1 in list1:
        name = l1.split(",")[0]  # 姓名
        img_url = l1.split(",")[1]  # 图片地址
        file_end = ".jpg"   # 文件后缀名
        file_end_num = img_url.rfind('/')  # 右侧查找文件名字前/的下标
        s = img_url[file_end_num + 1:]  # 切片文件名

        # 判断后缀
        if s.endswith('.png'):
            file_end = '.png'

        content = requests.get(img_url).content  # 编译图片二进制文件

        # 打开文件
        with open("./images/" + name + file_end, "wb") as f:
            f.write(content)
            print(name + '.jpg\t下载成功！')


getHerolist()
hero_id = input("英雄编号：")
downLoadById(hero_id)

