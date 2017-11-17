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

    for cromossomo in range(0, len(individuo) - 1):
        #Calcula a distancia do segmento ate o proximo ponto e adiciona a lenPath
        lenPath += obstaculos.distanciaPontos(individuo[cromossomo], individuo[cromossomo+1])

        #Calcula a distancia ate o obstaculo mais proximo do cromossomo e adiciona a lenDistObst
        distCromObs = obstaculos.distanciasPO(individuo[cromossomo])[0]

        #Calcula o cosseno entre a distancia ao obstaculo e a distancia ao target
        pontoObst = obstaculos.calculaPontoObst(individuo[cromossomo])
        distCosseno = obstaculos.calculaDistCosseno(individuo[cromossomo], pontoObst, target)

        lenDistObst += distCromObs * distCosseno

    lenPath += lenPath + obstaculos.distanciaPontos(individuo[len(individuo) - 1], target)

    return lenDistObst/lenPath

def roleta(populacao, start, target):
    #Calcula um vetor de fitness dos individuos da populacao
    fitPop = []
    for individuo in populacao:
        fitPop.append(fitness(individuo,start,target))


    #Calcula a soma total das fitness

    #Calcula a porcentagem de cada fitness individual em relacao a fitness total

    #Calcula a posicao da agulha da roleta - numero entre 0 e 1 randomico

    #Seleciona o individuo com base na posicao da agulha

    return fitPop












