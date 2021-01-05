if __name__ == '__main__':

    import random

    my_list1 = []
    my_list2 = []
    i = 0
    while i < 10:
        my_list1.append(random.randint(1, 10))
        my_list2.append(random.randint(1, 10))
        i += 1
        my_list3 = (set(my_list1 + my_list2))

    print(my_list3)
