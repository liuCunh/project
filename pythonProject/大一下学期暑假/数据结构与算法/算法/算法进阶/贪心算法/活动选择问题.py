# 假设有n个活动，这些活动要占用同一片场地，而场地在某时刻只能提供一个活动使用。
# 每个活动都有一个开始时间s和结束时间f(题目中时间以整数表示)，表示活动在[s, f)区间占用场地
# 问：安排哪些活动能够使该场地举办的活动的个数最多？
# (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)
timetable = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 解题关键：活动的结束时间越早，后面能够排入的活动就越多
timetable.sort()


def activity_selected(a):
    li = [a[0]]
    for i in range(1, len(a)):
        if li[-1][1] < a[i][0]:  # 开始时就小于上一个活动的结束时间from functools import cmp_to_key
            li.append(a[i])
    return li


timetable.sort(key=lambda x: x[1])


def my_second(a):
    table = [a[0]]
    for tims in a:
        if table[-1][1] <= tims[0]:
            table.append(tims)
    return table


print(activity_selected(timetable))
print(my_second(timetable))
