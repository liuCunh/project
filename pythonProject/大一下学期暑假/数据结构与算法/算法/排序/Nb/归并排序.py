# 假设现在的列表分两端有序，如何将其合成为一个有序列表  时间复杂度(nlongn)，空间复杂度O(n)
def merge(li, low, mid, high):  # low:第一个元素，mid:前列表最后的那个下标，high:两个列表加起来的长度减一
    i = low
    j = mid + 1  # 后列表的第一个元素的下标
    ltmp = []  # 临时列表

    # 左右两边共有的长度进行排序，只要两边有数
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    # 左列表多出来的元素
    while i <= mid:
        ltmp.append(li[i])
        i += 1

    # 右列表多出来的元素
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp  # 列表切片，释放临时列表


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)
