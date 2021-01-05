if __name__ == '__main__':
    import random

    my_list1 = []
    my_list2 = []
    i = 0
    while i < 100:
        i += 1
        my_list1.append(i)
        if i % 7 == 0 and i % 5 != 0:
            my_list2.append(i)
    print(my_list1)
    print(my_list2)
