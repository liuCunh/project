class Phone:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def call(self):
        print(f'使用{self.brand}品牌{self.type}型号手机正在打电话')

    def __str__(self):
        return f'brand={self.brand}, type={self.type}'


p = Phone('Iphone', 11)
p.call()
print(p)
