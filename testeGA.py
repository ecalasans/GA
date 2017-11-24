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

s = np.array([0.4,1.4])
t = np.array([3.4, 2.8])

genetics.run(start=s, target=t, tamPop=10, tamIndividuo=6, nGeracoes=100, probMutacao=0.01)