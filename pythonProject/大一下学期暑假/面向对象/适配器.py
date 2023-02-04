from abc import ABCMeta, abstractmethod
class payment(metaclass=ABCMeta):
    # abstarct class 抽象类
    @abstractmethod  # 抽象方法：让子类必须拥有相同的方法，子类中不含有此类方法则报错
    def pay(self, money):
        pass
class Alipay(payment):
    def pay(self, money):
        print(f'支付宝支付{money}元')

class WecharPay:
    def pay(self, money):
        print(f'微信支付{money}元')
class BankPay:
    def cost(self, money):
        print(f'银联支付{money}元')

# 适配器方法一：类适配器
# lass NewPay(payment, BankPay):
#     def pay(self, money):
#         self.cost(money)

# 适配器方法二：对象适配器
class PaymentAdapter(payment):
    def __init__(self, method):
        self.method = method

    def pay(self, money):
        self.method.cost(money)



p = PaymentAdapter(BankPay())
p.pay(100)

# 组合
# class A:
#     pass
# class B:
#     def __init__(self):
#         # 在B类中创建一个A类的属性，B类就能调用A类的属性跟方法了，这个过程叫做组合
#         self.a = A()
