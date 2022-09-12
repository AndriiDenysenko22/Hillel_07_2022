from datetime import date


class Auto(object):
    owner = 'Vitalii'
    brand = 'brand_name'
    age_years = 0
    mark = 'car`s mark'
    colour = 'colour of vehicle was not specified'
    weight = 'weight of vehicle was not specified'

    def __init__(self, brand, mark, age_years, owner='Vitalii', colour='colour of vehicle was not specified',
                 weight='weight of vehicle was not specified'):
        self.brand = brand
        self.age_years = age_years
        self.mark = mark
        self.owner = owner
        self.colour = colour
        self.weight = weight

    def move(self):
        print(f'{self.brand} {self.mark} {self.age_years} y.o.', 'move')

    def stop(self):
        print(f'{self.brand} {self.mark} {self.age_years} y.o.', 'stop')

    @property
    def full_name(self):
        return self.brand + ' ' + self.mark

    @staticmethod
    def light(weight):
        return weight < 3500

    @staticmethod
    def is_new(age_years):
        return age_years < 1

    @classmethod
    def from_year_of_make(cls, brand, mark, year):
        return cls(brand, mark,  date.today().year - year)

    @classmethod
    def sell_car(cls, brand, mark, age_years):
        print(Auto.owner, 'has sold', brand, mark, age_years, 'y.o.')


auto_1 = Auto('Honda', 'Civic', 0, weight='1400')

# testing age of the car
if Auto.is_new(0):
    print(f'{auto_1.full_name} is new car')
else:
    print(f'{auto_1.full_name} is used car')

# testing weight of the car
if Auto.light(1400):
    print(f'{auto_1.full_name} is a light car')
else:
    print(f'{auto_1.full_name} is heavy car')

auto_2 = Auto('Audi', 'A5', 3, colour='yellow', weight='1700')

# testing age of the car
if Auto.is_new(3):
    print(f'{auto_2.full_name} is new')
else:
    print(f'{auto_2.full_name} is used car')

# testing weight of the car
if Auto.light(1700):
    print(f'{auto_2.full_name} is a light car')
else:
    print(f'{auto_2.full_name} is heavy car')

# Vitalii get`s a heritage. He is testing age of the car:
auto_3 = Auto.from_year_of_make('Toyota', 'Highlander', 2007)
print(f'{auto_3.full_name} {auto_3.age_years} y.o.')

# Vitalii needs money
auto_3 = Auto.sell_car(auto_3.brand, auto_3.mark, auto_3.age_years)
# auto_3 is no more
