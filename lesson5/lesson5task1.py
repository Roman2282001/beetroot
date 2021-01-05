if __name__ == '__main__':

    import random

    my_list = []
    i = 0
    while i < 10:
        a = random.randint(1, 10)
        my_list.append(a)

        i += 1
print(my_list)
print(max(my_list))
