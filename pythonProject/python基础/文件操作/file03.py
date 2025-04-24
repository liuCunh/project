"""
源文件：c:\p1\girl.jpg
目标文件： c:\p2\girl.jpg


使用with 结合open使用，可以自动释放资源

"""

with open(r'1.jpg', 'rb') as stream:
    container = stream.read()

    with open(r'../test/1.jpg', 'wb') as wstream:
        wstream.write(container)
        print('复制成功！')

