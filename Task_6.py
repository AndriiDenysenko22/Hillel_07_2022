""" Я спробував зробити декілька функцій в цілях навчання. Я розумію, що ці
функції можна об`єднати в одну або дві. Як на Вашу думку краще?
Також питання щодо того, де ще можна використати функції. Можливо, можна ще щось покращити? """


def try_to_guess_bigger():
    if (int(user_value) - computer_mind) >= 10:
        print('Ви ввели надто велике число')
    elif 10 > (int(user_value) - computer_mind) > 3:
        print('Потрібно ввести трішки менше число...')
    elif 3 >= (int(user_value) - computer_mind) > 0:
        print('Потрібно ще трохи зменшити число...')


def try_to_guess_smaller():
    if (int(user_value) - computer_mind) <= -10:
        print('Ви ввели надто маленьке число')
    elif -10 < (int(user_value) - computer_mind) < -3:
        print('Потрібно ввести трішки більше число...')
    elif -3 <= (int(user_value) - computer_mind) < 0:
        print('Введіть трішечки більше число...')


def try_to_guess_equals():
    if (int(user_value) - computer_mind) == 0:
        print('Вітаємо! Русскіє втекли додому.')


def if_func():
    if (int(user_value) - computer_mind) != 0:
        try_to_guess_bigger()
        try_to_guess_smaller()
        print('-'*50)


user_mind = int(input('Введіть, будь-ласка число (наприклад, від 30 до 70):'))
"""Я взяв для прикладу такий діапазон, перевірку не робив
щоб код не був надто довгий"""
computer_mind = (user_mind + 23)  # для того, щоб було складніше вгадувати


while True:
    user_value = input('Спробуйте вгадати число в діапазоні від 1 до 99 (включно): ')
    if_func()
    if (int(user_value) - computer_mind) == 0:  # Чи можна тут створити функцію?
        try_to_guess_equals()
        break  # Коли я спробував, мені видало помилку break outside the loop. Я так розумію, що ні.
