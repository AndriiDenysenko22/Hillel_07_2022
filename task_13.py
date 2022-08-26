def digitis(a):
    for item in a:
        if item not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.', ',']:
            print('You`ve not entered a number', a)
            break
        dash = a.count('-')
        if dash > 1:
            print('You`ve not entered a number', a)
            break
        if '-' not in a[0]:
            if item in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']:
                continue
            else:
                print('You`ve not entered a number', a)
                break


def flo_at_2(a):
    test = a.replace(',', '').replace('.', '').replace('-', '')
    if test.isdigit():
        point = a.count('.')
        comma = a.count(',')
        if comma == 1 and point == 0:
            for item in a:
                if item == ',':
                    b = a.replace(item, '.')
                    if a[0] == '-' and '-' not in a[1:]:
                        fl_a = float(b)
                        print('Congrats! You`ve entered a negative float number:', fl_a)
                    elif a[0] != '-' and '-' not in a[1:]:
                        fl_a = float(b)
                        if fl_a != 0:
                            print('Congrats! You`ve entered a float number:', fl_a)
                        elif fl_a == 0:
                            print('Congrats! You`ve entered a float zero:', fl_a)
                            break
        if point == 1 and comma == 0:
            if a[0] == '-' and '-' not in a[1:]:
                fl_a = float(a)
                if fl_a < 0:
                    print('Congrats! You`ve entered a negative float number:', fl_a)
                elif fl_a == 0:
                    print('Congrats! You`ve entered a float zero with dash:', fl_a)
            elif a[0] != '-' and '-' not in a[1:]:
                fl_a = float(a)
                if fl_a != 0:
                    print('Congrats! You`ve entered a float number:', fl_a)
                elif fl_a == 0:
                    print('Congrats! You`ve entered a float zero:', fl_a)
        elif point + comma > 1:
            print('You`ve not entered a number')


def in_te_ger(a):
    for item in a:
        if item not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']:
            break
        else:
            if a[0] == '-' and a[1:].isdigit():
                neg_int = int(a)
                if neg_int < 0:
                    print('Congrats! You`ve entered a negative integer:', neg_int)
                    break
                if neg_int == 0:
                    print('You`ve entered a zero with dash')
                    break
            if a != '0' and a.isdigit():
                pos_int = int(a)
                print('Congrats! You`ve entered an integer:', pos_int)
                break
            elif a == '0':
                z_int = int(a)
                if z_int == 0:
                    print('Congrats! You`ve entered a zero:', z_int)


def go_out(a):
    if a.lower() in ('вихід', 'exit', 'quit', 'e', 'q'):
        quit()


while True:
    print('-' * 50)
    inpt = input('Enter your number, please\n'
                 '(for quit press q or e or enter "exit" or "вихід"): ')
    go_out(inpt)
    digitis(inpt)
    flo_at_2(inpt)
    in_te_ger(inpt)
    continue
