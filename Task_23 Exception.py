class Calculator(object):
    def add(self, a, b):
        try:
            if a < 10 and b < 10:
                raise ValueError('Too easy for U')
            return a + b
        except ValueError as ve:
            print(ve)

    def subtract(self, a, b):  # тут я хочу повернути і результат і помилку
        try:
            if a < b:
                raise ValueError('Attention! The subtrahend is bigger than minuend')
            return a - b
        except ValueError as ve:
            print(ve)

        return a - b

    def multiply(self, a, b):
        try:
            if 0 < a < 10:
                raise ValueError('The number, which you are trying to multiply too short')
            return a * b
        except ValueError as ve:
            print(ve)

    def divide(self, a, b):
        try:
            if b != 0:
                pass
            return a / b
        except ZeroDivisionError as err:
            print(err)

    def square_root(self, a):
        try:
            if a < 0:
                raise ValueError('you are trying to find square root from negative')
            return a ** 0.5
        except ValueError as ve:
            print(ve)

    def exponentiation(self, a, b):
        try:
            if b < 0:
                raise ValueError('you trying to exponent in negative')
            return a ** b
        except ValueError as ve:
            print(ve)



# create a calculator object
my_cl = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Square root")
    print("6: Exponentiation")
    print("7: Exit")

    ch = int(input("Select operation: "))

    # Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 6, 7):

        # first check whether user want to exit
        if (ch == 7):
            break

        # If not then ask fo the input and call appropiate methods
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if (ch == 1):
            if a < 10 and b < 10:
                my_cl.add(a, b)
            else:
                print(a, "+", b, "=", my_cl.add(a, b))
        elif (ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif (ch == 3):
            if not 0 < a < 10:
                print(a, "*", b, "=", my_cl.multiply(a, b))
            else:
                my_cl.multiply(a, b)
        elif (ch == 4):
            if b != 0:
                print(a, "/", b, "=",  my_cl.divide(a, b))
            else:
                my_cl.divide(a, b)
        # elif (ch == 5):
        #     print('square_root of', a, "=", my_cl.square_root(a))
        elif (ch == 6):
            if b >= 0:
                print(a, "**", b, "=", my_cl.exponentiation(a, b))
            else:
                my_cl.exponentiation(a, b)

    elif (ch == 5):
        a = int(input("Enter first number: "))
        if a >= 0:
            print('square_root of', a, "=", my_cl.square_root(a))
        else:
            my_cl.square_root(a)

    else:
        print("Invalid Input")
