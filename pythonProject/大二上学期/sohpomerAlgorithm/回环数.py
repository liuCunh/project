# 1到1000中既是质数又是回环数
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_pa(num):
    left = 0
    right = len(num) - 1
    while left <= right:
        if num[left] == num[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


li = []
for i in range(2, 1001):
    if is_pa(str(i)) and is_prime(i):
        li.append(i)
print(li)
