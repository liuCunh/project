class Computer:
    def __init__(self, n, s):
        self.num = n
        self.num1 = s

    def division(self):
        if self.num1 == 0:
            print('被除数不能为零！')
            return
        else:
            print(f'{self.num} / {self.num1} = {self.num / self.num1}')


computer = Computer(5, 10)
computer.division()
