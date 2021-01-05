def oops():
    my_list = [1, 2, 3, 4, 5]
    my_list[6]
    return my_list


if __name__ == '__main__':
    def fix_error():
        try:
            oops()
        except IndexError as err:
            print('Impossible expression,', err, '!')


    fix_error()
