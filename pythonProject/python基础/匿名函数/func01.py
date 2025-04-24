list1 = [2, 5, 8, 0, 9]
m = max(list1)

print(f'最大值={m}')

list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 20, 'b': 20}]
print(max(list2, key=lambda x: x['a']))
