class BankCard:
    def __init__(self, username):
        self.username = username
        self.__balance = 10

    def deposit(self, money):  # 存款
        self.__balance += money
        print("存款成功！")

    def draw_money(self, money):  # 取款
        if self.__balance > 0 and self.__balance >= money:
            self.__balance -= money
            print(f'取款成功！此次共取款{money}元')
        else:
            print("取款失败，你的账户余额不足！")

    def to_card(self, name, money):  # 转账
        if self.__balance > 0 and self.__balance >= money:
            self.__balance -= money
            print(f'{name}已经收到你转的{money}元！，你的账户余额{self.__balance}元')
        else:
            print("账户余额不足！")

    def __str__(self):
        return f'账户名：{self.username}, 余额: {self.__balance}'


liuchun = BankCard("刘春")
print(liuchun)

liuchun.deposit(100)
print(liuchun)

liuchun.to_card("Jack", 99)