import numpy as np

def generateGene():
    x = np.random.uniform(0, 5, 1)
    y = np.random.uniform(0, 5, 1)
    return [round(x[0], 1), round(y[0] ,1)]

def generateChromosome(tam):
    chromosome = []

    for i in range(0, tam):
        chromosome.append(generateGene())

    return chromosome

def generatePopulation(tamPop, tamChrom):
    pop = []

    for i in range(0, tamPop):
        pop.append(generateChromosome(tamChrom))

    return pop


