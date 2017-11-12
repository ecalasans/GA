import numpy as np


def generateChromosome():
    coord= np.random.uniform(0, 5, 2)
    x = 10*round(coord[0], 1)
    y = 10*round(coord[0], 1)

    return [x, y]
