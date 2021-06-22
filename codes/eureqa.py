
from classes import *
from constants import *
from functions import *
from eureqa_functions import *

import random
import numpy as np

from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def main():   
    num_population = 5
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

        # print("\033[92m-.-.-.-.-.-.-.-.-.-.- SELECTION -.-.-.-.-.-.-.-.-.-.-\033[0m")
        best_individuals = population[0: num_parents_mating]

        # print("\033[94m-.-.-.-.-.-.-.-.-.-. CROSSOVER -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
        new_children_by_crossover = crossover(best_individuals)

        # print("\033[95m-.-.-.-.-.-.-.-.-.-.- MUTATION -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
        population = mutation(best_individuals.copy(), new_children_by_crossover)

        # print("\033[95m-.-.-.-.-.-.-.-.-. SORT BY FITNESS -.-.-.-.-.-.-.-.-.-.-\033[0m")
        population.sort(key=lambda individuo: individuo.e, reverse=False)

        print("\033[96m-.-.-.-.-.-.-.-.-.-.- #{0} GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m".format(generation_counter))
        printGeneration(population)

        printChomosomeEcuation(population[0:4])

        population_data_chomosomes = population.copy()

if __name__ == "__main__":
    main()
