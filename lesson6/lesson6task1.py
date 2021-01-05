if __name__ == '__main__':
    import string

    split_sentence = input('Enter your sentence: ').lower()

    for i in string.punctuation:
        split_sentence = split_sentence.replace(i, ' ')

    split_sentence = split_sentence.split(" ")
    my_dict = {}
    for word in set(split_sentence):
        my_dict[word] = split_sentence.count(word)
    print(my_dict)
