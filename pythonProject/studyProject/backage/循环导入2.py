def func():
    print("--------循环导入2里面的func-------")
    from 循环导入1 import task1
    task1()
    print("--------循环导入2里面的func-------")