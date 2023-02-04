import itertools

li = [7, 2, 1, 10]


def count24(nums):
    for i in itertools.permutations(nums):
        for j in itertools.product("+-*/", repeat=3):
            res1 = f'({i[0]}{j[0]}{i[1]}){j[1]}({i[2]}{j[2]}{i[3]})'
            res2 = f'(({i[0]}{j[0]}{i[1]}){j[1]}{i[2]}){j[2]}{i[3]}'
            res3 = f'{i[0]}{j[0]}(({i[1]}{j[1]}{i[2]}){j[2]}{i[3]})'
            res = [res1, res2, res3]
            for bds in res:
                try:
                    if abs(eval(bds) - 24) <= 1e-10:
                        return True
                except ZeroDivisionError:
                    continue
    return False


if __name__ == '__main__':
    print(count24(li))
