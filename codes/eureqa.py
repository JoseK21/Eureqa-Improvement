from constants import *
from functions import *

from classes import *

import random
import numpy as np

from matplotlib import pyplot as plt

def main():
    ee = 9999999

    pob_inicial = []
    for p in range(POPULATION):
        chomosome = np.random.randint(5, size=2)
        newChromosome = []
        for c in range(2):
            newChromosome.append(chomosome[c])

        for k in range(6):
            newConstant = truncate(np.random.uniform(-5, 5), 5)
            newChromosome.append(newConstant)
        
        pob_inicial.append(newChromosome)

    # print("🚀 ~ pob_inicial", pob_inicial)

    population = []

    current_population = pob_inicial.copy()

    best_individuals = [None, None]

    e_array = []

    for ind in current_population[0:1]:
        [f, g, c1, c2, k1_f, k2_f, k1_g, k2_g] = ind # DESTRUCTING

        f_f = FUNCTIONS[f]
        f_g = FUNCTIONS[g]

        e_ = 0
        for x in range(1, 119): #  118
            h_x = H[x - 1]

            Va = truncate(f_f(x, k1_f, k2_f, c1) + f_g(x, k1_g, k2_g, c2), 5)
            e = error(h_x, Va)

            print("🚀 {0} ~ e: {1}".format(x, e))

            e_ =+ e
            # if(len(population) > POPULATION + 1):
            #     population[POPULATION] = Individual(x, Va, e, c1, c2, f, g, k1_f, k2_f, k1_g, k2_g)
            #     population.sort(key=lambda individuo: individuo.e, reverse=False)
            #     population.pop()
            #     population.pop()
            # else:
            #     population.append(Individual(x, Va, e, c1, c2, f, g, k1_f, k2_f, k1_g, k2_g))
        
        population.append(Individual('x', 0, 0, c1, c2, f, g, k1_f, k2_f, k1_g, k2_g))
        e_array.append(e_/118)
        # print(e_/118)

    # best_individuals = [population[0], population[1]]


    for p in population:
        p.printInfo()

    for a in e_array:
        print(a)

    # print("\033[92m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

    # for bi in best_individuals:
    #     # print(bi.e)
    #     bi.printInfo()

    # print("\033[92m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")


if __name__ == "__main__":
    main()



# plt.plot(range(118), h_x)
# plt.show()