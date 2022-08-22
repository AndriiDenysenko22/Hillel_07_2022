inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

print('Дано список слів', inputdata)

this_is_palindrome = list(filter(lambda item: item.lower() == item.lower()[::-1], inputdata))

print('З них паліндроми:', this_is_palindrome)
