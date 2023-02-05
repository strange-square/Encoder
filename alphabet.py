import string


alphabet_low = string.ascii_lowercase
alphabet_up = string.ascii_uppercase
alphabet_size = len(alphabet_low)
nums = [i for i in range(alphabet_size)]

alphabet_low_dict = dict(zip(alphabet_low, nums))
alphabet_up_dict = dict(zip(alphabet_up, nums))
