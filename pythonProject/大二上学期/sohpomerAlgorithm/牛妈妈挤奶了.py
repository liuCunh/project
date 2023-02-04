from queue import PriorityQueue


def main():
    # 输入牛的列表，0：起始时间，1：结束时间，2：牛的编号
    cow_list = []
    # 总共需要的畜栏
    total = 0
    # i表示编号为i的奶牛去的畜栏编号
    pos = [0 for _ in range(10)]
    # n头牛
    n = int(input())
    for i in range(1, n+1):
        temp = list(map(int, input().split()))
        temp.append(i)
        cow_list.append(temp)
    cow_list = sorted(cow_list, key=lambda x: x[0])
    # 按开始时间排序后的列表
    # [[1, 10, 1], [2, 4, 2], [3, 6, 3], [4, 7, 5], [5, 8, 4]]
    # pq优先权队列中元素是list，0：结束时间，1：畜栏编号
    pq = PriorityQueue()
    for i in range(n):
        if pq.empty():
            total += 1
            pq.put([cow_list[i][1], total])  # [end, total]
            pos[cow_list[i][2]] = total  # [1, 0...]
        else:
            # 获取pq队列中结束时间最早的列表st
            # st = pq.get()
            # 此处很重要，如果使用get会把队头元素删除，使用queue属性，则会返回
            # 整个队列元素的列表，为了去队头，所以索引是0
            st = pq.queue[0]
            # 队列中最早结束时间小于新加入这头牛的开始时间
            if st[0] < cow_list[i][0]:
                pos[cow_list[i][2]] = st[1]
                pq.put([cow_list[i][1], st[1]])
            # 新增加一个牛栏
            else:
                total += 1
                pq.put([cow_list[i][1], total])
                pos[cow_list[i][2]] = total

    print("最少需要的畜栏数:%d" % total)
    for i in range(1, n+1):
        print("%d" % pos[i])

    return 0


if __name__ == '__main__':
    main()
    li = [[1, 10], [2, 4], [3, 6], [5, 8], [4, 7]]
