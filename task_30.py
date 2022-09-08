class String(str):

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        x = str(self.x) + str(other)
        return str(x)

    def __sub__(self, other):
        self.x = str(self.x)
        other = str(other)

        if str(other) in str(self.x):
            print('-'*50)
            print('It`s inside')
            print('1:', self.x)
            print('2:', other)
            first_variable = str(self.x)
            second_variable = str(other)
            acdc = first_variable.split(second_variable, 1)
            answer = ''.join(acdc)
            return answer

        elif not str(other) in str(self.x):
            print('-' * 50)
            print('Not inside')
            print('1:', self.x)
            print('2:', other)
            answer = self.x
            return answer


print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
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
print('Result:', m-n)
