def hannoi(n, a, b, c):  # a,b,c为三根柱子
    if n > 0:
        hannoi(n-1, a, c, b)  # 第一步：将a上的n-1个盘子从a经过c移动到b
        print(f'moving from {a} to {c}')  # 第二步：将第n个盘子从a移动到c
        hannoi(n-1, b, a, c)  # 第三步：将b上的n-1个盘子从b经过a移动到c


hannoi(4, 'A', 'B', 'C')
