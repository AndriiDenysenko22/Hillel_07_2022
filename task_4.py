#Код буде відкидати спеціальні символи, розділові знаки та цифри автоматично
a = input('Введіть речення, яке складається з двох слів (бажано без розділових знаків цифр та спеціальних символів): ')

symbols = '''!()-[]{};:/@#$%^'"\,.&*_~1234567890+='''

for i in a:
    if i in symbols:
        a = a.replace(i, "")

length = len(a.split())

if length == 2:
    var = a.split()[0]
    var1 = a.split()[1]
    # змінюємо порядок слів:
    new_var1 = var1.upper()
    new_var = var.lower().title()
    new_string_1 = f'!{new_var1} {new_var}?'
    new_string_2 = '!{} {}?'.format(new_var1, new_var)
    new_string_3 = '!{0} {1}?'.format(new_var1, new_var)

    my_file = open('py.txt', 'w')

    print(a, new_var, new_var1, new_string_1, new_string_2, new_string_3, sep="\n <<<>>> \n", file=my_file)
    my_file.close()

elif length < 2:
    print('Потрібно було ввести ще одне слово')
else:
    print('Ви ввели надто багато слів')
