if __name__ == '__main__':
    from random import randint

    tries = int(input('How many tries: '))
    limit = int(input('How limit: '))
    max_value = 0
    value = 0
    t = 1
    while tries+1 != t:
        value = randint(1, limit)
        print("Random value", t, ':', value)
        if value > max_value:
            max_value = value
        else:
            pass
        t += 1
    print('Max value:', max_value)
