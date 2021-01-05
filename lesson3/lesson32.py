if __name__ == '__main__':
    import random

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.choice(['+', '-', '*'])

    a, b = (b, a) if a < b else (a, b)

    print(f'Какой результат {a}{c}{b}?: ')

    i = int(input('Ваш ответ: '))
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b

    if i == d:
        print('Hi')
    else:
        print('Нужно учить действия!')


