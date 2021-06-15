import random
import numpy as np

def constant(_, _1, _2, c=0):
   return c

def poli4(x, _, _1, _2):
    p = np.poly1d([2, 3, 2, -1])
    return p(x) 

def expo(x, k1=0, k2=0, _=None):
    return k1 * np.exp(k2 * x) 

def sin(x, k1=0, k2=0, _=None):
    return k1 * np.sin(k2 * x) 

def cos(x, k1=0, k2=0, _=None):
    return k1 * np.cos(k2 * x) 

def error(Vreal, Vaprox):
    return abs(Vreal - Vaprox) / Vreal