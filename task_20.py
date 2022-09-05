import time


class Auto(object):
    brand = 'brand_name'
    age_years = 0
    mark = 'car`s mark'
    colour = 'colour of vehicle was not specified'
    weight = 'weight of vehicle was not specified'

    def __init__(self, brand, mark, age_years, colour='colour of vehicle was not specified',
                 weight='weight of vehicle was not specified'):
        self.brand = brand
        self.age_years = age_years
        self.mark = mark
        self.colour = colour
        self.weight = weight

    def move(self):
        print(f'{self.brand} {self.mark} {self.age_years} y.o.', 'move')

    def stop(self):
        print(f'{self.brand} {self.mark} {self.age_years} y.o.', 'stop')

    def birthday(self):
        self.age_years += 1
        print(f'{self.brand} {self.mark} is getting older')


class Truck(Auto):
    max_load = 0

    def __init__(self, brand, mark, age_years, max_load, colour='colour of vehicle was not specified',
                 weight='weight of vehicle was not specified'):
        super().__init__(brand, mark, age_years, colour, weight)
        self.max_load = max_load

    def move(self):
        print('Attention! Atention! Atention! Attention! Atention! Atention!')
        super().move()

    def load(self):
        time.sleep(1)
        print(f'{self.brand} {self.mark} load')
        time.sleep(1)


class Car(Auto):
    max_speed = 0

    def __init__(self, brand, mark, age_years, max_speed, colour='colour of vehicle was not specified',
                 weight='weight of vehicle was not specified'):
        super().__init__(brand, mark, age_years, colour, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'{self.brand} {self.mark} {self.age_years} y.o. max_speed is {self.max_speed} kph')


print('-'*50)
truck_1 = Truck('Scania', 'R_420', 17, 20000)
truck_1.move()
truck_1.stop()
truck_1.load()
truck_1.birthday()
print(truck_1.brand, truck_1.mark, ':', truck_1.colour)
print(truck_1.brand, truck_1.mark, ':', truck_1.weight)
print(truck_1.brand, truck_1.mark, truck_1.age_years, 'y. o.', 'max load', truck_1.max_load, 'kg')

print('-'*50)
truck_2 = Truck('Renault', 'Magnum', 8, 18000, colour='white', weight='7659')
truck_2.move()
truck_2.stop()
truck_2.load()
truck_2.birthday()
truck_2.birthday()
truck_2.birthday()
print(truck_2.brand, truck_2.mark, ':', truck_2.colour)
print(truck_2.brand, truck_2.mark, ':', truck_2.weight, 'kg')
print(truck_2.brand, truck_2.mark, truck_2.age_years, 'y.o.', 'max load', truck_2.max_load, 'kg')

print('-'*50)
car_1 = Car('Volvo', 'xc-90', 4, 185, colour='blue')
car_1.move()
car_1.birthday()
car_1.birthday()
car_1.birthday()
car_1.birthday()
car_1.stop()
print(car_1.brand, car_1.mark, ':', car_1.colour)
print(car_1.brand, car_1.mark, ':', car_1.weight)
print(car_1.brand, car_1.mark, car_1.age_years, 'y.o.', 'max speed', car_1.max_speed, 'kph')

print('-'*50)
car_2 = Car('Ford', 'Explorer', 2, 176, weight='2300')
car_2.move()
car_2.birthday()
car_2.birthday()
car_2.stop()
print(car_2.brand, car_2.mark, ':', car_2.colour)
print(car_2.brand, car_2.mark, ':', car_2.weight, 'kg')
print(car_2.brand, car_2.mark, car_2.age_years, 'y.o.', 'max speed', car_2.max_speed, 'kph')
