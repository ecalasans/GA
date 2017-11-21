import vrep
import numpy as np
import time

def getRobotPosition(clientID):
    posXR = vrep.simxGetFloatSignal(clientID, 'posXR', vrep.simx_opmode_buffer)
    posYR = vrep.simxGetFloatSignal(clientID, 'posYR', vrep.simx_opmode_buffer)

    return np.array([round(posXR[1], 2), round(posYR[1], 2)])