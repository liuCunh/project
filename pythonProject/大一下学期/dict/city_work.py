# 1、完成省份与城市
#
# 2、实现动态添加省份与城市的功能
#
# 3、实现查找省份与城市的功能
provinces = {}


def append(province,cities):
    global provinces
    if province not in provinces.keys():
        provinces[province] = cities
    else:
        print(f'{province}已经存在')


def show():
    for p in provinces.keys():
        print(p, provinces[p])


def seekProvince(province):
    if province in provinces.keys():
        print(province, end=":")
        for c in provinces[province]:
            print(c, end=' ')
        print()
    else:
        print('没有这个省份！')


def seekCity(city):
    for p in provinces.keys():
        if city in provinces[p]:
            print(f'{city}属于{p}省')
            return
    print('没有这个城市！')


append('四川', ['成都', '绵阳'])
append('广东', ['广州', '佛山'])
print(provinces)
show()
seekProvince('四川')
seekCity('成都')

