import numpy as np
import genetics
import obstaculos
import scipy.spatial.distance as ssd

"""
a = range(0, 10)

for i in range(0, len(a)):
    print i
"""


s = [2.4, 1.0]
t = [4.2, 3.6]

#individuo = genetics.generateIndividual(10)
#print individuo

#fitness = genetics.fitness(individuo, s, t)

#print fitness

dist = obstaculos.distanciasPO(t)
print dist