def geo_progres(value):
    while value > 1:
        value -= 1
        yield value**2


listic = []
for item in geo_progres(25):
    listic.append(item)

print('Geometric progression:', listic[::-1])
