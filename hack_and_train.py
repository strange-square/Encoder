import string
from collections import defaultdict
from caesar import caesar_encode, caesar_decode


alphabet_size = 26


def analyse(text):
    model_dict = defaultdict(int)

    num_alpha = 0

    for i in text:
        if i.isalpha():
            num_alpha += 1
            model_dict[i.lower()] += 1

    for i in string.ascii_lowercase:
        model_dict[i] = model_dict[i] / num_alpha

    return dict(model_dict)


def caesar_hack(text, model_dict):

    min_sum = alphabet_size
    best_text = text

    for i in range(alphabet_size):
        temp_text = caesar_decode(i, text)
        text_dict = analyse(temp_text)
        sum = 0

        for k in string.ascii_lowercase:
            sum += abs(model_dict[k] - text_dict[k])

        if sum < min_sum:
            best_text, min_sum = temp_text, sum

    return best_text