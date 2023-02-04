
"""
time模块
重点:
    time()
    sleep()
    strftime()
了解:
    loacltime()  ->tm_year, tm_day
    ...
"""
import time


t = time.time()
print(t)
# for i in range(99999):
#     print(" ", end="")

# time.sleep(3)
t1 = time.time()  # 获取当前时间戳
print(t1)

# 将世家戳转成字符串
s = time.ctime(t)  # 将秒数转换成字符串
print(s)

t = time.localtime(t)  # 将时间戳转换成元组数据
print(t)
print(t.tm_year, t.tm_mon, t.tm_mday)


# 将元组的转换成时间戳
tt = time.mktime(t)
print(tt)

# 将元组(时间戳)转换成字符串, 默认当前时间
s = time.strftime("%Y-%m-%d %H:%M:%S")
print(s)

# 将字符串转成元组
r = time.strptime("2022/09/26", "%Y/%m/%d")
print(r)


