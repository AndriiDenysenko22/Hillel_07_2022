values = [1, 2, '3', 'forth', 'end', 99, True, None]

lst22 = list(map(lambda symbol: str(symbol) if type(symbol) == int else symbol, values))

print(lst22)
print('--'*50)
for i in lst22:
    print(type(i))
