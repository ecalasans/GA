from numpy import random


def generateChromosome(x):
    chromosome = bin(x)[2:]
    chromosome = chromosome.zfill(20)
    return chromosome

def generatePopulation(tam):
    popInt = random.randint(0,101,tam)

    popBin = []

    for i in popInt:
        popBin.append(generateChromosome(i))

    return popBin
