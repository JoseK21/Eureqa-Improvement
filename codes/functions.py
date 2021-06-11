import random
import numpy as np

def constant(_):
   return random.uniform(0, 175)

def poli4(x):
    p = np.poly1d([2, 3, 2, -1])

    return p(x) 

def euler(x):
    k1 = random.uniform(0, 50)
    k2 = random.uniform(0, 50)

    return k1 * np.exp(k2 * x) 

def sin(x):
    k1 = random.uniform(0, 50)
    k2 = random.uniform(0, 50)

    return k1 * np.sin(k2 * x) 

def cos(x):
    k1 = random.uniform(0, 50)
    k2 = random.uniform(0, 50)

    return k1 * np.cos(k2 * x) 
