a1 = 2602
a2 = 2602
a3 = 2602
b1 = 2203
b2 = '2203'

'''#а можна ще так?:
b1 = 2203
b2 = 2200
b2+=3'''

print('TASK1')

print('id(a1)', id(a1))
print('id(a2)', id(a2))
print('id(a3)', id(a3))

print('перевірка a1 == a2 == a3:', a1 == a2 == a3)
print('перевірка a1 is a2 is a3:', a1 is a2 is a3)

a1 = float(a1)
a2 = int(a2)  # якщо клас змінної був спочатку int, то можна також змінити його на bool?
a3 = str(a3)

print('новий id(a1):', id(a1))
print('id(a2):      ', id(a2))
print('новий id(a3):', id(a3))
print('Таким чином:', a1, ',', a2, ',', a3)

print('TASK2')

print(b1)
print(b2)
print(id(b1))
print(id(b2))
# приводимо b1 i b2 одного типу даних:
b1 = bool(b1)
b2 = bool(b2)
print('b1 =', b1)
print('b2 =', b2)
print('id(b1):', id(b1))
print('id(b1):', id(b2))
