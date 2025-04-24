from abc import ABCMeta, abstractmethod
class payment(metaclass=ABCMeta):
    # abstarct class 抽象类
    @abstractmethod  # 抽象方法：让子类必须拥有相同的方法，子类中不含有此类方法则报错
    def pay(self, money):
        pass

# 花呗支付，支付宝支付
class Alipay(payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print(f'花呗支付{money}元')
        else:
            print(f'支付宝支付{money}元')


# 微信支付
class WecharPay:
    def pay(self, money):
        print(f'微信支付{money}元')

class BankPay:
    def pay(self, money):
        print(f'银行卡支付{money}元')


# 简单工厂模式
# class Paymentfactory:
#     def create_payment(self, method):
#         if method == 'Alipay':
#             return Alipay()
#         elif method == 'WecharPay':
#             return WecharPay()
#         elif method == 'huabei':
#             return Alipay(use_huabei=True)
#         else:
#             raise TypeError(f"No such payment named {method}")


# 完善工厂模式：
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WecharPayFactory(PaymentFactory):
    def create_payment(self):
        return WecharPay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()

pf = BankPayFactory()
p = pf.create_payment()
p.pay(100)