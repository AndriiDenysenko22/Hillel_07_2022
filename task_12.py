from datetime import datetime


def do_smth(my_func):
    def the_wrapper():
        now = datetime.now()
        my_func()
        spend_time_1 = (datetime.now() - now)
        print('--'*50)
        print('spend_time:', spend_time_1)
        print('--' * 50)
    return the_wrapper


@do_smth
def first_function():
    a = 546664665646546546456464654654654646546456486432 ** 2500
    print('Переглядаючи урок 4, я повторив Ваш код. Але в мене інтерпретатор не виводить \n'
          'час виконання програми в мікросекундах в надто простих функціях.\n'
          'Або, якщо виводить, то якусь одну з п`яти і завжди різну. А у Вас на 4 уроці мікросекунди\n'
          'відображались без додаткових маніпуляцій з Вашого боку.\n'
          'В чому може бути причина? І як можна це виправити?')
    return a


@do_smth
def second_function():
    b = 653331 ** 1651657
    print('Наприклад, результат виконання коду з 4 уроку:\n'
          'spend_time_1: 0:00:00\n'
          'spend_time_2: 0:00:00\n'
          'spend_time_3: 0:00:00.000998\n'
          'spend_time_4: 0:00:00\n'
          'spend_time_5: 0:00:00')
    return b


first_function()
second_function()
