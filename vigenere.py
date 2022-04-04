from math import ceil


import string


alphabet_low = string.ascii_lowercase
alphabet_up = string.ascii_uppercase
alphabet_size = len(alphabet_low)


def vigenere_encode(key, text):
    res = []
    key = key * ceil(len(text) / len(key))
    key_up = key.upper()

    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():

            new_num = alphabet_low.find(text[i]) + alphabet_low.find(key[i])
            res.append(alphabet_low[new_num % alphabet_size])

        elif text[i].isalpha() and text[i].isupper():

            new_num = alphabet_up.find(text[i]) + alphabet_up.find(key_up[i])
            res.append(alphabet_up[new_num % alphabet_size])

        else:
            res.append(text[i])

    return ''.join(res)


def vigenere_decode(key, text):
    new_key = []

    for i in key:
        new_num = (alphabet_size - alphabet_low.find(i))
        new_key.append(alphabet_low[new_num])

    return vigenere_encode(''.join(new_key), text)