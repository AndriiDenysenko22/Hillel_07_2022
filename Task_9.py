# Це все, чи потрібно було ще щось доробити?
old_dict = {'asd': 321, 'hoho': 3192, 'hist': 42}
new_dict = {value: key for key, value in old_dict.items()}

print(old_dict)
print(new_dict)
