import numpy as np
import scipy.spatial.distance as ssd
import vrep
import time

def carregaObstaculos(clientID):
    obsCollection = None

    for i in range(0, 2):
        posXR = vrep.simxGetFloatSignal(clientID, 'posXR', vrep.simx_opmode_buffer)
        posYR = vrep.simxGetFloatSignal(clientID, 'posYR', vrep.simx_opmode_buffer)

        posX1 = vrep.simxGetFloatSignal(clientID, 'posX1', vrep.simx_opmode_buffer)
        posY1 = vrep.simxGetFloatSignal(clientID, 'posY1', vrep.simx_opmode_buffer)
        obs1 = [posX1[1], posY1[1]]

        posX2 = vrep.simxGetFloatSignal(clientID, 'posX2', vrep.simx_opmode_buffer)
        posY2 = vrep.simxGetFloatSignal(clientID, 'posY2', vrep.simx_opmode_buffer)
        obs2 = [posX2[1], posY2[1]]

        posX3 = vrep.simxGetFloatSignal(clientID, 'posX3', vrep.simx_opmode_buffer)
        posY3 = vrep.simxGetFloatSignal(clientID, 'posY3', vrep.simx_opmode_buffer)
        obs3 = [posX3[1], posY3[1]]

        posX4 = vrep.simxGetFloatSignal(clientID, 'posX4', vrep.simx_opmode_buffer)
        posY4 = vrep.simxGetFloatSignal(clientID, 'posY4', vrep.simx_opmode_buffer)
        obs4 = [posX4[1], posY4[1]]

        posX5 = vrep.simxGetFloatSignal(clientID, 'posX5', vrep.simx_opmode_buffer)
        posY5 = vrep.simxGetFloatSignal(clientID, 'posY5', vrep.simx_opmode_buffer)
        obs5 = [posX5[1], posY5[1]]

        posX6 = vrep.simxGetFloatSignal(clientID, 'posX6', vrep.simx_opmode_buffer)
        posY6 = vrep.simxGetFloatSignal(clientID, 'posY6', vrep.simx_opmode_buffer)
        obs6 = [posX6[1], posY6[1]]

        obsCollection = [np.array(obs1), np.array(obs2), np.array(obs3),
                         np.array(obs4), np.array(obs5), np.array(obs6)]


        time.sleep(0.5)

    return obsCollection

