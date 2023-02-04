class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            res = a % b
            a = b
            b = res
        return a

    def zgs(self, a, b):
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(a, b)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)

    def __str__(self):
        return '%d/%d' % (self.a, self.b)


a = Fraction(1, 3)
b = Fraction(1, 2)
c = a+b
print(c)



