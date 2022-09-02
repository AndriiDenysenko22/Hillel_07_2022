import json
from random import randint
i = 0
academic_performance_book = {}
while i < 6:
    name = input('Please, enter student`s name: ')
    age = int(input('Please, enter student`s age: '))
    student = (name, age)
    stud_id = randint(100000, 999999)
    academic_performance_book[stud_id] = student
    print(academic_performance_book)
    i += 1

with open('task_16.json', 'w') as file:
    json.dump(academic_performance_book, file)
