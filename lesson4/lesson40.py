if __name__ == '__main__':
    import random

    # Игра в угадайку.

    answer = random.randint(1, 50)
    print('Давай сыграем в угадайку!')
    print('О каком числе я думаю?\nВведи число: ')
    while True:
        guess = int(input())
        if guess < answer:
            print('Немного выше')
        elif guess > answer:
            print('Немного ниже')
        else:
            print('Ты победил!')
            break