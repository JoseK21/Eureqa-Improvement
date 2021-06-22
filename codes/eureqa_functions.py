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

    for newPopulation in pob_inicial:
        newPopulation.printInfo('x', "# -> ")

    return pob_inicial

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

                Va = f_f(x, k1_f, k2_f, cf) + f_g(x, k1_g, k2_g, cg)
                e = error(h_x, Va)
                e_ =+ e

            population.append(Individual(f, g, cf, cg, k1_f, k2_f, k1_g, k2_g, (e_/118) * 100))
        
        return population

def printChomosomeEcuation(best_individuals):
    print("\033[92m")
    rank = 0
    for bi in best_individuals[0: 4]:
        rank += 1
        bi.printInfo('x', "\tBest Individual: <{0}> ".format(rank))
        print('\tFitness Score : ', bi.e)
    print("\033[0m")

def printGeneration(population):
    ind = 1
    for newPopulation in population:
        print(truncate(newPopulation.e, 1), end=' <-> ')
        newPopulation.printInfo('x', "#{0} -> ".format(ind))
        ind += 1

def mutation(ni, new_children_by_crossover):
    list1 = range(0, 8) 

    selectedCrossOver_toMutation = random.sample(list1, 2)
    current_population_1 = ni + new_children_by_crossover

    current_population_1.sort(key=lambda individuo: individuo.e, reverse=False)

    gene = ['f_f', 'f_g', 'cf', 'cg', 'k1_f', 'k2_f', 'k1_g', 'k2_g']

    gen_a_cambiar = random.sample(range(0,8), 1)[0]

    g = gene[gen_a_cambiar]

    for sco in selectedCrossOver_toMutation:
        f_O_g = random.sample(range(0,2), 1)[0]
        i9_10 = None
        aaa = current_population_1.copy()
        ind = aaa[sco]

        if(f_O_g == 0):
            if(ind.f == 0):
                g = 'cf'
            elif(ind.f >= 2):
                gen_a_cambiar = random.sample([0, 4, 5], 1)[0]
                g = gene[gen_a_cambiar]
        else:
            if(ind.g == 0):
                g = 'cg'
            elif(ind.g >= 2):
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