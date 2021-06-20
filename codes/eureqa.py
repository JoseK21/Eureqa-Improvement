from constants import *
from functions import *

from classes import *

import random
from random import sample
import numpy as np

from matplotlib import pyplot as plt

def main():
    ee = 9999999
    num_parents_mating = 4
    num_population = 100
    
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
        # pob_inicial.append(newChromosome)

    for pppp in range(num_population):

        population = []

        current_population = pob_inicial.copy()

        best_individuals = [None, None]

        e_array = []

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

        print("\033[96m-.-.-.-.-.-.-.-.-.-.- FIRST GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        for newPopulation in population:
            newPopulation.printInfo('x')

        print("\033[96m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        population.sort(key=lambda individuo: individuo.e, reverse=False)

        best_individuals = population[0:num_parents_mating] # 4

        print("\033[92m-.-.-.-.-.-.-.-.-.-.-.- Selección & Fitness Score -.-.-.-.-.-.-.-.-.-.-\033[0m")

        for bi in best_individuals:
            bi.printInfo('x')

        print("\033[92m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")


        print("\033[94m-.-.-.-.-.-.-.-.-.-.- CrossOver -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        ni = best_individuals.copy()
        new_children_by_crossover = []

        i0 = Individual(ni[0].f, ni[0].g, ni[1].c1, ni[1].c2, ni[1].k1_f, ni[1].k2_f, ni[1].k1_g, ni[1].k2_g)
        i1 = Individual(ni[1].f, ni[1].g, ni[0].c1, ni[0].c2, ni[0].k1_f, ni[0].k2_f, ni[0].k1_g, ni[0].k2_g)
        i2 = Individual(ni[2].f, ni[2].g, ni[3].c1, ni[3].c2, ni[3].k1_f, ni[3].k2_f, ni[3].k1_g, ni[3].k2_g)
        i3 = Individual(ni[3].f, ni[3].g, ni[2].c1, ni[2].c2, ni[2].k1_f, ni[2].k2_f, ni[2].k1_g, ni[2].k2_g)
        new_children_by_crossover.append(i0)
        new_children_by_crossover.append(i1)
        new_children_by_crossover.append(i2)
        new_children_by_crossover.append(i3)

        # for ncbc in new_children_by_crossover:
        #     ncbc.printInfo('x')

        print("\033[94m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        print("\033[95m-.-.-.-.-.-.-.-.-.-.- MUTATION -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
        list1 = range(0, 8) 
    
        selectedCrossOver = sample(list1, 2)
        current_population_1 = new_children_by_crossover + ni

        gene = ['f_f', 'f_g', 'c1', 'c2', 'k1_f', 'k2_f', 'k1_g', 'k2_g']

        gen_a_cambiar = sample(range(0,8), 1)[0]

        g = gene[gen_a_cambiar]

        for sco in selectedCrossOver:
            r = sample(range(0,2), 1)[0]
            i9_10 = None
            ind = current_population_1[sco]
            print('>>>>>>>>>>>>>>>>>>>>>>> <', ind.f,'><', ind.g, '>')

            if(r == 0):
                if(ind.f == 0):
                    g = 'c1'
                # TODO cambiar variables del poli4
                elif(ind.f >= 2):
                    gen_a_cambiar = sample(range(4, 6), 1)[0]
                    g = gene[gen_a_cambiar]
            else:
                if(ind.g == 0):
                    g = 'c2'
                # TODO cambiar variables del poli4
                elif(ind.g >= 2):
                    gen_a_cambiar = sample(range(6, 8), 1)[0]
                    g = gene[gen_a_cambiar]

            if(g == 'f_f'):
                new_f_f = sample(range(0, 4), 1)[0]
                i9_10 = Individual(new_f_f, ind.g, ind.c1, ind.c2, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)
            
            elif(g == 'f_g'):
                new_f_g = sample(range(0, 4), 1)[0]
                i9_10 = Individual(ind.f, new_f_g, ind.c1, ind.c2, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'c1'): # -----
                new_c1 = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, new_c1, ind.c2, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'c2'):
                new_c2 = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.c1, new_c2, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k1_f'):
                new_k1_f = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.c1, ind.c2, new_k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k2_f'):
                new_k2_f = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.c1, ind.c2, ind.k1_f, new_k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k1_g'):
                new_k1_g = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.c1, ind.c2, ind.k1_f, ind.k2_f, new_k1_g, ind.k2_g)

            elif(g == 'k2_g'):
                new_k2_g = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.c1, ind.c2, ind.k1_f, ind.k2_f, ind.k1_g, new_k2_g)

            current_population_1.append(i9_10)


        print("\033[94m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        print("\033[96m-.-.-.-.-.-.-.-.-.-.- NEW GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        for newPopulation in current_population_1:
            newPopulation.printInfo('x')

        pob_inicial = current_population_1.copy()

        print("\033[96m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")


if __name__ == "__main__":
    main()
