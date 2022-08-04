a1 = (2602, 2203)
a2 = (2602, 2203)
a3 = (2602, 2203)
b1 = (7, 8)
b2 = [7, 8]

'''#а можна ще було так?:
b1 = 2203
b2 = 2200
b2+=3'''

print('TASK1')

print('id(a1)', id(a1))
print('id(a2)', id(a2))
print('id(a3)', id(a3))

print('перевірка a1 == a2 == a3:', a1 == a2 == a3)
print('перевірка a1 is a2 is a3:', a1 is a2 is a3)

a1 = tuple(a1)
a2 = list(a2)
a3 = set(a3)

print('новий id(a1):', id(a1))
print('новий id(a2):', id(a2))
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
