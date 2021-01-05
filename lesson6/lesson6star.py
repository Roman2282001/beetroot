if __name__ == '__main__':
    dict_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'

    }
    dict_week = {value: key for key, value in dict_week.items()}
    print(dict_week)
