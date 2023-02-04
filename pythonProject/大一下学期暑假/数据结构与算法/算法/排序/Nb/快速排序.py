# 时间复杂度(nlongn)，空间复杂度:平均O(logn)，最坏(n)
def partition(li, left, right):
    tmp = li[left]  # 将第一个数抽取出来，变相这个下标对应的元素为空

    # 至少剩余两个元素
    while left < right:

        # 右侧抽取比第一个值小的数，left<right：至少存在两个元素
        while left < right and li[right] >= tmp:  # 只要比第一个数大就一直找
            right -= 1  # 往左走一步
        li[left] = li[right]  # 将选取出来的数放入第一个数留下来的空位，原来这个位置就留出一个空位

        # 左侧抽取比第一个大的数
        while left < right and li[left] <= tmp:  # 只要比第一个数小就一直循环
            left += 1  # 往右边走一步
        li[right] = li[left]  # 将右侧空出来的位置填上

    li[left] = tmp  # 将取出的值放在序列中合适的位置，此时的left=right
    return left


def quick_sort(li, left, right):
    if left < right:  # 至少存在两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li, 0, len(li)-1)
print(li)
