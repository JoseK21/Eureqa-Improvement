from functions import * 

METHOD_DICTIONARY = {
    1: [constant, constant], 2:[constant, poli4], 3: [constant, euler], 4: [constant, sin], 5: [constant, cos],
    6: [poli4, constant], 7:[poli4, poli4], 8: [poli4, euler], 9: [poli4, sin], 10: [poli4, cos],
    11: [euler, constant], 12:[euler, poli4], 13: [euler, euler], 14: [euler, sin], 15: [euler, cos],
    16: [sin, constant], 17:[sin, poli4], 18: [sin, euler], 19: [sin, sin], 20: [sin, cos],
    21: [cos, constant], 22:[cos, poli4], 23: [cos, euler], 24: [cos, sin], 25: [cos, cos],
}

X_VALUES = range(1, 118)