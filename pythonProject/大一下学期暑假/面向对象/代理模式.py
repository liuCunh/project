from abc import ABCMeta, abstractmethod
import sys
sys.setrecursionlimit(100000)

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf8')
        self.content = f.read()
        f.close()
        print('文件内容已被读取')

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None  # 代理

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProtectProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('没有写入权限')  # 没有权限的异常


sub = ProtectProxy('test.txt')
# print(sub.get_content())
sub.set_content('haha')