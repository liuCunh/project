s = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(s)
print(type(s))
print('\033[0;31mend\033[0m')
week = ("日", "一", "二", "三", "四", "五", "六")
print(week)

while True:
    w = int(input("Enter an integer:"))
    if 0 <= w <=6:
        print("星期"+week[w])
    elif w == 7:
        break
    else:
        print("输入错误")
print('\033[0;31mend\033[0m')

