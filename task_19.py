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


auto_1 = Auto('Honda', 'Civic', 2)
auto_2 = Auto('Audi', 'A5', 3, colour='yellow', weight='1700')
print(auto_1)  # shows object_1
print(auto_2)  # shows object_2
auto_1.move()
auto_2.move()
auto_1.birthday()
auto_1.birthday()
auto_2.birthday()
auto_1.stop()
auto_2.stop()
print('Default colour of Honda:', auto_1.colour)
print('Default weight of Honda:', auto_1.weight)
auto_1.colour = 'green'
auto_1.weight = '1570'
print('Colour of Honda, that was specified by User:', auto_1.colour)
print('Weight of Honda, that was specified by User:', auto_1.weight)
