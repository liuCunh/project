class Person:
    def __init__(self, n):
        print(f'[__init__-->self-]:{self},[-->n]:{n}')
        self.name = n

    def __del__(self):
        print(f'[__del__-->self]:{self}')

    def show(self):
        print(f'[show.self]:{self},[show.self.name]:{self.name}')


p = Person('james')
p.show()
print(f'[p]:{p}')
