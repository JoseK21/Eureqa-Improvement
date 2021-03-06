
from classes import *
from constants import *
from functions import *
from eureqa_functions import *

import random
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def main():    # True | False
    useStop = False
    plotOutput = True
    printSteps_ = True
    num_population = 10
    num_parents_mating = 4
    generation_counter = 0
    generalFitness_ = float('Inf')
    # Generate Initial Population
    print("\033[96m-.-.-.-.-.-.-.-.-.-.- #INITIAL GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m")
    population_data_chomosomes = generateInitialPopulation(POPULATION) # e.g.: [1, 2, 4, 3, 564, 34, 43]
    
    population = formatChomosomesToPopulation(population_data_chomosomes)

    population.sort(key=lambda individuo: individuo.e, reverse=False)

    best_individuals = population[0: num_parents_mating] # 4
    
    printChomosomeEcuation(best_individuals[0:1])

    gf = generalFitness(population)
    for _population in range(num_population):
        if(useStop and gf >= generalFitness_):
            # print('Current Fitness Score :', gf)
            # print('Previous Fitness Score :', generalFitness_)
            break

        generalFitness_ = gf 
        generation_counter += 1
        print("\033[96m-.-.-.-.-.-.-.-.-.-.- #{0} GENERATION  -.-.-.-.-.-.-.-.-.-.-.-.-\033[0m".format(generation_counter))

        # print(-.-.-.-.-.-.- SELECTION -.-.-.-.-.-.-.-.-.")
        best_individuals = population[0: num_parents_mating]

        if(printSteps_):
            printSteps('\033[95m', '>>>>>> PARENTS: ', best_individuals.copy())

        # print(-.-.-.-.-.-.-.- CROSSOVER -.-.-.-.-.-.-.-.-.-")
        new_children_by_crossover = crossover(best_individuals)
        if(printSteps_):
            printSteps('\033[94m', '>>>>>> CROSSOVER: ', new_children_by_crossover.copy())

        # print(-.-.-.-.-.-.-.-.-.-.-.- MUTATION -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        population = mutation(best_individuals.copy(), new_children_by_crossover)
        if(printSteps_):
            printSteps('\033[93m', '>>>>>> MUTATION: ', population[8:10].copy())

        # print(-.-.-.-.-.-.-.-.- SORT BY FITNESS -.-.-.-.-.-.-.-.-.-.-")
        population.sort(key=lambda individuo: individuo.e, reverse=False)

        printChomosomeEcuation(population[0:1])
        gf = generalFitness(population)

    if(plotOutput):
        ecu = population[0].printInfo('x', '')
        plot(logToEcu(ecu))

if __name__ == "__main__":
    main()
