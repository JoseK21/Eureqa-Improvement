import random
import numpy as np

import math

def constant(_, _1, _2, c=0):
   return c

def poli4(x, _, _1, _2):
    p = np.poly1d([5, 4, 3, 2, 1]) # 5x4 + 4x3 + 3x2 + 2x + 1

    return p(x) 

def expo(x, k1=0, k2=0, _=None):
    # return k1 * np.exp(k2 * x) 

    return k1 * math.exp(k2 * x) 


def sin(x, k1=0, k2=0, _=None):
    return k1 * np.sin(k2 * x) 

def cos(x, k1=0, k2=0, _=None):
    return k1 * np.cos(k2 * x) 

# Fitness Function:
def error(Vreal, Vaprox):
    if(Vreal != 0):
        return abs(Vreal - Vaprox) / Vreal
    return 9999999

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)