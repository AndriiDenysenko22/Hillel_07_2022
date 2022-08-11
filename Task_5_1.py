while True:
    age = input('Будь-ласка, введіть Ваш вік: ')
    name = input('Будь-ласка, введіть Ваше ім`я: ')
    if not age.isdigit() or int(age) <= 0:
        print('Помилка, повторіть введення')
    elif int(age) < 10:
        print('Привіт, шкет', name)
    elif int(age) < 18:
        print('Як життя', name, '?')
    elif int(age) < 100:
        print('Що бажаєте', name, '?')
    else:
        print(name+', Ви брешете - в наш час скільки не живуть...')
    answer = input('Бажаєте вийти? (y/д): ')
    if answer in ('Y', 'y', 'Д', 'д'):
        break
