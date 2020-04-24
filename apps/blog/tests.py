from django.test import TestCase


# Create your tests here.

def firstUniqChar(word):
    alpha_dict = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
    for i, s in enumerate(word):
        if alpha_dict[s] == -1:
            alpha_dict[s] = i
        elif alpha_dict[s] != -1:
            alpha_dict[s] = -2
    try:
        min_index = min([value for value in alpha_dict.values() if value != -1 and value != -2])
    except:
        min_index = -1
    return min_index


index = firstUniqChar("javajava")
print(index)
