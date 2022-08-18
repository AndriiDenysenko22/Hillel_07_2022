from random import randint
lst = [randint(-2, 2) for i in range(10)]  # діапазон такий вузький, щоб було більше повторів
print('Випадковий список: ', lst)
print('-' * 50)


def count_items():
    new_dict = {i: lst.count(i) for i in lst}
    print('Кількість повторів чисел у словнику: ', new_dict)
    print('-' * 50)
    b = [key for key in new_dict]
    print('Перелік ключів у словнику: ', sorted(b))
    print('-' * 50)
    print('Кількість цифр 0 у словнику: ', new_dict.get(0))  # наприклад перевіримо кількість цифр 0 у словнику


count_items()
