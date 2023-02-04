def binary():
    left, right = 1, 100
    while left < right:
        mid = (left + right) / 2
        res = mid ** 3 - 5 * mid ** 2 + 19 * mid - 80
        print(res)
        if res <= 1e-10:
            return mid
        elif res > 0:
            right = mid - 1e-10
        else:
            left = mid + 1e-10


print(binary())
