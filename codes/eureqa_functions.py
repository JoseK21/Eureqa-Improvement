import numpy as np
from functions import truncate
from classes import *


def generateInitialPopulation(POPULATION):
    pob_inicial = []

    for p in range(POPULATION):
        chomosome = np.random.randint(5, size=2)
        newChromosome = []
        for c in range(2):
            newChromosome.append(chomosome[c])

        for k in range(6):
            newConstant = truncate(np.random.uniform(-50, 50), 2)
            newChromosome.append(newConstant)
        
        pob_inicial.append(Individual(newChromosome[0], newChromosome[1], newChromosome[2], newChromosome[3], newChromosome[4], newChromosome[5], newChromosome[6], newChromosome[7]))

    return pob_inicial

def formatChomosomesToPopulation(pob_inicial):
        population = []

        current_population = pob_inicial.copy()

        best_individuals = [None, None, None, None]

        for ind in current_population:
            f = ind.f
            g = ind.g
            c1 = ind.c1
            c2 = ind.c2
            k1_f = ind.k1_f
            k2_f = ind.k2_f
            k1_g = ind.k1_g
            k2_g = ind.k2_g

            f_f = FUNCTIONS[f]
            f_g = FUNCTIONS[g]

            e_ = 0
            for x in range(1, 119):
                h_x = H[x - 1]

                Va = f_f(x, k1_f, k2_f, c1) + f_g(x, k1_g, k2_g, c2)
                e = error(h_x, Va)
                e_ =+ e

            population.append(Individual(f, g, c1, c2, k1_f, k2_f, k1_g, k2_g, (e_/118) * 100))
        
        return population