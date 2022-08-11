# Умовою задачі не передбачено перевірку на коректність введення числа, тому її тут нема
number = int(input('Введіть ціле число: '))

# Спосіб 1
q = 0
result = 0
while number > q:
    q += 1
    if not q % 3 == 0:
        cube = q ** 3
        result += cube
print("Result is: ", result)

# Спосіб 2
result = 0
for item in range(1, number+1):
    if not item % 3 == 0:
        cube = item ** 3
        result += cube
print("Result_1 is: ", result)
