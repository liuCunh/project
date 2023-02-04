"""
    open（path/filename, 'rt） --返回：stream（管道）

    container = stream.read() --读取管道中的内容

    注意：path出问题报错FileNotFountError
        如果读取文件是图片则不能使用默认读取方式， mode='rb'

    总结：
    read() 读取所有内容
    readline() 每次读取一行内容
    radlines() 读取所有行并且保存到列表中
    readable() 判断文件是否可以读取

"""

stream = open('aa.txt', 'r')
# data = stream.read()
#
# print(data)


"""
readable 判断文件是否可以读取
"""
result = stream.readable()

print(result)

'''readline读取一行内容,读取结果最后添加一行空格'''
# line = stream.readline()
# print(line)
#
# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break

'''readlines 读取所有，换行用/n代替，返回一个列表'''
# lines = stream.readlines()
# print(lines)
# for i in lines:
#     print(i)


stream = open('girl.jpg', 'rb')
container = stream.read()
# print(container)
