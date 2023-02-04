from itertools import permutations


def four_num(s):
    for element in permutations(s):
        res = "".join(list(element))
        print(res)


four_num('55555')

