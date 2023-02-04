# 在计数排序中，元素范围比较大，使用桶排序:首先将元素分布在不同的桶中，在对每个桶中的元素进行排序
def bucket_sort(li, n=100, max_num=10000):  # n:划分桶的个数
    buckets = [[] for _ in range(n)]  # 划分桶的个数

    # 将列表中的元素按照范围存储在桶中
    for var in li:
        i = min(var // (max_num // n), n-1)   # (var//(max_num//n:每个桶的平均范围):将元素划分到适合的桶中,n-1):超过范围的元素都放在最后一个桶中
        buckets[i].append(var)  # 将元素放入桶中

        # 整理桶中元素
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


import random
li = [random.randint(0, 4) for _ in range(10)]
print(li)
print(bucket_sort(li))
