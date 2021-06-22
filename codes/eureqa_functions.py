from classes import *
from functions import *
from constants import *

import matplotlib.pyplot as plt
import numpy as np

def plot(ecuation):
    e_ = 0
    y_ = []
    x_ = []

    for i in range(1, 119):
        x = i
        h_x = H[x - 1]

        Va = eval(ecuation)
        y_.append(Va)
        x_.append(x)

        e = error(h_x, Va)
        e_ =+ e

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')

    ax1.plot(x_, y_)
    ax2.scatter(x_, y_)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('_Eureqa_')
    plt.show()



def logToEcu(ecu):
    new_e = ecu.replace('cos', '*math.cos').replace('sin', '*math.sin').replace('e**', 'math.e**')
    return new_e

def generateInitialPopulation(POPULATION):
    pob_inicial = []

    for p in range(POPULATION):
        chomosome = np.random.randint(5, size=2)
        newChromosome = []
        for c in range(2):
            newChromosome.append(chomosome[c]) # 2

        for k in range(6):
            newConstant = truncate(np.random.uniform(-50, 50), 2)
            newChromosome.append(newConstant)
        
        pob_inicial.append(Individual(newChromosome[0], newChromosome[1], newChromosome[2], newChromosome[3], newChromosome[4], newChromosome[5], newChromosome[6], newChromosome[7]))

    for newPopulation in pob_inicial:
        newPopulation.printInfo('x', "# -> ")

    return pob_inicial

def setMax(value):
    if(value > num_max_min):
        return num_max_min
    return value

def formatChomosomesToPopulation(pob_inicial):
        population = []

        current_population = pob_inicial.copy()

        best_individuals = [None, None, None, None]

        for ind in current_population:
            f = ind.f
            g = ind.g
            cf = ind.cf
            cg = ind.cg
            k1_f = ind.k1_f
            k2_f = ind.k2_f
            k1_g = ind.k1_g
            k2_g = ind.k2_g

            f_f = FUNCTIONS[f]
            f_g = FUNCTIONS[g]

            e_ = 0
            for x in range(1, 119):
                h_x = H[x - 1]
                
                result_f = setMax(f_f(x, k1_f, k2_f, cf))
                result_g = setMax(f_g(x, k1_g, k2_g, cg))

                Va = result_f + result_g
                e = error(h_x, setMax(Va))
                e_ =+ e

            population.append(Individual(f, g, cf, cg, k1_f, k2_f, k1_g, k2_g, (e_/118) * 100))
        
        return population

def printChomosomeEcuation(best_individuals):
    print("\033[92m")
    for bi in best_individuals[0: 4]:
        bi.printInfo('x', "\tBest Individual: ")
        print('\tFitness Score: ', bi.e)
    print("\033[0m")

def printGeneration(population):
    ind = 1
    print('\n', end='')
    for newPopulation in population:
        print(truncate(newPopulation.e, 1), end=' <-> ')
        newPopulation.printInfo('x', "#{0} -> ".format(ind))
        ind += 1

def mutation(ni, new_children_by_crossover):
    selectedCrossOver_toMutation = random.sample(range(0, 8), 2)
    current_population_1 = ni + new_children_by_crossover

    current_population_1.sort(key=lambda individuo: individuo.e, reverse=False)

    #         0       1    2      3    4        5        6      7
    gene = ['f_f', 'f_g', 'cf', 'cg', 'k1_f', 'k2_f', 'k1_g', 'k2_g']

    for sco in selectedCrossOver_toMutation:
        params_of_f_O_g = random.sample(range(0,2), 1)[0]
        i9_10 = None
        g = None
        gen_a_cambiar = None

        aaa = current_population_1.copy()
        ind = aaa[sco]

        if(params_of_f_O_g == 0):
            if(ind.f == 0): # constante de c de f(x)
                g = 'cf'
            # elif(ind.f == 1):
            #     # TODO: CAmbiar parametros del polinomio
            #     v = 0
            else:
                gen_a_cambiar = random.sample([0, 4, 5], 1)[0]
                g = gene[gen_a_cambiar]
        else:
            if(ind.g == 0): # constante de c de f(x)
                g = 'cg'
            # elif(ind.g == 1):
            #     # TODO: CAmbiar parametros del polinomio
            #     v = 0
            else:
                gen_a_cambiar = random.sample([1, 6, 7], 1)[0]
                g = gene[gen_a_cambiar]

        if(g == 'f_f'):
            new_f_f = random.sample(range(0, 4), 1)[0]
            i9_10 = Individual(new_f_f, ind.g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)
        
        elif(g == 'f_g'):
            new_f_g = random.sample(range(0, 4), 1)[0]
            i9_10 = Individual(ind.f, new_f_g, ind.cf, ind.cg, ind.k1_f, ind.k2_f, ind.k1_g, ind.k2_g)

        elif(g == 'cf'):
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

        current_population_1.append(i9_10)

    return current_population_1

def crossover(best_individuals):
    parents4 = best_individuals.copy()
    new_children_by_crossover = []

    i0 = Individual(parents4[0].f, parents4[0].g, parents4[1].cf, parents4[1].cg, parents4[1].k1_f, parents4[1].k2_f, parents4[1].k1_g, parents4[1].k2_g)
    i0.update_e()
    i1 = Individual(parents4[1].f, parents4[1].g, parents4[0].cf, parents4[0].cg, parents4[0].k1_f, parents4[0].k2_f, parents4[0].k1_g, parents4[0].k2_g)
    i1.update_e()
    i2 = Individual(parents4[2].f, parents4[2].g, parents4[3].cf, parents4[3].cg, parents4[3].k1_f, parents4[3].k2_f, parents4[3].k1_g, parents4[3].k2_g)
    i2.update_e()
    i3 = Individual(parents4[3].f, parents4[3].g, parents4[2].cf, parents4[2].cg, parents4[2].k1_f, parents4[2].k2_f, parents4[2].k1_g, parents4[2].k2_g)
    i3.update_e()
    new_children_by_crossover.append(i0)
    new_children_by_crossover.append(i1)
    new_children_by_crossover.append(i2)
    new_children_by_crossover.append(i3)

    return new_children_by_crossover

def printSteps(color, label, array):
    print(color, end='')
    for newPopulation in array:
        print(newPopulation.e, end=' ')
        print(label, end='')
        newPopulation.printInfo('x', "", False)
    print('\033[0m', end='')

