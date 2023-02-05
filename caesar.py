from alphabet import alphabet_low, alphabet_up, alphabet_size
from alphabet import alphabet_low_dict, alphabet_up_dict


def caesar_encode(key, text):
    res = []

    for i in text:
        if i.isalpha() and i.islower():
            new_num = alphabet_low[(
                alphabet_low_dict[i] + key) % alphabet_size]
            res.append(new_num)

        elif i.isalpha() and i.isupper():
            new_num = alphabet_up[(alphabet_up_dict[i] + key) % alphabet_size]
            res.append(new_num)

        else:
            res.append(i)

    return ''.join(res)


def caesar_decode(key, text):
    return caesar_encode(-key, text)
