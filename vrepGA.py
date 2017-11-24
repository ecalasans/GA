# -*- coding:  UTF-8 -*-
import numpy as np
import vrep
import sys
import time
import obstaculosVRep as oVrep
import robotFunctions as RF


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

#Destino
codErro, target = vrep.simxGetObjectHandle(clientID, 'target', operationMode=vrep.simx_opmode_oneshot)

#Medidores de colisão
codErro, pioneerColDetect = vrep.simxGetCollisionHandle(clientID, 'pioneerColDetect',
                                                        operationMode=vrep.simx_opmode_blocking)

#Medidores de distância
codErro, roboObstDist = vrep.simxGetDistanceHandle(clientID, 'roboObstDistDetect',
                                                        operationMode=vrep.simx_opmode_blocking)
codErro, roboTargetDist = vrep.simxGetDistanceHandle(clientID, 'roboTargetDistDetect',
                                                     operationMode=vrep.simx_opmode_blocking)

codErro, obstaculos = vrep.simxGetCollectionHandle(clientID, 'obstaculos#',
                                                   operationMode=vrep.simx_opmode_oneshot)
codErro, robo = vrep.simxGetObjectHandle(clientID, 'Pionee_p3dx',
                                         operationMode=vrep.simx_opmode_oneshot)


codErro, motorE = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_blocking)
codErro, motorD = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_blocking)

codErro, colisao = vrep.simxReadCollision(clientID, pioneerColDetect,
                                          operationMode=vrep.simx_opmode_streaming)

posXR = vrep.simxGetFloatSignal(clientID, 'posXR', vrep.simx_opmode_streaming)
posYR = vrep.simxGetFloatSignal(clientID, 'posYR', vrep.simx_opmode_streaming)


posX1 = vrep.simxGetFloatSignal(clientID, 'posX1', vrep.simx_opmode_streaming)
posY1 = vrep.simxGetFloatSignal(clientID, 'posY1', vrep.simx_opmode_streaming)

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


#Grava posição dos obstaculos
mapaObstaculos = oVrep.carregaObstaculos(clientID)
posRobo = RF.getRobotPosition(clientID)

distRO = vrep.simxReadDistance(clientID, roboObstDist, operationMode=vrep.simx_opmode_blocking)
distRT = vrep.simxReadDistance(clientID, roboTargetDist, operationMode=vrep.simx_opmode_blocking)

print mapaObstaculos

