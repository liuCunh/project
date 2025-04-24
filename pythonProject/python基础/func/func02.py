def enumerate(li):
    index = 0
    tmp = list()
    for i in li:
        t = (index, i)
        tmp.append(t)
        index += 1
    for ind, val in tmp:
        print(ind, val)


li = [1, 2, 3, 4, 5, 6, 89, 1]
enumerate(li)

