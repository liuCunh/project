import os

src_path = r'D:\pythonProject\home'
target_path = r'd:\test'


# 封装成函数
def copy1(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)
        for file in filelist:
            path = os.path.join(src, file)
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完毕！')


def copy(src_path, target_path):
    filelist = os.listdir(src_path)  # 获取目录里面的内容
    # 遍历列表
    for file in filelist:
        path = os.path.join(src_path, file)  # 拼接路径
        # 判断为文件还是文件夹
        if os.path.isdir(path):
            tp = os.path.join(target_path, file)  # 拼接目标文件夹
            # 检查文件夹是否存在
            if not os.path.exists(tp):
                os.mkdir(tp)  # 创建目标文件夹
                copy(path, tp)  # 递归调用copy

        else:  # 不是文件夹直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成')


copy(src_path, target_path)