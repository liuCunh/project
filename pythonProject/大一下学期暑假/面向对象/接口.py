# 比如写一个支付程序
# 接口方法一：使用类继承跟重写
# class payment:
# #     def pay(self, money):
# #         raise NotImplementedError  # 不调用pay方法的话就不会报错

# 方法二：调用ABCMeta跟abstractmethod方法
from abc import ABCMeta, abstractmethod
class payment(metaclass=ABCMeta):
    # abstarct class 抽象类
    @abstractmethod  # 抽象方法：让子类必须拥有相同的方法，子类中不含有此类方法则报错
    def pay(self, money):
        pass
class Alipay(payment):
    def pay(self, money):
        print(money)

class WecharPay:
    def pay(self, money):
        print(money)

p = Alipay()
p.pay(100)
li = []
li.sort()