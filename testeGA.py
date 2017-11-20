import numpy as np
import genetics
import obstaculos
import scipy.spatial.distance as ssd
from intervals import FloatInterval
import itertools

#
# s = np.array([0.8, 1.4])
# t = np.array([3.5, 4])
#
# populacao = genetics.generatePopulation(10, 6)
#
# roleta = genetics.roleta(populacao, s, t)
#
# print roleta

populacao = genetics.generatePopulation(2, 5)

print populacao[0]
print populacao[1]

c = genetics.crossover(populacao[0], populacao[1], np.floor(len(populacao[0])/2))

print c