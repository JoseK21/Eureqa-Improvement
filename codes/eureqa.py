
from classes import *
from constants import *
from functions import *
from eureqa_functions import *

import random
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def main():   
    num_population = 3
    num_parents_mating = 4
    generation_counter = 0

    # Generate Initial Population
    print("\033[96m-.-.-.-.-.-.-.-.-.-.- #INITIAL GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
    population_data_chomosomes = generateInitialPopulation(POPULATION) # e.g.: [1, 2, 4, 3, 564, 34, 43]
    
    population = formatChomosomesToPopulation(population_data_chomosomes)

    population.sort(key=lambda individuo: individuo.e, reverse=False)

    best_individuals = population[0: num_parents_mating] # 4
    
    printChomosomeEcuation(best_individuals)

    # print("\033[92m-.-.-.-.-.-.-.-.-.-.- LOOP -.-.-.-.-.-.-.-.-.-.-\033[0m")
    for _population in range(num_population):
        generation_counter += 1
        print("\033[96m-.-.-.-.-.-.-.-.-.-.- #{0} GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m".format(generation_counter))

        # print(-.-.-.-.-.-.- SELECTION -.-.-.-.-.-.-.-.-.")
        best_individuals = population[0: num_parents_mating]

        printSteps('\033[95m', '>>>>>> PARENTS: ', best_individuals.copy())

        # print(-.-.-.-.-.-.-.- CROSSOVER -.-.-.-.-.-.-.-.-.-")
        new_children_by_crossover = crossover(best_individuals)
        printSteps('\033[94m', '>>>>>> CROSSOVER: ', new_children_by_crossover.copy())

        # print(-.-.-.-.-.-.-.-.-.-.-.- MUTATION -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        population = mutation(best_individuals.copy(), new_children_by_crossover)
        printSteps('\033[93m', '>>>>>> MUTATION: ', population[8:10].copy())

        # print(-.-.-.-.-.-.-.-.- SORT BY FITNESS -.-.-.-.-.-.-.-.-.-.-")
        population.sort(key=lambda individuo: individuo.e, reverse=False)

        printChomosomeEcuation(population[0:1])

    ecu = population[0].printInfo('x', '')

    plot(logToEcu(ecu))

if __name__ == "__main__":
    main()
