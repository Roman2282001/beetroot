if __name__ == '__main__':
    def make_operations(operators, first_value, *args):
        if operators in ('+', '-', '*'):
            for number in args:
                if operators == '+':
                    first_value += number
                elif operators == '-':
                    first_value -= number
                elif operators == '*':
                    first_value *= number
        else:
            print('Your operators is wrong!')

            return first_value

    make_operations('+', 6, 7, 8)
    make_operations('-', 50, 20, 9)
    make_operations('*', 1, 3, 7)

