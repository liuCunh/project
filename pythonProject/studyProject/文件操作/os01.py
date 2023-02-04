import os

"""
os模块的常用方法:
    os.getcwd() 获取当前目录
    os.listdir() 浏览当前目录下的文件
    os.mkdir() 创建目录(空目录)
    os.rmdir() 删除空文件夹
    os.remove() 删除文件
    os.chdir() 切换目录    
"""
# print(os.path)
# path = (os.path.dirname(__file__))  # 以绝对路径的方式返回当前文件所在的位置
#
# print(path)
# res = os.path.join(path, 'a1.jpg')  # 对路路径进行拼接
# print(res)
# print()
# print()
# print()


# with open(r"E:\Download\Chrome\u=3294377371,3708031862&fm=193&f=GIF.jpg", 'rb') as stream:
#     container = stream.read()
#     print(stream.name)  # 得到文件的的路径
#
#     # 截取文件名字
#     file = stream.name
#     filename = file[file.rfind('\\'):]
#     print(filename)
#
#     # 得到当前文件路径
#     path = os.path.dirname(__file__)
#     res = os.path.join(path, filename)
#
#     with open(res, 'wb') as f:
#         f.write(container)

"""
os模块：
    absolute 绝对的，测试是否为绝对路径 return boolean
    eg: os.path.isabs(f"c:\p1\girl.jpg")
    
 """
# path = os.path.abspath('aa.txt')  # 获取文件的绝对路径
# print(path)
# path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
# print(path)
#
#
# path = os.getcwd()  # 获取当前的工作路径
# print(path)

# path = os.path.isfile(os.path.abspath(__file__))  # 判断文件是否为文件  return --> boolean
# print(path)

# path = os.path.isdir(os.getcwd())  # 判断文件是否为文件夹  return --> boolean
# print(path)

# path = os.path.abspath(__file__)
# result = os.path.split(path)  # 对路径进切片为两个元素，一个为文件目录，一个文件  return --> tuple
#
# print(result)
# res = os.path.splitext(path)  # 分割文件与拓展名, return --> tuple
#
# print(res)
# size = os.path.getsize(path)  # 获取文件大小， 单位字节
# print(size)

# res = os.path.join(os.getcwd(), 'file', 'os.py')  # 每次多一个参数,文件就多一个目录
# print(res)

# dir = os.getcwd()  # 获取当前文件夹
# print(dir)
#
# all = os.listdir(dir)  # 返回指定目录下的所有文件和文件夹, 保存在列表中
# print(all)
#
# if not os.path.exists(r'd:\test'):  # 判断路径是否存在
#     os.mkdir(r'd:\test')  # 创建文件夹
#
# # os.rmdir(r'd:\test')  # 删除空文件夹
# os.removedirs(r'd:\test')  # 删除多个目录

# os.remove(r'd:\test\p1\1.txt')


# # 逐个删除文件
# path = r'd:\test\p1'
# filelist = os.listdir(path)
# for file in filelist:
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# else:
#     os.rmdir(path)


# path = os.getcwd()
# print(path)
# # 切换目录
# os.chdir(r'd:\test')  # 切换到指定路径
# path = os.getcwd()
# print(path)

