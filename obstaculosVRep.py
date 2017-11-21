import numpy as np
import scipy.spatial.distance as ssd

def carregaObstaculos(obstaculos):
    resultado = []

    for obstaculo in obstaculos:
        resultado.append(np.array(obstaculo))

    return resultado