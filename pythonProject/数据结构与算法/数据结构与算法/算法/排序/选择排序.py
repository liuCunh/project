# 选择排序就是将序列中最小的一个数提到当前无序序列的最前面  时间复杂度(n ^ 2)，空间复杂度O(1)
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):

    # 给最小值移动到最前方
    for i in range(len(li)-1):  # 该次数：筛选到n-1的过程中把最小的值给选走了，留下的n项肯定就为最大的元素了
        min_index = i  # 最小值下标

        # 找出最小值的下标
        for j in range(i+1, len(li)):  # i 前面的都是已经排序好了的元素，而i+1是因为min_index顶替了i的位置
            if li[min_index] > li[j]:
                min_index = j
        li[min_index], li[i] = li[i], li[min_index]
        print(li)


def extra_selct(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


li = [0, 3, 4, 2, 1, 5]
# print(select_sort_simple(li))
select_sort(li)
