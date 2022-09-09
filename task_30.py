class String(str):
    def __add__(self, other):
        x = str(self) + str(other)
        return String(x)

    def __sub__(self, other):
        other = str(other)
        if str(other) in self:
            first_variable = self
            second_variable = str(other)
            acdc = first_variable.split(second_variable, 1)
            answer = String(''.join(acdc))
            return answer
        elif not str(other) in self:
            answer = self
            return String(answer)


print(String('New') + String(890))
print(String(1234) + 5678+7)
print(String('New') + 'castle'+55+'aas'+True+None+[12, 'as', 35]+(12, 'asd', 43)-5-12)
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)
print(String('Old')+'school')

a = String('New bala7nce')
b = 7
print('Result:', a-b)

c = String('New balance')
d = 'bal'
print('Result:', c-d)

e = String('New balance')
f = 'Bal'
print('Result:', e-f)

g = String('pineapple apple pine')
h = 'apple'
print('Result:', g-h)

i = String('New balance')
j = 'apple'
print('Result:', i-j)

k = String('NoneType')
ll = None
print('Result:', k-ll)

m = String(55678345672)
n = 7
sd = m-n
print(sd)
print(sd-n-n+5-456+'as'+None+True-'t'-'u')
