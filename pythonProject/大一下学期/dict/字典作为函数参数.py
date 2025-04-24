def fun(dict):
    dict['name'] = 'aaa'
    print("inside:", dict)


dict={"name": "xxx", "age": 30}
print("before:", dict)
fun(dict)
print("after:", dict)
