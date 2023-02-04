# 集合推导式
list1 = [1, 2, 1, 3, 5, 2, 1, 8, 9, 7, 6]
set1 = {x for x in list1 if x > 5}
print(set1)

# 字典推导式
dict1 = {'a':'A', 'b':"B", "c":"C", "d":"C"}

newdict = {value: key for key, value in dict1.items()}
print(newdict)
