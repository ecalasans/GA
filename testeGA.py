import numpy as np
import genetics
import obstaculos
import scipy.spatial.distance as ssd

"""
a = range(0, 10)

for i in range(0, len(a)):
    print i
"""

s = np.array([0.8, 1.4])
t = np.array([3.5, 4])

populacao = genetics.generatePopulation(10, 6)

rol = genetics.roleta(populacao, s, t)

print rol

