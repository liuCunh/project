class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = f"No={self.no}, name={self.name}, salary={self.salary}"
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary


class SalesMan(Person):
    def __init__(self, no, name, salary, saleMoney, percent):
        super().__init__(no, name, salary)
        self.salesMoney = saleMoney
        self.percent = percent

    def getSalary(self):
        money = self.salesMoney * self.percent
        self.salary += money
        return self.salary


w = Worker("001", "King", 2000, 160, 50)
print(w.getSalary())
print(w)

saler = SalesMan("002", "Jack", 5000, 5000000, 0.003)
print(saler.getSalary())
print(saler)

