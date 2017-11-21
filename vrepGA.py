import numpy as np
import vrep
import sys
import time
import obstaculosVRep as oVrep


# Encerra conexoes previas
vrep.simxFinish(-1)

# Faz a conexao com o Vrep
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to V-REP

# Verifica se a conexao foi efetiva
if clientID != -1:
    print("Conectado ao VRep!!  Obaaaaa!!!")
    vrep.simxAddStatusbarMessage(clientID, "Conexao estabelecida!", operationMode=vrep.simx_opmode_oneshot)

else:
    print("Nao conectado ao VRep!!!")
    sys.exit("Xau!!")

#Instancia objetos no Python para os handlers
codErro, ref = vrep.simxGetObjectHandle(clientID, 'ref',
                                        operationMode=vrep.simx_opmode_oneshot)
codErro, dummy = vrep.simxGetObjectHandle(clientID, 'dummy', operationMode=vrep.simx_opmode_oneshot)
codErro, pioneerColDetect = vrep.simxGetCollisionHandle(clientID, 'pioneerColDetect',
                                                        operationMode=vrep.simx_opmode_blocking)
codErro, pioneerDistDetect = vrep.simxGetDistanceHandle(clientID, 'pioneerDistDetect',
                                                        operationMode=vrep.simx_opmode_blocking)
codErro, obstaculos = vrep.simxGetCollectionHandle(clientID, 'obstaculos',
                                                   operationMode=vrep.simx_opmode_oneshot)
codErro, robo = vrep.simxGetObjectHandle(clientID, 'Pionee_p3dx',
                                         operationMode=vrep.simx_opmode_oneshot)
codErro, chao = vrep.simxGetObjectHandle(clientID, 'ResizableFloor_5_25',
                                         operationMode=vrep.simx_opmode_oneshot)

codErro, motorE = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_blocking)
codErro, motorD = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_blocking)


posXR = vrep.simxGetFloatSignal(clientID, 'posXR', vrep.simx_opmode_streaming)
posYR = vrep.simxGetFloatSignal(clientID, 'posYR', vrep.simx_opmode_streaming)


posX1 = vrep.simxGetFloatSignal(clientID, 'posX1', vrep.simx_opmode_streaming)
posY1 = vrep.simxGetFloatSignal(clientID, 'posY1', vrep.simx_opmode_streaming)
obs1 = [posX1[1], posY1[1]]

time.sleep(3)
print obs1

posX2 = vrep.simxGetFloatSignal(clientID, 'posX2', vrep.simx_opmode_streaming)
posY2 = vrep.simxGetFloatSignal(clientID, 'posY2', vrep.simx_opmode_streaming)


posX3 = vrep.simxGetFloatSignal(clientID, 'posX3', vrep.simx_opmode_streaming)
posY3 = vrep.simxGetFloatSignal(clientID, 'posY3', vrep.simx_opmode_streaming)


posX4 = vrep.simxGetFloatSignal(clientID, 'posX4', vrep.simx_opmode_streaming)
posY4 = vrep.simxGetFloatSignal(clientID, 'posY4', vrep.simx_opmode_streaming)


posX5 = vrep.simxGetFloatSignal(clientID, 'posX5', vrep.simx_opmode_streaming)
posY5 = vrep.simxGetFloatSignal(clientID, 'posY5', vrep.simx_opmode_streaming)


posX6 = vrep.simxGetFloatSignal(clientID, 'posX6', vrep.simx_opmode_streaming)
posY6 = vrep.simxGetFloatSignal(clientID, 'posY6', vrep.simx_opmode_streaming)

for i in range(0, 10000):
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

    obsCollection = [obs1, obs2, obs3, obs4, obs5, obs6]
    mapaObstaculos = oVrep.carregaObstaculos(obsCollection)
    print mapaObstaculos
#
#     codErro = vrep.simxSetJointTargetVelocity(clientID, jointHandle=motorE, targetVelocity=0,
#                                               operationMode=vrep.simx_opmode_streaming)
#     codErro = vrep.simxSetJointTargetVelocity(clientID, jointHandle=motorD, targetVelocity=0,
#                                               operationMode=vrep.simx_opmode_streaming)
#
    time.sleep(1)
