def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(li, 9))
