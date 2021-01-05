if __name__ == '__main__':
    user_name = 'roman'
    while True:
        user_name2 = input('Введите имя: ')
        if user_name == user_name2.lower():
            print('Имена совпадают')
            break
        else:
            print('Имена не совпадают')
