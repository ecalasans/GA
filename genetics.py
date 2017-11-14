import numpy as np
import scipy.spatial.distance as ssd
import obstaculos

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

def fitness(individuo, start, target):
    lenPath = obstaculos.distanciaPontos(start, individuo[0])
    lenDistObst = 0

    for i in range(1, len(individuo) - 1):
        #Calcula a distancia do segmento ate o proximo ponto e adiciona a lenPath
        lenPath += obstaculos.distanciaPontos(individuo[i], individuo[i+1])

        #Calcula o cosseno entre o vetor













