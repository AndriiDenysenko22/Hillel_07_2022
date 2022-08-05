a1 = 'my_name_is_Andrii'
a2 = 'my_name_is_Andrii'
a3 = 'my_name_is_Andrii'

print('TASK1')

print('перевірка a1 == a2 == a3:', a1 == a2 == a3)
print('перевірка a1 is a2 is a3:', a1 is a2 is a3)

print('id(a1)', id(a1))
print('id(a2)', id(a2))
print('id(a3)', id(a3))

a1 = list(a1)
a2 = list(a2)
a3 = list(a3)

print('новий id(a1):', id(a1))
print('новий id(a2):', id(a2))
print('новий id(a3):', id(a3))
print('Таким чином:', '\n', a1, '\n', a2, '\n', a3)

print('TASK2')

b1 = ['True']
b2 = ['True']
print(b1)
print(b2)
print(id(b1))
print(id(b2))
b1 = bool(b1)
b2 = bool(b2)
print(id(b1))
print(id(b2))

print(b1)
print(b2)
