class Computer:
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1

    def add(self):
        print(f'{self.num}+{self.num1}={self.num + self.num1}')


objeComputer = Computer(1, 3)
objeComputer.add()
