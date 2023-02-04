"""
stream = open(r'path', 'w')
mode 是w表示就是写操作

方法
    write(内容) 每次都会讲原来的内容清空，然后写当前的内容
    writelins(Iterable) 没有换行效果，想要换行需要手动添加换行符\n
    stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星'])


"""

stream = open('aa.txt', 'a')


s = '''
你好！
    欢迎来到澳门破财赌场，赠送给你一个金币！
            赌王：高进

'''
stream.write('王自强')
result = stream.write('hello\n')
print(result)
stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])
stream.write('僵尸先生')

stream.close()  # 释放资源

# stream.write('龙五')

