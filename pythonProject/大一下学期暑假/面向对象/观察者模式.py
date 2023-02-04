from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


class Notice:  # 抽象发布者
    def __init__(self):
        self.observers = []

    def attach(self, obs):  # 关注
        self.observers.append(obs)

    def detach(self, obs):  # 取消关注
        self.observers.remove(obs)

    def notify(self):  # 推送
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property  # 让私有成员可以在外面被调用
    def company_info(self):
        return self.__company_info

    @company_info.setter  # 初始化属性在函数外面可以被重写
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):  # 具体观察者
    def __init__(self):
        self.company_info = None

    def update(self, notice):  # notice对象为具体的发布者

        self.company_info = notice.company_info


notice = StaffNotice('初始公司属性')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = '公司今年业绩非常好，给大家发奖金！！！'
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = '公司明天放假！！！'
print(s1.company_info)
print(s2.company_info)

