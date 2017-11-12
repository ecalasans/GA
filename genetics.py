import numpy as np
import intervals as intervalo

OBS_1X = intervalo.FloatInterval.closed(0.75, 1.25)
OBS_1Y = intervalo.FloatInterval.closed(0.75, 1.25)

OBS_2X = intervalo.FloatInterval.closed(1.25, 1.75)
OBS_2Y = intervalo.FloatInterval(3.25, 3.75)

OBS_3X = intervalo.FloatInterval.closed(2.25, 2.75)
OBS_3Y = intervalo.FloatInterval.closed(2.25, 2.75)

OBS_4X = intervalo.FloatInterval.closed(4.25, 4.75)
OBS_4Y = intervalo.FloatInterval.closed(1.75, 2.25)

OBS_5X = intervalo.FloatInterval.closed(2.75, 3.25)
OBS_5Y = intervalo.FloatInterval.closed(0.75, 1.25)

OBS_6X = intervalo.FloatInterval.closed(3.75, 4.25)
OBS_6Y = intervalo.FloatInterval.closed(2.75, 3.25)

def generateChromosome():
    x = np.random.uniform(0, 5, 1)
    y = np.random.uniform(0, 5, 1)
    return np.array((round(x[0], 1), round(y[0], 1)))

def generateIndividual(tamInd):
    individuo = []

    for i in range(0, tamInd):
        individuo.append(generateChromosome())

    return individuo

def generatePopulation(nIndividuals, tamInd):
    pop = []

    for i in range(0, nIndividuals):
        pop.append(generateIndividual(tamInd))

    return pop

def fitness(individuo, target):
    distPT = []

    for i in individuo[0]:
        distPT.append(round(np.linalg.norm(i - target), 2))



