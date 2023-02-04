def func(n):
    li = []
    for cube in range(n, 1, -1):

        for a in range(2, cube):
            for b in range(a+1, cube):
                for c in range(b+1, cube):
                    if cube**3 == a**3+b**3+c**3:
                        li.append([cube, a, b, c])

    li.sort(key=lambda x: x[0], reverse=False)
    return li


for i in func(24):
    print(f'cube={i[0]}, Triple={i[1:]}')
