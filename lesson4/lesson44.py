if __name__ == '__main__':

    # Задание со звездочкой.

    limit = int(input('Set your limit: '))
    number = 0
    while limit != number:
        if (number == 0 or number % 18 != 0) and number != 42 \
                and number < 50 or number > 80:
            print(number)
        elif number == 42:
            print('Because')
        else:
            pass
        number += 1
