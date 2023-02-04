"""
datetime模块：
    time 时间
    date 日期
    datetime  日期时间 now()
    timedelta 时间差  timedelta(day="", weeks="",,,,)
"""

import datetime
import time

print(datetime.time.hour)
print(time.localtime().tm_hour)
d = datetime.date(2022, 9, 26)
print(datetime.date.day)

print(datetime.date.ctime(d))
print(datetime.date.today())  # 返回当前日期

# 时间差
timedel = datetime.timedelta(weeks=3, hours=18)
print(timedel)

# datetime.datetime.now() 得到当前的日期跟时间
now = datetime.datetime.now()  # 当前时间
print(now)
result = now + timedel
print(result)

