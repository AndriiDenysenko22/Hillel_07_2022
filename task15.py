first_string = input('Enter first string: ')
second_string = input('Enter second string: ')
third_string = input('Enter third string: ')
fourth_string = input('Enter fourth string: ')

f = open('file_for_record.txt', 'w')
try:
    f.write(first_string + '\n' + second_string)
finally:
    f.close()

f = open('file_for_record.txt', 'a')
try:
    f.write('\n' + third_string + '\n' + fourth_string)
finally:
    f.close()
