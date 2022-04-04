import string


alphabet_low = string.ascii_lowercase
alphabet_up = string.ascii_uppercase
alphabet_size = len(alphabet_low)


def caesar_encode(key, text):
    res = []

    for i in text:
        if i.isalpha() and i.islower():

            new_num = alphabet_low[(
                alphabet_low.find(i) + key) % alphabet_size]
            res.append(new_num)

        elif i.isalpha() and i.isupper():

            new_num = alphabet_up[(alphabet_up.find(i) + key) % alphabet_size]
            res.append(new_num)

        else:
            res.append(i)

    return ''.join(res)


def caesar_decode(key, text):
    return caesar_encode(-key, text)