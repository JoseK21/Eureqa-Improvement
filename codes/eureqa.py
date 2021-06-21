
from classes import *
from constants import *
from functions import *
from eureqa_functions import *

import random
import numpy as np

from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 


'35.06sin(-33.27*x) + 46.33'

def main():   
    ee = 9999999
    num_population = 100
    num_parents_mating = 4
    generation_counter = 1

    e_generation = float('inf')
    # Generate Initial Population
    population_data_chomosomes = generateInitialPopulation(POPULATION)

    ind__ = 0
    print("\033[96m-.-.-.-.-.-.-.-.-.-.- #INITIAL GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m".format(generation_counter))

    for newPopulation in population_data_chomosomes:
        # print(truncate(0, 1), end=' <-> ')
        newPopulation.printInfo('x', "# -> ")
        # temp_e_generation += newPopulation.e
        ind__ += 1
    
    # TODO Evaluar y sacar e
    
    population = formatChomosomesToPopulation(population_data_chomosomes)

    population.sort(key=lambda individuo: individuo.e, reverse=False)

    best_individuals = population[0: num_parents_mating] # 4
    
    print("\033[92m")
    rank = 0
    for bi in best_individuals[0: 4]:
        rank += 1
        bi.printInfo('x', "\tBest Individual: <{0}> ".format(rank))
        print('\tFitness Score : ', bi.e)
    print("\033[0m")

    for pppp in range(num_population):
        generation_counter += 1

        population = formatChomosomesToPopulation(population_data_chomosomes)

        print("\033[96m-.-.-.-.-.-.-.-.-.-.- #{0} GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m".format(generation_counter))

        ind__ = 1
        # temp_e_generation = 0

        population.sort(key=lambda individuo: individuo.e, reverse=False)

        for newPopulation in population:
            print(truncate(newPopulation.e, 1), end=' <-> ')
            newPopulation.printInfo('x', "#{0} -> ".format(ind__))
            # temp_e_generation += newPopulation.e
            ind__ += 1
        
        
        # if(e_generation < temp_e_generation):
        #     print('.........DETENER.........')
        #     break
        # e_generation = temp_e_generation
    

        best_individuals = population[0: num_parents_mating] # 4

        # print("\033[92m-.-.-.-.-.-.-.-.-.-.-.- Selección & Fitness Score -.-.-.-.-.-.-.-.-.-.-\033[0m")

        # print("\033[93m")
        # for bi in best_individuals:
        #     bi.printInfo('x', "\tBest Individual: {0}".format(bi.rank))
        #     print('\tFitness Score : ', bi.e)
        # print("\033[0m")


        # print("\033[94m-.-.-.-.-.-.-.-.-.-.- CrossOver -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        ni = best_individuals.copy()
        new_children_by_crossover = []

        i0 = Individual(ni[0].f, ni[0].g, ni[1].cf, ni[1].cg, ni[1].k1_f, ni[1].k2_f, ni[1].k1_g, ni[1].k2_g)
        i0.update_e()
        i1 = Individual(ni[1].f, ni[1].g, ni[0].cf, ni[0].cg, ni[0].k1_f, ni[0].k2_f, ni[0].k1_g, ni[0].k2_g)
        i1.update_e()
        i2 = Individual(ni[2].f, ni[2].g, ni[3].cf, ni[3].cg, ni[3].k1_f, ni[3].k2_f, ni[3].k1_g, ni[3].k2_g)
        i2.update_e()
        i3 = Individual(ni[3].f, ni[3].g, ni[2].cf, ni[2].cg, ni[2].k1_f, ni[2].k2_f, ni[2].k1_g, ni[2].k2_g)
        i3.update_e()
        new_children_by_crossover.append(i0)
        new_children_by_crossover.append(i1)
        new_children_by_crossover.append(i2)
        new_children_by_crossover.append(i3)

        # for ncbc in new_children_by_crossover:
        #     ncbc.printInfo('x', 'CROSSOVER >>>>>> ')

        # print("\033[94m-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")

        # print("\033[95m-.-.-.-.-.-.-.-.-.-.- MUTATION -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
        list1 = range(0, 8) 
    
        selectedCrossOver_toMutation = random.sample(list1, 2)
        current_population_1 = ni + new_children_by_crossover

        current_population_1.sort(key=lambda individuo: individuo.e, reverse=False)

        # for ncbc in current_population_1:
        #     ncbc.printInfo('x', 'TOTAL ---------------> ')

        gene = ['f_f', 'f_g', 'cf', 'cg', 'k1_f', 'k2_f', 'k1_g', 'k2_g']

        gen_a_cambiar = random.sample(range(0,8), 1)[0]

        g = gene[gen_a_cambiar]

        # print(selectedCrossOver_toMutation)

        for sco in selectedCrossOver_toMutation:
            f_O_g = random.sample(range(0,2), 1)[0]
            i9_10 = None
            aaa = current_population_1.copy()
            ind = aaa[sco]

            # ind.printInfo('X', '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            # print('>>>>>>>>>>>>>>>>>>>>>>> <', ind.f,'><', ind.g, '>')

            if(f_O_g == 0):
                if(ind.f == 0):
                    g = 'cf'
                # TODO cambiar variables del poli4
                elif(ind.f >= 2):
                    gen_a_cambiar = random.sample([0, 4, 5], 1)[0]
                    g = gene[gen_a_cambiar]
            else:
                if(ind.g == 0):
                    g = 'cg'
                # TODO cambiar variables del poli4
                elif(ind.g >= 2):
                    gen_a_cambiar = random.sample([1, 6, 7], 1)[0]
                    g = gene[gen_a_cambiar]

            if(g == 'f_f'):
                new_f_f = random.sample(range(0, 4), 1)[0]
                i9_10 = Individual(new_f_f, ind.g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)
            
            elif(g == 'f_g'):
                new_f_g = random.sample(range(0, 4), 1)[0]
                i9_10 = Individual(ind.f, new_f_g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'cf'): # -----
                new_c1 = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, new_c1, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'cg'):
                new_c2 = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.cf, new_c2, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k1_f'):
                new_k1_f = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.cf, ind.cg, new_k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k2_f'):
                new_k2_f = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.cf, ind.cg, ind.k1_f, new_k2_f, ind.k1_g, ind.k2_g)

            elif(g == 'k1_g'):
                new_k1_g = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, new_k1_g, ind.k2_g)

            elif(g == 'k2_g'):
                new_k2_g = truncate(np.random.uniform(-50, 50), 2)
                i9_10 = Individual(ind.f, ind.g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, new_k2_g)

            i9_10.update_e()
            # i9_10.printInfo('w', '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            current_population_1.append(i9_10)

        # for newPopulation in current_population_1:
        #     # print(truncate(0, 1), end=' <-> ')
        #     newPopulation.printInfo('x', "#{0} -> ".format(ind__))
        #     # temp_e_generation += newPopulation.e
        #     ind__ += 1

        population.sort(key=lambda individuo: individuo.e, reverse=False)

        rank_ = 0
        print("\033[92m")
        for bi in current_population_1[0:4]:
            rank_ +=1
            bi.printInfo('x', "\tBest Individual: <{0}> ".format(rank_))
            print('\tFitness Score : ', bi.e)
        print("\033[0m")

        population_data_chomosomes = current_population_1.copy()

if __name__ == "__main__":
    main()
