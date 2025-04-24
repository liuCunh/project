from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handler_leave(self, day):
        pass


class GeneralManager(Handler):
    def handler_leave(self, day):
        if day <= 10:
            print(f'总经理准假{day}天')
        else:
            print('你还是辞职吧！')


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handler_leave(self, day):
        if day <= 5:
            print(f'部门经理准假{day}天')
        else:
            print(f'部门经理无权限！')
            self.next.handler_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handler_leave(self, day):
        if day <= 1:
            print(f'项目主管准假{day}天')
        else:
            print(f'项目主管无权限！')
            self.next.handler_leave(day)


day = 11
h = ProjectDirector()
h.handler_leave(day)
