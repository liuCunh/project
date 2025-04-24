dict = {"Alice":"2341", "Beth":"9102", "Cecil":"3258"}
print("type(dict):", type(dict))
print('\033[0;31mend\033[0m')

dict = {"Name":"Zara", "Age":7, "Class":"First"}
print("dict['Name']:", dict["Name"])
print("dict['Age']:", dict["Age"])
# print("None_keys", dict["gender"])
# gender值不存在
print('\033[0;31mend\033[0m')

# 字典的值是列表
zone={"province":"广东", "city":["广州", "深圳"]}
print('zone["province"]:', zone["province"])
print("zone['city']:", zone["city"])
for c in zone["city"]:
    print(c)
print('\033[0;31mend\033[0m')

# 修改字典
zone['citys']="广东"
print(zone['citys'])

# 删除
del zone['city']        # 删除单个keys
print('zone["city"]:', zone)
zone.clear()            # 清空整个字典
print('zone.clear(): ', zone)
try:
    del zone                # 删除字典
    print(zone)
except Exception as err:
    print(err)
print('\033[0;31mend\033[0m')
# 获取键值对函数
dict={"Name":"Zare", "Age":7}
print("dict.keys():", dict.keys())
print("dict.items():", dict.items())
print('\033[0;31mend\033[0m')

