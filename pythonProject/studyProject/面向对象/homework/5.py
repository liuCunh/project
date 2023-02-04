class Road:
    def __init__(self, road_name, road_length):
        self.road_name = road_name
        self.road_length = road_length


class Car:
    def __init__(self, car_name, velocity):
        self.car_name = car_name
        self.velocity = velocity

    def get_time(self, road, length):
        road = Road(road, length)
        print(f'{self.car_name}在{road.road_name}上以{self.velocity}km/h的时速跑了{road.road_length}米，就被逮住了。')

    def __str__(self):
        return f'车名：{self.car_name}, 时速：{self.velocity}km/h'


car = Car("特斯拉", 100)
car.get_time("成华大道", 300)
print(car)


import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = f'{self.brand}品牌的车在{road.name}上以{self.speed}速度的行驶{ran_time}小时'
        print(msg)

    def __str__(self):
        return f'{self.brand}品牌的，速度：{self.speed}'


r = Road("成华大道", 12000)
r.name = "京哈高速"
audi = Car("奥迪", 120)
print(audi)
audi.get_time(r)

