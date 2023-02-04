def max(*arge):
    print(arge)
    m = arge[0]
    for i in range(1, len(arge)):
        if m < arge[i]:
            m = arge[i]
    return m


print(max(1, 2, 3, 4, 5, 5, 6, 7))
