if __name__ == '__main__':

    while True:
        number = input('Enter your number: ')
        if number.isnumeric():
            if len(number) > 10:
                print('Your number is too long!')
            elif len(number) < 10:
                print('Your number is too short!')
            else:
                print('Your number is correct!')
                break
        else:
            print('The number contains not only numbers!')


    while True:
        phone_number = input('Введите ваш номер: ')
        if phone_number.isdigit() and len(phone_number) == 10:
            print('Ваш номер введен корректно!')
            break
        else:
            print('Попробуйте еще раз!')


