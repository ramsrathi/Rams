word_dict = {word.strip('\r\n'): None for word in open('words.txt')}


def find_rev_pairs():
    for word in word_dict:
        if word[::-1] in word_dict:
            print (word, word[::-1])

find_rev_pairs()
