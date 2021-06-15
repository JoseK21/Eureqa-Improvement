from constants import *
from classes import *

def main():
    k1_f = 10
    k2_f = 5

    k1_g = 7
    k2_g = 3

    c = 50 # Const

    ee = 9999999

    test_x = 2

    individual = Individual()

    for x in range(1, len(METHOD_DICTIONARY.keys())):
        method = METHOD_DICTIONARY[x]
        Va = method[0](test_x, k1_f, k2_f, c) + method[1](test_x, k1_g, k2_g, c)
        e = error(TABLE[test_x], Va)
        if(e < ee):
            individual._update(test_x, Va, e, method[0], method[1], k1_f, k2_f, k1_g, k2_g)
            ee = e
        
    individual.printInfo()

if __name__ == "__main__":
    main()
