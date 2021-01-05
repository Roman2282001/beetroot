if __name__ == '__main__':
    def take_numbers():
        try:
            f_number = int(input('Enter first number: '))
            s_number = int(input('Enter second number: '))
            expression = (f_number * f_number) / s_number
        except ZeroDivisionError as err:
            print('Division by zero occurred in the expression,', err, '!')
        except ValueError as err:
            print('Only numbers,', err, '!')
        else:
            return expression

    print(take_numbers())


