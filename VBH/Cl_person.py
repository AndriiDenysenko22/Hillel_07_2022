import datetime

class Person(object):

    def get_list(first_name, sex, date_of_birth, last_name='', patronomic='', date_of_death=''):
        while True:
            first_name = input('Enter a person`s first_name')
            if first_name.isalpha():
                break
            else:
                print('Please use only letters for entering name.')
                continue
        while True:
            sex = input('Enter a person`s sex (male/female)')
            if sex == 'male' or sex == 'female':
                break
            else:
                print('Please type male or female')
                continue
        while True:
            date_entry = input('Enter a person`s date_of_birth in DD-MM-YYYY format')
            for item in date_entry:
                if item in ['/', ' ', '-']:
                    date_1 = date_entry.replace(item, '.')
                    (day, month, year) = map(int, date_1.split('.'))
                elif item in ['.']:
                    date_1 = date_entry
            (day, month, year) = map(int, date_1.split('.'))
            date_2 = datetime.date(year, month, day)
            date_of_birth = date_2.strftime('%d.%m.%Y')
            break

        while True:
            last_name = input('Enter a person`s last_name')
            if last_name.isalpha():
                break
            else:
                print('Please use only letters for entering  lastname.')
                continue
        while True:
            patronomic = input('Enter a person`s patronomic')
            if patronomic.isalpha():
                break
            else:
                print('Please use only letters for entering  patronomic.')
                continue

        while True:
            date_entry2 = input('Enter a person`s date_of_death in DD-MM-YYYY format')
            if date_entry2 == '':
                date_of_death = ''
                break
            else:
                for item in date_entry2:
                    if item in ['/', ' ', '-']:
                        date_3 = date_entry2.replace(item, '.')
                        (day, month, year) = map(int, date_3.split('.'))
                    elif item in ['.']:
                        date_3 = date_entry2
                (day, month, year) = map(int, date_3.split('.'))
                date_4 = datetime.date(year, month, day)
                date_of_death = date_4.strftime('%d.%m.%Y')
                break


        # date_of_death = input('Enter a person`s date_of_death')
        print(first_name, last_name, patronomic, sex, date_of_birth, date_of_death)
        return (first_name, last_name, patronomic, sex, date_of_birth, date_of_death)

    if __name__ == "__main__":
       get_list('first_name', 'sex', 'date_of_birth')

