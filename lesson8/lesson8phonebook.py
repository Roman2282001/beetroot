def create_new_contact():
    return {
        'name': input('Enter your first name: '),
        'surname': input('Enter your surname: '),
        'city': input('Enter your city: '),
        'state': input('Enter your state: '),
        'telephone number': input('Enter your telephone number: '),
    }


def find_by_name():
    name = input('Enter the first name you want to find: ').lower()
    if name in phone_book:
        return name
    else:
        print('This first name is not in the phone book!')


def find_by_surname():
    name = input('Enter the last name you want to find: ').lower()
    if name in phone_book:
        return name
    else:
        print('This last name is not in the phone book!')


def find_by_fullname():
    name = input('Enter the fullname (name and surname) you want to find: ').lower()
    if name in phone_book:
        return name
    else:
        print('This fullname is not in the phone book!')


if __name__ == '__main__':

    phone_book = []

    while True:
        choice_action = input('Enter what you want to do?\n '
                              'Enter cn = create new contact,\n'
                              'Enter n = Search by name,\n'
                              'Enter sn = Search by surname, \n'
                              'Enter fn = Search by fullname, \n'
                              'Enter phone = Search by telephone number, \n'
                              'Enter c = Search by city, \n'
                              'Enter s = Search by state, \n'
                              'Enter del = Delete a record for a given telephone number, \n'
                              'Enter upd = Update a record for a given telephone number, \n'
                              'Enter q = Exit the program.\n'
                              'Input something: ')
        if choice_action == 'cn':
            new_c = create_new_contact()
            phone_book.append(new_c)
        elif choice_action == 'q':
            break
        elif choice_action == 'name':
            find_by_name()
        elif choice_action == 'sn':
            find_by_surname()
        elif choice_action == 'fn':
            find_by_fullname()

    print(phone_book)
