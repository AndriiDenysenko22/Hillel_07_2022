# Умовою задачі не передбачено перевірку на коректність введення числа, тому її тут нема
c = int(input('Введіть ціле число: '))

# Спосіб 1
q = 0
result = 0
while c > q:
    q += 1
    if not q % 3 == 0:
        a = q ** 3
        result += a

print('Result is: ', result)

# Спосіб 2
result_1 = 0
for item in range(0, c+1):
    if not item % 3 == 0:
        b = item ** 3
        result_1 += b
print('Result_1 is: ', result_1)
