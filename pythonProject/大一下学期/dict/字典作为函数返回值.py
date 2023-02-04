def fun():
    dict={}
    dict["name"]="aaa"
    dict["age"]=20
    dict["gender"]="male"
    return dict


def show(dict):
    keys=dict.keys()
    for key in keys:
        print(key, dict[key])


dict=fun()
print(dict)
show(dict)

