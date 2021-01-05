if __name__ == '__main__':
    from random import randint, choice
trying = 0
while trying < 2:
    a, b, c = randint(1, 10), randint(1, 10), randint(1, 10)
    expression1, expression2 = choice(['+', '-', '*']), choice(['+', '-', '*'])
    if expression1 == '+' and expression2 == '-':
        result = a + b - c
    elif expression1 == '+' and expression2 == '+':
        result = a + b + c
    elif expression1 == '+' and expression2 == '*':
        result = a + b * c
    elif expression1 == '-' and expression2 == '+':
        result = a - b + c
    elif expression1 == '-' and expression2 == '-':
        result = a - b - c
    elif expression1 == '-' and expression2 == '*':
        result = a + b * c
    elif expression1 == '*' and expression2 == '+':
        result = a * b - c
    elif expression1 == '*' and expression2 == '-':
        result = a * b - c
    elif expression1 == '*' and expression2 == '*':
        result = a * b * c
    print(f'Какой будет ответ: {a} {expression1} {b} {expression2} {c}?')
    answer = int(input('Enter your answer: '))
    if answer == result:
        print("E!Right answer.There's still one!")
        trying += 1
    else:
        print('Your answer is wrong!')
        trying == 0
