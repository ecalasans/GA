# -*- coding: UTF-8 -*-
import numpy as np
import scipy.spatial.distance as ssd
import obstaculos
from intervals import FloatInterval as fInterval

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
    porcFitness = []
    sumFitness = 0
    for individuo in populacao:
        fitIndividuo = fitness(individuo, start, target)
        fitPop.append(fitIndividuo)
        sumFitness += fitIndividuo

    #Calcula a soma total das fitness
    #sumFitness = sum(fitPop)

    #Calcula a porcentagem de cada fitness individual em relacao a fitness total
    for fit in fitPop:
        porcFitness.append(round(fit/sumFitness,2))

    # Calcula a posicao da agulha da roleta - numero entre 0 e 1 randomico
    agulha = np.random.uniform(0, max(porcFitness), 1)/sumFitness

    #Cria os intervalos da roleta e faz o giro
    resultado = 0
    a = 0
    for porc in porcFitness:
        b = a + porc
        if float(agulha) in fInterval.closed(a, b):
            break
        else:
            resultado += 1
        a = b

    return populacao[resultado]

def crossover(indivA, indivB, ponto):
    #Calcula o ponto de corte do vetor
    crossPonto = np.floor(len(indivA)/2)

    crossAB = []     #Primeiro descendente
    crossBA = []     #Segundo descendente

    #Faz os cruzamentos
    for i in range(0, int(ponto)):
        crossAB.append(indivA[i])
        crossBA.append(indivB[i])

    for j in range(int(ponto), len(indivA)):
        crossAB.append(indivB[j])
        crossBA.append(indivA[j])

    return crossAB, crossBA


def run(start, target, tamPop, tamIndividuo, nGeracoes):
    fitInicial = []
    proximaPopulacao = []
    fitnessIndividuo = 0
    geracao = 0

    #Gere uma populacao de individuos aleatorios
    print "Gerando população com " + str(tamPop) + " indivíduos..."
    popIncial = generatePopulation(tamPop, tamIndividuo)

    #Verifique a fitness de cada indivíduo da população inicial
    print ""
    print "Calculando a fitness inicial da população..."
    for individuoInicial in popIncial:
        fitnessIndividuo = fitness(individuoInicial, start, target)
        fitInicial.append(fitnessIndividuo)

    #Crie a próxima população
        #Garante na próxima população a maior fitness
    print ""
    print "Criando a próxima população..."

    while geracao < nGeracoes:
        proximaPopulacao = []
        print str(geracao + 1) + "ª geração..."
        proximaPopulacao.append(popIncial[fitInicial.index(max(fitInicial))])
        print proximaPopulacao, fitInicial.index(max(fitInicial))

        for i in range(0, int(np.floor(len(popIncial) / 2))):
            # Seleciona um par de individuos da populacao para ser os pais
            paiA = roleta(populacao=popIncial, start=start, target=target)
            paiB = roleta(populacao=popIncial, start=start, target=target)

            # Gera os filhos e adiciona à próxima população, cruzando-os pelo meio
            filhos = crossover(paiA, paiB, np.floor(len(paiA) / 2))
            proximaPopulacao.append(filhos[0])
            proximaPopulacao.append(filhos[1])

        popIncial = proximaPopulacao

        geracao += 1













