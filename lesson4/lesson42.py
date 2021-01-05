if __name__ == '__main__':
    import random

    # Задание 1.

    start, end = 0, 10
    number = random.randint(start, end)
    guess = input('Guess what number I wished for: ')
    if number == str(guess):
        print('You guessed it')
    else:
        print(f"You don't guess it.This number is: {number}")