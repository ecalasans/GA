import numpy as np
import vrep
import sys
import time


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


posicao = vrep.simxGetObjectPosition(clientID,dummy,ref,vrep.simx_opmode_blocking)
#angulos = vrep.simxGetObjectOrientation(clientID, robo, -1, vrep.simx_opmode_blocking)
#distancia = vrep.simxReadDistance(clientID, pioneerDistDetect,
                                  #operationMode=vrep.simx_opmode_blocking)

time.sleep(3)
print posicao

codErroPosicao = vrep.simxSetObjectPosition(clientID, dummy, ref, [1, 2, 0],
                           operationMode=vrep.simx_opmode_oneshot)
time.sleep(3)

print codErroPosicao

print posicao
#print angulos[1][1]
#print distancia[1]