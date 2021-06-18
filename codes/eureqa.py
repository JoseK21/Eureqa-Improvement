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
            newConstant = truncate(np.random.uniform(-50, 50), 2)
            newChromosome.append(newConstant)
        
        pob_inicial.append(newChromosome)

    # print("🚀 ~ pob_inicial", pob_inicial)

    population = []

    current_population = pob_inicial.copy()

    best_individuals = [None, None]

    e_array = []

    for ind in current_population:
        [f, g, c1, c2, k1_f, k2_f, k1_g, k2_g] = ind # DESTRUCTING

        f_f = FUNCTIONS[f]
        f_g = FUNCTIONS[g]

        e_ = 0
        for x in range(1, 119): #  118
            h_x = H[x - 1]

            Va = f_f(x, k1_f, k2_f, c1) + f_g(x, k1_g, k2_g, c2)
            e = error(h_x, Va)
            e_ =+ e

        population.append(Individual(f, g, c1, c2, k1_f, k2_f, k1_g, k2_g, (e_/118) * 100))

    population.sort(key=lambda individuo: individuo.e, reverse=False)

    # for p in population:
    #     p.printInfo('x')
    #     print("\033[91m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

    best_individuals = population[0:2]

    print("\033[92m-.-.-.-.-.-.-.-.-.-.-.- Selección & Fitness Score -.-.-.-.-.-.-.-.-.-.-\033[0m")

    for bi in best_individuals:
        bi.printInfo('x')

    print("\033[92m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")


    print("\033[94m-.-.-.-.-.-.-.-.-.-.- CrossOver -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

    # CrossOver
    # [f, g, | c1, c2, k1_f, k2_f, k1_g, k2_g]

    ni = best_individuals.copy()
    new_children_by_crossover = []

    i1 = Individual(ni[0].f, ni[0].g, ni[1].c1, ni[1].c2, ni[1].k1_f, ni[1].k2_f, ni[1].k1_g, ni[1].k2_g)
    i2 = Individual(ni[1].f, ni[1].g, ni[0].c1, ni[0].c2, ni[0].k1_f, ni[0].k2_f, ni[0].k1_g, ni[0].k2_g)

    new_children_by_crossover.append(i1)
    new_children_by_crossover.append(i2)

    for ncbc in new_children_by_crossover:
        ncbc.printInfo('x')

    print("\033[94m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")


if __name__ == "__main__":
    main()
