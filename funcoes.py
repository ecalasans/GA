import numpy as np
import vrep

VEL_LINEAR = 0.5
VEL_ANGULAR = 0.5

def andar(rodaE, rodaE, inicio, fim):


    distancia = np.linalg.norm(fim-inicio)