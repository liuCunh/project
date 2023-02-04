provinces = {}
def append(province, cities):
    global provinces
    if province not in provinces.keys():
        provinces[province]=cities
    else:
        print(province+'已经存在')


def show():
    for p in provinces.keys():
        print(p, provinces[p])


def seekProvince(province):
    if province in provinces.keys():
        print(province, end=":")
        for c in provinces[province]:
            print(c, end=" ")
        print()
    else:
        print("没有这个省份！")


def seekCity(city):
    for p in provinces.keys():
        if city in provinces[p]:
            print((city+"属于"+p+"省"))
            return
        print("没有这个城市！")


append("广东", ["广州", "深圳"])
append("四川", ["成都", "内江", "乐山"])
append("贵州", ["贵阳", "六盘水", "兴义"])
show()
seekProvince("四川")
seekCity("六盘水")
