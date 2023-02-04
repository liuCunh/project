# 时间复杂度(n ^ 2)，空间复杂度O(1)
def bubble_sort(li):
    for i in range(len(li)-1):  # len(li)-1次是因为第n-1次就已经将最大的数字移动到最后面去了，所以最后一次不用考虑
        exchange = False  # 标识顺序是否存在

        # 对为无序集合排序
        for j in range(len(li)-i-1):
            # 判断前后是否有序
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]  # 冒泡排序的精髓，下标对应的元素进行交换
                exchange = True
        if not exchange:
            return


# li = [random.randint(0, 1000) for i in range(100)]
li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print(li)
