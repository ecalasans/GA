import numpy as np
import vrep
import sys
import time


# Encerra conexoes previas
vrep.simxFinish(-1)

# Faz a conexao com o Vrep
clientID = vrep.simxStart('192.168.11.7', 19999, True, True, 5000, 5)  # Connect to V-REP

# Verifica se a conexao foi efetiva
if clientID != -1:
    print("Conectado ao VRep!!  Obaaaaa!!!")
    vrep.simxAddStatusbarMessage(clientID, "Conexao estabelecida!", operationMode=vrep.simx_opmode_oneshot)

else:
    print("Nao conectado ao VRep!!!")
    sys.exit("Xau!!")

#Instancia objetos no Python para os handlers
codErro, dummy = vrep.simxGetObjectHandle(clientID, 'dummy', operationMode=vrep.simx_opmode_oneshot)
codErro, pioneerColDetect = vrep.simxGetCollisionHandle(clientID, 'pioneerColDetect#',
                                                        operationMode=vrep.simx_opmode_blocking)
codErro, pioneerDistDetect = vrep.simxGetDistanceHandle(clientID, 'pioneerDistDetect#',
                                                        operationMode=vrep.simx_opmode_blocking)
codErro, obstaculos = vrep.simxGetCollectionHandle(clientID, 'obstaculos#',
                                                   operationMode=vrep.simx_opmode_oneshot)
codErro, robo = vrep.simxGetObjectHandle(clientID, 'Pionee_p3dx',
                                         operationMode=vrep.simx_opmode_oneshot)
codErro, chao = vrep.simxGetObjectHandle(clientID, 'ResizablFloor_5_25',
                                         operationMode=vrep.simx_opmode_oneshot)

time.sleep(3)

posicao = vrep.simxGetObjectPosition(clientID, dummy, -1, vrep.simx_opmode_oneshot_wait)
angulos = vrep.simxGetObjectOrientation(clientID, dummy, -1, vrep.simx_opmode_oneshot_wait)
distancia = vrep.simxReadDistance(clientID, dummy,
                                  operationMode=vrep.simx_opmode_blocking)

print posicao
print angulos
print distancia[1]