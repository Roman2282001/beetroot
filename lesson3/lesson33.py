if __name__ == '__main__':

    word = input('Enter your word: ')
    if word.lower() != word[::-1]:
        print("It's not palindrome")
    else:
        print("It's palindrome")
