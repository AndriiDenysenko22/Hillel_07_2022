# Это умножение на какое-то заданное число, к примеру, геометрическая прогрессия на 3 от единицы:
# 1, 3, 9, 27, 81... и т.д.

def geo_progression(i):
    for value in range(i):
        yield 3**value
        value += 1


listic = []
for item in geo_progres(5):
    listic.append(item)
listic.append('.... и т.д.')
print(listic)
