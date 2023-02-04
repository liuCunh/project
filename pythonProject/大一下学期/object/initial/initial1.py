class Compute:
    def __init__(self, num, num1):
        self.num=num
        self.num1=num1
    def add(self):
        print(self.num + self.num1)
    def subtraction(self):
        print(self.num - self.num1)
    def multiply(self):
        print(self.num * self.num1)
    def division(self): 
        if self.num1 == 0:
            print('被除数不能为零！')
        else:
            print(self.num / self.num1)
object1 = Compute(1, 2)
object1.add()
object1.division()


