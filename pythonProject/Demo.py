import math
def num(s) :
    s_sqrt=math.sqrt(s)
    i=2
    while i <= s_sqrt :
        if s% i == 0 :
            result = False
            break
        i=i+1
    else :
        result = True
    return result
t=int(input())
n=t//2
while n >= 2 :
    m=t-n
    if num(n) and num(m) is True :
        print(n*m)
        break
    else :
        n=n-1
